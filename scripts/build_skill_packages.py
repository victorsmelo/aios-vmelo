#!/usr/bin/env python3
"""Gera referências por assunto e distribuições Claude sem instalar ou publicar."""
from __future__ import annotations
import argparse
import hashlib
import io
import json
import posixpath
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE_REVISION = 'b0b151540bf9c5061d3c2529f0d4657d4344ed0f'
TARGET_VERSION = 'v1.3.0'
REPO = 'https://github.com/victorsmelo/aios-vmelo'
NAMES = ('aios', 'aios-maintenance', 'orchestrate')
ENVIRONMENTS = {
    'openai': '''# Ambiente OpenAI

Usar somente ferramentas disponíveis na sessão. Acesso ao GitHub, arquivos e histórico depende dos conectores e permissões atuais. Uma skill instalada não fornece esses acessos.

Para delegação, usar as ferramentas reais de colaboração. Se houver controle de contexto, preferir atribuições autocontidas; `fork_turns: "none"` só se esse parâmetro existir na ferramenta. Se for necessário herdar todo o histórico, respeitar eventuais restrições de modelo e esforço. Não transferir parâmetros deste ambiente para outras plataformas.

Ao escolher esforço, preferir low para investigação delimitada, medium para execução e high para ambiguidades ou implementação difícil, somente se essas opções estiverem disponíveis. Ajustar ao trabalho; não elevar todos os agentes por padrão.
''',
    'claude-code': '''# Ambiente Claude Code

Ler arquivos do checkout e usar terminal ou conectores somente conforme ferramentas e permissões da sessão. Não presumir acesso ao GitHub, a conversas anteriores ou às instalações de outro produto.

Quando a ferramenta Agent estiver disponível e a delegação for permitida, enviar atribuições delimitadas com entradas e instruções necessárias. Verificar capacidades reais do subagente; não presumir herança de skills ou ferramentas. Não criar arquivos de configuração de agentes sem necessidade no pedido. Sem delegação disponível, executar diretamente.

Usar apenas parâmetros anunciados pela versão instalada. Preferir o modelo do coordenador quando a ferramenta permitir; não converter níveis de esforço de outra plataforma automaticamente. A instalação desta skill não concede permissões nem habilita equipes.

Referências oficiais: [skills](https://code.claude.com/docs/en/skills) e [subagentes](https://code.claude.com/docs/en/sub-agents), consultadas em 2026-09-07.
''',
    'claude-app': '''# Ambiente Claude app e web

Trabalhar com mensagens, arquivos fornecidos e conectores realmente disponíveis. Não presumir checkout local, terminal, acesso ao GitHub, histórico de outras conversas ou ferramentas do Claude Code. Quando faltar uma fonte, usar a cópia identificada do pacote e informar a limitação relevante.

Não presumir subagentes neste ambiente. Executar diretamente as frentes de trabalho; só delegar se a sessão expuser uma ferramenta real compatível e permitir seu uso. Não narrar rodadas entre personas como se fossem agentes. Orientações de orquestração continuam úteis para organizar dependências sem afirmar paralelismo.

Para alterações que o ambiente não consegue aplicar, preparar conteúdo revisável e dizer que ainda não foi aplicado. Não inventar comandos, instalação ou verificação externa.

Referência oficial: [criação e carregamento de skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills), consultada em 2026-09-07.
''',
}

def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def sources(name: str) -> list[str]:
    paths = ['docs/core/AIOS.md', 'docs/editorial.md']
    if name != 'orchestrate':
        paths += ['docs/constitution/aios-constitution.md', 'docs/protocols/focus-protocol.md',
                  'docs/personas-index.md', 'docs/architecture/layers.md']
        paths += [p.relative_to(ROOT).as_posix() for p in sorted((ROOT/'docs/personas').rglob('*.md'))]
    if name == 'aios-maintenance':
        paths += ['DOCOPS.md', 'RELEASE_PROCESS.md', 'docs/templates/persona-template.md']
    return sorted(set(paths))

def snapshot(path: str, selected: set[str]) -> bytes:
    original = (ROOT/path).read_bytes()
    body = original.decode('utf-8')
    def link(match: re.Match) -> str:
        label, target = match.groups()
        if target.startswith(('#', 'http:', 'https:', 'mailto:')):
            return match.group(0)
        file, sep, anchor = target.partition('#')
        resolved = posixpath.normpath(posixpath.join(posixpath.dirname(path), file))
        if resolved in selected:
            return match.group(0)
        return f'[{label}]({REPO}/blob/{TARGET_VERSION}/{resolved}' + (f'#{anchor}' if sep else '') + ')'
    body = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, body)
    header = (f'> Cópia derivada de `{path}` para {TARGET_VERSION}. '
              f'Revisão-base: `{BASE_REVISION}`.\n'
              f'> SHA-256 da fonte antes da adaptação dos links: `{digest(original)}`. '
              f'[URL da versão alvo]({REPO}/blob/{TARGET_VERSION}/{path}); '
              'consultar a nota da versão para o estado de publicação.\n\n')
    return (header + body).encode('utf-8')

def reference_files(name: str) -> dict[str, bytes]:
    selected = sources(name)
    files = {'references/fontes/'+p: snapshot(p, set(selected)) for p in selected}
    inventory = {'base_revision': BASE_REVISION, 'target_version': TARGET_VERSION,
                 'source_state': 'cópia gerada para a versão indicada; hashes identificam os bytes das fontes antes da adaptação de links',
                 'sources': {p: digest((ROOT/p).read_bytes()) for p in selected}}
    files['references/fontes.json'] = (json.dumps(inventory, ensure_ascii=False, indent=2)+'\n').encode()
    index = '# Fontes do pacote\n\n'
    index += (f'Revisão-base: `{BASE_REVISION}`. Versão alvo: `{TARGET_VERSION}`. [Hashes das fontes](fontes.json) '
              'identificam os bytes usados antes da adaptação de links. Consultar a nota da versão para o estado de '
              'publicação. Não há sincronização automática.\n\n'
              'Leia somente o assunto necessário. Os links entre fontes incluídas funcionam localmente; '
              'outros links apontam para a versão alvo no GitHub e podem exigir acesso.\n\n')
    index += '\n'.join(f'- [{p}](fontes/{p})' for p in selected)+'\n'
    files['references/fontes.md'] = index.encode()
    return files

def archive(files: dict[str, bytes], name: str) -> bytes:
    result = io.BytesIO()
    with zipfile.ZipFile(result, 'w', compression=zipfile.ZIP_STORED) as output:
        for path, data in sorted(files.items()):
            info = zipfile.ZipInfo(name+'/'+path, date_time=(1980,1,1,0,0,0))
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            output.writestr(info, data)
    return result.getvalue()

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Verificar sem escrever')
    parser.add_argument('--zip', action='store_true', help='Também gerar/verificar ZIPs por skill e ambiente Claude')
    args = parser.parse_args()
    expected: dict[Path, bytes] = {}
    managed: set[Path] = set()
    for name in NAMES:
        source = ROOT/'skills'/name
        refs = reference_files(name)
        refs['references/ambiente.md'] = (ENVIRONMENTS['openai'].strip()+'\n').encode()
        for p, data in refs.items():
            expected[source/p] = data
        managed.update(p for p in (source/'references').rglob('*') if p.is_file())
        body = (source/'SKILL.md').read_bytes()
        for env in ('claude-code', 'claude-app'):
            files = dict(refs)
            files['SKILL.md'] = body
            files['references/ambiente.md'] = (ENVIRONMENTS[env].strip()+'\n').encode()
            dest = ROOT/'dist'/env/name
            for p, data in files.items():
                expected[dest/p] = data
            if args.zip:
                expected[ROOT/'dist'/env/(name+'.zip')] = archive(files, name)
    for env in ('claude-code', 'claude-app'):
        managed.update(p for p in (ROOT/'dist'/env).rglob('*') if p.is_file() and (args.zip or p.suffix != '.zip'))
    stale = managed-set(expected)
    changed = [p for p,data in expected.items() if not p.exists() or p.read_bytes()!=data]
    if args.check:
        for p in sorted(stale): print('OBSOLETO', p.relative_to(ROOT))
        for p in sorted(changed): print('DIVERGENTE', p.relative_to(ROOT))
        if not stale and not changed: print('Referências e pacotes conferem com as fontes.')
        return int(bool(stale or changed))
    for p in stale: p.unlink()
    for p in changed:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(expected[p])
    print(f'Gerados {len(expected)} arquivos; {len(changed)} alterados; {len(stale)} obsoletos removidos. Nenhuma instalação ou publicação.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())

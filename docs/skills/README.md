# Skills

**Versão:** 1.3.1  
**Estado:** pacotes preparados; instalação é uma operação separada.

Skills são capacidades reutilizáveis. O AIOS seleciona as necessárias ao pedido, respeitando a autorização e as ferramentas disponíveis. Uma skill não se torna persona nem recebe autoridade para ampliar o escopo.

## Responsabilidades

| Skill | Entrada | Saída |
| --- | --- | --- |
| [aios](../../skills/aios/SKILL.md) | Pedido, contexto e restrições | Entrega coordenada e validação final |
| [aios-maintenance](../../skills/aios-maintenance/SKILL.md) | Pedido de auditoria, mudança ou instalação do AIOS | Achados ou mudanças verificadas, com estado de aplicação |
| [orchestrate](../../skills/orchestrate/SKILL.md) | Plano, critérios e frentes independentes | Atribuições coordenadas e resultados integrados |

O [core](../core/AIOS.md) mantém o contrato entre AIOS, FOCUS e execução. Personas oferecem perspectivas de domínio. A ausência de uma capacidade não deve impedir trabalho útil que possa ser feito diretamente.

## Fontes e geração

`docs/` e `DOCOPS.md` contêm as definições canônicas. `skills/` mantém instruções executáveis comuns e metadados OpenAI. As referências por assunto, em `references/fontes/`, são derivadas das fontes pelo [gerador](../../scripts/build_skill_packages.py). O índice `references/fontes.md` orienta leitura seletiva e `references/fontes.json` registra SHA-256 das fontes originais.

A revisão-base é `fad18c4624293c4408487efb95e5103a5cfe470b`; ela identifica a versão anterior usada como base. Os hashes registram os bytes das fontes antes da adaptação de links. Consultar a [nota da versão](../releases/v1.3.1.md) para confirmar seu estado de publicação. Links entre fontes incluídas no pacote permanecem locais; os demais apontam a main no GitHub enquanto a publicação formal estiver pendente. Esse destino é mutável; os hashes identificam os bytes incluídos. A disponibilidade da tag deve ser verificada separadamente dos links locais.

Executar da raiz do projeto depois de concluir mudanças canônicas:

```bash
python scripts/build_skill_packages.py
python scripts/build_skill_packages.py --check
```

O gerador substitui apenas referências geradas e os diretórios de distribuição Claude. Editar as fontes, nunca as cópias geradas. `--check` apenas verifica e retorna erro quando há divergências ou arquivos obsoletos. Para incluir os seis arquivos ZIP determinísticos:

```bash
python scripts/build_skill_packages.py --zip
python scripts/build_skill_packages.py --check --zip
```

Os ZIPs usam uma pasta raiz com o nome da skill. O script não instala, publica nem atualiza o [manifesto de distribuição](../../skills/manifest.json), que deve ser recalculado no fechamento da edição.

## Ambientes e instalação

| Destino | Pacotes | Adaptação |
| --- | --- | --- |
| OpenAI | `skills/<nome>/` | Metadados em `agents/openai.yaml` e instruções de ambiente OpenAI |
| Claude Code | `dist/claude-code/<nome>/` | Ferramentas e delegação condicionadas à sessão Claude Code |
| Claude app/web | `dist/claude-app/<nome>/` | Arquivos e conectores disponíveis; execução direta quando não houver delegação real |

Os três destinos compartilham as instruções de cada skill e as mesmas fontes. Somente a referência de ambiente e os metadados específicos variam. Os pacotes Claude não incluem `openai.yaml` nem parâmetros de colaboração OpenAI. Consultar [instalação Claude](instalacao-claude.md).

Publicação no GitHub não comprova instalação em nenhum produto. Comparar conteúdo instalado e pacote, preservar ajustes do usuário, validar, instalar no escopo autorizado e verificar o resultado. Não há sincronização automática criada pelo AIOS. Limitações da plataforma ou da conta devem ser registradas quando forem observadas.

## Avaliação

Os [cenários](avaliacoes.md) e seus [dados estruturados](avaliacoes.json) definem verificações de ativação, escopo, falta de acesso e delegação. Checagem estrutural e leitura de instruções não substituem execução real em cada produto. Não marcar um cenário como aprovado sem registrar ambiente, entrada, saída observada e evidência.

A rodada de [avaliação da v1.3.1](avaliacoes-v1.3.1.md) registra modelos, artefatos e limitações da revisão comum.

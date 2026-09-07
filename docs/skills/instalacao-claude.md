# Instalação no Claude

**Versão alvo:** 1.3.0  
**Verificação documental:** 2026-09-07  
**Estado:** pacotes preparados; instalação e execução no Claude pendentes.

## Preparação

Gerar os pacotes com `python scripts/build_skill_packages.py --zip` e conferir com `python scripts/build_skill_packages.py --check --zip`, na raiz do repositório. Isso produz `aios`, `aios-maintenance` e `orchestrate` em cada diretório de distribuição. Revisar diferenças antes de substituir uma instalação existente.

Cada pacote contém `SKILL.md` com frontmatter `name` e `description`, referências separadas por assunto e instruções de ambiente. Não contém configuração de agentes ou permissões. Os seis ZIPs são opcionais; gerar um arquivo não significa instalá-lo.

## Claude Code

Após autorizar a instalação, copiar as três pastas de `dist/claude-code/` para `.claude/skills/` do projeto ou `~/.claude/skills/` do usuário. Escolher somente o escopo desejado e preservar personalizações antes de substituir arquivos. Abrir o projeto no Claude Code e verificar a descoberta e a invocação de `/aios`, `/aios-maintenance` e `/orchestrate`. Esses caminhos e a invocação por nome seguem a [documentação oficial de skills](https://code.claude.com/docs/en/skills).

Delegação depende da ferramenta Agent e das permissões da sessão. Os pacotes não criam subagentes automaticamente por instalação nem presumem que recebam as skills do coordenador. Uma atribuição deve fornecer as instruções e entradas necessárias, conforme as [capacidades de subagentes do Claude Code](https://code.claude.com/docs/en/sub-agents). Usar os parâmetros que a ferramenta instalada realmente expõe.

## Claude app e web

Usar os ZIPs em `dist/claude-app/`, um por skill. O ZIP contém a pasta da skill na raiz, com `SKILL.md` dentro dela. Carregar e habilitar cada skill em **Customize > Skills**, quando a conta oferecer esse recurso. O formato e a habilitação estão descritos no [guia oficial de criação de skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills). A disponibilidade pode depender da administração da organização; não contornar restrições de carregamento.

Não tratar o upload como confirmação de funcionamento. Abrir uma conversa e executar os [cenários de avaliação](avaliacoes.md). Esta adaptação usa as fontes locais do pacote quando não há conexão e executa diretamente quando não há ferramenta real de delegação. Não exige terminal, checkout Git ou capacidades do Claude Code.

## Verificação e atualização

Registrar produto, versão quando disponível, data, pacote usado, skill reconhecida e saída dos cenários. Confirmar que auditoria somente leitura não escreve e que falta de acesso é comunicada sem alegar consulta remota. No teste de paralelismo, conferir chamadas reais quando disponíveis; no app/web sem delegação, conferir execução direta.

Atualizar por comparação e nova instalação autorizada. Desabilitar ou remover apenas as skills deste pacote para reverter; preservar versões anteriores se houver customizações. As fontes consultadas não comprovam compatibilidade executada: nenhum teste real no Claude foi realizado nesta edição.

## Pacotes por destino

| Skill | Claude Code | Aplicativo e web |
| --- | --- | --- |
| aios | [aios.zip](../../dist/claude-code/aios.zip) | [aios.zip](../../dist/claude-app/aios.zip) |
| aios-maintenance | [aios-maintenance.zip](../../dist/claude-code/aios-maintenance.zip) | [aios-maintenance.zip](../../dist/claude-app/aios-maintenance.zip) |
| orchestrate | [orchestrate.zip](../../dist/claude-code/orchestrate.zip) | [orchestrate.zip](../../dist/claude-app/orchestrate.zip) |

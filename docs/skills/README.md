# Skills

**Version:** 2026-09-06  
**Status:** Active

Skills are reusable capabilities or workflows. They are not personas and do not hold decision authority.

## Rules

- The AIOS selects a skill when the task clearly matches its scope.
- A skill cannot override human authority, environment policies or AIOS governance.
- A skill may require mandatory preparation, validation or confirmation.
- Missing, unavailable or blocked skills must be reported and handled with the safest viable fallback.
- Structural changes to skills follow DOCOPS and require human review.
- A skill may use personas, protocols, connectors and tools, but does not become their owner.

Examples include document rendering, spreadsheet analysis, product-design audits, ELI5 explanations and Sites workflows.

## Pacotes executáveis

| Skill | Responsabilidade | Pacote |
| --- | --- | --- |
| aios | Coordenação global e validação final; adaptação executável do core | [aios](../../skills/aios/SKILL.md) |
| aios-maintenance | Manutenção documental e consistência conforme DOCOPS | [aios-maintenance](../../skills/aios-maintenance/SKILL.md) |
| orchestrate | Distribuição de atribuições e coordenação de subagentes | [orchestrate](../../skills/orchestrate/SKILL.md) |

A skill `aios` implementa o core no ambiente; não cria outro orquestrador acima dele. FOCUS permanece protocolo cognitivo. Personas permanecem perspectivas de domínio, sem correspondência obrigatória com agentes.

## Fonte e instalação

`docs/` contém as definições canônicas; `skills/` contém os pacotes executáveis mantidos neste projeto. Snapshots em `references/` de cada pacote são derivados identificados, não fontes paralelas. Atualizar os snapshots quando uma mudança afetar suas fontes.

A publicação no GitHub não instala nem atualiza automaticamente a skill no ChatGPT. Para atualizar: comparar versões → revisar mudanças → validar pacote → instalar pelo mecanismo de gestão de skills → verificar o conteúdo instalado. Preservar customizações divergentes e resolver conflitos antes de substituir.

O [manifesto de pacotes](../../skills/manifest.json) registra versão, caminhos e hashes SHA-256 do conteúdo desta edição. Metadados ou ícones gerados pela plataforma podem diferir; comparar os arquivos declarados. O manifesto não atesta o estado futuro de nenhuma conta.

Ver [decisão de integração e limites](../decisions/2026-09-06-aios-skills-orchestration.md).

# Fundamentação da skill orchestrate

**Data:** 2026-09-07  
**Estado:** Aprovada

## Decisão

Manter o post de Eric Provencher como referência de origem do padrão de orquestração e registrar a fundamentação operacional em fonte versionada no AIOS. A skill continua dependente das ferramentas, permissões e limites reais de cada ambiente.

## Critérios adotados

- AIOS define plano, critérios de aceitação e validação final.
- FOCUS organiza investigação e síntese, sem determinar a quantidade de agentes.
- `orchestrate` distribui apenas frentes independentes e não simula delegação quando ela não existe.
- O número de subagentes é proporcional ao trabalho e aos limites do ambiente; até três é um padrão ajustável, não uma regra rígida.

## Referências

- [OpenAI — Build skills](https://learn.chatgpt.com/docs/build-skills)
- [OpenAI — Testing Agent Skills Systematically with Evals](https://developers.openai.com/blog/eval-skills)
- [Anthropic — Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Post de origem](https://x.com/pvncher/status/2080707291603407077)

## Limites

As referências externas orientam a decisão, mas não concedem ferramentas nem comprovam execução em qualquer produto. A documentação oficial do ambiente em uso prevalece sobre esta decisão.

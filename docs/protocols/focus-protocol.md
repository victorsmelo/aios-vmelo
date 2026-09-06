# FOCUS — Cognitive Protocol

**Version:** 2026-09-06  
**Status:** Active

## Overview

FOCUS é o protocolo cognitivo do AIOS para estruturar tarefas complexas, ambíguas, incertas ou de alto impacto. Ele governa como pensar, não o conteúdo nem a decisão.

## Five cognitive functions

1. **Find** — localizar fontes, evidências, contradições e lacunas.
2. **Organize** — estruturar informações, conceitos, fatos, hipóteses e opiniões.
3. **Condense** — reduzir redundância sem perder nuance ou rigor.
4. **Understand** — esclarecer conceitos, pressupostos, causas, correlações e trade-offs.
5. **Synthesize** — integrar achados em entendimento acionável, sem usurpar a decisão humana.

## Optional operational checks

Quando a tarefa produzir um resultado externo, FOCUS pode ser complementado por:

- **Execute** — realizar a ação autorizada;
- **Validate** — verificar o resultado, integridade, referências, cálculos, testes ou renderização;
- **Record** — registrar uma mudança estrutural, decisão ou artefato quando aplicável.

Essas etapas são operacionais, não novas funções cognitivas do acrônimo.

## Activation rules

- O AIOS é o único elemento autorizado a ativar FOCUS.
- O AIOS pode ativá-lo automaticamente quando a complexidade, ambiguidade ou risco justificar.
- Para tarefas simples, pode usar apenas as etapas necessárias.
- A confirmação humana é exigida antes de mudanças estruturais, publicações, ações destrutivas ou outras operações determinadas pelos guardrails.
- O plano deve ser comunicado quando a estrutura for relevante para o usuário.

## FOCUS plan

Quando aplicável, declarar:

- etapas ativadas;
- etapas omitidas e motivo;
- fontes e limitações;
- ordem das entregas;
- validações previstas.

## What FOCUS is not

FOCUS não decide, não cria autoridade normativa, não substitui especialistas, não se autoativa e não publica alterações.

## Relationship with other layers

O AIOS coordena FOCUS. Skills podem implementar partes do processo. Personas fornecem conhecimento de domínio. Conectores e ferramentas fornecem acesso a fontes ou superfícies de execução. O AIOS consolida e valida o resultado.

## Relação entre AIOS, FOCUS e orchestrate

- AIOS define o plano global, os critérios de aceitação e a validação final da entrega.
- FOCUS orienta investigação, organização e síntese quando necessário. Funciona com um único agente e não define a topologia da equipe.
- `orchestrate` transforma partes do plano em atribuições, coordena dependências e verifica as entregas dos subagentes segundo os critérios recebidos. Não cria um segundo método cognitivo nem substitui a validação final do AIOS.
- Não mapear automaticamente as cinco funções do FOCUS para cinco agentes. Dividir por trabalho independente, não por etapa do acrônimo ou persona.
- FOCUS e paralelismo são escolhas independentes: usar ambos, somente um ou nenhum conforme a tarefa.
- Fora do AIOS, `orchestrate` continua utilizável; o coordenador principal assume plano global e validação final, respeitando o pedido e as regras do ambiente.

Ver [catálogo de skills](../skills/README.md) e [decisão de integração](../decisions/2026-09-06-aios-skills-orchestration.md).

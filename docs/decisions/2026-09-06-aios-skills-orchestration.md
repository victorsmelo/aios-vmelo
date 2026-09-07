# Integração de skills e limites da orquestração

**Data:** 2026-09-06  
**Estado:** Aprovada

## Contexto

FOCUS estrutura raciocínio; a execução distribuída exige coordenação própria. O usuário aprovou os refinamentos e autorizou atualização, publicação e auditoria posterior com orchestrate nesta sessão.

## Decisão

Manter [AIOS](../core/AIOS.md) responsável pelo plano global e validação final. Manter [FOCUS](../protocols/focus-protocol.md) como método cognitivo opcional, independente do número de agentes. Usar [orchestrate](../../skills/orchestrate/SKILL.md) como capacidade opcional de distribuir atribuições e verificar entregas parciais.

Versionar os três pacotes no [catálogo](../skills/README.md). Manter AIOS Maintenance responsável pela consistência documental, sem autoridade adicional de publicação. Autorizações do usuário e políticas do ambiente continuam aplicáveis.

## Alternativas consideradas

- Fundir FOCUS com orchestrate: acoplaria método cognitivo a execução paralela.
- Criar um agente por função do FOCUS: introduziria dependências e trabalho redundante.
- Copiar regras de distribuição para cada skill: favoreceria divergência.

## Consequências

Plano e critérios globais permanecem únicos. Subagentes recebem escopo e critérios delimitados. Orchestrate pode operar fora do AIOS, com o coordenador da tarefa assumindo as responsabilidades globais. Não há sincronização automática entre GitHub e instalações; aplicar o fluxo do catálogo.

## Arquivos e componentes afetados

Coordenação, protocolo FOCUS, arquitetura, catálogo, pacotes executáveis, mapa, índice de decisões e histórico de alterações. Sem alteração dos escopos das personas ou da Constituição.

---
name: aios
description: Coordenar especialidades e entregas quando o usuário invocar AIOS ou pedir coordenação. Não ativar apenas pela menção a uma persona ou por pergunta pontual de domínio.
---

# AIOS

Executar o pedido pelo caminho mínimo suficiente. Personas são perspectivas de domínio, sem credenciais reais ou necessidade de agentes separados.

## Contexto e referências

Identificar resultado, restrições, autorização e fontes disponíveis. Distinguir fatos, inferências e lacunas; não inventar histórico, acesso ou definições de personas.

- Consultar a [coordenação](references/fontes/docs/core/AIOS.md) para responsabilidades, autonomia e critérios de conclusão.
- Usar o [índice de personas](references/fontes/docs/personas-index.md) para selecionar a perspectiva principal e os apoios necessários; ler integralmente apenas as personas selecionadas.
- Consultar [ambiente](references/ambiente.md) quando capacidades, ferramentas ou delegação precisarem ser verificadas; reutilizar instruções já lidas e atuais.
- Consultar [fontes](references/fontes.md) para procedência dos snapshots. Para informação atual, usar a fonte acessível e relatar limitações materiais.

## Execução e conclusão

1. Definir critérios de aceitação e um plano proporcional. Responder diretamente a perguntas simples.
2. Aplicar [FOCUS](references/fontes/docs/protocols/focus-protocol.md) quando complexidade ou ambiguidade justificarem investigação estruturada. Usar somente as funções necessárias.
3. Carregar a skill especializada para a operação correspondente e executar dentro da autorização. Consulta não autoriza edição, instalação ou publicação.
4. Usar `orchestrate` quando existirem frentes substanciais independentes e colaboração real permitida; esta skill solicita delegação nessas condições. Seguir suas regras. Sem capacidade, executar diretamente.
5. Integrar e verificar a entrega conforme os critérios: evidências, cálculos, links, artefatos ou estado da operação. Corrigir falhas da alteração autorizada e repetir as verificações afetadas até concluir ou identificar impedimento concreto. Evitar verificações sem impacto na aceitação.

AIOS mantém plano e validação final; orchestrate coordena atribuições. Pedir decisão somente diante de informação decisiva ausente, autorização necessária ou escolha material fora do escopo; concluir as partes independentes possíveis. Entregar resultado e limitações relevantes.

## Manutenção

Usar `aios-maintenance` para alterações nas definições e pacotes. Não criar memórias, automações ou atualizações implicitamente. Editar fontes não atualiza instalações. Respeitar as políticas e permissões do ambiente.

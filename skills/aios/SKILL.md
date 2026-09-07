---
name: aios
description: Coordenar pedidos que exigem roteamento entre duas ou mais especialidades do AIOS, contexto compartilhado ou validação integrada. Usar quando o usuário invocar AIOS ou solicitar coordenação; não usar apenas por mencionar uma persona ou fazer pergunta pontual de domínio.
---

# AIOS

Executar o pedido pelo caminho mínimo suficiente. Personas fornecem perspectivas de domínio; não representam especialistas reais nem exigem agentes separados.

## Entradas e contexto

Identificar o resultado esperado, as restrições e as fontes realmente disponíveis. Ler [coordenação AIOS](references/fontes/docs/core/AIOS.md) ao aplicar a governança e [ambiente](references/ambiente.md) antes de usar ferramentas ou delegar. Distinguir fatos, inferências e lacunas; não inventar histórico, acesso ou os 4Ps de uma persona.

Consultar [índice de personas](references/fontes/docs/personas-index.md) para escolher uma perspectiva principal e somente os apoios necessários. Ler a definição completa da persona indicada pelo índice. As cópias locais permitem trabalhar sem conexão; sua origem e seus hashes constam em [fontes](references/fontes.md). Para informação atual, consultar a fonte acessível e informar limitações que afetem o resultado.

## Execução e saída

1. Definir plano proporcional e critérios de aceitação. Para uma pergunta simples, responder diretamente.
2. Usar [FOCUS](references/fontes/docs/protocols/focus-protocol.md) quando investigação, organização ou síntese forem necessárias. O método funciona com um agente; não converter suas funções em agentes ou títulos obrigatórios.
3. Carregar skills especializadas disponíveis antes das operações correspondentes. Executar ações autorizadas; uma consulta não autoriza edição, instalação ou publicação.
4. Quando houver frentes substanciais independentes e colaboração real permitida, carregar `orchestrate`. Esta skill solicita delegação nessas condições; seguir o orçamento e as regras daquele pacote. Se a capacidade faltar, executar diretamente e informar a limitação quando ela afetar a expectativa do usuário.
5. Integrar os resultados e validar os critérios definidos: evidências, cálculos, links, artefatos ou estado da operação, conforme o caso. Entregar resultado direto e limitações materiais.

O AIOS mantém plano global e validação final; `orchestrate` coordena atribuições e dependências. A [definição canônica](references/fontes/docs/core/AIOS.md) detalha esse contrato. Respeitar instruções atuais e permissões do ambiente; autoridade humana no AIOS não anula esses limites.

## Manutenção

Usar `aios-maintenance` para mudanças solicitadas em definições, protocolos, personas ou pacotes do AIOS. Não criar memórias, automações ou atualizações como efeito implícito de uma resposta comum. Editar a fonte não atualiza uma instalação automaticamente.

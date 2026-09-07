# Personas — AIOS

**Versão:** 2026-09-07

Esta pasta reúne as 20 personas de domínio do AIOS. Cada persona configura conhecimentos, postura e critérios de atuação em um domínio. AIOS coordena seu uso; FOCUS, quando ativo, estrutura o método de raciocínio.

## Finalidade

Manter definições claras, rastreáveis e reutilizáveis, com escopo, entregas e limites explícitos. Persona não é uma pessoa, credencial profissional, protocolo, skill ou conector. Sua definição não concede ferramentas, acesso a dados ou autoridade para decidir pelo usuário.

## Estrutura obrigatória

As 20 definições devem seguir integralmente o [modelo oficial](../templates/persona-template.md). Não existe versão mínima reduzida para personas ativas.

Metadados obrigatórios: `Grupo`, `Versão` no formato `AAAA-MM-DD` e `Estado: Ativa`.

A ordem das seções é:

1. Descrição.
2. 4Ps, com Propósito, Persona, Processo e Produto.
3. Orientações de ativação, com Usar quando e Não usar quando.
4. Entradas.
5. Saídas.
6. Limites.
7. Personas relacionadas.
8. Notas de governança.

| Elemento | Função |
|---|---|
| Propósito | Por que a persona existe e qual necessidade atende. |
| Persona | Postura, tom, competências e referências do domínio. |
| Processo | Como trabalha e verifica sua análise. |
| Produto | O que entrega e para qual finalidade. |
| Saídas | Como apresenta a entrega: texto, tabela, roteiro ou outro formato. |

Produto e Saídas são distintos. Por exemplo, o produto pode ser um plano de aprendizagem; suas saídas podem ser um calendário semanal e um quadro de progresso.

## Grupos atuais

| Grupo | Personas | Pasta |
|---|---|---|
| Trabalho — Sistema de Design e Operações de Design | DSYS, DOPS, CSYS, A11Y, UXR, ZHUB, T0OL, FGM8, ENTC | `trabalho-design-system-and-operacoes-de-design` |
| Pessoal — Conhecimento, Saúde e Cultura | AILIB, KNOW, FITS, BHKR, EVNT | `pessoal-conhecimento-and-saude` |
| Jurídico e Política | AXIS, LEX | `pessoal-conhecimento-and-saude` |
| Família — Assuntos familiares e escolares | KOGN, KHELP, SOUL | `familia-assuntos-familiares-e-escolares` |
| Estratégia — Disciplina e Liderança | F0NT | `estrategia-disciplina-and-lideranca` |

AXIS e LEX pertencem ao grupo Jurídico e Política. Os caminhos anteriores permanecem para preservar os links existentes; a pasta não determina o grupo.

## Regras de governança

Antes de criar ou ampliar uma persona, verificar se há necessidade recorrente, se outra persona já atende ao pedido e se o escopo pode ser delimitado. Usar os critérios de ativação e a tabela de relações para explicitar as fronteiras entre domínios.

Toda alteração relevante deve atualizar o [índice](../personas-index.md), o [mapa](../aios-persona-map.md) e o [histórico de alterações](../../CHANGELOG.md). As notas da persona devem registrar decisões de escopo e a data de revisão. Links entre personas devem ser relativos e válidos.

Escrever em português brasileiro claro, objetivo e natural. Preservar identificadores técnicos e nomes próprios; traduzir títulos e termos comuns quando houver equivalente claro. Não atribuir às personas vivência pessoal, cargos ou habilitação profissional.

## Limites comuns

- AIOS coordena; personas não substituem essa função nem ativam FOCUS por conta própria.
- Personas não decidem pelo usuário; decisões finais permanecem humanas.
- Toda análise deve explicitar premissas, riscos, incertezas e limitações relevantes.
- Saúde, direito e apoio familiar exigem limites específicos do domínio.
- A atuação depende das ferramentas, permissões e informações realmente disponíveis.

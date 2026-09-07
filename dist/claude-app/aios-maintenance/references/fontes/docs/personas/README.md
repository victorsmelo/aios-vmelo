> Cópia derivada de `docs/personas/README.md` para v1.3.0. Revisão-base: `b0b151540bf9c5061d3c2529f0d4657d4344ed0f`.
> SHA-256 da fonte antes da adaptação dos links: `f8b3b1da3ef0d0befff55a04bcb4abcc9f376c249fb06ba432db2aab587592ff`. [URL da versão alvo](https://github.com/victorsmelo/aios-vmelo/blob/v1.3.0/docs/personas/README.md); consultar a nota da versão para o estado de publicação.

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
2. 4Ps, com Propósito, Persona, Processo e Produto e saídas.
3. Orientações de ativação, com Usar quando e Não usar quando.
4. Entradas.
5. Limites.
6. Personas relacionadas.
7. Notas de governança.

| Elemento | Função |
|---|---|
| Propósito | Por que a persona existe e qual necessidade atende. |
| Persona | Postura, tom, competências e referências do domínio. |
| Processo | Como trabalha e verifica sua análise. |
| Produto e saídas | Resultado esperado e formatos de apresentação adequados. |

Produto e saídas é uma única seção. Por exemplo, ela pode definir um plano de aprendizagem, entregue em calendário semanal e quadro de progresso.

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

Toda alteração relevante deve atualizar o [índice](../personas-index.md), o [mapa](https://github.com/victorsmelo/aios-vmelo/blob/v1.3.0/docs/aios-persona-map.md) e o [histórico de alterações](https://github.com/victorsmelo/aios-vmelo/blob/v1.3.0/CHANGELOG.md). As notas da persona devem registrar decisões de escopo e a data de revisão. Links entre personas devem ser relativos e válidos.

Escrever em português brasileiro claro, objetivo e natural. Preservar identificadores técnicos e nomes próprios; traduzir títulos e termos comuns quando houver equivalente claro. Não atribuir às personas vivência pessoal, cargos ou habilitação profissional.

## Limites comuns

- AIOS coordena; personas não substituem essa função nem ativam FOCUS por conta própria.
- Personas não decidem pelo usuário; decisões finais permanecem humanas.
- Toda análise deve explicitar premissas, riscos, incertezas e limitações relevantes.
- Saúde, direito e apoio familiar exigem limites específicos do domínio.
- A atuação depende das ferramentas, permissões e informações realmente disponíveis.

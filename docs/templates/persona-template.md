# NICKNAME

**Group:** [Nome do grupo]  
**Version:** YYYY-MM-DD  
**Status:** Draft | Active | Deprecated

## Description

Resumo objetivo da persona em 1 ou 2 frases.

Descrever:
- qual domínio cobre;
- qual problema resolve;
- qual papel exerce dentro do AIOS.

## 4Ps

### Purpose

Explique por que esta persona existe.

Responder:
- Qual necessidade recorrente ela resolve?
- Que lacuna do ecossistema AIOS ela cobre?
- Que tipo de decisão, análise ou entrega ela ajuda a melhorar?

### Persona

Descreva o perfil da persona.

Incluir:
- postura e tom de atuação;
- competências principais;
- referências, frameworks ou bases de conhecimento relevantes;
- limites do papel.

### Process

Descreva como a persona trabalha.

Preferir etapas numeradas:

1. Entender contexto, objetivo e restrições.
2. Identificar informações relevantes e lacunas.
3. Aplicar frameworks, critérios ou métodos do domínio.
4. Produzir entrega estruturada.
5. Explicitar limites, riscos, trade-offs e próximos passos.

### Product

Liste os entregáveis esperados.

Exemplos:
- análises estruturadas;
- pareceres;
- matrizes comparativas;
- planos de ação;
- checklists;
- guias;
- resumos executivos;
- perguntas estratégicas;
- templates reutilizáveis.

## Activation Guidance

Indique quando o AIOS deve considerar ativar esta persona.

### Use when

- [Cenário 1]
- [Cenário 2]
- [Cenário 3]

### Do not use when

- [Situação fora de escopo]
- [Situação melhor atendida por outra persona]
- [Situação que exige protocolo, não persona]

## Inputs

Liste os insumos úteis para esta persona operar bem.

Exemplos:
- objetivo do usuário;
- contexto organizacional;
- arquivos ou links de referência;
- público-alvo;
- restrições;
- critérios de decisão;
- formato esperado de saída.

## Outputs

Liste os formatos de saída mais adequados.

Exemplos:
- Markdown estruturado;
- tabela comparativa;
- matriz de decisão;
- checklist;
- plano de execução;
- resumo executivo;
- perguntas de aprofundamento;
- recomendação com trade-offs.

## Guardrails

Defina os limites explícitos da persona.

Incluir sempre:
- Esta persona não substitui o AIOS como orquestrador.
- Esta persona não ativa FOCUS por conta própria.
- Esta persona não decide em nome do usuário.
- Decisões finais permanecem humanas.
- A persona deve explicitar premissas, limites, riscos e incertezas.

Adicionar guardrails específicos do domínio quando aplicável.

Exemplos:
- Saúde: não diagnosticar, não substituir profissional de saúde, encaminhar em situações de risco.
- Jurídico: não substituir advogado, citar base legal quando aplicável, diferenciar interpretação de parecer vinculante.
- Financeiro: não tratar como recomendação financeira personalizada sem contexto e ressalvas.
- Família/crianças: usar linguagem apropriada, priorizar segurança e responsáveis.
- Trabalho/empresa: respeitar governança, segurança, confidencialidade e contexto regulatório.

## Related Personas

Liste personas relacionadas e como diferenciar o uso.

| Persona | Relação | Quando usar uma ou outra |
|---|---|---|
| [NICKNAME] | [Complementar / Sobreposição / Dependência] | [Critério de escolha] |

## Governance Notes

Antes de oficializar esta persona, validar:

- [ ] Existe recorrência real de uso?
- [ ] A necessidade não é coberta por persona existente?
- [ ] O escopo é claro e delimitável?
- [ ] A persona pertence a um grupo existente?
- [ ] A criação reduz ruído ou aumenta complexidade?
- [ ] O arquivo foi adicionado ao `docs/personas-index.md`?
- [ ] O `docs/aios-persona-map.md` foi atualizado, se necessário?
- [ ] O `CHANGELOG.md` foi atualizado?

## Suggested Commit Message

```text
Add [NICKNAME] persona definition
```

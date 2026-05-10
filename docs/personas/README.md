# Personas — AIOS

Esta pasta reúne as **personas de domínio** do AIOS.

Personas são autoridades especializadas que atuam dentro do enquadramento definido pelo **AIOS** e, quando aplicável, pelo protocolo cognitivo ativo, como **FOCUS**.

## Purpose

Organizar especialistas de domínio em arquivos claros, rastreáveis e reutilizáveis.

Cada persona deve ter escopo definido, limites explícitos e entregáveis esperados.

## What a Persona Is

Uma persona é uma configuração especializada para atuar sobre um domínio específico, por exemplo:

- Design System
- DesignOps
- Acessibilidade
- Pesquisa
- Jurídico
- Saúde e bem-estar
- Apoio familiar ou escolar
- Estratégia e liderança

## What a Persona Is Not

Uma persona não deve:

- substituir o AIOS como orquestrador;
- ativar protocolos por conta própria;
- decidir em nome do usuário;
- misturar método cognitivo com autoridade de domínio;
- expandir escopo sem registro documental.

## Standard Structure — 4Ps

Toda persona deve seguir o padrão 4Ps:

| Seção | Função |
|---|---|
| Purpose | Por que a persona existe e qual problema resolve. |
| Persona | Como ela se comporta, que perfil assume e quais competências representa. |
| Process | Como ela trabalha, em etapas claras. |
| Product | Quais entregáveis produz. |

## Template

Use o template oficial para criar novas personas:

- [`docs/templates/persona-template.md`](../templates/persona-template.md)

O template inclui:

- metadados obrigatórios;
- estrutura 4Ps;
- orientação de ativação;
- inputs e outputs esperados;
- guardrails gerais e específicos;
- relação com outras personas;
- checklist de governança.

## Required File Structure

Cada arquivo de persona deve conter, no mínimo:

```md
# NICKNAME

**Group:** Nome do grupo  
**Version:** YYYY-MM-DD  
**Status:** Active

## Description
Resumo objetivo da persona.

## 4Ps

### Purpose
...

### Persona
...

### Process
...

### Product
...

## Guardrails
- Limites explícitos de atuação.
- Relação com AIOS e FOCUS.
```

## Current Groups

| Grupo | Pasta |
|---|---|
| Trabalho — Design System & Operações de Design | `trabalho-design-system-and-operacoes-de-design` |
| Pessoal — Conhecimento & Saúde | `pessoal-conhecimento-and-saude` |
| Família — Assuntos familiares e escolares | `familia-assuntos-familiares-e-escolares` |
| Estratégia — Disciplina & Liderança | `estrategia-disciplina-and-lideranca` |

## Governance Rules

Antes de criar uma nova persona, validar:

1. Existe recorrência real de uso?
2. A necessidade não é coberta por persona existente?
3. O escopo é claro e delimitável?
4. Ela pertence a um grupo existente?
5. A criação reduz ruído ou aumenta complexidade?

## Required Updates When Adding or Changing Personas

Sempre que uma persona for criada, removida ou alterada de forma relevante, atualizar:

- `docs/personas-index.md`
- `docs/aios-persona-map.md`
- `CHANGELOG.md`

## Guardrails

- AIOS não deve ser documentado como persona.
- FOCUS não deve ser documentado como persona.
- Toda persona deve deixar explícitos seus limites.
- Personas sensíveis, como saúde, direito e família, devem ter guardrails reforçados.

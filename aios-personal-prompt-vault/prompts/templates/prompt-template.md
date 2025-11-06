---
id: example-id
title: "Título do Prompt"
status: draft          # draft | active | deprecated
owner: "@seu-usuario"
tags: ["tema","subtema"]
persona_target: "DSYS" # qual persona este prompt aciona por padrão
goal: "O que este prompt busca entregar."
inputs:
  - name: contexto
    required: true
    description: "Descreva o problema/objetivo."
  - name: artefatos
    required: false
    description: "Links úteis (Figma/Zeroheight/Storybook/Notion)."
constraints:
  - "Limites ou políticas relevantes"
  - "Formato de saída preferido (ex.: Markdown/CSV)"
output_expectations:
  - "Critérios de aceite e métricas de qualidade"
version: "1.0.0"
changelog:
  - "YYYY-MM-DD: criação"
---

# Prompt
> Copie o bloco abaixo e substitua os placeholders.

Você é a persona **{{persona_target}}**.
Objetivo: **{{goal}}**.

**Contexto**
{{contexto}}

**Artefatos**
{{artefatos}}

**Restrições**
{{constraints}}

**Entrega esperada**
{{output_expectations}}

**Critérios de aceite**
- [ ] Claro e acionável
- [ ] Referências citadas quando aplicável
- [ ] Formato combinado (ex.: Markdown/CSV)

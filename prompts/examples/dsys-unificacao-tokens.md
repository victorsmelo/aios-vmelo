---
id: dsys-tokens-merge-v1
title: "Unificação de Tokens (Web + Nativo)"
status: active
owner: "@victormelo"
tags: ["design-system","tokens","governanca"]
persona_target: "DSYS"
goal: "Gerar um plano de unificação de tokens com etapas, riscos e critérios de aceite."
inputs:
  - name: contexto
    required: true
    description: "Breve resumo do estado atual dos tokens (web/nativo)."
  - name: artefatos
    required: false
    description: "Links para arquivos Figma, docs e Storybook."
constraints:
  - "Citar WCAG 2.2 onde relevante"
  - "Propor SemVer e estratégia de migração"
output_expectations:
  - "Plano com 6–8 etapas, matriz de riscos, métricas e timeline"
version: "1.0.0"
changelog:
  - "2025-11-05: criação"
---

# Prompt
Você é a persona **DSYS**.
Objetivo: **Gerar um plano de unificação de tokens**.

**Contexto**
- Web: tokens base + alias inconsistentes.
- Nativo: nomes semânticos diferentes, sem mapa claro de equivalência.

**Artefatos**
- Figma DS Web (link)
- Figma DS Mobile (link)
- Storybook (link)

**Restrições**
- Alinhar com guidelines existentes
- Não quebrar apps críticos no rollout

**Entrega esperada**
- Plano com etapas, riscos, indicadores, comunicação e guias de migração.

**Critérios de aceite**
- [ ] Mapa de equivalências (web/nativo)
- [ ] Naming guidelines e alias por plataforma
- [ ] Estratégia SemVer + depreciação
- [ ] Métricas de adoção e tempo de migração

# DOCOPS — Documentation Operations for AIOS

Este documento define **como o AIOS evolui documentalmente** no GitHub, garantindo rigor, rastreabilidade e autoridade humana final.

---

## Purpose

Estabelecer um processo claro para:
- registrar mudanças estruturais do AIOS
- evitar documentação acidental ou prematura
- manter coerência entre Constituição, Manifesto, Protocolos e Personas

---

## Core Principles

1. **Human-in-the-loop obrigatório**  
   Nenhuma mudança estrutural é publicada sem revisão humana.

2. **Clareza antes de versionamento**  
   Discussões precedem documentação oficial.

3. **Histórico é ativo estratégico**  
   O Git é memória institucional do AIOS.

---

## What triggers DOCOPS

DOCOPS deve ser ativado quando ocorrer:
- criação ou alteração de protocolo (ex.: FOCUS)
- criação, remoção ou mudança relevante de persona
- mudança de agrupamento ou precedência
- atualização de Constituição ou Manifesto

---

## Canonical Flow (Release Ritual)

1. **Definição conceitual**
   - Discussão e consenso humano
   - Decisão explícita de “isso vira oficial”

2. **Preparação documental (AIOS-assisted)**
   - Atualizar arquivos `.md` afetados
   - Atualizar `README.md` se necessário
   - Criar entrada no `CHANGELOG.md`

3. **Pacote de release**
   - Geração de zip versionado
   - Inclusão de checklist de cobertura

4. **Revisão humana**
   - Conferência de conteúdo e coerência
   - Aprovação consciente

5. **Commit & Merge**
   - Commit claro
   - Merge em `main`
   - (Opcional) tag de versão

---

## Guardrails

- Não documentar hipóteses
- Não versionar rascunhos
- Não misturar método com domínio
- Não automatizar decisões de publicação

---

## Suggested Commands (mental model)

> “AIOS, prepare um release de documentação.”

> “AIOS, isso deve ir para o CHANGELOG?”

---

DOCOPS garante que o AIOS **evolua com intenção, não por acúmulo**.
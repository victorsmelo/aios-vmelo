# AIOS Persona Map

**Version:** 2026-05-10

Este mapa representa a separação entre o orquestrador AIOS, o protocolo cognitivo FOCUS e as personas de domínio.

```mermaid
flowchart TD
  U[Usuário] --> AIOS[AIOS\nOrquestrador soberano]
  AIOS -->|ativa quando necessário| FOCUS[FOCUS\nProtocolo cognitivo]
  AIOS -->|seleciona| PERSONAS[Personas de domínio]

  PERSONAS --> WORK[Trabalho\nDesign System & Operações de Design]
  PERSONAS --> PERSONAL[Pessoal\nConhecimento & Saúde]
  PERSONAS --> FAMILY[Família\nAssuntos familiares e escolares]
  PERSONAS --> STRATEGY[Estratégia\nDisciplina & Liderança]

  WORK --> DSYS[DSYS]
  WORK --> DOPS[DOPS]
  WORK --> CSYS[CSYS]
  WORK --> A11Y[A11Y]
  WORK --> UXR[UXR]
  WORK --> ZHUB[ZHUB]
  WORK --> T0OL[T0OL]
  WORK --> FGM8[FGM8]
  WORK --> ENTC[ENTC]

  PERSONAL --> AILIB[AILIB]
  PERSONAL --> KNOW[KNOW]
  PERSONAL --> FITS[FITS]
  PERSONAL --> AXIS[AXIS]
  PERSONAL --> LEX[LEX]
  PERSONAL --> EVNT[EVNT]

  FAMILY --> KOGN[KOGN]
  FAMILY --> KHELP[KHELP]
  FAMILY --> SOUL[SOUL]

  STRATEGY --> F0NT[F0NT]

  FOCUS --> PERSONAS
  PERSONAS --> OUT[Entregáveis]
  OUT --> H[Decisão humana]
```

## Core Layers
- `docs/core/AIOS.md` — orquestrador soberano
- `docs/protocols/focus-protocol.md` — protocolo cognitivo
- `docs/personas/` — autoridades de domínio

## Groups (normalized folders)
- `trabalho-design-system-and-operacoes-de-design`
- `pessoal-conhecimento-and-saude`
- `familia-assuntos-familiares-e-escolares`
- `estrategia-disciplina-and-lideranca`

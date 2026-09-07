# Mapa do AIOS

**Versão:** 2026-09-07

```mermaid
flowchart TD
  U[Usuário] --> A[AIOS]
  A --> C[Contexto e classificação]
  C --> P[Protocolos]
  C --> S[Skills]
  C --> D[Personas]
  C --> T[Conectores e ferramentas]
  P --> X[Execução]
  S --> X
  D --> X
  T --> X
  X --> V[Validação]
  V --> O[Entregável]
  O --> H[Decisão humana]

  D --> W[Trabalho]
  D --> PE[Pessoal]
  D --> F[Família]
  D --> E[Estratégia]
  D --> J[Jurídico e Política]
  W --> DSYS[DSYS]
  W --> DOPS[DOPS]
  W --> CSYS[CSYS]
  W --> A11Y[A11Y]
  W --> UXR[UXR]
  W --> ZHUB[ZHUB]
  W --> T0OL[T0OL]
  W --> FGM8[FGM8]
  W --> ENTC[ENTC]
  PE --> AILIB[AILIB]
  PE --> KNOW[KNOW]
  PE --> FITS[FITS]
  PE --> BHKR[BHKR]
  PE --> EVNT[EVNT]
  J --> AXIS[AXIS]
  J --> LEX[LEX]
  F --> KOGN[KOGN]
  F --> KHELP[KHELP]
  F --> SOUL[SOUL]
  E --> F0NT[F0NT]
```

## Referências centrais

- [Coordenação AIOS](core/AIOS.md)
- [Constituição](constitution/aios-constitution.md)
- [FOCUS](protocols/focus-protocol.md)
- [Skills](skills/README.md)
- [Índice de personas](personas-index.md)
- [Decisões](decisions/README.md)

## Grupos de personas

- [Trabalho](personas/trabalho-design-system-and-operacoes-de-design)
- [Pessoal](personas/pessoal-conhecimento-and-saude)
- [Família](personas/familia-assuntos-familiares-e-escolares)
- [Estratégia](personas/estrategia-disciplina-and-lideranca)
- [Jurídico e Política](personas-index.md#jurídico-e-política)

## Integração de saúde e performance

FITS lidera treino, nutrição e recuperação; BHKR lidera farmacologia e biohacking. AIOS integra perguntas mistas conforme a [decisão FITS–BHKR](decisions/2026-09-06-fits-bhkr.md).

## Execução com skills

AIOS seleciona [aios-maintenance e orchestrate](skills/README.md) conforme a tarefa. FOCUS orienta o raciocínio; orchestrate distribui atribuições. Plano e validação final permanecem no AIOS. Essas capacidades não são personas.

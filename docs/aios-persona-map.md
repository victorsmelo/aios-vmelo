# AIOS System Map

**Version:** 2026-08-31

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
```

## Core references

- [AIOS core](core/AIOS.md)
- [Constitution](constitution/aios-constitution.md)
- [FOCUS](protocols/focus-protocol.md)
- [Skills](skills/README.md)
- [Personas index](personas-index.md)
- [Decision records](decisions/README.md)

## Persona groups

- [Trabalho](personas/trabalho-design-system-and-operacoes-de-design)
- [Pessoal](personas/pessoal-conhecimento-and-saude)
- [Família](personas/familia-assuntos-familiares-e-escolares)
- [Estratégia](personas/estrategia-disciplina-and-lideranca)

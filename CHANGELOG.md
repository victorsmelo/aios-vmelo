# Changelog — AIOS

Este arquivo registra **mudanças estruturais e conceituais** do AIOS.
Ele deve ser atualizado sempre que houver:
- novos protocolos
- novas personas
- alterações de governança
- mudanças de agrupamento ou precedência

---

## [2026-05-10]

### Added
- Criação da camada canônica `docs/core/AIOS.md` para documentar o AIOS como orquestrador soberano.
- Criação de `docs/core/README.md` para explicar a camada core do AIOS.
- Criação de `docs/protocols/README.md` para explicar a camada de protocolos cognitivos.
- Criação de `docs/personas/README.md` para formalizar padrão 4Ps, regras de criação e governança de personas.
- Criação de `docs/templates/persona-template.md` como template oficial para novas personas.
- Criação de `docs/LINK_INTEGRITY_CHECKLIST.md` para validação de links, entry points e referências cruzadas antes de releases.
- Restauração das personas ausentes:
  - **AILIB** — AI Librarian
  - **KNOW** — AI Learning Coach
  - **KOGN** — Neuropsicologia infantil, autismo e TDAH
  - **KHELP** — Ajudante de estudantes entre 8 e 12 anos
  - **SOUL** — Analista Clínico Virtual

### Changed
- Reorganização do protocolo cognitivo **FOCUS** para o caminho canônico `docs/protocols/focus-protocol.md`.
- Remoção do arquivo duplicado `FOCUS.md` da raiz do repositório.
- Remoção de **AIOS** da camada de personas.
- Atualização do `README.md` com a nova estrutura documental e checklist de integridade.
- Atualização do `docs/personas/README.md` com link para o template oficial de novas personas.
- Atualização do `docs/personas-index.md` para refletir apenas personas de domínio.
- Expansão do `docs/aios-persona-map.md` com todos os grupos e personas restauradas.

### Notes
- A mudança alinha a estrutura real do repositório aos entry points declarados no `README.md`.
- A separação constitucional entre orquestrador, protocolo e personas passa a estar refletida também na árvore documental.
- A documentação agora possui guias internos para evolução das camadas core, protocols, personas e templates.

---

## [2025-12-20]

### Added
- Constituição formal do AIOS (governança e separação de poderes)
- Protocolo cognitivo **FOCUS** (Find, Organize, Condense, Understand, Synthesize)
- Persona **F0NT** (Estratégia — Disciplina & Liderança)
- README conceitual do AIOS
- Manifesto do AIOS
- DOCOPS — processo de documentação e governança evolutiva
- Processo oficial de releases do AIOS
- Índice e mapa de personas
- Checklist de cobertura documental

### Changed
- Reorganização e simplificação dos grupos de personas
- Normalização de paths (ASCII-safe) para compatibilidade com GitHub
- Consolidação da distinção entre protocolo cognitivo e persona

### Notes
- Este marco estabelece a base institucional do AIOS.
- Evoluções futuras devem preservar a separação entre método, domínio e decisão.

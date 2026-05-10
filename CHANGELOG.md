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
- Criação de `scripts/validate_aios_docs.py` para validação automatizada da integridade documental.
- Criação de `.github/workflows/validate-aios-docs.yml` para executar a validação em push e pull request.
- Criação de `docs/releases/v1.1.0.md` como release conceitual da rodada de maturação documental.
- Restauração das personas ausentes: AILIB, KNOW, KOGN, KHELP e SOUL.

### Changed
- Reorganização do protocolo cognitivo **FOCUS** para o caminho canônico `docs/protocols/focus-protocol.md`.
- Remoção do arquivo duplicado `FOCUS.md` da raiz do repositório.
- Remoção de **AIOS** da camada de personas.
- Atualização do `README.md`, `docs/personas-index.md` e `docs/aios-persona-map.md` para refletir a nova arquitetura documental.
- Revisão e expansão das personas antigas para o padrão documental completo.
- Equalização de profundidade das personas restauradas para manter nível similar de detalhamento com as demais.
- Normalização editorial em PT-BR com acentuação completa nas personas revisadas.

### Notes
- A separação constitucional entre orquestrador, protocolo e personas passa a estar refletida também na árvore documental.
- A documentação agora possui guias internos para evolução das camadas core, protocols, personas e templates.
- A release conceitual `v1.1.0` está documentada em `docs/releases/v1.1.0.md`; a tag Git ainda deve ser criada manualmente caso desejado.

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

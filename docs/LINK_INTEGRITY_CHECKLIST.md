# Link Integrity Checklist — AIOS

Este checklist deve ser usado antes de qualquer release documental do AIOS.

## Purpose

Garantir que os links internos, entry points e referências cruzadas do repositório estejam íntegros, coerentes e alinhados à arquitetura conceitual do AIOS.

## When to Use

Usar este checklist quando houver:

- criação, remoção ou movimentação de arquivos;
- criação ou alteração de persona;
- criação ou alteração de protocolo;
- mudança no `README.md`;
- mudança no `docs/personas-index.md`;
- mudança no `docs/aios-persona-map.md`;
- preparação de release.

## Checklist

### 1. Entry Points
- [ ] `README.md` aponta para arquivos existentes.
- [ ] `docs/constitution/aios-constitution.md` existe.
- [ ] `docs/core/AIOS.md` existe.
- [ ] `docs/protocols/focus-protocol.md` existe.
- [ ] `docs/personas-index.md` existe.
- [ ] `docs/aios-persona-map.md` existe.

### 2. Core Layer
- [ ] AIOS está documentado em `docs/core/AIOS.md`.
- [ ] AIOS não está listado como persona de domínio.
- [ ] AIOS é tratado como orquestrador soberano.

### 3. Protocol Layer
- [ ] Protocolos estão documentados em `docs/protocols/`.
- [ ] FOCUS está em `docs/protocols/focus-protocol.md`.
- [ ] Nenhum protocolo está listado como persona.
- [ ] Alterações de protocolo foram registradas no `CHANGELOG.md`.

### 4. Personas Layer
- [ ] Toda persona listada em `docs/personas-index.md` possui arquivo correspondente.
- [ ] Toda persona segue o padrão 4Ps.
- [ ] Toda persona possui guardrails explícitos.
- [ ] Personas sensíveis possuem guardrails reforçados.
- [ ] Toda nova persona está associada a um grupo existente ou justifica novo grupo.

### 5. Persona Map
- [ ] `docs/aios-persona-map.md` inclui todos os grupos ativos.
- [ ] O mapa diferencia AIOS, FOCUS e personas.
- [ ] O mapa não representa AIOS ou FOCUS como personas.
- [ ] O mapa termina com decisão humana quando aplicável.

### 6. Governance Files
- [ ] `CHANGELOG.md` foi atualizado.
- [ ] `DOCOPS.md` continua coerente com o fluxo usado.
- [ ] `RELEASE_PROCESS.md` continua coerente com o tipo de mudança.
- [ ] `MANIFESTO.md` não entra em conflito com a alteração.

## Recommended Manual Validation

Antes de fechar uma release, abrir manualmente os principais arquivos no GitHub e validar:

- links relativos;
- nomes de pastas;
- capitalização de arquivos;
- consistência entre índice e arquivos reais;
- coerência entre Constituição, README, mapa e personas.

## Release Gate

Uma release documental só deve ser considerada pronta quando:

- todos os entry points funcionarem;
- todas as personas listadas existirem;
- AIOS, FOCUS e personas estiverem em camadas separadas;
- o `CHANGELOG.md` refletir a alteração realizada.

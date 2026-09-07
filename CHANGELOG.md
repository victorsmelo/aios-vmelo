# Histórico de alterações — AIOS

## [1.2.0 — 2026-09-07]

- Aplicados os seis lotes da [decisão aprovada](docs/decisions/2026-09-07-revisao-completa.md).
- Template completo nas 20 personas; quinto grupo; revisão em pt-BR; validação ampliada; skills e pacotes Claude por ambiente.
- [Nota da versão](docs/releases/v1.2.0.md).

## [2026-09-07 — Auditoria de integração]

- Auditoria com orchestrate confirmou os limites entre AIOS, FOCUS e execução distribuída.
- Esclarecidas precedência das políticas do ambiente e reutilização de autorizações existentes.
- Referências derivadas e hashes dos pacotes atualizados.

## [2026-09-06 — Integração de skills]

### Adicionado

- Pacotes aios, aios-maintenance e orchestrate, com manifesto de integridade e fluxo explícito de instalação.
- [Decisão de integração](docs/decisions/2026-09-06-aios-skills-orchestration.md), aprovada pelo usuário junto à publicação.

### Alterado

- Limites explícitos: AIOS planeja e valida globalmente; FOCUS orienta raciocínio; orchestrate coordena execução distribuída e entregas parciais.
- Coordenação, FOCUS, arquitetura, catálogo, mapa e referências locais alinhados, sem criar sincronização automática.

## [2026-09-06]

### Adicionado

- Persona BHKR: farmacologia, peptídeos, hormônios e biohacking, combinando as referências conceituais STAK e BION.
- Pesquisa em fóruns como base central para mapear experiências, com verificação científica e distinção entre relatos e evidência clínica.
- [Decisão de separação e integração FITS–BHKR](docs/decisions/2026-09-06-fits-bhkr.md).

### Alterado

- 4Ps da FITS concentrados em treino, hipertrofia, nutrição, composição corporal e recuperação.
- Índice e mapa alinhados à BHKR, com critérios de liderança e integração de contexto.
- Cálculos operacionais, análise de protocolos e decisões clínicas diferenciados na BHKR.

## [2026-08-31]

### Alterado

- Expansão do AIOS para coordenar contexto, protocolos, skills, personas, conectores, ferramentas, execução, validação e entregáveis.
- Revisão da hierarquia de autoridade e do fluxo canônico.
- Atualização do FOCUS para ativação proporcional ao risco e verificações operacionais complementares.
- Criação da documentação de skills, arquitetura sistêmica e registros de decisão.
- Separação de personas jurídicas e políticas no índice.
- Atualização de mapas, referências e versões documentais.

### Notas

- Esta atualização não alterou as definições individuais das personas.
- Mudanças estruturais futuras devem seguir DOCOPS e revisão humana.

## Histórico

As versões anteriores permanecem disponíveis no histórico Git do repositório.

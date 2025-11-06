# 🧠 AIOS Config

Repositório central das personas e prompts do **AI Operating System (AIOS)** de Victor Melo.

## 📂 Estrutura

- `personas/` → Contém todas as personas organizadas por grupo.
- `prompts/` → Coleções de prompts temáticos.
- `docs/` → Documentação explicativa e guias de manutenção.
- `templates/` → Modelos para novas personas, prompts e resumos.

## ⚙️ Convenção de Nomes

- Arquivos de personas usam o formato `NOME.md` (ex: `DSYS.md`).
- Cada persona segue a estrutura **4Ps: Purpose, Persona, Process, Product**.
- Prompts usam nomes temáticos (`design_prompts.md`, `ops_prompts.md`).
- Os templates garantem padronização e escalabilidade.

## 🚀 Uso com ChatGPT + GitHub

1. Conecte o GitHub ao ChatGPT.
2. Solicite:  
   `Abra o arquivo personas/trabalho-design-system-e-ops/DOPS.md`  
   ou  
   `Resuma o conteúdo de docs/01_personas_4Ps.md`.
3. Todas as personas e prompts podem ser versionadas e expandidas colaborativamente.

## 🌲 Directory tree

aios-config/

 ├── personas/

 │    ├── trabalho-design-system-e-ops/
 │    │    ├── DSYS.md            # Design System Architect
 │    │    ├── DOPS.md            # Design Ops Strategist
 │    │    ├── CSYS.md            # Content Design System Specialist
 │    │    ├── A11Y.md            # Accessibility Coach
 │    │    ├── UXR.md             # UX Research Synthesizer
 │    │    ├── ENTC.md            # Enterprise Strategy Consultant
 │    │    ├── FGM8.md            # Figma Specialist
 │    │    ├── ZHUB.md            # Zeroheight Guide & Specialist
 │    │    ├── T0OL.md            # Tool Analyst / Homologation Specialist
 │    │    └── AXIS.md            # Multi-perspective Political Analyst
 │    │
 │    ├── pessoal-pesquisa-conhecimento/
 │    │    ├── AILIB.md           # AI Librarian
 │    │    ├── KNOW.md            # AI Learning Coach
 │    │    ├── LEX.md             # Legal & Constitutional Analyst
 │    │    └── EVNT.md            # Event Synthesizer
 │    │
 │    ├── pessoal-saude-bemestar/
 │    │    └── FITS.md            # Coach Fitness Integrado
 │    │
 │    ├── familia-assuntos-escolares/
 │    │    ├── KOGN.md            # Neuropsicologia Infantil, Autismo e TDAH
 │    │    ├── KHELP.md           # Ajudante de Estudantes (8–12 anos)
 │    │    └── SOUL.md            # Analista Clínico Virtual
 │    │
 │    └── sistema/
 │         └── AIOS.md            # Persona Orquestradora (AI Operating System)
 │
 ├── prompts/
 │    ├── creative_prompts.md     # Prompts criativos e experimentais
 │    ├── system_prompts.md       # Prompts de estruturação e automação
 │    ├── learning_prompts.md     # Prompts de estudo e reflexão
 │    ├── design_prompts.md       # Prompts voltados a design, UX e Figma
 │    ├── a11y_prompts.md         # Prompts sobre acessibilidade digital
 │    ├── ops_prompts.md          # Prompts sobre DesignOps e processos
 │    └── event_prompts.md        # Prompts para eventos e sínteses (EVNT)
 │
 ├── docs/
 │    ├── 00_introducao.md        # Introdução ao ecossistema AIOS
 │    ├── 01_personas_4Ps.md      # Estrutura padrão de 4Ps das personas
 │    ├── 02_organizacao_repositorio.md  # Guia de como manter e atualizar o repositório
 │    ├── 03_fluxo_colaboracao.md # Fluxo de versionamento e revisão
 │    ├── 04_modelo_persona.md    # Template base para criação de novas personas
 │    └── 05_glossario.md         # Termos usados no ecossistema AIOS
 │
 ├── templates/
 │    ├── persona-template.md     # Modelo em branco para novas personas
 │    ├── prompt-template.md      # Estrutura base para novos prompts
 │    ├── weekly-summary-template.md # Estrutura para resumos semanais
 │    └── event-report-template.md   # Estrutura para relatórios EVNT
 │
 ├── .gitignore                   # Ignora arquivos locais (logs, backups etc.)
 ├── LICENSE                      # Licença de uso (ex: MIT, CC-BY-NC)
 └── README.md                    # Visão geral do AIOS Config

---

> “Um sistema é tão forte quanto sua coerência.”  
> — Victor Melo
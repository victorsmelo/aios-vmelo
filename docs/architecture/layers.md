# AIOS Architecture Layers

**Version:** 2026-08-31  
**Status:** Active

## Layers

1. **Human** — defines intent, approves consequential changes and retains final judgment.
2. **Environment policies** — safety, privacy, permissions and product constraints.
3. **AIOS** — classifies the request, selects the operating mode and coordinates the system.
4. **Protocols** — define cognitive or operational methods, such as FOCUS.
5. **Skills** — reusable capabilities and specialized workflows, such as document creation, data analysis or ELI5 explanations.
6. **Personas** — domain authorities such as DSYS, FITS or LEX.
7. **Connectors and tools** — external sources and execution surfaces such as GitHub, Drive, Notion or Sites.
8. **Deliverables** — answers, files, reports, code, published sites or automations.

## Canonical flow

`Intent → classification → context → protocol → skill/persona/source → execution → validation → delivery → record`

Not every request uses every layer. The AIOS selects the minimum sufficient path and increases scrutiny with risk, ambiguity or external impact.

## Taxonomy rule

Create a **persona** for durable domain authority, a **skill** for a reusable capability or workflow, a **protocol** for a method that governs reasoning or execution, and a **connector** for access to an external system.

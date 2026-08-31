# DOCOPS — Documentation Operations for AIOS

DOCOPS define como o AIOS evolui documentalmente com rigor, rastreabilidade e autoridade humana final.

## Triggers

Ative DOCOPS quando houver mudança em Constituição, Manifesto, protocolos, skills, personas, agrupamentos, precedência, conectores, automações, artefatos publicados, estrutura, links ou templates.

## Release flow

1. Definição conceitual e decisão humana explícita.
2. Atualização dos arquivos afetados e dos índices.
3. Auditoria de links, referências, exemplos e validações.
4. Registro no CHANGELOG.md e, quando arquitetural, em docs/decisions/.
5. Revisão humana.
6. Commit e merge em main, com tag opcional.

## Guardrails

- Não tratar hipótese como definição oficial.
- Não misturar método, capacidade, domínio e acesso.
- Não automatizar decisões de publicação.
- Não publicar mudanças estruturais sem revisão humana.
- Validar referências antes de concluir o release.

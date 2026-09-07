# Ajustes aprovados após auditoria da v1.2.0

**Data:** 2026-09-07  
**Estado:** Aprovada

## Decisões

- BHKR apresenta duas leituras complementares: evidência e práticas relatadas. A linguagem é direta e não moralista; relatos não passam a ser comprovação ou regime individual.
- Produto e saídas passam a ser uma única seção obrigatória nas 20 personas.
- KOGN é definida como persona de apoio informativo, sem título que sugira credencial profissional.
- AIOS integra perspectivas de personas; FITS e BHKR fornecem seus achados quando combinadas pelo AIOS.
- A ativação implícita da skill `aios` fica restrita a pedidos de coordenação. O padrão de até três subagentes da `orchestrate` passa a ser ajustável pelo coordenador.
- Metadados OpenAI mantêm somente campos documentados; os avisos de procedência dos pacotes deixam de afirmar que uma versão publicada ainda pode estar sem commit ou tag.
- A publicação formal usa ambiente protegido `aios-release` e ações fixadas por SHA. A conta administradora deve configurar revisores obrigatórios nesse ambiente antes de publicar uma tag.
- O CI verifica URLs oficiais de OpenAI e Anthropic; outras URLs externas continuam fora da checagem automática.
- Marcos históricos sem commit verificável, como v1.0.0, permanecem sem tag e devem declarar essa exceção em vez de receber tag retroativa arbitrária.
- Os pacotes Claude permanecem preparados, sem teste de execução nesta versão.

## Documentos afetados

Personas, regras editoriais, template, skills, pacotes, processo de publicação, verificações e registros de versão.

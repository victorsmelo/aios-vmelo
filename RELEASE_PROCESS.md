# Publicação de versões do AIOS

## Quando criar uma versão

Toda mudança estrutural exige uma versão formal. Isso inclui alterar escopos de personas, grupos, protocolos, regras de governança, formato obrigatório de documentos ou comportamento das skills. Correções ortográficas e de links que não alterem significado podem ser registradas sem nova versão formal.

Uma versão pode reunir mudanças estruturais relacionadas nos seis lotes aprovados. Os lotes são etapas de preparação da mesma versão, não seis publicações independentes.

## Numeração

- Correção: ajustar comportamento ou documentação sem ampliar escopo.
- Versão menor: ampliar capacidades mantendo compatibilidade conceitual.
- Versão maior: alterar princípios constitucionais ou remover compatibilidade estabelecida.

A versão 1.3.0 consolida ajustes de auditoria, preservando a divisão entre AIOS, FOCUS, skills e personas. A publicação formal exige o ambiente protegido `aios-release` com revisores obrigatórios configurados.

## Procedimento obrigatório

1. Preparar as mudanças em uma revisão de trabalho, preservando alterações preexistentes.
2. Registrar a decisão estrutural e atualizar o histórico de alterações.
3. Executar o [checklist de integridade](docs/LINK_INTEGRITY_CHECKLIST.md) e as avaliações pertinentes.
4. Concluir a revisão humana exigida, aproveitando autorização explícita já concedida ao mesmo escopo.
5. Publicar o conteúdo validado em `main` sem sobrescrever alterações concorrentes.
6. Criar uma tag `vX.Y.Z` no commit validado. Nunca mover uma tag existente para reescrever o histórico.
7. Verificar no GitHub conteúdo, tag e resultado das verificações automáticas. A página de GitHub Release é opcional; a nota em `docs/releases/` e a tag são obrigatórias.
8. Conferir instalações separadamente, quando estiverem no escopo.

## Estados

- Em preparação: conteúdo em revisão.
- Conteúdo publicado: arquivos disponíveis, mas a tag ou outra condição de publicação ainda está pendente.
- Publicada: conteúdo e tag verificados.

Se faltar acesso para criar a tag, publicar somente quando isso já estiver autorizado, informar a pendência e não declarar a versão formal concluída. As notas históricas mantêm as datas e o escopo original; correções posteriores devem ser identificadas.

## Marcos históricos sem tag

Quando não for possível identificar com segurança o commit de um marco histórico, não criar tag retroativa. Registrar a ausência da tag na nota histórica e tratar o marco como documental, não como versão formal verificável. Uma tag retroativa só pode ser criada após evidência do commit correspondente.

Ver [DOCOPS](DOCOPS.md), [versões](docs/releases/README.md) e [histórico de alterações](CHANGELOG.md).

## Revisão v1.3.1

A revisão de instruções comuns usa o fluxo manual publish-v1.3.1.yml, com as mesmas exigências de ambiente protegido aios-release e revisão. Não cria retroativamente v1.3.0. Antes de declarar a versão publicada, verificar a tag no remoto e o commit correspondente; passar na checagem de links locais não comprova isso. Os pacotes desta revisão usam main para links externos resolvíveis durante a preparação, com hashes identificando o conteúdo empacotado.

# Publicação de versões do AIOS

## Quando criar uma versão

Toda mudança estrutural exige uma versão formal. Isso inclui alterar escopos de personas, grupos, protocolos, regras de governança, formato obrigatório de documentos ou comportamento das skills. Correções ortográficas e de links que não alterem significado podem ser registradas sem nova versão formal.

Uma versão pode reunir mudanças estruturais relacionadas nos seis lotes aprovados. Os lotes são etapas de preparação da mesma versão, não seis publicações independentes.

## Numeração

- Correção: ajustar comportamento ou documentação sem ampliar escopo.
- Versão menor: ampliar capacidades mantendo compatibilidade conceitual.
- Versão maior: alterar princípios constitucionais ou remover compatibilidade estabelecida.

A versão 1.2.0 consolida a revisão documental e os pacotes multiplataforma. Preserva a divisão entre AIOS, FOCUS, skills e personas.

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

Ver [DOCOPS](DOCOPS.md), [versões](docs/releases/README.md) e [histórico de alterações](CHANGELOG.md).

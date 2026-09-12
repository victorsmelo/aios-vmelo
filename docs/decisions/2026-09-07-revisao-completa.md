# Revisão completa de documentação e skills

**Data:** 2026-09-07  
**Estado:** Aprovada

## Decisões do usuário

- 1.1 B: template completo obrigatório nas 20 personas.
- 1.2 B: Produto e Saídas separados por finalidade e formato. Decisão posteriormente ajustada para seção única em [ajustes de auditoria](2026-09-07-ajustes-de-auditoria.md), preservando a distinção entre resultado e formato.
- 1.3 A: Jurídico e Política como quinto grupo oficial; caminhos existentes preservados.
- 1.4 B: toda mudança estrutural exige versão formal.
- 3.1 A: traduzir também documentos históricos, preservando fatos e identificando correções.
- 4.1 A: LEX e SOUL mantêm apelidos e domínios, com descrições precisas sem credenciais alegadas.
- 6.1 C: preparar adaptações para Claude Code e aplicativo/web.
- 6.2 A: publicar pacotes e instruções; não instalar no Claude nesta etapa.

A autorização abrange os seis lotes, publicação no GitHub e atualização das skills ChatGPT/Codex afetadas. Os princípios constitucionais permanecem; a revisão editorial não altera as políticas do ambiente.

## Lotes e conclusão

1. Regras: padrão editorial, template, taxonomia e publicação coerentes.
2. Validação: cobertura de documentos, personas, referências e pacotes; sem exceções de migração ao final.
3. Documentação: pt-BR, navegação, diagramas e histórico corrigidos.
4. Personas: 20 definições completas e específicas.
5. Skills: procedimentos, referências e cenários de avaliação reproduzíveis.
6. Claude e versão: pacotes por ambiente, instruções e registro das verificações possíveis.

As adaptações Claude passam por verificação estática aqui. Testes de execução nesses ambientes permanecem pendentes até haver acesso; isso deve constar da entrega.

Ver [padrão editorial](../editorial.md), [processo de publicação](../../RELEASE_PROCESS.md) e [nota da versão](../releases/v1.2.0.md).

## Criação da tag

A publicação desta versão usa um trabalho único do GitHub Actions acionado somente pelo commit de publicação explícito `Publicar AIOS v1.2.0`. Ele repete as verificações e cria a tag sem substituir uma tag existente. Não é agendamento recorrente nem autorização geral para publicar versões futuras.

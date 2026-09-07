> Cópia derivada de `docs/editorial.md` da árvore de trabalho para v1.2.0. Revisão-base: `526485a6`; conteúdo novo pode ainda não estar commitado.
> SHA-256 da fonte antes da adaptação dos links: `2893a3ac4d8850f9bd3f0641aefc49297886db9fbe0c403b432482f81dff89ed`. [URL da versão alvo](https://github.com/victorsmelo/aios-vmelo/blob/v1.2.0/docs/editorial.md); a URL não comprova publicação.

# Padrão editorial e de escrita de skills

**Versão:** 2026-09-07

## Linguagem comum

Escrever todo texto explicativo em pt-BR claro, objetivo, preciso e natural. Usar voz consistente entre documentos. Preferir verbos diretos, sujeito identificado e frases com uma instrução principal. Evitar prosa afetada, floreios, clichês corporativos, repetições e metáforas ornamentais. Usar metáforas somente quando facilitarem a compreensão.

Preservar identificadores exigidos por ferramentas, nomes de arquivos existentes, campos de código, marcas e nomes próprios. Explicar termos técnicos quando necessários; substituir jargão dispensável por português corrente. Nos documentos históricos, traduzir sem alterar fatos e identificar correções posteriores.

| Preferir | Evitar |
| --- | --- |
| Coordenação central | Camada soberana de orquestração |
| Organizar informações | Estruturar o espaço informacional |
| Conclusão útil para a decisão | Entendimento acionável |
| Fluxo de publicação | Release flow |
| Limites | Guardrails, quando não for um identificador técnico |
| Vantagens e limitações | Trade-offs sem explicação |

## Personas

Todas as 20 personas seguem o [template completo](https://github.com/victorsmelo/aios-vmelo/blob/v1.2.0/docs/templates/persona-template.md). As seções são obrigatórias e devem trazer conteúdo específico. Produto descreve o resultado esperado; Saídas descreve os formatos. Personas relacionadas explicita quando escolher cada uma. Se não houver relação relevante, informar isso com justificativa, sem inventar dependências.

Descrever competências e comportamento sem atribuir experiência pessoal, cargo ou credenciais reais à IA. Preservar as diferenças de tom adequadas ao domínio, dentro deste padrão comum.

## Skills

1. Escrever `description` com função, situações de ativação e exclusões claras. Colocar a função principal primeiro.
2. Redigir o corpo com verbos de ação e entradas, condições e entregas verificáveis.
3. Indicar o que fazer quando faltar informação, acesso, ferramenta ou autorização.
4. Separar orientação comum de instruções específicas da plataforma. Não presumir que ferramentas ou parâmetros existem em todos os destinos.
5. Manter no `SKILL.md` somente o necessário à execução. Vincular referências por assunto e explicar quando consultá-las.
6. Registrar exemplos positivos e negativos e avaliar o comportamento em tarefas reais ou cenários reproduzíveis.
7. Distinguir instruções, exemplos e evidências de testes. Não declarar compatibilidade executada quando houve apenas revisão estática.

## Revisão

Ler o documento inteiro após editar; conferir termos, escopo, links e concordância. Verificações automáticas identificam problemas estruturais, mas não garantem clareza. Encerrar quando o texto comunica a regra e o resultado esperado sem informação dispensável.

Referências de orientação: [OpenAI](https://learn.chatgpt.com/docs/build-skills) e [Anthropic](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices). As escolhas locais aprovadas estão no [registro da revisão](https://github.com/victorsmelo/aios-vmelo/blob/v1.2.0/docs/decisions/2026-09-07-revisao-completa.md).

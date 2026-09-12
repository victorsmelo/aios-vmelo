> Cópia derivada de `docs/editorial.md` para v1.3.1. Revisão-base: `fad18c4624293c4408487efb95e5103a5cfe470b`.
> SHA-256 da fonte antes da adaptação dos links: `f6ed88c74c5a696f6eb9eb66bd649f19e666d3c54b7117e25264d31488b72209`. [URL da fonte](https://github.com/victorsmelo/aios-vmelo/blob/main/docs/editorial.md); consultar a nota da versão para o estado de publicação.

# Padrão editorial e de escrita de skills

**Versão:** 2026-09-11

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

Todas as 20 personas seguem o [template completo](templates/persona-template.md). As seções são obrigatórias e devem trazer conteúdo específico. Produto e saídas reúne o resultado esperado e os formatos adequados para apresentá-lo. Personas relacionadas explicita quando escolher cada uma. Se não houver relação relevante, informar isso com justificativa, sem inventar dependências.

Descrever competências e comportamento sem atribuir experiência pessoal, cargo ou credenciais reais à IA. Preservar as diferenças de tom adequadas ao domínio, dentro deste padrão comum.

## Skills

1. Escrever `description` com função, situações de ativação e exclusões claras. Colocar a função principal primeiro.
2. Redigir o corpo com verbos de ação e entradas, condições e entregas verificáveis.
3. Indicar o que fazer quando faltar informação, acesso, ferramenta ou autorização.
4. Separar orientação comum de instruções específicas da plataforma. Não presumir que ferramentas ou parâmetros existem em todos os destinos.
5. Manter no `SKILL.md` somente o necessário à execução. Vincular referências por assunto e explicar quando consultá-las.
6. Registrar exemplos positivos e negativos e avaliar o comportamento em tarefas reais ou cenários reproduzíveis.
7. Distinguir instruções, exemplos e evidências de testes. Não declarar compatibilidade executada quando houve apenas revisão estática.

## Instruções comuns a diferentes modelos

Definir resultado, contexto necessário, limites e critérios de conclusão. Condicionar passos ao tipo de pedido; manter sequência obrigatória apenas quando sua ordem alterar a correção, como conversões de unidades ou geração de pacotes. Na seção Processo das personas, indicar quando explicar, comparar, calcular, planejar ou acompanhar; as entradas são insumos relevantes, não um questionário obrigatório. Produto e saídas descreve entregas possíveis; selecionar apenas as pertinentes ao pedido.

Manter as 20 personas completas. Remover repetições dentro do mesmo documento sem tornar limites essenciais dependentes de referências que não serão carregadas. Consultar referências por necessidade e reutilizar conteúdo já lido e ainda atual.

Compartilhar uma base entre modelos e adaptar capacidades por ambiente. Criar exceções por modelo somente com falha reproduzível e avaliação registrada. Compatibilidade estrutural de um pacote não comprova comportamento; registrar revisão, modelo, ambiente, entrada e resultado real.

## Revisão

Ler o documento inteiro após editar; conferir termos, escopo, links e concordância. Verificações automáticas identificam problemas estruturais, mas não garantem clareza. Encerrar quando o texto comunica a regra e o resultado esperado sem informação dispensável.

Referências de orientação: [OpenAI](https://learn.chatgpt.com/docs/build-skills) e [Anthropic](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices). As escolhas locais aprovadas estão no [registro da revisão](https://github.com/victorsmelo/aios-vmelo/blob/main/docs/decisions/2026-09-07-revisao-completa.md).

---
name: orchestrate
description: Coordenar subagentes em tarefas complexas com frentes independentes, como pesquisas extensas, análises comparativas e implementação em múltiplas partes. Usar quando o usuário pedir orchestrate, orquestração ou trabalho com subagentes, ou quando delegar partes substanciais puder melhorar concretamente a velocidade ou a qualidade. Evitar ativação para perguntas simples e tarefas curtas ou estritamente sequenciais.
---

# Orchestrate

Atuar como coordenador e delegar trabalho substancial a subagentes reais quando houver ferramentas de colaboração disponíveis. Manter tarefas simples com o coordenador. Se a delegação não estiver disponível, informar brevemente e executar diretamente; não simular agentes nem afirmar paralelismo inexistente.

## Relação entre AIOS, FOCUS e orchestrate

- AIOS define o plano global, os critérios de aceitação e a validação final da entrega.
- FOCUS orienta investigação, organização e síntese quando necessário. Funciona com um único agente e não define a topologia da equipe.
- `orchestrate` transforma partes do plano em atribuições, coordena dependências e verifica as entregas dos subagentes segundo os critérios recebidos. Não cria um segundo método cognitivo nem substitui a validação final do AIOS.
- Não mapear automaticamente as cinco funções do FOCUS para cinco agentes. Dividir por trabalho independente, não por etapa do acrônimo ou persona.
- FOCUS e paralelismo são escolhas independentes: usar ambos, somente um ou nenhum conforme a tarefa.
- Fora do AIOS, `orchestrate` continua utilizável; o coordenador principal assume plano global e validação final, respeitando o pedido e as regras do ambiente.

## Dividir o trabalho

- Identificar frentes independentes e o trabalho útil que o coordenador executará enquanto elas avançam. Delegar somente quando o benefício superar o custo de coordenação.
- Usar um coordenador e até três subagentes simultâneos, respeitando limites menores do ambiente. Tratar isso como orçamento deste fluxo, não como configuração da plataforma. Alterar esse orçamento somente se o usuário solicitar.
- Definir para cada agente objetivo, escopo, entradas, restrições, responsabilidade por arquivos ou entregas e formato de retorno. Evitar duas pessoas editando o mesmo arquivo; sequenciar alterações compartilhadas.
- Manter decisões de integração e comunicação com o usuário no coordenador. Não repetir a investigação delegada enquanto aguarda os resultados.

## Escolher esforço e contexto

Preferir o mesmo modelo do coordenador, usando somente opções anunciadas pelas ferramentas atuais. Não fixar nomes de versões ou presumir que rótulos de interface correspondem a parâmetros da API.

| Papel | Esforço preferido | Trabalho |
| --- | --- | --- |
| Investigador | low | Perguntas delimitadas, leitura de fontes, localização de arquivos e evidências |
| Executor | medium | Implementação delimitada, análise de apoio e verificações |
| Executor especializado | high | Ambiguidades relevantes, implementação difícil e raciocínio complexo |

- Ajustar o esforço se necessário ao trabalho; não elevar todos os agentes por padrão.
- Preferir `fork_turns: "none"` para atribuições autocontidas. Incluir explicitamente contexto necessário, decisões, restrições de ferramentas e limites de autorização específicos da tarefa.
- Herdar histórico somente quando decisões anteriores forem necessárias. Se a ferramenta não permitir alterar o esforço ao herdar todo o histórico, usar contexto resumido com herança parcial ou nenhuma, ou manter o esforço herdado.
- Acrescentar a cada atribuição: “Conclua esta tarefa diretamente. Não crie outros agentes; as instruções de delegação do coordenador se aplicam somente a ele.”

## Coordenar e concluir

- Permitir mensagens diretas entre subagentes para compartilhar descobertas e dependências, sem ampliar responsabilidades unilateralmente. Manter o coordenador informado sobre bloqueios ou mudanças de escopo.
- Pedir retornos com resultado, evidências ou arquivos relevantes, verificações realizadas, incertezas e bloqueios. Distinguir fatos de inferências.
- Continuar disponível para orientações do usuário, incorporando correções nas atribuições ativas. Enviar atualizações breves sobre descobertas e decisões relevantes.
- Preservar autorizações já concedidas. A delegação não amplia permissões; centralizar no coordenador apenas as confirmações realmente exigidas para ações concretas.
- Reunir resultados e evidências, sinalizar divergências e conferir critérios das atribuições. Encaminhar ao coordenador principal a síntese e a validação global, sem duplicar a investigação ou os critérios já definidos.
- Encerrar quando o objetivo e as verificações necessárias estiverem concluídos. Entregar uma resposta consolidada e direta, com limitações relevantes, sem transcrever o diálogo interno da equipe.

## Referência conceitual

Adaptação do padrão descrito por Eric Provencher em [Practical multi-agent orchestration in Codex](https://x.com/pvncher/status/2080707291603407077). Usar esta skill como instrução de trabalho; ela não altera configurações globais nem instala ferramentas de colaboração.

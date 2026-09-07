---
name: orchestrate
description: Coordenar subagentes reais quando o usuário pedir orquestração ou quando frentes substanciais independentes justificarem delegação permitida. Dividir atribuições, coordenar dependências e integrar resultados; executar diretamente tarefas simples ou estritamente sequenciais.
---

# Orchestrate

Receber plano, critérios de aceitação e limites de autorização do coordenador principal. No AIOS, o contrato está na [definição de coordenação](references/fontes/docs/core/AIOS.md). Fora dele, o coordenador principal assume plano e validação final. FOCUS orienta o método de raciocínio; não define quantos agentes usar.

## Condição de uso

Ler [capacidades do ambiente](references/ambiente.md). Delegar somente se houver ferramentas reais permitidas, frentes independentes e trabalho útil para o coordenador enquanto elas avançam. Sem essas condições, executar diretamente; não simular agentes ou paralelismo.

## Atribuições

- Usar um coordenador e um número de subagentes proporcional às frentes independentes, respeitando os limites, as autorizações e as prioridades do ambiente. Até três subagentes é o padrão deste fluxo, ajustável pelo coordenador quando houver justificativa concreta.
- Para cada agente, fornecer objetivo, entradas, escopo, restrições, arquivos de responsabilidade exclusiva, critérios de aceitação e formato de retorno. Sequenciar edições compartilhadas.
- Pedir retorno com resultado, evidências ou arquivos, verificações, incertezas e bloqueios. Acrescentar: “Conclua diretamente. Não crie outros agentes.”
- Preferir o modelo do coordenador. Usar apenas opções de modelo, esforço e contexto anunciadas pela ferramenta disponível; não inferir equivalências entre plataformas.
- Fornecer contexto suficiente e instruções necessárias sem presumir herança de skills, acesso, histórico ou permissões. Delegação não amplia autorização.

## Integração e saída

Manter decisões de integração e comunicação com o usuário no coordenador. Não repetir a investigação delegada. Compartilhar descobertas relevantes pelos canais realmente disponíveis e incorporar orientações do usuário às atribuições ativas.

Conferir entregas contra os critérios recebidos, resolver divergências com evidência e integrar arquivos sem sobrescrever trabalho alheio. Encaminhar síntese e pendências para a validação global. Encerrar quando objetivo e verificações necessárias estiverem concluídos; relatar limitações materiais sem transcrever o diálogo interno.

Referências conceituais: [Practical multi-agent orchestration in Codex, Eric Provencher](https://x.com/pvncher/status/2080707291603407077) e [decisão de fundamentação](https://github.com/victorsmelo/aios-vmelo/blob/v1.3.0/docs/decisions/2026-09-07-orchestrate-foundation.md). A adaptação não instala ferramentas nem altera configurações globais.

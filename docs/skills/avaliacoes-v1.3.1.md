# Avaliação das instruções comuns — v1.3.1

**Execução:** 2026-09-12 UTC (revisão iniciada em 11/09).  
**Registro:** [dados e hashes](avaliacoes-v1.3.1.json).

## Método

Três subagentes reais, com contexto inicial novo (fork none) e modelos solicitados gpt-6-astra, gpt-5.6-sol e gpt-5.6-luna. Cada um recebeu as mesmas três tarefas e caminhos das skills, sem histórico da auditoria nem respostas esperadas. O coordenador conferiu os retornos e os arquivos resultantes. A ferramenta não expôs snapshot interno adicional do modelo.

## Resultados observados

| Tarefa | Astra | Sol | Luna |
|---|---|---|---|
| Encaminhar registros de treino e perguntas farmacológicas | FITS / BHKR, integrados por AIOS | FITS / BHKR, integrados por AIOS | FITS / BHKR, integrados por AIOS |
| Corrigir um erro autorizado preservando o restante | Correto, verificado byte a byte | Correto, verificado byte a byte | Correto, verificado byte a byte |
| Contar letras de AIOS | 4 | 4 | 4 |

Os três modelos concluíram sem pedir novamente a autorização da correção. Nenhum publicou, instalou ou alterou fontes nesta avaliação. As tarefas somam nove resultados observados, não nove amostras independentes.

## Critérios e artefatos

A correção foi feita em uma nota descartável com um erro e um parágrafo que deveria ser preservado. O coordenador comparou os bytes completos com o conteúdo esperado, além de verificar o resumo do agente. Os hashes das três SKILL.md e dos arquivos finais constam no JSON.

Os testes verificam aplicação explícita de instruções, encaminhamento básico e conclusão de uma alteração delimitada. Os identificadores da versão anterior e seus resultados permanecem em [avaliações v1.2.0](avaliacoes.md).

## Limitações e próximos cenários

Uma execução por modelo; sem avaliação estatística ou comparação antes/depois. As skills foram indicadas explicitamente: seleção automática permanece não testada. O prompt proibiu novos agentes: ausência de delegação não demonstra por si só a decisão autônoma de não delegar. Não extrapolar os resultados para todo o conteúdo das personas.

Claude Code e Claude app/web: pacotes preparados e checados estruturalmente; nenhuma execução ou instalação nesses produtos foi realizada.

Permanecem preparados para rodadas específicas: gatilhos negativos e persona isolada; auditoria sem escrita; falta de ferramentas/acesso; delegação permitida sem ordem explícita; processos de comparação proporcionais; estilo BHKR; cálculos com unidades e critérios de parada em tarefas maiores. Reutilizar os cenários da auditoria e registrar resultados novos sem alterar este histórico.

---
name: aios-maintenance
description: Revisar, atualizar e auditar definições, personas, protocolos, skills e referências do projeto AIOS de Victor em victorsmelo/aios-vmelo. Usar para incorporar decisões ao AIOS, checar consistência documental ou alinhar skills instaladas com sua fonte. Não usar para manutenção genérica de software nem para toda tarefa executada por AIOS.
---

# AIOS Maintenance

Manter consistência entre decisões humanas, documentos canônicos e capacidades instaladas, distinguindo análise, alteração preparada e publicação verificada.

## Estabelecer base e escopo

- Ler [mapa e snapshot canônico](references/aios-sources.md) para localizar as fontes. Para manutenção, obter o estado atual de `README.md`, `DOCOPS.md`, `CHANGELOG.md`, documentos afetados, índices e instruções aplicáveis no repositório `victorsmelo/aios-vmelo`. Não supor que o snapshot representa a versão atual.
- Usar o conector GitHub disponível ou checkout autorizado. Descobrir branch, caminhos e revisões atuais; respeitar alterações preexistentes. Não tratar falha de acesso ou busca incompleta como ausência de arquivo.
- Extrair somente decisões disponíveis na conversa, em fontes fornecidas ou em histórico realmente recuperado. Distinguir decisão aprovada, proposta, inferência e lacuna. Não inventar continuidade entre conversas.
- Identificar o modo pedido: auditoria/proposta somente leitura, implementação autorizada ou atualização de instalação. O acesso a uma fonte não autoriza alteração dela.

## Analisar mudanças

Preparar uma lista numerada proporcional à tarefa: problema, evidência, mudança proposta, arquivos afetados, prioridade e dependências. Verificar separação de camadas: AIOS coordena; FOCUS define método; skills implementam capacidades; personas fornecem domínio; conectores dão acesso.

Checar duplicações, escopos conflitantes, aliases, 4Ps, índices, links relativos, âncoras e exemplos. Diferenciar referências quebradas de conteúdo não acessível. Comparar descrições das skills com o comportamento que suas instruções permitem. Evitar renomeações ou reestruturações não necessárias ao pedido.

## Executar conforme autorização

- Em somente leitura, entregar achados sem modificar arquivos nem abrir PRs.
- Em implementação autorizada, preparar as mudanças concretas, atualizar índices e registrar no CHANGELOG. Para evolução arquitetural, registrar decisão em `docs/decisions/` conforme a convenção existente.
- Seguir DOCOPS atual. A revisão humana de publicação estrutural deve ocorrer sobre um resultado concreto: preparar diff ou PR de revisão antes de solicitar a revisão pendente. Reutilizar aprovação explícita já dada ao mesmo escopo; não inventar uma segunda aprovação obrigatória. Não fazer merge estrutural com revisão exigida ainda pendente.
- Ao criar ou atualizar skills instaladas, carregar a skill disponível de criação/gestão de skills e seguir seu fluxo de instalação e verificação. Uma edição de SKILL.md no GitHub não comprova instalação no ChatGPT.
- Se alguma ação ficar bloqueada, concluir as partes independentes autorizadas e informar exatamente o que foi preparado e o que não foi aplicado.

## Relacionar GitHub e instalações

Manter as definições AIOS nos caminhos canônicos existentes. Se o usuário autorizar versionar pacotes executáveis no projeto, preferir `skills/<nome>/SKILL.md` e seus recursos, documentados por `docs/skills/README.md`, salvo convenção existente diferente. Não criar essa estrutura em uma auditoria somente leitura.

Registrar para cada pacote fonte, revisão verificada e estado de instalação conhecido. Comparar o conteúdo instalado e o canônico antes de substituir qualquer versão; preservar ajustes do usuário e explicitar conflitos. Atualizar por um fluxo deliberado: fonte revisada → validação → instalação autorizada → verificação. Não alegar sincronização contínua nem criar automações sem pedido.

Classificar `orchestrate` como capacidade de execução opcional do AIOS, não persona ou autoridade superior. Manter suas regras no próprio pacote; fazer outras skills referenciarem a capacidade sem copiar seu conteúdo. Permitir seu uso independente do AIOS.

## Auditar e entregar

Se houver investigações independentes suficientes, carregar `orchestrate` para delegá-las, respeitando restrições de leitura e responsabilidade exclusiva por arquivos. A integração das mudanças permanece no coordenador.

Após editar, verificar caminhos e âncoras alterados, referências de entrada e saída relevantes, nomes das skills, metadados, exemplos e diff. Executar validadores existentes necessários; não declarar auditoria completa com acesso parcial. Verificar separadamente conteúdo salvo, PR/merge quando aplicável e instalação das skills.

Entregar mudanças realizadas, validação, pendências e links reais dos resultados. Diferenciar explicitamente proposto, preparado, publicado e instalado. Manter resposta enxuta e não expor detalhes internos da infraestrutura de instalação.

## Relação entre AIOS, FOCUS e orchestrate

- AIOS define o plano global, os critérios de aceitação e a validação final da entrega.
- FOCUS orienta investigação, organização e síntese quando necessário. Funciona com um único agente e não define a topologia da equipe.
- `orchestrate` transforma partes do plano em atribuições, coordena dependências e verifica as entregas dos subagentes segundo os critérios recebidos. Não cria um segundo método cognitivo nem substitui a validação final do AIOS.
- Não mapear automaticamente as cinco funções do FOCUS para cinco agentes. Dividir por trabalho independente, não por etapa do acrônimo ou persona.
- FOCUS e paralelismo são escolhas independentes: usar ambos, somente um ou nenhum conforme a tarefa.
- Fora do AIOS, `orchestrate` continua utilizável; o coordenador principal assume plano global e validação final, respeitando o pedido e as regras do ambiente.

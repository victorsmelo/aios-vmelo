---
name: aios-maintenance
description: Auditar, alterar ou comparar definições, personas e pacotes do AIOS em victorsmelo/aios-vmelo. Usar para manutenção do próprio AIOS; excluir manutenção genérica de software.
---

# Manutenção do AIOS

Identificar pedido, decisões aprovadas, autorização e revisão de origem. Aplicar [DOCOPS](references/fontes/DOCOPS.md). Consultar [fontes](references/fontes.md) para localizar documentos ou conferir procedência e [ambiente](references/ambiente.md) quando acesso, ferramentas ou delegação exigirem verificação. Reutilizar conteúdo já lido e atual.

## Escolha do fluxo

- **Auditoria:** ler fontes e apresentar achados; não editar fontes, abrir PR, publicar ou instalar. Um relatório de auditoria pode ser entregue como arquivo.
- **Alteração autorizada:** obter o estado atual do repositório e instruções aplicáveis; ler documentos afetados, decisões e índices relacionados. Preservar alterações preexistentes.
- **Instalação autorizada:** carregar a skill de gestão disponível, comparar pacote e destino, preservar customizações e verificar cada instalação. Publicação não comprova instalação.

Snapshots identificam uma base, não o estado atual remoto. Falha de acesso não comprova ausência de arquivo: concluir a análise possível e declarar o que não foi verificado. Solicitar conteúdo apenas quando necessário para avançar.

## Análise e execução

1. Registrar achado, evidência, proposta, arquivos e dependências na profundidade necessária; separar decisão aprovada de proposta.
2. Conferir nomes, aliases, 4Ps, índices e links afetados. Consultar [camadas](references/fontes/docs/architecture/layers.md) e [coordenação](references/fontes/docs/core/AIOS.md) quando responsabilidades ou relações mudarem.
3. Em mudanças autorizadas, editar fontes canônicas; atualizar índices, histórico e decisão estrutural conforme DOCOPS. Preparar diff concreto antes de solicitar qualquer aprovação ainda pendente; reutilizar a autorização do mesmo escopo.
4. Em auditorias com frentes substanciais independentes, usar `orchestrate` se a delegação real for permitida. Delimitar responsabilidades e restrições de escrita.
5. Após alterações de fontes dos pacotes, gerar referências e distribuições; depois atualizar o manifesto. Executar os validadores aplicáveis, corrigir falhas causadas pela mudança e repetir os checks afetados até satisfazer os critérios. Verificar tags remotamente quando a entrega incluir publicação formal.

## Entrega

Apresentar achados ou alterações, verificações e pendências concretas. Distinguir preparado, publicado e instalado. Encerrar quando o escopo e suas verificações estiverem concluídos; se bloqueado, concluir partes independentes e indicar a causa e o estado exatos. Não alegar sincronização automática.

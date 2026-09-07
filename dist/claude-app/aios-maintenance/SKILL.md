---
name: aios-maintenance
description: Revisar, alterar ou auditar definições, personas, protocolos, skills e referências do projeto AIOS de Victor em victorsmelo/aios-vmelo. Usar para manutenção do próprio AIOS e comparação de instalações com a fonte, não para manutenção genérica de software.
---

# Manutenção do AIOS

Distinguir proposta, alteração preparada, publicação e instalação verificada.

## Entradas e modo

Identificar o pedido, as decisões aprovadas e os arquivos afetados. Ler [ambiente](references/ambiente.md), [mapa das fontes](references/fontes.md) e [DOCOPS](references/fontes/DOCOPS.md). Para editar, obter o estado atual do repositório, instruções aplicáveis, documentos afetados, índices e CHANGELOG por checkout ou conector disponível. Os snapshots identificam a base; não comprovam o estado atual remoto.

- Auditoria somente leitura: consultar e apresentar achados sem alterar arquivos, abrir PR ou instalar.
- Implementação autorizada: preparar mudanças dentro do escopo e preservar alterações preexistentes.
- Instalação autorizada: comparar pacote e conteúdo instalado, preservar customizações e seguir o mecanismo de gestão disponível. Carregar a skill de criação/gestão de skills aplicável antes dessa operação.

Não interpretar falha de acesso como ausência de arquivo. Quando faltar acesso, concluir a análise possível com as fontes fornecidas e indicar o que não foi verificado. Pedir conteúdo somente se sua ausência impedir trabalho útil.

## Análise e execução

1. Registrar problema, evidência, mudança proposta, arquivos e dependências na profundidade necessária. Separar decisão aprovada, proposta e inferência.
2. Verificar consistência entre [camadas](references/fontes/docs/architecture/layers.md), nomes, aliases, 4Ps, índices, links e exemplos. Usar a [definição AIOS](references/fontes/docs/core/AIOS.md) para o contrato entre coordenação, FOCUS e execução; evitar repeti-lo em cada documento.
3. Implementar apenas o modo autorizado. Atualizar índices, CHANGELOG e decisão arquitetural quando DOCOPS exigir. Preparar diff revisável antes de pedir uma aprovação ainda necessária; reutilizar autorização explícita já dada ao mesmo escopo.
4. Para frentes independentes de auditoria, usar `orchestrate` se disponível e permitido. Manter responsabilidade exclusiva por arquivos e restrições de leitura nas atribuições.
5. Após alterar fontes de pacotes, regenerar referências e distribuições pelo script do projeto e executar os validadores aplicáveis. Conferir diff, links, metadados e hashes.

## Saída e limites

Entregar achados ou mudanças, verificações realizadas e pendências concretas. Confirmar separadamente conteúdo salvo, publicação e instalação. Não afirmar instalação pela existência de um arquivo no GitHub, nem sincronização contínua. Se uma ação ficar bloqueada, concluir as partes independentes autorizadas e identificar o estado exato da entrega.

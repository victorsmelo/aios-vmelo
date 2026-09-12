# Instruções comuns a diferentes modelos

**Data:** 2026-09-11  
**Estado:** Aprovada

## Contexto e autorização

Após auditoria, Victor autorizou executar os cinco lotes para adequar a base a Astra, Sol, Luna e Claude: coerência documental; instruções centrais; personas; pacotes/publicação; instalações e validação. A intenção é compartilhar instruções claras e testar comportamento, sem afirmar compatibilidade universal.

## Decisões

- Definir resultado e critérios; condicionar leitura e processos ao pedido. Manter passos cuja ordem afete a correção.
- Preservar template completo, identidades, grupos, escopos, tom BHKR e critérios de evidência/unidades.
- Corrigir a menção antiga a Produto e Saídas separados e preservar o histórico da decisão substituída.
- Centralizar a regra de conclusão no AIOS, com instruções operacionais suficientes nas skills.
- Usar base comum com adaptações por ambiente. Registrar exceções de modelo apenas se houver evidência reproduzível.
- Gerar derivados e ZIPs antes do manifesto; conferir fonte, distribuição e instalação separadamente.
- Usar main nos links externos dos pacotes durante a publicação pendente, declarando mutabilidade e conservando hashes. A tag é verificada remotamente; o validador local não a comprova.
- Publicação formal mantém o ambiente protegido e revisão exigidos. A revisão v1.3.1 não cria retroativamente a tag v1.3.0.

## Alternativas e consequências

Reescrever uma variante completa por modelo aumentaria divergência sem benefício demonstrado. Apagar seções do template contrariaria escolhas anteriores. As alterações preservam detalhe de domínio e removem obrigações sem relação com a tarefa.

A [avaliação](../skills/avaliacoes-v1.3.1.md) identifica testes reais e pendências. Seguir [DOCOPS](../../DOCOPS.md) e [publicação](../../RELEASE_PROCESS.md).

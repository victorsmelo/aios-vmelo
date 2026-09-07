# Arquitetura do AIOS

**Versão:** 2026-09-07  
**Estado:** Ativa

## Componentes

| Componente | Função |
| --- | --- |
| Usuário | Definir objetivos e decisões finais |
| Políticas do ambiente | Delimitar permissões, privacidade e segurança de todas as ações |
| AIOS | Planejar, selecionar recursos, coordenar e validar |
| Protocolos | Orientar métodos de investigação e execução |
| Skills | Descrever procedimentos reutilizáveis |
| Personas | Fornecer perspectivas de domínio |
| Conectores e ferramentas | Acessar fontes e executar operações |
| Entregas | Apresentar respostas, arquivos e resultados verificados |

## Escolha do recurso

Criar uma persona quando houver um domínio recorrente com critérios próprios. Criar uma skill para um procedimento reutilizável. Definir um protocolo para um método e usar um conector para acesso a um sistema externo.

Cada pedido usa apenas os componentes necessários. O plano e a validação final permanecem no coordenador, conforme as [responsabilidades do AIOS](../core/AIOS.md). FOCUS orienta o método e orchestrate distribui trabalho independente.

Ver [mapa](../aios-persona-map.md), [personas](../personas-index.md), [protocolos](../protocols/README.md) e [skills](../skills/README.md).

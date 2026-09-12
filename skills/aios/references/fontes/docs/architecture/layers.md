> Cópia derivada de `docs/architecture/layers.md` para v1.3.1. Revisão-base: `fad18c4624293c4408487efb95e5103a5cfe470b`.
> SHA-256 da fonte antes da adaptação dos links: `a737b9cd319d671d2c6dd46c74400b56dc312d5be78ab5afc8b64573916ef0a1`. [URL da fonte](https://github.com/victorsmelo/aios-vmelo/blob/main/docs/architecture/layers.md); consultar a nota da versão para o estado de publicação.

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

Ver [mapa](https://github.com/victorsmelo/aios-vmelo/blob/main/docs/aios-persona-map.md), [personas](../personas-index.md), [protocolos](https://github.com/victorsmelo/aios-vmelo/blob/main/docs/protocols/README.md) e [skills](https://github.com/victorsmelo/aios-vmelo/blob/main/docs/skills/README.md).

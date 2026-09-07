> Cópia derivada de `docs/architecture/layers.md` da árvore de trabalho para v1.2.0. Revisão-base: `526485a6`; conteúdo novo pode ainda não estar commitado.
> SHA-256 da fonte antes da adaptação dos links: `a737b9cd319d671d2c6dd46c74400b56dc312d5be78ab5afc8b64573916ef0a1`. [URL da versão alvo](https://github.com/victorsmelo/aios-vmelo/blob/v1.2.0/docs/architecture/layers.md); a URL não comprova publicação.

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

Ver [mapa](https://github.com/victorsmelo/aios-vmelo/blob/v1.2.0/docs/aios-persona-map.md), [personas](../personas-index.md), [protocolos](https://github.com/victorsmelo/aios-vmelo/blob/v1.2.0/docs/protocols/README.md) e [skills](https://github.com/victorsmelo/aios-vmelo/blob/v1.2.0/docs/skills/README.md).

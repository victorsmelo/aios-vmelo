> Cópia derivada de `DOCOPS.md` para v1.3.0. Revisão-base: `b0b151540bf9c5061d3c2529f0d4657d4344ed0f`.
> SHA-256 da fonte antes da adaptação dos links: `3c09a8a9780e80eb44809e211a2b4263307f9181ff26b5500e7074eafb6494d9`. [URL da versão alvo](https://github.com/victorsmelo/aios-vmelo/blob/v1.3.0/DOCOPS.md); consultar a nota da versão para o estado de publicação.

# DOCOPS — manutenção documental do AIOS

DOCOPS define como revisar e publicar as definições deste projeto. É distinto das operações de documentação de produtos descritas pela persona ZHUB.

## Quando aplicar

Aplicar ao criar ou alterar personas, protocolos, skills, grupos, regras, referências, documentos e pacotes. Em auditorias somente leitura, apresentar achados sem modificar ou publicar arquivos.

## Procedimento

1. Identificar o pedido, a autorização existente e a revisão de origem.
2. Comparar a proposta com os documentos relacionados e registrar decisões estruturais em [Decisões](https://github.com/victorsmelo/aios-vmelo/blob/v1.3.0/docs/decisions/README.md).
3. Preparar alterações concretas, atualizar índices e seguir o [padrão editorial](docs/editorial.md).
4. Executar `python scripts/build_skill_packages.py --zip` e `python scripts/build_manifest.py` na raiz para gerar pacotes e atualizar o manifesto de hashes e executar as verificações de integridade e comportamento aplicáveis.
5. Apresentar para revisão humana quando houver aprovação pendente. Reutilizar a autorização explícita já dada ao mesmo escopo; não exigir uma segunda confirmação automática.
6. Publicar e verificar o estado remoto. Toda mudança estrutural exige versão formal, nota de versão e tag conforme o [processo de publicação](RELEASE_PROCESS.md).
7. Atualizar instalações somente quando autorizado e verificar cada destino separadamente. Publicação no GitHub não comprova instalação.

## Critério de conclusão

Entregar mudanças, verificações, limitações e links reais. Distinguir preparado, publicado e instalado. Não apresentar uma versão como formalmente publicada antes de verificar sua tag. Não transformar decisões propostas em fatos históricos.

Ver [checklist de integridade](https://github.com/victorsmelo/aios-vmelo/blob/v1.3.0/docs/LINK_INTEGRITY_CHECKLIST.md) e [histórico de alterações](https://github.com/victorsmelo/aios-vmelo/blob/v1.3.0/CHANGELOG.md).

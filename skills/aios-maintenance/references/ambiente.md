# Ambiente OpenAI

Usar somente ferramentas disponíveis na sessão. Acesso ao GitHub, arquivos e histórico depende dos conectores e permissões atuais. Uma skill instalada não fornece esses acessos.

Para delegação, usar as ferramentas reais de colaboração. Se houver controle de contexto, preferir atribuições autocontidas; `fork_turns: "none"` só se esse parâmetro existir na ferramenta. Se for necessário herdar todo o histórico, respeitar eventuais restrições de modelo e esforço. Não transferir parâmetros deste ambiente para outras plataformas.

Ao escolher esforço, preferir low para investigação delimitada, medium para execução e high para ambiguidades ou implementação difícil, somente se essas opções estiverem disponíveis. Ajustar ao trabalho; não elevar todos os agentes por padrão.

# Verificação de integridade

Aplicar antes de publicar mudanças, conforme [DOCOPS](../DOCOPS.md).

## Estrutura e referências

- [ ] Os documentos estão acessíveis a partir do [índice principal](../README.md).
- [ ] Links relativos, âncoras e caminhos do próprio repositório resolvem corretamente.
- [ ] Arquivos, índice e mapa contêm as mesmas personas e os cinco grupos oficiais.
- [ ] As 20 personas seguem o [template completo](templates/persona-template.md), sem seções genéricas ou vazias.
- [ ] Alterações de caminho preservam ou atualizam referências de entrada e saída.

## Pacotes e comportamento

- [ ] Metadados e referências das skills são válidos.
- [ ] Pacotes derivados correspondem às fontes e aos hashes do manifesto.
- [ ] As avaliações relevantes foram executadas e suas limitações registradas.
- [ ] O estado da instalação foi verificado separadamente da publicação.

## Escrita e publicação

- [ ] O texto segue o [padrão editorial](editorial.md) em pt-BR.
- [ ] As decisões e o histórico descrevem o que foi realmente alterado.
- [ ] Toda mudança estrutural está associada a uma nota de versão e tag verificadas.
- [ ] Não há alegação de testes executados em ambientes indisponíveis.

Execute `python3 scripts/validate_aios_docs.py` e os testes do validador na raiz. A verificação local de caminhos não comprova disponibilidade HTTP de fontes externas.

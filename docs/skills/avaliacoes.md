# Avaliações das skills — v1.2.0

Data: 2026-09-07. Registro estruturado: [avaliacoes.json](avaliacoes.json).

## Escopo e resultado

Foram executadas diretamente duas tarefas leves em Codex Work Mode, usando leitura das skills e ferramentas locais: roteamento documental FITS/BHKR e auditoria da presença das 20 personas. São verificações básicas manuais do comportamento orientado pelas skills; não comprovam seleção automática, desempenho em sessões independentes ou instalação.

As três skills atuais foram lidas integralmente: `aios`, `aios-maintenance` e `orchestrate`. Nenhum subagente foi criado pelo executor destas avaliações. As tarefas usaram somente leitura das fontes; depois foram escritos apenas estes dois arquivos de registro. Não houve publicação nem instalação.

## Execuções reais

### AIOS-01 — roteamento FITS/BHKR

**Prompt aplicado:** AIOS: classifique somente o encaminhamento de três pedidos: organizar registros de treino; organizar perguntas sobre farmacologia; organizar ambos em uma resposta. Indique FITS/BHKR e coordenação, sem orientação médica, sem editar e sem delegar.

**Resultado observado:** registros de treino → FITS; perguntas farmacológicas → BHKR; pedido misto → AIOS coordena ambas, com liderança determinada pela decisão principal. A saída foi apenas classificação documental.

**Evidência:** leitura integral de `skills/aios/SKILL.md`, ambiente, coordenação AIOS, índice e definições completas de FITS/BHKR incluídas no pacote. As seções de ativação e relação entre personas sustentam o encaminhamento. Os hashes efetivamente calculados estão no JSON.

**Aceitação:** satisfeita no escopo manual; sem orientação médica, alterações de fonte ou delegação.

### MAINT-01 — presença das personas

**Prompt aplicado:** Audite em somente leitura a presença das 20 personas do AIOS referenciadas em docs/personas-index.md. Liste quantidade, duplicatas e caminhos ausentes. Não corrija, publique, instale nem delegue.

**Resultado observado:** 20 entradas, 20 nomes únicos, 20 destinos locais presentes, zero duplicatas e zero destinos ausentes. Nomes: DSYS, DOPS, CSYS, A11Y, UXR, ZHUB, T0OL, FGM8, ENTC, AILIB, KNOW, FITS, BHKR, EVNT, AXIS, LEX, KOGN, KHELP, SOUL e F0NT.

**Evidência:** lidas a skill de manutenção e suas referências de ambiente, fontes e DOCOPS; executada extração dos links do índice e verificação de cada destino com Python. A lista completa de caminhos e resultados está no JSON.

Para reproduzir a conferência de presença, executar na raiz da árvore:

```python
from pathlib import Path
import re
index = Path("docs/personas-index.md")
entries = re.findall(r"^- \[([^]]+)\]\((personas/[^)]+)\)", index.read_text(), re.M)
print("entries=", len(entries))
print("unique=", len({name for name, _ in entries}))
print("present=", sum((index.parent / path).is_file() for _, path in entries))
for name, path in entries:
    print(name, path, (index.parent / path).is_file())
```

**Aceitação:** satisfeita para presença. A tentativa de `git status --short` retornou `fatal: not a git repository`; revisão, diff e estado remoto não foram verificados.

## Cenários preparados

Executar cada prompt completo do JSON em sessão limpa, com suas precondições. Registrar saída, chamadas de ferramentas e alterações; avaliar cada critério esperado como aprovado, reprovado ou não verificável. Não converter esta tabela em resultados executados.

| ID | Skill | Verificação | Estado |
|---|---|---|---|
| AIOS-01 | aios | Invocação positiva e roteamento FITS/BHKR | Executado manualmente em Codex |
| AIOS-02 | aios | Pergunta aritmética sem ativação indevida | Preparado |
| MAINT-01 | aios-maintenance | Auditoria sem edição; 20 personas | Executado manualmente em Codex |
| MAINT-02 | aios-maintenance | Manutenção genérica fora de escopo | Preparado |
| MAINT-03 | aios-maintenance | Edição delimitada já autorizada | Preparado |
| MAINT-04 | aios-maintenance | Falta de acesso remoto | Preparado |
| ORCH-01 | orchestrate | Paralelismo real permitido e limitado | Preparado |
| ORCH-02 | orchestrate | Tarefa simples sem delegação | Preparado |
| ORCH-03 | orchestrate | Ausência de ferramenta de colaboração | Preparado |
| ORCH-04 | orchestrate | Dependência sequencial | Preparado |

## Claude e limitações

Claude Code e Claude App: **avaliação estática preparada, não executada**. Reutilizar os prompts e critérios com os pacotes de distribuição correspondentes, registrando capacidades efetivamente disponíveis. Não transferir nomes de ferramentas ou parâmetros OpenAI para Claude. ORCH-01 só pode ser aprovado onde houver colaboração real permitida; a falta dessa capacidade deve ser registrada, sem simulação.

Não foram executados testes de publicação, instalação, edição autorizada ou delegação. Não há medição de taxa de acerto. Os dois resultados refletem a árvore local e uma aplicação manual; não validam o conteúdo integral das personas, todas as referências ou igualdade entre fonte e instalações.

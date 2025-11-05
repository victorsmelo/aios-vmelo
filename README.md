# Prompt Repo (Prompt Ops)

Repositório para versionar, revisar e publicar *prompts* e *personas*.

## Estrutura
```
prompt-repo/
├─ prompts/
│  ├─ work/
│  │  ├─ DSYS/
│  │  ├─ DOPS/
│  │  └─ A11Y/
│  └─ personal/
│     └─ AILIB/
├─ schemas/
├─ tools/
└─ .github/workflows/
```

## Quickstart
1) Faça fork/clone deste repo.
2) Edite os arquivos `.md` em `prompts/**` (front‑matter + exemplos).
3) Ao abrir um PR, a *CI* valida front‑matter contra o schema e faz *lint* de Markdown.
4) (Opcional) Ative o **GitHub Pages** para publicar um catálogo dos prompts marcados `status: active`.

> **Segurança:** mantenha este repositório privado se existirem conteúdos internos/sensíveis.

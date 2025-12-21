# AIOS Release Process

Este documento descreve o **processo oficial de release** do AIOS.

---

## Versioning Philosophy
- Versionamento semântico conceitual
- Releases marcam **estabilidade conceitual**, não frequência

Exemplo:
- v1.0.0 — Constituição + FOCUS + Personas base
- v1.1.0 — Novo protocolo ou persona estratégica
- v2.0.0 — Mudança constitucional

---

## Release Checklist

Antes de qualquer release:
- [ ] Constituição revisada (se aplicável)
- [ ] Manifesto coerente
- [ ] Protocolos atualizados
- [ ] Personas documentadas (4Ps)
- [ ] CHANGELOG atualizado
- [ ] README atualizado (se necessário)

---

## Recommended Git Flow

1. Branch de trabalho (`aios-release-x.y.z`)
2. Commit(s) documentais claros
3. Pull Request com descrição conceitual
4. Merge em `main`
5. Tag da versão

---

## Authority

- O humano decide quando algo vira release
- O AIOS auxilia, organiza e prepara
- O Git registra

---

> *Releases não celebram quantidade de mudanças,  
celebram clareza alcançada.*

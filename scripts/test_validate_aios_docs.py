"""Regressões por mutações temporárias; nenhum teste altera o repositório real."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

import validate_aios_docs as validator


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        for relative in validator.REQUIRED_FILES:
            self.write(relative, "# Documento\n\nConteúdo de referência.\n")
        self.persona = "docs/personas/juridico/AXIS.md"
        index = "# Índice\n"
        for group in validator.GROUPS:
            index += f"\n## {group}\n"
            if group == "Jurídico e Política":
                for name in ("AXIS", "LEX"):
                    index += f"\n- [{name}](personas/juridico/{name}.md)\n"
                    body = f"# {name}\n\n**Grupo:** {group}\n**Versão:** 1.2.0\n**Estado:** Ativa\n"
                    for section in validator.SECTIONS:
                        body += f"\n{section}\n\n" + ("1. Examinar o contexto e registrar a conclusão.\n" if section == "### Processo" else "Aplicar critérios do domínio ao contexto informado.\n")
                    self.write(f"docs/personas/juridico/{name}.md", body)
        self.write("docs/personas-index.md", index)
        nodes = "U A C P S D T X V O H W PE J F E AXIS LEX".split()
        diagram = "```mermaid\nflowchart TD\n" + "\n".join(f"  {node}[{node}]" for node in nodes)
        diagram += "\n" + "\n".join(f" D --> {node}" for node in validator.GROUPS.values())
        diagram += "\n J --> AXIS\n J --> LEX\n```\n"
        self.write("docs/aios-persona-map.md", diagram)
        for name in ("aios", "aios-maintenance", "orchestrate"):
            self.write(f"skills/{name}/SKILL.md", f"---\nname: {name}\ndescription: Executar o trabalho solicitado.\n---\n\n# Instruções\n\nVerificar o resultado.\n")
        self.refresh_manifest()
        self.assertEqual([], validator.validate(self.root))

    def write(self, relative, text):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def refresh_manifest(self):
        files = {p.relative_to(self.root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in (self.root / "skills").rglob("SKILL.md")}
        source = "docs/personas-index.md"
        self.write("skills/manifest.json", json.dumps({"files": files, "source_files": {source: hashlib.sha256((self.root / source).read_bytes()).hexdigest()}}))

    def assert_error(self, text):
        self.assertTrue(any(text in error for error in validator.validate(self.root)), text)

    def test_link_quebrado(self):
        self.write("README.md", "[Destino](docs/ausente.md)\n")
        self.assert_error("link quebrado")

    def test_persona_orfa(self):
        self.write("docs/personas/juridico/ORFA.md", (self.root / self.persona).read_text())
        self.assert_error("Persona órfã")

    def test_secao_faltante(self):
        body = (self.root / self.persona).read_text().replace("## Limites", "## Restrições")
        self.write(self.persona, body)
        self.assert_error("seção obrigatória ausente ou duplicada: ## Limites")

    def test_hash_invalido(self):
        self.write("skills/aios/SKILL.md", (self.root / "skills/aios/SKILL.md").read_text() + "\nAlteração.\n")
        self.assert_error("hash SHA-256 inválido")

    def test_ancora_invalida(self):
        self.write("README.md", "[Destino](docs/core/AIOS.md#não-existe)\n")
        self.assert_error("âncora inválida")

    def test_ancoras_unicode_repetidas_e_links_referencia(self):
        self.write("docs/core/AIOS.md", "# Descrição e ação\n\n# Descrição e ação\n")
        self.write("README.md", "[primeiro][ref]\n\n[ref]: docs/core/AIOS.md#descrição-e-ação-1\n")
        self.assertEqual([], validator.validate(self.root))

    def test_urls_repo_main_e_tag(self):
        for version in ("main", "v1.2.0"):
            self.write("README.md", f"[Core](https://github.com/victorsmelo/aios-vmelo/blob/{version}/docs/core/AIOS.md#documento)\n")
            self.assertEqual([], validator.validate(self.root))
        self.write("README.md", "[Core](https://github.com/victorsmelo/aios-vmelo/blob/v1.2.0/docs/inexistente.md)\n")
        self.assert_error("link quebrado")

    def test_indice_duplicado(self):
        self.write("docs/personas-index.md", (self.root / "docs/personas-index.md").read_text() + "\n[AXIS](personas/juridico/AXIS.md)\n")
        self.assert_error("persona duplicada")

    def test_mapa_grupo_incorreto(self):
        body = (self.root / "docs/aios-persona-map.md").read_text().replace("J --> AXIS", "PE --> AXIS")
        self.write("docs/aios-persona-map.md", body)
        self.assert_error("Mapa: relação obrigatória ausente: J --> AXIS")

    def test_skill_distribuida_sem_frontmatter(self):
        self.write("dist/claude-app/aios/SKILL.md", "# Skill sem frontmatter\n")
        self.assert_error("frontmatter ausente")
        self.assert_error("arquivo sem hash")

    def test_processo_curto_valido_e_placeholder_rejeitado(self):
        self.assertEqual([], validator.validate(self.root))
        body = (self.root / self.persona).read_text().replace("1. Examinar o contexto e registrar a conclusão.", "1. TODO")
        self.write(self.persona, body)
        self.assert_error("seção vazia ou placeholder: ### Processo")

    def test_links_com_parenteses_e_codigo_ignorado(self):
        self.write("docs/um(exemplo).md", "# Exemplo\n")
        self.write("README.md", "[Exemplo](docs/um(exemplo).md#exemplo)\n\n```md\n[Modelo](inexistente.md)\n```\n")
        self.assertEqual([], validator.validate(self.root))


if __name__ == "__main__":
    unittest.main()

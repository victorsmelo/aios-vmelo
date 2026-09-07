#!/usr/bin/env python3
"""Verifica a documentação AIOS, sem rede e apenas com a biblioteca padrão.

Links GitHub do próprio repositório em main ou tags v* representam caminhos
na árvore em validação; este teste não atesta a existência remota de uma tag.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "victorsmelo/aios-vmelo"
REQUIRED_FILES = (
    "README.md", "AIOS.md", "MANIFESTO.md", "DOCOPS.md", "RELEASE_PROCESS.md",
    "CHANGELOG.md", "docs/core/AIOS.md", "docs/core/README.md",
    "docs/constitution/aios-constitution.md", "docs/protocols/focus-protocol.md",
    "docs/protocols/README.md", "docs/personas/README.md", "docs/personas-index.md",
    "docs/aios-persona-map.md", "docs/LINK_INTEGRITY_CHECKLIST.md",
    "docs/templates/persona-template.md", "docs/skills/README.md", "skills/manifest.json",
    "skills/aios/SKILL.md", "skills/aios-maintenance/SKILL.md", "skills/orchestrate/SKILL.md",
)
GROUPS = {
    "Trabalho — Sistema de Design e Operações de Design": "W",
    "Pessoal — Conhecimento, Saúde e Cultura": "PE",
    "Jurídico e Política": "J",
    "Família — Assuntos familiares e escolares": "F",
    "Estratégia — Disciplina e Liderança": "E",
}
SECTIONS = (
    "## Descrição", "## 4Ps", "### Propósito", "### Persona", "### Processo",
    "### Produto", "## Orientações de ativação", "### Usar quando",
    "### Não usar quando", "## Entradas", "## Saídas", "## Limites",
    "## Personas relacionadas", "## Notas de governança",
)
PLACEHOLDER = re.compile(r"(?i)(\bTODO\b|\bTBD\b|\bFIXME\b|\bplaceholder\b|\ba preencher\b|\bpreencher aqui\b|\[descreva[^\]]*\]|<descreva[^>]*>)")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def prose(text: str) -> str:
    """Retira blocos de código e comentários, preservando quebras de linha."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    lines, fence = [], None
    for line in text.splitlines():
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if match and fence is None:
            fence = match[1]
            lines.append("")
        elif fence is not None:
            if re.match(r"^\s{0,3}" + re.escape(fence[0]) + "{" + str(len(fence)) + r",}\s*$", line):
                fence = None
            lines.append("")
        else:
            lines.append(line)
    return "\n".join(lines)


def links(text: str) -> list[tuple[str, str]]:
    """Links inline (parênteses balanceados), referências e autolinks."""
    text = re.sub(r"(`+).*?\1", "", prose(text))
    definitions = {}
    for m in re.finditer(r"(?m)^\s{0,3}\[([^\]]+)\]:\s*(?:<([^>]+)>|(\S+))", text):
        definitions[" ".join(m[1].lower().split())] = m[2] or m[3]
    text = re.sub(r"(?m)^\s{0,3}\[[^\]]+\]:[^\n]*", "", text)
    result = [(label, target) for label, target in definitions.items()]
    pattern = re.compile(r"(?<!!)\[([^\]\n]+)\]|!\[([^\]\n]*)\]")
    for m in pattern.finditer(text):
        label = m[1] if m[1] is not None else m[2]
        tail = text[m.end():]
        if tail.startswith("("):
            if tail.startswith("(<"):
                end = tail.find(">")
                if end >= 0:
                    result.append((label, tail[2:end]))
                continue
            depth, chars, escaped = 0, [], False
            for char in tail[1:]:
                if escaped:
                    chars.append(char)
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == "(":
                    depth += 1
                    chars.append(char)
                elif char == ")":
                    if depth == 0:
                        break
                    depth -= 1
                    chars.append(char)
                elif char.isspace() and depth == 0:
                    break
                else:
                    chars.append(char)
            result.append((label, "".join(chars)))
        else:
            ref = re.match(r"\[([^\]]*)\]", tail)
            key = (ref[1] or label) if ref else label
            key = " ".join(key.lower().split())
            if key in definitions:
                result.append((label, definitions[key]))
    result.extend((m[1], m[1]) for m in re.finditer(r"<(https?://[^>]+)>", text))
    return result


def anchors(text: str) -> set[str]:
    text = prose(text)
    headings = []
    lines = text.splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        if m:
            headings.append(m[1])
        elif i and re.fullmatch(r" {0,3}(?:=+|-+)\s*", line) and lines[i - 1].strip():
            headings.append(lines[i - 1].strip())
    found, counts = set(), Counter()
    for heading in headings:
        heading = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", heading)
        heading = re.sub(r"<[^>]*>", "", heading).lower()
        slug = "".join(c for c in heading if c in " _-" or unicodedata.category(c)[0] in "LN").replace(" ", "-")
        candidate = slug
        while candidate in found:
            counts[slug] += 1
            candidate = f"{slug}-{counts[slug]}"
        found.add(candidate)
    found.update(m[1] for m in re.finditer(r"(?:id|name)=[\"']([^\"']+)[\"']", text))
    return found


def local_target(root: Path, origin: Path, target: str) -> tuple[Path, str] | None:
    parsed = urlsplit(target)
    path = unquote(parsed.path)
    if parsed.scheme or parsed.netloc:
        if parsed.netloc.lower() == "github.com":
            m = re.fullmatch(re.escape("/" + REPOSITORY) + r"/(?:blob|tree)/(main|v[^/]+)(?:/(.*))?", path)
        elif parsed.netloc.lower() == "raw.githubusercontent.com":
            m = re.fullmatch(re.escape("/" + REPOSITORY) + r"/(main|v[^/]+)(?:/(.*))?", path)
        else:
            return None
        if not m:
            return None
        destination = root / (m[2] or "")
    else:
        destination = (root / path.lstrip("/")) if path.startswith("/") else (origin.parent / path if path else origin)
    return destination.resolve(), unquote(parsed.fragment)


def validate_links(root: Path, errors: list[str]) -> None:
    for origin in sorted(root.rglob("*.md")):
        if ".git" in origin.parts:
            continue
        for _, target in links(read(origin)):
            try:
                resolved = local_target(root, origin, target)
            except ValueError:
                errors.append(f"{origin.relative_to(root)}: URL inválida: {target}")
                continue
            if resolved is None:
                continue
            destination, fragment = resolved
            if not destination.is_relative_to(root) or not destination.exists():
                errors.append(f"{origin.relative_to(root)}: link quebrado: {target}")
            elif fragment:
                if destination.is_dir():
                    destination = destination / "README.md"
                if destination.suffix.lower() == ".md" and destination.is_file() and fragment not in anchors(read(destination)):
                    errors.append(f"{origin.relative_to(root)}: âncora inválida: {target}")


def validate_personas(root: Path, errors: list[str]) -> dict[str, str]:
    index = root / "docs/personas-index.md"
    if not index.is_file():
        return {}
    group, entries, seen_paths = "", {}, set()
    index_text = read(index)
    headings = re.findall(r"^## (.+)$", index_text, re.M)
    for expected in GROUPS:
        if headings.count(expected) != 1:
            errors.append(f"Índice: grupo obrigatório ausente ou duplicado: {expected}")
    for line in index_text.splitlines():
        if line.startswith("## "):
            group = line[3:].strip()
        for nickname, target in links(line):
            resolved = local_target(root, index, target)
            if resolved is None:
                continue
            path = resolved[0]
            if not path.is_relative_to(root / "docs/personas") or path.name == "README.md":
                continue
            if nickname in entries or path in seen_paths:
                errors.append(f"Índice: persona duplicada: {nickname}")
            entries[nickname] = group
            seen_paths.add(path)
            if nickname in {"AIOS", "FOCUS"}:
                errors.append(f"Índice: {nickname} não é persona")
            if group not in GROUPS:
                errors.append(f"Índice: grupo inválido para {nickname}: {group}")
            if not path.is_file():
                continue
            body = read(path)
            prefix = f"Persona {nickname}"
            if not re.match(r"\A# " + re.escape(nickname) + r"\s*(?:\n|$)", body):
                errors.append(f"{prefix}: título incompatível com o índice")
            for field in ("Grupo", "Versão", "Estado"):
                matches = re.findall(r"^\*\*" + field + r":\*\*\s*(\S[^\n]*)", body, re.M)
                if len(matches) != 1 or not matches[0].strip():
                    errors.append(f"{prefix}: metadado obrigatório ausente ou duplicado: {field}")
                elif field == "Grupo" and matches[0].strip() != group:
                    errors.append(f"{prefix}: Grupo diverge do índice")
                elif field == "Estado" and matches[0].strip() != "Ativa":
                    errors.append(f"{prefix}: Estado deve ser Ativa")
            for section in SECTIONS:
                matches = list(re.finditer(r"^" + re.escape(section) + r"\s*$", body, re.M))
                if len(matches) != 1:
                    errors.append(f"{prefix}: seção obrigatória ausente ou duplicada: {section}")
                    continue
                end = re.search(r"^#{1,3} ", body[matches[0].end():], re.M)
                content = body[matches[0].end():][:end.start() if end else None].strip()
                if section not in {"## 4Ps", "## Orientações de ativação"} and (not content or PLACEHOLDER.search(content) or content in {"...", "…", "-"}):
                    errors.append(f"{prefix}: seção vazia ou placeholder: {section}")
                if section == "### Processo" and not re.search(r"^\s*\d+[.)]\s+\S", content, re.M):
                    errors.append(f"{prefix}: Processo exige etapas numeradas com conteúdo")
    actual = {p.resolve() for p in (root / "docs/personas").rglob("*.md") if p.name != "README.md"}
    for orphan in sorted(actual - seen_paths):
        errors.append(f"Persona órfã, ausente do índice: {orphan.relative_to(root)}")
    if not entries:
        errors.append("Índice: nenhuma persona encontrada")
    return entries


def validate_map(root: Path, entries: dict[str, str], errors: list[str]) -> None:
    path = root / "docs/aios-persona-map.md"
    if not path.is_file():
        return
    blocks = "\n".join(re.findall(r"```mermaid\s*\n(.*?)```", read(path), re.S))
    nodes = set(re.findall(r"\b([A-Za-z][A-Za-z0-9_]*)\s*(?:\[|\(|\{)", blocks))
    edges = set(re.findall(r"\b([A-Za-z][A-Za-z0-9_]*)(?:\[[^\]]*\]|\([^)]*\)|\{[^}]*\})?\s*-->\s*([A-Za-z][A-Za-z0-9_]*)", blocks))
    for node in set("U A C P S D T X V O H W PE J F E".split()) | set(entries):
        if node not in nodes:
            errors.append(f"Mapa: nó obrigatório ausente: {node}")
    required = {("D", node) for node in GROUPS.values()} | {("J", "AXIS"), ("J", "LEX")}
    required |= {(GROUPS[group], name) for name, group in entries.items() if group in GROUPS}
    for edge in sorted(required - edges):
        errors.append(f"Mapa: relação obrigatória ausente: {edge[0]} --> {edge[1]}")
    for source, target in edges:
        if source in GROUPS.values() and target in entries and GROUPS.get(entries[target]) != source:
            errors.append(f"Mapa: grupo incorreto: {source} --> {target}")


def validate_skills(root: Path, errors: list[str]) -> None:
    skills = sorted((root / "skills").rglob("SKILL.md"))
    skills += sorted((root / "dist").rglob("SKILL.md")) if (root / "dist").exists() else []
    for path in skills:
        body = read(path)
        match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", body, re.S)
        if not match:
            errors.append(f"{path.relative_to(root)}: frontmatter ausente ou não encerrado")
            continue
        for field in ("name", "description"):
            values = re.findall(r"^" + field + r":\s*([^\n]*(?:\n[ \t]+[^\n]+)*)", match[1], re.M)
            if len(values) != 1 or not values[0].strip().strip("\"'") or values[0].strip() in {"|", ">", "|-", ">-", "null", "~"}:
                errors.append(f"{path.relative_to(root)}: frontmatter exige {field} não vazio e único")
        names = re.findall(r"^name:\s*([^\n]+)", match[1], re.M)
        if names and not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", names[0].strip().strip("\"'")):
            errors.append(f"{path.relative_to(root)}: name deve usar letras minúsculas, números e hífens")
        if not body[match.end():].strip():
            errors.append(f"{path.relative_to(root)}: instruções da skill vazias")


def validate_manifest(root: Path, errors: list[str]) -> None:
    path = root / "skills/manifest.json"
    if not path.is_file():
        return
    def unique_pairs(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"chave duplicada: {key}")
            result[key] = value
        return result
    try:
        manifest = json.loads(read(path), object_pairs_hook=unique_pairs)
        if not isinstance(manifest, dict):
            raise ValueError("objeto JSON esperado")
    except (ValueError, TypeError) as exc:
        errors.append(f"Manifesto inválido: {exc}")
        return
    for section in ("files", "source_files"):
        values = manifest.get(section)
        if not isinstance(values, dict) or not values:
            errors.append(f"Manifesto: {section} deve ser um objeto não vazio")
            continue
        for relative, expected in values.items():
            target = (root / relative).resolve()
            if not target.is_relative_to(root) or not target.is_file():
                errors.append(f"Manifesto {section}: arquivo ausente ou externo: {relative}")
            elif not isinstance(expected, str) or not re.fullmatch(r"[0-9a-f]{64}", expected) or hashlib.sha256(target.read_bytes()).hexdigest() != expected:
                errors.append(f"Manifesto {section}: hash SHA-256 inválido: {relative}")
    recorded = manifest.get("files", {})
    if isinstance(recorded, dict):
        for folder in ("skills", "dist"):
            for item in sorted((root / folder).rglob("*")):
                if item.is_file() and item != path and item.suffix.lower() in {".md", ".yaml", ".yml", ".json"} and item.relative_to(root).as_posix() not in recorded:
                    errors.append(f"Manifesto files: arquivo sem hash: {item.relative_to(root)}")


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    for required in REQUIRED_FILES:
        if not (root / required).is_file():
            errors.append(f"Arquivo obrigatório ausente: {required}")
    validate_links(root, errors)
    entries = validate_personas(root, errors)
    validate_map(root, entries, errors)
    validate_skills(root, errors)
    validate_manifest(root, errors)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="Raiz do repositório a validar")
    args = parser.parse_args()
    errors = validate(args.root)
    if errors:
        print("Falha na validação da documentação AIOS:\n")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Documentação AIOS validada: links, personas, mapa, skills e hashes íntegros.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

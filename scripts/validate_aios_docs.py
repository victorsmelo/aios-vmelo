#!/usr/bin/env python3
"""Validate AIOS documentation integrity.

This script performs lightweight checks for the AIOS repository:
- required entry point files exist;
- personas listed in docs/personas-index.md exist;
- persona files include required sections;
- AIOS and FOCUS are not listed as personas;
- persona map references the active personas;
- common unaccented Portuguese terms are not present in persona files.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "MANIFESTO.md",
    "DOCOPS.md",
    "RELEASE_PROCESS.md",
    "CHANGELOG.md",
    "docs/core/AIOS.md",
    "docs/core/README.md",
    "docs/constitution/aios-constitution.md",
    "docs/protocols/focus-protocol.md",
    "docs/protocols/README.md",
    "docs/personas/README.md",
    "docs/personas-index.md",
    "docs/aios-persona-map.md",
    "docs/LINK_INTEGRITY_CHECKLIST.md",
    "docs/templates/persona-template.md",
]

REQUIRED_PERSONA_SECTIONS = [
    "## Description",
    "## 4Ps",
    "### Purpose",
    "### Persona",
    "### Process",
    "### Product",
    "## Guardrails",
]

COMMON_UNACCENTED_TERMS = [
    "Operacoes",
    "governanca",
    "documentacao",
    "decisao",
    "estrategia",
    "Nao ",
    "metodo",
]


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_persona_links(index_text: str) -> list[tuple[str, str]]:
    pattern = re.compile(r"- \[([^\]]+)\]\((personas/[^)]+\.md)\)")
    return pattern.findall(index_text)


def validate_required_files(errors: list[str]) -> None:
    for relative_path in REQUIRED_FILES:
        if not (ROOT / relative_path).is_file():
            fail(f"Missing required file: {relative_path}", errors)


def validate_persona_index(errors: list[str]) -> list[tuple[str, Path]]:
    index_path = ROOT / "docs/personas-index.md"
    if not index_path.is_file():
        fail("Missing docs/personas-index.md", errors)
        return []

    index_text = read(index_path)
    links = extract_persona_links(index_text)

    if not links:
        fail("No persona links found in docs/personas-index.md", errors)
        return []

    persona_files: list[tuple[str, Path]] = []
    for nickname, relative_link in links:
        persona_path = ROOT / "docs" / relative_link
        if nickname in {"AIOS", "FOCUS"}:
            fail(f"{nickname} must not be listed as a persona", errors)
        if not persona_path.is_file():
            fail(f"Persona listed but file missing: {nickname} -> docs/{relative_link}", errors)
        else:
            persona_files.append((nickname, persona_path))

    return persona_files


def validate_persona_files(persona_files: list[tuple[str, Path]], errors: list[str]) -> None:
    for nickname, path in persona_files:
        text = read(path)

        if not text.startswith(f"# {nickname}"):
            fail(f"Persona {nickname} should start with '# {nickname}'", errors)

        if "**Group:**" not in text:
            fail(f"Persona {nickname} missing Group metadata", errors)
        if "**Version:**" not in text:
            fail(f"Persona {nickname} missing Version metadata", errors)
        if "**Status:** Active" not in text:
            fail(f"Persona {nickname} missing Status Active metadata", errors)

        for section in REQUIRED_PERSONA_SECTIONS:
            if section not in text:
                fail(f"Persona {nickname} missing required section: {section}", errors)

        process_match = re.search(r"### Process\n(?P<body>.*?)(?:\n### Product|\Z)", text, re.DOTALL)
        if process_match:
            steps = re.findall(r"^\d+\. ", process_match.group("body"), re.MULTILINE)
            if len(steps) < 5:
                fail(f"Persona {nickname} should have at least 5 numbered process steps", errors)
        else:
            fail(f"Persona {nickname} missing Process body", errors)

        for term in COMMON_UNACCENTED_TERMS:
            if term in text:
                fail(f"Persona {nickname} contains unnormalized term: {term.strip()}", errors)


def validate_persona_map(persona_files: list[tuple[str, Path]], errors: list[str]) -> None:
    map_path = ROOT / "docs/aios-persona-map.md"
    if not map_path.is_file():
        fail("Missing docs/aios-persona-map.md", errors)
        return

    map_text = read(map_path)

    for required in ["AIOS", "FOCUS", "Decisão humana"]:
        if required not in map_text:
            fail(f"Persona map missing core node/text: {required}", errors)

    for nickname, _ in persona_files:
        if nickname not in map_text:
            fail(f"Persona map missing persona: {nickname}", errors)


def main() -> int:
    errors: list[str] = []

    validate_required_files(errors)
    persona_files = validate_persona_index(errors)
    validate_persona_files(persona_files, errors)
    validate_persona_map(persona_files, errors)

    if errors:
        print("AIOS documentation validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print("AIOS documentation validation passed.")
    print(f"Validated {len(persona_files)} personas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

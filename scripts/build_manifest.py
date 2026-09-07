#!/usr/bin/env python3
"""Atualiza ou verifica o inventário de integridade dos pacotes da versão."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Verificar sem alterar arquivos')
    args = parser.parse_args()
    manifest = ROOT / 'skills/manifest.json'
    files = sorted(p for folder in ['skills', 'dist'] for p in (ROOT/folder).rglob('*') if p.is_file() and p != manifest)
    sources = sorted(set(p for folder in ['docs','references','scripts'] for p in (ROOT/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts) | set(ROOT.glob('*.md')))
    data = {'version': '1.2.0', 'automatic_sync': False,
            'files': {p.relative_to(ROOT).as_posix(): digest(p) for p in files},
            'source_files': {p.relative_to(ROOT).as_posix(): digest(p) for p in sources}}
    content = json.dumps(data, ensure_ascii=False, indent=2)+'\n'
    if args.check:
        valid = manifest.exists() and manifest.read_text() == content
        print('Manifesto confere com as fontes e pacotes.' if valid else 'Manifesto diverge; regenerar após revisar as mudanças.')
        return 0 if valid else 1
    manifest.write_text(content)
    print(f'Manifesto atualizado: {len(files)} arquivos de pacotes e {len(sources)} fontes.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())

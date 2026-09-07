#!/usr/bin/env python3
"""Verifica URLs oficiais críticas usadas na documentação do AIOS."""
from __future__ import annotations

from pathlib import Path
import re
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
ALLOWED_HOSTS = {
    "developers.openai.com",
    "learn.chatgpt.com",
    "docs.anthropic.com",
    "code.claude.com",
    "platform.claude.com",
    "support.claude.com",
}
URL = re.compile(r"https://[^\s)>]+")


def urls() -> set[str]:
    found = set()
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        for target in URL.findall(path.read_text(encoding="utf-8")):
            if urlsplit(target).netloc.lower() in ALLOWED_HOSTS:
                found.add(target.rstrip(".,;"))
    return found


def available(target: str) -> bool:
    for attempt in range(3):
        try:
            request = Request(target, method="HEAD", headers={"User-Agent": "AIOS-link-check/1.0"})
            with urlopen(request, timeout=15) as response:
                return 200 <= response.status < 400
        except HTTPError as error:
            if error.code == 405:
                try:
                    request = Request(target, headers={"User-Agent": "AIOS-link-check/1.0"})
                    with urlopen(request, timeout=15) as response:
                        return 200 <= response.status < 400
                except (HTTPError, URLError, TimeoutError):
                    pass
            elif 400 <= error.code < 500:
                return False
        except (URLError, TimeoutError):
            pass
        if attempt < 2:
            time.sleep(attempt + 1)
    return False


def main() -> int:
    failed = [target for target in sorted(urls()) if not available(target)]
    if failed:
        print("URLs oficiais indisponíveis:")
        print("\n".join(failed))
        return 1
    print(f"URLs oficiais críticas verificadas: {len(urls())}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

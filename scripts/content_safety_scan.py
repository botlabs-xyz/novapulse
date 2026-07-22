"""Scan repository content without printing matched secret values."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "_site", "vendor", "__pycache__"}
TEXT_EXTENSIONS = {
    ".css", ".html", ".js", ".json", ".md", ".py", ".txt", ".xml", ".yml", ".yaml"
}

PATTERNS = {
    "Discord bot token": re.compile(r"(?:mfa\.[\w-]{40,}|[A-Za-z0-9_-]{23,28}\.[A-Za-z0-9_-]{6}\.[A-Za-z0-9_-]{25,})"),
    "Stripe secret key": re.compile(r"\b(?:sk|rk)_(?:live|test)_[A-Za-z0-9]{16,}\b"),
    "Discord webhook credential": re.compile(r"https://(?:canary\.|ptb\.)?discord(?:app)?\.com/api/webhooks/\d+/[A-Za-z0-9_-]+", re.I),
    "Authorization header": re.compile(r"authorization\s*[:=]\s*[\"']?(?:bearer|basic)\s+[A-Za-z0-9+/_.=-]+", re.I),
    "Private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "Assigned secret": re.compile(r"(?:BOT_TOKEN|CLIENT_SECRET|STRIPE_SECRET|WEBHOOK_TOKEN)\s*=\s*[^\s<][^\r\n]*", re.I),
    "Local Windows path": re.compile(r"\b[A-Za-z]:\\(?:Users|Tools|Program Files|Windows)\\", re.I),
}


def main() -> int:
    findings: list[tuple[str, int, str]] = []
    prohibited_files: list[tuple[str, str]] = []

    for path in sorted(ROOT.rglob("*")):
        relative = path.relative_to(ROOT)
        if path.is_dir() and path.name == ".git":
            if relative != Path(".git"):
                prohibited_files.append((str(relative), "Nested Git repository"))
            continue
        if any(part in SKIP_DIRS for part in relative.parts):
            continue
        if path.is_dir():
            continue
        lower_name = path.name.lower()
        if lower_name == ".env" or (lower_name.startswith(".env.") and lower_name != ".env.example"):
            prohibited_files.append((str(relative), "Environment file"))
        if path.suffix.lower() in {".db", ".sqlite", ".sqlite3", ".log", ".zip", ".7z", ".bak"}:
            prohibited_files.append((str(relative), "Runtime, archive, backup, or database file"))
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for line_number, line in enumerate(lines, start=1):
            for category, pattern in PATTERNS.items():
                if pattern.search(line):
                    findings.append((str(relative), line_number, category))

    if prohibited_files or findings:
        print(f"FAIL: {len(prohibited_files) + len(findings)} content-safety finding(s)")
        for path, category in prohibited_files:
            print(f"{path} | line - | {category} | Remove before commit")
        for path, line, category in findings:
            print(f"{path} | line {line} | {category} | Remove or replace before commit")
        return 1

    print("PASS: no credentials, webhook tokens, private keys, runtime data, archives, databases, nested Git repositories, or local Windows paths detected")
    return 0


if __name__ == "__main__":
    sys.exit(main())

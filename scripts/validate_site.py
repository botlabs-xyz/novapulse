"""Validate the generated NovaPulse Jekyll site without external services."""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "_site"
BASEURL = "/novapulse"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[tuple[str, str]] = []
        self.ids: set[str] = set()
        self.h1_count = 0
        self.html_lang = ""
        self.title_seen = False
        self.description_seen = False
        self.canonical_seen = False
        self.images_without_alt = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "html":
            self.html_lang = values.get("lang") or ""
        if tag == "h1":
            self.h1_count += 1
        if tag == "title":
            self.title_seen = True
        if values.get("id"):
            self.ids.add(values["id"] or "")
        if tag == "meta" and values.get("name") == "description" and values.get("content"):
            self.description_seen = True
        if tag == "link" and values.get("rel") == "canonical" and values.get("href"):
            self.canonical_seen = True
        if tag == "img" and "alt" not in values:
            self.images_without_alt += 1
        for attr in ("href", "src"):
            if values.get(attr):
                self.links.append((attr, values[attr] or ""))


def resolve_internal(url: str) -> tuple[Path, str] | None:
    parsed = urlparse(url)
    if parsed.scheme or parsed.netloc or url.startswith(("mailto:", "tel:", "data:")):
        return None
    path = unquote(parsed.path)
    if not path:
        return None
    if path.startswith(BASEURL):
        path = path[len(BASEURL) :]
    elif path.startswith("/"):
        raise ValueError(f"root-relative path misses baseurl: {url}")
    else:
        return None
    relative = path.lstrip("/")
    target = BUILD / relative
    if not relative or path.endswith("/"):
        target = target / "index.html"
    elif not target.suffix:
        target = target / "index.html"
    return target, parsed.fragment


def main() -> int:
    failures: list[str] = []
    parsers: dict[Path, PageParser] = {}

    for yaml_path in (ROOT / "_config.yml", ROOT / "_data" / "navigation.yml"):
        text = yaml_path.read_text(encoding="utf-8")
        if "\t" in text or not text.strip():
            failures.append(f"YAML {yaml_path.relative_to(ROOT)}: empty content or tab indentation")

    if not BUILD.exists():
        failures.append("Build directory is missing")
    else:
        for html_path in sorted(BUILD.rglob("*.html")):
            parser = PageParser()
            parser.feed(html_path.read_text(encoding="utf-8"))
            parsers[html_path.resolve()] = parser
            relative = html_path.relative_to(BUILD)
            if not parser.html_lang:
                failures.append(f"HTML {relative}: missing lang")
            if not parser.title_seen:
                failures.append(f"HTML {relative}: missing title")
            if not parser.description_seen:
                failures.append(f"HTML {relative}: missing meta description")
            if not parser.canonical_seen:
                failures.append(f"HTML {relative}: missing canonical link")
            if parser.h1_count != 1:
                failures.append(f"HTML {relative}: expected one h1, found {parser.h1_count}")
            if parser.images_without_alt:
                failures.append(f"HTML {relative}: image missing alt")

        for source_path, parser in parsers.items():
            source_relative = source_path.relative_to(BUILD.resolve())
            for attr, url in parser.links:
                try:
                    resolved = resolve_internal(url)
                except ValueError as exc:
                    failures.append(f"LINK {source_relative}: {exc}")
                    continue
                if resolved is None:
                    continue
                target, fragment = resolved
                target = target.resolve()
                if not target.exists():
                    failures.append(f"LINK {source_relative}: missing {attr} target {url}")
                    continue
                if fragment and target.suffix.lower() == ".html":
                    target_parser = parsers.get(target)
                    if target_parser and fragment not in target_parser.ids:
                        failures.append(f"LINK {source_relative}: missing fragment #{fragment} in {url}")

    try:
        json.loads((BUILD / "search.json").read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        failures.append(f"JSON search.json: {exc}")

    css = (ROOT / "assets" / "css" / "style.css").read_text(encoding="utf-8")
    css_without_comments = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    if css_without_comments.count("{") != css_without_comments.count("}"):
        failures.append("CSS style.css: unbalanced braces")

    expected_links = {
        "https://discord.com/oauth2/authorize?client_id=1354663481021829150",
        "https://discord.gg/BusuZp2G8w",
        "https://afterpartylabs.xyz",
    }
    built_text = "\n".join(path.read_text(encoding="utf-8") for path in parsers)
    for expected in expected_links:
        if expected not in built_text:
            failures.append(f"LINK expected public URL missing: {expected}")

    if failures:
        print(f"FAIL: {len(failures)} validation finding(s)")
        for failure in failures:
            print(failure)
        return 1

    print(f"PASS: {len(parsers)} HTML pages, internal links, assets, metadata, YAML structure, JSON, and CSS checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Public-copy gate checker (universal prose rules).

Stdlib only. See docs/public-copy-gates.md. wavves-specific purpose gates are
manual (docs/purpose-gates.md).

Usage:
  python3 evals/check_public_copy.py [paths...]
  python3 evals/check_public_copy.py --fix path/to/file.md
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parent.parent
SUPPORTED = {".html", ".htm", ".md", ".txt"}
DEFAULT_PATHS = [
    PLUGIN_ROOT / "index.html",
    PLUGIN_ROOT / "README.md",
    PLUGIN_ROOT / "docs",
    PLUGIN_ROOT / "examples",
]

AFFIRM = re.compile(r"\b(rather than|instead of)\b", re.IGNORECASE)
NO_LONGER = re.compile(r"\bno longer\b", re.IGNORECASE)
ASCII_DASH = re.compile(r"\s--\s")
FILLER = [
    re.compile(r"\bactually\b", re.IGNORECASE),
    re.compile(r"\bperhaps\b", re.IGNORECASE),
    re.compile(r"could lead to", re.IGNORECASE),
    re.compile(r"might result in", re.IGNORECASE),
    re.compile(r"what if i told you", re.IGNORECASE),
    re.compile(r"what emerges", re.IGNORECASE),
    re.compile(r"let's see what happens", re.IGNORECASE),
    re.compile(r"it's not just", re.IGNORECASE),
    re.compile(r"not just\b.*[\u2013\u2014-]", re.IGNORECASE),
]
OXFORD_LIST = re.compile(r",(\s+[^,]+),\s+(and|or)\s", re.IGNORECASE)
COMMA_AND = re.compile(r",\s+and\s", re.IGNORECASE)
SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")
WORD = re.compile(r"\b[\w']+\b")
HTML_BLOCK = re.compile(r"<(style|script)\b.*?</\1>|<!--.*?-->", re.IGNORECASE | re.DOTALL)
HTML_TAG = re.compile(r"<[^>]*>")
MD_FENCE = re.compile(r"```.*?```", re.DOTALL)
ENTITIES = {"&amp;": "&", "&lt;": "<", "&gt;": ">", "&nbsp;": " "}


def decode_entities(s: str) -> str:
    for key, value in ENTITIES.items():
        s = s.replace(key, value)
    return s


def visible_lines(path: Path, text: str) -> list[tuple[int, str]]:
    ext = path.suffix.lower()
    if ext in (".html", ".htm"):
        text = HTML_BLOCK.sub(lambda m: "\n" * m.group(0).count("\n"), text)
        return [
            (i, decode_entities(HTML_TAG.sub("", line)).strip())
            for i, line in enumerate(text.split("\n"), 1)
        ]
    if ext == ".md":
        text = MD_FENCE.sub(lambda m: "\n" * m.group(0).count("\n"), text)
        return [(i, line.strip()) for i, line in enumerate(text.split("\n"), 1)]
    return [(i, line.strip()) for i, line in enumerate(text.split("\n"), 1)]


def oxford_hit(txt: str) -> bool:
    return bool(COMMA_AND.search(txt) or OXFORD_LIST.search(txt))


def oxford_remedy(snippet: str) -> str:
    if COMMA_AND.search(snippet):
        return "try: replace ', and' with ', while' or split into two sentences"
    if OXFORD_LIST.search(snippet):
        return "try: remove the comma before the final and/or in the list"
    return ""


def apply_oxford_fixes(text: str) -> tuple[str, int]:
    changes = 0
    fixed, n = OXFORD_LIST.subn(r"\1 \2 ", text)
    changes += n
    fixed, n = COMMA_AND.subn(", while ", fixed)
    changes += n
    return fixed, changes


def heading_lines(path: Path, text: str) -> set[int]:
    ext = path.suffix.lower()
    heads: set[int] = set()
    for i, line in enumerate(text.split("\n"), 1):
        s = line.strip()
        if ext in (".html", ".htm") and re.search(r"<h[1-6]\b", s, re.IGNORECASE):
            heads.add(i)
        elif ext == ".md" and re.match(r"#{1,6}\s", s):
            heads.add(i)
    return heads


def hero_lines(path: Path, text: str) -> set[int]:
    if path.suffix.lower() not in (".html", ".htm"):
        return set()
    return {i for i, line in enumerate(text.split("\n"), 1) if 'class="hero-copy"' in line}


def lead_sentences(
    path: Path, vlines: list[tuple[int, str]], heads: set[int], heroes: set[int]
) -> list[tuple[int, str]]:
    leads: list[tuple[int, str]] = []
    cur: list[str] = []
    start = 0
    after_head = False
    for lineno, txt in vlines:
        if lineno in heroes and txt:
            first = SENTENCE_SPLIT.split(txt)[0]
            leads.append((lineno, first))
            continue
        is_head = lineno in heads
        if not txt or is_head:
            if cur and after_head:
                first = SENTENCE_SPLIT.split(" ".join(cur))[0]
                leads.append((start, first))
            cur = []
            after_head = is_head
            start = lineno + 1 if is_head else start
            continue
        if not cur:
            start = lineno
        cur.append(txt)
    if cur and after_head:
        first = SENTENCE_SPLIT.split(" ".join(cur))[0]
        leads.append((start, first))
    return leads


def check_file(path: Path) -> list[tuple[str, str, int, str]]:
    findings: list[tuple[str, str, int, str]] = []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        return [("READ", "fail", 0, str(exc))]

    vlines = visible_lines(path, text)
    for lineno, txt in vlines:
        if not txt:
            continue
        if AFFIRM.search(txt):
            findings.append(("AFFIRM", "fail", lineno, txt))
        if "\u2014" in txt or "\u2013" in txt or ASCII_DASH.search(txt):
            findings.append(("DASH", "fail", lineno, txt))
        if NO_LONGER.search(txt):
            findings.append(("NO_LONGER", "fail", lineno, txt))
        for pat in FILLER:
            if pat.search(txt):
                findings.append(("FILLER", "fail", lineno, txt))
                break
        if oxford_hit(txt):
            findings.append(("OXFORD", "fail", lineno, txt))

    if path.suffix.lower() in (".html", ".htm", ".md"):
        heads = heading_lines(path, text)
        heroes = hero_lines(path, text)
        for start, first in lead_sentences(path, vlines, heads, heroes):
            wc = len(WORD.findall(first))
            if 0 < wc < 15:
                findings.append(("LEAD", "warn", start, f"{wc} words: {first[:120]}"))

    return findings


def gather(paths: list[Path]) -> list[Path]:
    out: list[Path] = []
    for path in paths:
        if path.is_dir():
            out.extend(
                sorted(
                    f for f in path.rglob("*") if f.is_file() and f.suffix.lower() in SUPPORTED
                )
            )
        elif path.is_file():
            out.append(path)
        else:
            print(f"warning: not found: {path}", file=sys.stderr)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Public-copy gate checker (wavves plugin).")
    ap.add_argument("paths", nargs="*", help="files or dirs (default: plugin public surfaces)")
    ap.add_argument("--fix", action="store_true", help="apply OXFORD remedies to given files")
    ap.add_argument("--strict", action="store_true", help="treat LEAD warnings as failures")
    args = ap.parse_args()

    if args.fix:
        if not args.paths:
            ap.error("--fix requires explicit file path(s)")
        for path in [Path(p) for p in args.paths]:
            if not path.is_file():
                print(f"skip: {path}", file=sys.stderr)
                continue
            original = path.read_text(encoding="utf-8", errors="replace")
            fixed, n = apply_oxford_fixes(original)
            if n:
                path.write_text(fixed, encoding="utf-8")
                print(f"fixed {path}: {n} OXFORD rewrite(s)")
            else:
                print(f"unchanged: {path}")
        return 0

    targets = [Path(p) for p in args.paths] if args.paths else DEFAULT_PATHS
    files = gather(targets)
    fails = warns = 0
    for path in files:
        findings = check_file(path)
        if not findings:
            continue
        print(f"\n{path}")
        for gate, sev, lineno, snippet in findings:
            tag = "FAIL" if sev == "fail" else "warn"
            print(f"  {tag} {gate} L{lineno}: {snippet[:140]}")
            if gate == "OXFORD":
                hint = oxford_remedy(snippet)
                if hint:
                    print(f"         → {hint}")
            if sev == "fail":
                fails += 1
            else:
                warns += 1

    print(f"\nChecked {len(files)} file(s): {fails} hard-fail, {warns} review.")
    if fails or (args.strict and warns):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

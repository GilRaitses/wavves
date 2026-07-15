#!/usr/bin/env python3
"""Mechanical paragraph-tunnel fixture checker.

Stdlib only. No network. No LLM.

WHAT THIS SCRIPT DOES NOT DO:
  It does not replay a live Grok adversarial gate. It is a tripwire on
  closed-vocab heuristics against fixture expected.md.

WHAT THIS SCRIPT DOES:
  For each evals/fixtures/paragraph-tunnel-*/ directory, read input.md and
  expected.md, detect fail ids, compare to expected_verdict + fail_ids.

Whitelist (PTG-NICE-BECAUSE / APPL-NICE-BECAUSE-ALLOWED):
  "nice because" / "because it is" NEVER alone produce a fail id.
  PN-BECAUSE / P2-BECAUSE / PN-EXPLAIN / P2-EXPLAIN are never emitted.

Usage:
  python3 evals/check_paragraph_tunnel.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"
PREFIX = "paragraph-tunnel-"

STRUCK_IDS = frozenset(
    {"PN-BECAUSE", "P2-BECAUSE", "PN-EXPLAIN", "P2-EXPLAIN", "BECAUSE", "EXPLAIN"}
)

GLOSS_RE = re.compile(r"personality of|part of how", re.IGNORECASE)
COMPARE_RE = re.compile(
    r"\bthan the\b|\bcompared to\b|\bunlike\b|\bquieter than\b|\bdestination food\b",
    re.IGNORECASE,
)
STANDIN_RE = re.compile(
    r"\bstand-ins?\b|\bstand in\b|\bfair stand-in\b|\bkind of place\b|"
    r"\bfair example\b|\blooked like a\b",
    re.IGNORECASE,
)
RESEARCH_RE = re.compile(
    r"early research|research phase|part i care about|for my research",
    re.IGNORECASE,
)
PLACE_TYPE_RE = re.compile(
    r"\b(shop|bar|florist|bagel|cafe|restaurant|wine bar)\b", re.IGNORECASE
)
FIXTURE_TOKENS = ("glass", "planter", "awning", "curb")
SCENE_RE = re.compile(
    r"\b(patio|frontage|sidewalk|block|line|queue|awning)\b", re.IGNORECASE
)
TYPE_RESTATE_RE = re.compile(
    r"\b(wine bar|bagel shop|florist|outdoor seating|independent)\b", re.IGNORECASE
)
COME_TOGETHER_RE = re.compile(r"come together", re.IGNORECASE)
SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")


def parse_expected(text: str) -> dict:
    verdict_m = re.search(r"^expected_verdict:\s*(PASS|FAIL)\s*$", text, re.MULTILINE)
    ids_m = re.search(r"^fail_ids:\s*(\[.*\])\s*$", text, re.MULTILINE)
    ground_m = re.search(r"^ground_truth:\s*(.+)$", text, re.MULTILINE)
    forbid_m = re.search(r"^forbidden_claims:\s*(.+)$", text, re.MULTILINE)
    if not verdict_m:
        raise ValueError("missing expected_verdict")
    fail_ids: list[str] = []
    if ids_m:
        fail_ids = json.loads(ids_m.group(1))
    return {
        "expected_verdict": verdict_m.group(1),
        "fail_ids": fail_ids,
        "ground_truth": ground_m.group(1).strip() if ground_m else "",
        "forbidden_claims": forbid_m.group(1).strip() if forbid_m else "",
    }


def extract_paragraph(input_text: str) -> str:
    """Prefer a `paragraph:` field; else first non-empty non-heading line block."""
    field = re.search(
        r"^paragraph:\s*(.+?)(?=\n[a-z_]+:|\Z)",
        input_text,
        re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    if field:
        return " ".join(field.group(1).split())
    lines = []
    for line in input_text.splitlines():
        s = line.strip()
        if not s or s.startswith("#") or re.match(r"^[a-z_]+:\s*", s, re.I):
            if lines:
                break
            continue
        lines.append(s)
    return " ".join(lines).strip()


def sentence_count(text: str) -> int:
    parts = [p.strip() for p in SENTENCE_SPLIT.split(text.strip()) if p.strip()]
    return len(parts) if parts else 0


def detect_fixture(text: str) -> bool:
    hits = sum(1 for tok in FIXTURE_TOKENS if re.search(rf"\b{tok}", text, re.I))
    return hits >= 2 and not PLACE_TYPE_RE.search(text)


def detect_stack(text: str) -> bool:
    """STACK = gloss piled onto place fact, or come-together + type restatement.

    A single place-fact sentence (type + sidewalk line) is NOT stack.
    """
    has_gloss = bool(GLOSS_RE.search(text))
    has_scene = bool(SCENE_RE.search(text))
    has_type = bool(TYPE_RESTATE_RE.search(text))
    has_come = bool(COME_TOGETHER_RE.search(text))
    if has_gloss and (has_scene or has_type or has_come or sentence_count(text) > 1):
        return True
    if has_come and has_type and has_scene:
        return True
    return False


def detect_falsefact(text: str, expected: dict) -> bool:
    forbidden = expected.get("forbidden_claims") or ""
    if forbidden:
        for claim in re.split(r"\s*\|\s*", forbidden):
            claim = claim.strip()
            if claim and re.search(re.escape(claim), text, re.IGNORECASE):
                return True
    ground = expected.get("ground_truth") or ""
    if not ground:
        return False
    # Minimal: if ground_truth tokens include a required place cue and text
    # asserts a conflicting forbidden phrase already handled; otherwise no
    # world-knowledge FALSEFACT without forbidden_claims.
    return False


def detect_fail_ids(text: str, expected: dict) -> list[str]:
    found: list[str] = []
    if sentence_count(text) > 1:
        found.append("PN-MULTI")
    if GLOSS_RE.search(text):
        found.append("PN-GLOSS")
    if COMPARE_RE.search(text):
        found.append("PN-COMPARE")
    if detect_stack(text):
        found.append("PN-STACK")
    if detect_fixture(text):
        found.append("PN-FIXTURE")
    if STANDIN_RE.search(text):
        found.append("STANDIN")
    if RESEARCH_RE.search(text):
        found.append("RESEARCH-META")
    if detect_falsefact(text, expected):
        found.append("FALSEFACT")
    # Explicit whitelist: never emit struck ids even if somehow listed
    return [fid for fid in found if fid not in STRUCK_IDS]


def load_fixture(path: Path) -> dict:
    input_path = path / "input.md"
    expected_path = path / "expected.md"
    missing = [p.name for p in (input_path, expected_path) if not p.exists()]
    if missing:
        return {"name": path.name, "error": f"missing files: {missing}"}
    expected = parse_expected(expected_path.read_text(encoding="utf-8"))
    paragraph = extract_paragraph(input_path.read_text(encoding="utf-8"))
    if not paragraph:
        return {"name": path.name, "error": "empty paragraph in input.md"}
    detected = detect_fail_ids(paragraph, expected)
    return {
        "name": path.name,
        "paragraph": paragraph,
        "expected": expected,
        "detected": detected,
    }


def verdict_from_ids(fail_ids: list[str]) -> str:
    return "FAIL" if fail_ids else "PASS"


def main() -> int:
    if not FIXTURES_DIR.is_dir():
        print(f"FAIL: fixtures dir missing: {FIXTURES_DIR}", file=sys.stderr)
        return 2

    fixtures = sorted(
        p for p in FIXTURES_DIR.iterdir() if p.is_dir() and p.name.startswith(PREFIX)
    )
    if not fixtures:
        print(f"FAIL: no {PREFIX}* fixtures under {FIXTURES_DIR}", file=sys.stderr)
        return 2

    passed = 0
    failed = 0
    results = []

    for path in fixtures:
        loaded = load_fixture(path)
        if "error" in loaded:
            failed += 1
            print(f"FAIL  {path.name}: {loaded['error']}")
            results.append({"name": path.name, "status": "FAIL", "error": loaded["error"]})
            continue

        expected_ids = set(loaded["expected"]["fail_ids"])
        detected_ids = set(loaded["detected"])
        expected_verdict = loaded["expected"]["expected_verdict"]
        actual_verdict = verdict_from_ids(loaded["detected"])

        # Guard: expected must not ask for struck ids
        if expected_ids & STRUCK_IDS:
            failed += 1
            print(
                f"FAIL  {path.name}: expected fail_ids contain struck ids "
                f"{sorted(expected_ids & STRUCK_IDS)}"
            )
            results.append({"name": path.name, "status": "FAIL", "error": "struck ids"})
            continue

        ok = expected_ids == detected_ids and expected_verdict == actual_verdict
        if ok:
            passed += 1
            print(
                f"PASS  {path.name}: verdict={actual_verdict} "
                f"fail_ids={sorted(detected_ids)}"
            )
            results.append(
                {
                    "name": path.name,
                    "status": "PASS",
                    "verdict": actual_verdict,
                    "fail_ids": sorted(detected_ids),
                }
            )
        else:
            failed += 1
            print(
                f"FAIL  {path.name}: expected_verdict={expected_verdict} "
                f"actual_verdict={actual_verdict} "
                f"expected_ids={sorted(expected_ids)} "
                f"detected_ids={sorted(detected_ids)}"
            )
            results.append(
                {
                    "name": path.name,
                    "status": "FAIL",
                    "expected_verdict": expected_verdict,
                    "actual_verdict": actual_verdict,
                    "expected_ids": sorted(expected_ids),
                    "detected_ids": sorted(detected_ids),
                }
            )

    print(f"\nsummary: pass={passed} fail={failed} total={passed + failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

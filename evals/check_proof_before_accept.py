#!/usr/bin/env python3
"""Mechanical proof-before-accept fixture checker.

Stdlib only. No network. No LLM.

WHAT THIS SCRIPT DOES NOT DO:
  It does not run a live DOM/host probe. It is a tripwire on keyed fields
  and ACCEPT criteria text against fixture expected.md.
  It never emits review-only ids (PROC-CHROME-THRASH, PROC-DEBT-AS-DONE,
  PROC-BLANK-CANVAS).

WHAT THIS SCRIPT DOES:
  For each evals/fixtures/proof-before-accept-*/ directory, read input.md
  and expected.md, detect mechanical fail ids, compare to expected_verdict
  + fail_ids.

Usage:
  python3 evals/check_proof_before_accept.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"
PREFIX = "proof-before-accept-"

MECHANICAL_IDS = frozenset({"PROC-PASS-NO-PROOF", "PROC-NO-VISUAL"})
REVIEW_ONLY_IDS = frozenset(
    {"PROC-CHROME-THRASH", "PROC-DEBT-AS-DONE", "PROC-BLANK-CANVAS"}
)

PROCESS_MARKERS = (
    "LAND-C",
    "honesty",
    "e2e shell",
    "HEAD match",
)
PROOF_HARNESS_TOKENS = (
    "check_proof_before_accept",
    "proof_job",
    "host_height",
    "primary product host",
)
PROOF_CAPTURE_RE = re.compile(r"gate-captures/.*proof", re.IGNORECASE)

FIELD_RE = re.compile(
    r"^(?P<key>[a-z_][a-z0-9_]*)\s*:\s*(?P<value>.*?)\s*$",
    re.IGNORECASE | re.MULTILINE,
)
ACCEPT_BLOCK_RE = re.compile(
    r"(?:^|\n)\s*(?:accept_criteria|acceptance)\s*:\s*"
    r"(?P<body>.*?)(?=\n[a-z_][a-z0-9_]*\s*:|\Z)",
    re.IGNORECASE | re.DOTALL,
)


def parse_expected(text: str) -> dict:
    verdict_m = re.search(r"^expected_verdict:\s*(PASS|FAIL)\s*$", text, re.MULTILINE)
    ids_m = re.search(r"^fail_ids:\s*(\[.*\])\s*$", text, re.MULTILINE)
    if not verdict_m:
        raise ValueError("missing expected_verdict")
    fail_ids: list[str] = []
    if ids_m:
        fail_ids = json.loads(ids_m.group(1))
    return {
        "expected_verdict": verdict_m.group(1),
        "fail_ids": fail_ids,
    }


def _normalize_value(raw: str) -> str:
    return " ".join(raw.strip().split())


def parse_fields(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for m in FIELD_RE.finditer(text):
        key = m.group("key").lower()
        # Skip accept_criteria / acceptance; handled as a block.
        if key in {"accept_criteria", "acceptance"}:
            continue
        fields[key] = _normalize_value(m.group("value"))
    return fields


def extract_accept_block(text: str) -> str:
    m = ACCEPT_BLOCK_RE.search(text)
    if m:
        return m.group("body").strip()
    # Fallback: lines under a markdown Acceptance / ACCEPT heading.
    heading = re.search(
        r"(?im)^#{1,6}\s*(accept(?:ance)?(?:\s+criteria)?|ACCEPT)\s*$",
        text,
    )
    if not heading:
        return ""
    rest = text[heading.end() :]
    stop = re.search(r"(?m)^#{1,6}\s+\S", rest)
    body = rest[: stop.start()] if stop else rest
    return body.strip()


def field_present_nonempty(fields: dict[str, str], key: str) -> bool:
    val = fields.get(key)
    return bool(val)


def has_process_only_accept(accept_text: str) -> bool:
    if not accept_text:
        return False
    lower = accept_text.lower()
    has_process = any(marker.lower() in lower for marker in PROCESS_MARKERS)
    if not has_process:
        return False
    has_token = any(tok.lower() in lower for tok in PROOF_HARNESS_TOKENS)
    has_capture = bool(PROOF_CAPTURE_RE.search(accept_text))
    return not (has_token or has_capture)


def has_optout_without_rationale(fields: dict[str, str]) -> bool:
    proof_ref = fields.get("proof_reference", "").lower()
    visual = fields.get("visual_accept", "").lower()
    rationale_keys = (
        "rationale",
        "proof_reference_rationale",
        "visual_accept_rationale",
    )
    has_rationale = any(field_present_nonempty(fields, k) for k in rationale_keys)

    optout = False
    if proof_ref in {"none", "no"}:
        optout = True
    if visual == "no":
        optout = True
    return optout and not has_rationale


def has_harness(fields: dict[str, str], text: str) -> bool:
    if field_present_nonempty(fields, "proof_harness"):
        return True
    if field_present_nonempty(fields, "dom_harness"):
        return True
    # Command string anywhere in input (field values or prose).
    if re.search(r"check_proof_before_accept(?:\.py)?", text, re.IGNORECASE):
        return True
    if re.search(r"evals/check_proof_before_accept\.py", text, re.IGNORECASE):
        return True
    return False


def needs_visual_harness(fields: dict[str, str]) -> bool:
    """True when visual accept is required and harness must be present."""
    if "visual_accept" not in fields:
        # Omitted while proof_required yes: need harness unless explicit
        # visual_accept:no + rationale (which would set the key).
        return True
    visual = fields["visual_accept"].lower()
    if visual == "yes":
        return True
    return False


def detect_fail_ids(text: str) -> list[str]:
    fields = parse_fields(text)
    accept = extract_accept_block(text)
    proof_required = fields.get("proof_required", "").lower()

    found: list[str] = []
    if proof_required != "yes":
        return found

    # PROC-PASS-NO-PROOF
    missing_job = not field_present_nonempty(fields, "proof_job")
    process_only = has_process_only_accept(accept)
    bad_optout = has_optout_without_rationale(fields)
    if missing_job or process_only or bad_optout:
        found.append("PROC-PASS-NO-PROOF")

    # PROC-NO-VISUAL
    if needs_visual_harness(fields) and not has_harness(fields, text):
        found.append("PROC-NO-VISUAL")

    # Never emit review-only ids.
    return [fid for fid in found if fid in MECHANICAL_IDS]


def load_fixture(path: Path) -> dict:
    input_path = path / "input.md"
    expected_path = path / "expected.md"
    missing = [p.name for p in (input_path, expected_path) if not p.exists()]
    if missing:
        return {"name": path.name, "error": f"missing files: {missing}"}
    expected = parse_expected(expected_path.read_text(encoding="utf-8"))
    input_text = input_path.read_text(encoding="utf-8")
    if not input_text.strip():
        return {"name": path.name, "error": "empty input.md"}
    detected = detect_fail_ids(input_text)
    return {
        "name": path.name,
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

    for path in fixtures:
        loaded = load_fixture(path)
        if "error" in loaded:
            failed += 1
            print(f"FAIL  {path.name}: {loaded['error']}")
            continue

        expected_ids = set(loaded["expected"]["fail_ids"])
        detected_ids = set(loaded["detected"])
        expected_verdict = loaded["expected"]["expected_verdict"]
        actual_verdict = verdict_from_ids(loaded["detected"])

        if expected_ids & REVIEW_ONLY_IDS:
            failed += 1
            print(
                f"FAIL  {path.name}: expected fail_ids contain review-only ids "
                f"{sorted(expected_ids & REVIEW_ONLY_IDS)}"
            )
            continue

        ok = expected_ids == detected_ids and expected_verdict == actual_verdict
        if ok:
            passed += 1
            print(
                f"PASS  {path.name}: verdict={actual_verdict} "
                f"fail_ids={sorted(detected_ids)}"
            )
        else:
            failed += 1
            print(
                f"FAIL  {path.name}: expected_verdict={expected_verdict} "
                f"actual_verdict={actual_verdict} "
                f"expected_ids={sorted(expected_ids)} "
                f"detected_ids={sorted(detected_ids)}"
            )

    print(f"\nsummary: pass={passed} fail={failed} total={passed + failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

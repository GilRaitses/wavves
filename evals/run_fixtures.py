#!/usr/bin/env python3
"""Structured checklist verifier for the wavves eval fixture corpus.

WHAT THIS SCRIPT DOES NOT DO (read this before trusting a PASS):

It does not invoke an LLM. It does not replay a real `mod-check` review
against a fixture's `input.md`. It cannot reproduce actual agent judgment.

WHAT THIS SCRIPT DOES:

For each fixture under `evals/fixtures/<case-name>/`, it reads
`expected.md`, extracts the fixture's declared `seeded_defect_category`,
`defect_keywords` and `lens_that_should_catch` fields, then reads the four
lens rows out of the real, live `skills/mod-check/SKILL.md` "Default
parallel lenses" table and checks whether the named lens's "hunts for" text
contains at least one of the declared keywords (case-insensitive substring
match). It reports PASS when the current lens wording plausibly still
claims coverage of the fixture's defect category, and FAIL when it does
not (for example, after a future edit narrows that lens's wording so none
of the keywords remain).

This is a regression tripwire on the LENS WORDING, not a test of whether an
agent would actually catch the seeded defect in practice. See
`evals/README.md` "Known limitation" for the full statement of this gap.
"""

import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"
# Override to point the runner at a scratch copy of mod-check/SKILL.md
# instead of the live installed file, per the regression-gate workflow in
# charter/SKILL.md ("apply the proposed diff to a scratch copy ... point
# the runner at that scratch copy").
MOD_CHECK_SKILL = Path(
    os.environ.get(
        "WAVVES_EVAL_MOD_CHECK_SKILL",
        str(REPO_ROOT / "skills" / "mod-check" / "SKILL.md"),
    )
)

LENS_TABLE_ROW_RE = re.compile(
    r"^\|\s*`<CODE>-(W1[a-d])`\s*\|\s*([a-z]+)\s*\|\s*`([^`]+)`\s*\|\s*(.+?)\s*\|\s*$"
)


def parse_mod_check_lenses(skill_text: str) -> dict:
    """Return {lens_name: hunts_for_text} parsed from the real lens table."""
    lenses = {}
    for line in skill_text.splitlines():
        m = LENS_TABLE_ROW_RE.match(line.strip())
        if m:
            _wave_id, lens_name, _owns, hunts_for = m.groups()
            lenses[lens_name] = hunts_for
    return lenses


def parse_expected_field(text: str, field: str) -> str:
    m = re.search(rf"^{re.escape(field)}:\s*(.+)$", text, re.MULTILINE)
    return m.group(1).strip() if m else ""


def load_fixture(fixture_dir: Path) -> dict:
    input_path = fixture_dir / "input.md"
    expected_path = fixture_dir / "expected.md"
    missing = [p.name for p in (input_path, expected_path) if not p.exists()]
    if missing:
        return {"name": fixture_dir.name, "error": f"missing files: {missing}"}

    expected_text = expected_path.read_text(encoding="utf-8")
    category = parse_expected_field(expected_text, "seeded_defect_category")
    keywords_raw = parse_expected_field(expected_text, "defect_keywords")
    keywords = [k.strip().lower() for k in keywords_raw.split(",") if k.strip()]
    lens = parse_expected_field(expected_text, "lens_that_should_catch")
    verdict = parse_expected_field(expected_text, "expected_verdict")

    return {
        "name": fixture_dir.name,
        "category": category,
        "keywords": keywords,
        "lens": lens,
        "expected_verdict": verdict,
        "error": None,
    }


def check_fixture(fixture: dict, lenses: dict) -> dict:
    if fixture.get("error"):
        return {**fixture, "status": "FAIL", "reason": fixture["error"]}

    lens_name = fixture["lens"]
    hunts_for = lenses.get(lens_name)

    if hunts_for is None:
        return {
            **fixture,
            "status": "FAIL",
            "reason": (
                f"lens '{lens_name}' not found in current mod-check/SKILL.md "
                f"lens table (found lenses: {sorted(lenses.keys())})"
            ),
        }

    hunts_for_lower = hunts_for.lower()
    matched_keywords = [k for k in fixture["keywords"] if k in hunts_for_lower]

    if matched_keywords:
        return {
            **fixture,
            "status": "PASS",
            "reason": (
                f"lens '{lens_name}' hunts-for text still contains keyword(s) "
                f"{matched_keywords} -> plausibly still covers "
                f"'{fixture['category']}'"
            ),
        }
    return {
        **fixture,
        "status": "FAIL",
        "reason": (
            f"lens '{lens_name}' hunts-for text ({hunts_for!r}) contains none "
            f"of the declared keywords {fixture['keywords']} -> "
            f"'{fixture['category']}' no longer plausibly covered"
        ),
    }


def main() -> int:
    if not MOD_CHECK_SKILL.exists():
        print(f"ERROR: {MOD_CHECK_SKILL} not found")
        return 2

    skill_text = MOD_CHECK_SKILL.read_text(encoding="utf-8")
    lenses = parse_mod_check_lenses(skill_text)

    if not FIXTURES_DIR.exists():
        print(f"ERROR: {FIXTURES_DIR} not found")
        return 2

    fixture_dirs = sorted(p for p in FIXTURES_DIR.iterdir() if p.is_dir())
    if not fixture_dirs:
        print(f"ERROR: no fixture directories found under {FIXTURES_DIR}")
        return 2

    print(f"wavves eval fixture runner")
    print(f"mod-check skill file: {MOD_CHECK_SKILL}")
    print(f"lenses parsed from current file: {sorted(lenses.keys())}")
    print(f"fixtures found: {len(fixture_dirs)}")
    print("-" * 72)

    results = []
    for fixture_dir in fixture_dirs:
        fixture = load_fixture(fixture_dir)
        result = check_fixture(fixture, lenses)
        results.append(result)
        print(f"[{result['status']}] {result['name']}")
        print(f"    seeded_defect_category: {result.get('category')}")
        print(f"    lens_that_should_catch:  {result.get('lens')}")
        print(f"    reason: {result['reason']}")
        print()

    passed = sum(1 for r in results if r["status"] == "PASS")
    failed = sum(1 for r in results if r["status"] == "FAIL")
    print("-" * 72)
    print(f"TOTAL: {len(results)}  PASS: {passed}  FAIL: {failed}")
    print()
    print(
        "LIMITATION: this is a structured checklist verifier over "
        "mod-check/SKILL.md's lens wording, not a replay of real agent "
        "judgment against the fixture inputs. See evals/README.md."
    )

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

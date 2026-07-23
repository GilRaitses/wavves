#!/usr/bin/env python3
"""Mechanical wave-orchestrator fan-out fixture checker.

Stdlib only. No network. No LLM.

Reads evals/fixtures/wave-orch-fanout-*/trace.json + expected.md.
Emits mechanical PROC-ORCH-* when fields match; MOD-* only if expected
marks them review-only and fixture labels them so.

Usage:
  python3 evals/check_wave_orchestrator_fanout.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"
PREFIX = "wave-orch-fanout-"

MECHANICAL = frozenset({
    "PROC-ORCH-EARLY-EXIT",
    "PROC-ORCH-LAUNCH-AND-EXIT",
    "PROC-ORCH-SOLO-BUILD",
    "PROC-ORCH-ROLE-COLLAPSE",
    "PROC-ORCH-DEP-OVERCLAIM",
    "PROC-ORCH-NO-RESUME-CONTRACT",
    "PROC-ORCH-FOREGROUND-HOLD",
})
REVIEW_ONLY = frozenset({
    "PROC-MOD-FOREGROUND-HOLD",
    "PROC-MOD-PROGRESS-THEATER",
    "PROC-ORCH-FOREGROUND-HOLD",  # allowed review-only when unlabeled
})


def parse_expected(text: str) -> dict:
    verdict_m = re.search(r"^expected_verdict:\s*(PASS|FAIL)\s*$", text, re.M)
    ids_m = re.search(r"^fail_ids:\s*(\[.*\])\s*$", text, re.M)
    review_m = re.search(r"^review_only_ids:\s*(\[.*\])\s*$", text, re.M)
    if not verdict_m:
        raise ValueError("missing expected_verdict")
    fail_ids = json.loads(ids_m.group(1)) if ids_m else []
    review_ids = json.loads(review_m.group(1)) if review_m else []
    return {
        "expected_verdict": verdict_m.group(1),
        "fail_ids": fail_ids,
        "review_only_ids": review_ids,
    }


def detect(trace: dict) -> tuple[list[str], list[str]]:
    """Return (mechanical_fail_ids, review_only_ids)."""
    mech: list[str] = []
    review: list[str] = []

    charges = list(trace.get("charges_launched") or [])
    workers = list(trace.get("worker_ids") or [])
    charge_map = dict(trace.get("charge_id_to_worker_id") or {})
    rollup = bool(trace.get("rollup_path_present"))
    gate = bool(trace.get("gate_path_present"))
    hard_fail = bool(trace.get("hard_fail_artifact_present"))
    op_gate = bool(trace.get("operator_gate_escalate_present"))
    orch_returned = bool(trace.get("orch_returned_before_rollup"))
    checkpoint = bool(trace.get("checkpoint_path_present"))
    yield_awaiting = bool(trace.get("yield_awaiting_children"))
    serialize_reason = (trace.get("serialize_reason") or "").strip()
    colliding_file = (trace.get("colliding_file_path") or "").strip()
    poll = bool(trace.get("orch_poll_or_blocking_await"))
    foreground_labeled_review = bool(trace.get("foreground_hold_review_only"))
    mod_fg = bool(trace.get("mod_foreground_hold"))
    mod_theater = bool(trace.get("mod_progress_theater"))
    same_worker_multi = bool(trace.get("same_worker_for_independent_charges"))

    legal_return = rollup or gate or hard_fail or op_gate

    if orch_returned and not legal_return:
        if len(charges) >= 1 and not rollup:
            mech.append("PROC-ORCH-LAUNCH-AND-EXIT")
        mech.append("PROC-ORCH-EARLY-EXIT")

    if yield_awaiting and not checkpoint and not legal_return:
        mech.append("PROC-ORCH-NO-RESUME-CONTRACT")

    if orch_returned and not legal_return and not checkpoint:
        if "PROC-ORCH-NO-RESUME-CONTRACT" not in mech:
            mech.append("PROC-ORCH-NO-RESUME-CONTRACT")

    # solo build: one worker executed >=2 independent charges, or orch authored charges
    if same_worker_multi or (
        len(charges) >= 2
        and len(set(workers)) < 2
        and not colliding_file
        and not serialize_reason
    ):
        mech.append("PROC-ORCH-SOLO-BUILD")

    if len(charges) >= 2 and (not charge_map or len(charge_map) < len(charges)):
        if "PROC-ORCH-ROLE-COLLAPSE" not in mech:
            mech.append("PROC-ORCH-ROLE-COLLAPSE")

    if serialize_reason and not colliding_file:
        mech.append("PROC-ORCH-DEP-OVERCLAIM")

    if poll:
        mech.append("PROC-ORCH-FOREGROUND-HOLD")
    elif foreground_labeled_review:
        review.append("PROC-ORCH-FOREGROUND-HOLD")

    if mod_fg:
        review.append("PROC-MOD-FOREGROUND-HOLD")
    if mod_theater:
        review.append("PROC-MOD-PROGRESS-THEATER")

    # dedupe preserve order
    def uniq(xs: list[str]) -> list[str]:
        seen = set()
        out = []
        for x in xs:
            if x not in seen:
                seen.add(x)
                out.append(x)
        return out

    return uniq(mech), uniq(review)


def main() -> int:
    fixtures = sorted(
        p for p in FIXTURES_DIR.iterdir()
        if p.is_dir() and p.name.startswith(PREFIX)
    )
    if not fixtures:
        print("FAIL: no fixtures", file=sys.stderr)
        return 1
    failed = 0
    for fix in fixtures:
        trace_path = fix / "trace.json"
        exp_path = fix / "expected.md"
        if not trace_path.is_file() or not exp_path.is_file():
            print(f"FAIL {fix.name}: missing trace.json or expected.md")
            failed += 1
            continue
        trace = json.loads(trace_path.read_text(encoding="utf-8"))
        exp = parse_expected(exp_path.read_text(encoding="utf-8"))
        mech, review = detect(trace)
        # For PASS fixtures, no mechanical fails allowed
        if exp["expected_verdict"] == "PASS":
            if mech:
                print(f"FAIL {fix.name}: expected PASS got mech={mech}")
                failed += 1
            else:
                print(f"PASS {fix.name}")
            continue
        # FAIL: compare mechanical set (order-insensitive) to expected fail_ids
        # that are mechanical; review_only_ids compared separately
        exp_mech = [i for i in exp["fail_ids"] if i in MECHANICAL or i.startswith("PROC-ORCH-")]
        exp_mech = [i for i in exp["fail_ids"] if i not in REVIEW_ONLY or i == "PROC-ORCH-FOREGROUND-HOLD" and "PROC-ORCH-FOREGROUND-HOLD" in mech]
        # Simpler: expected fail_ids must equal mech (as sets) for mechanical cases
        # expected.md fail_ids lists mechanical; review_only_ids lists review
        if set(mech) != set(exp["fail_ids"]):
            print(
                f"FAIL {fix.name}: mech={sorted(mech)} expected_fail_ids={sorted(exp['fail_ids'])}"
            )
            failed += 1
            continue
        if set(review) != set(exp.get("review_only_ids") or []):
            print(
                f"FAIL {fix.name}: review={sorted(review)} expected_review={sorted(exp.get('review_only_ids') or [])}"
            )
            failed += 1
            continue
        print(f"PASS {fix.name}")
    if failed:
        print(f"\n{failed} fixture(s) failed", file=sys.stderr)
        return 1
    print(f"\nAll {len(fixtures)} fixtures PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

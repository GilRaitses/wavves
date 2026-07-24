#!/usr/bin/env python3
"""Mechanical proceed-all-standing fixture checker (FR PS-10).

Stdlib only. No network. No LLM.

Reads evals/fixtures/proceed-all-standing-*/trace.json + expected.md.
Emits mechanical PROC-PROCEED-* fail ids from keyed trace fields.

Usage:
  python3 evals/check_proceed_all_standing.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"
PREFIX = "proceed-all-standing-"

MECHANICAL = frozenset({
    "PROC-PROCEED-NO-STANDING-QUEUE",
    "PROC-PROCEED-FORCE-BLOCKED-LOCK",
    "PROC-PROCEED-SILENT-SKIP-LOCK",
    "PROC-PROCEED-SHRUG-WIDEN",
    "PROC-PROCEED-COMMIT-WITHOUT-AUTH",
    "PROC-PROCEED-STALE-QUEUE",
    "PROC-PROCEED-CHAT-INVENTORY",
    "PROC-PROCEED-DISPATCH-STORM",
})

ALL_STANDING_PHRASES = (
    "all still standing",
    "queue all standing and move",
    "proceed all standing",
    "/wavves proceed all standing",
)


def parse_expected(text: str) -> dict:
    verdict_m = re.search(r"^expected_verdict:\s*(PASS|FAIL)\s*$", text, re.M)
    ids_m = re.search(r"^fail_ids:\s*(\[.*\])\s*$", text, re.M)
    if not verdict_m:
        raise ValueError("missing expected_verdict")
    fail_ids = json.loads(ids_m.group(1)) if ids_m else []
    return {
        "expected_verdict": verdict_m.group(1),
        "fail_ids": fail_ids,
    }


def _uniq(xs: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for x in xs:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def _trigger_has_all_standing_phrase(trace: dict) -> bool:
    if "trigger_has_all_standing_phrase" in trace:
        return bool(trace.get("trigger_has_all_standing_phrase"))
    trigger = (trace.get("trigger") or "").lower()
    return any(p in trigger for p in ALL_STANDING_PHRASES)


def _is_bare_shrug(trace: dict) -> bool:
    if "bare_shrug" in trace:
        return bool(trace.get("bare_shrug"))
    trigger = (trace.get("trigger") or "").strip()
    # bare shrug / bare /shrug; leftover chat after emoji still counts as bare
    # for widen purposes when no closed all-standing phrase is present
    if trigger.startswith("/shrug"):
        rest = trigger[len("/shrug"):].strip()
        return not any(p in rest.lower() for p in ALL_STANDING_PHRASES)
    if "¯\\_(ツ)_/¯" in trigger or "shrug" in trigger.lower():
        return not _trigger_has_all_standing_phrase(trace)
    return False


def detect(trace: dict) -> list[str]:
    """Return mechanical fail ids."""
    mech: list[str] = []

    mode = (trace.get("mode") or "").strip()
    queue_present = bool(trace.get("standing_queue_path_present"))
    remasured = bool(trace.get("standing_queue_remasured"))
    items = list(trace.get("items") or [])
    inventory_from_chat = bool(trace.get("inventory_from_chat"))
    dispatch_storm = bool(trace.get("dispatch_storm"))
    widened = bool(trace.get("widened_from_bare_shrug"))

    all_standing = mode == "proceed-all-standing"

    if all_standing and not queue_present:
        mech.append("PROC-PROCEED-NO-STANDING-QUEUE")

    if all_standing and queue_present and not remasured:
        mech.append("PROC-PROCEED-STALE-QUEUE")

    if (_is_bare_shrug(trace) and not _trigger_has_all_standing_phrase(trace)
            and (all_standing or widened)):
        mech.append("PROC-PROCEED-SHRUG-WIDEN")
    elif widened:
        mech.append("PROC-PROCEED-SHRUG-WIDEN")

    if inventory_from_chat:
        mech.append("PROC-PROCEED-CHAT-INVENTORY")

    if dispatch_storm:
        mech.append("PROC-PROCEED-DISPATCH-STORM")

    for item in items:
        if not isinstance(item, dict):
            continue
        cls = (item.get("class") or "").strip()
        hard_lock = bool(item.get("hard_lock"))
        gate_path = (item.get("gate_path") or "").strip()
        forced = bool(item.get("forced_past_lock"))
        files_ok = bool(item.get("files_list_present"))

        if cls == "commit" and not files_ok:
            mech.append("PROC-PROCEED-COMMIT-WITHOUT-AUTH")

        if hard_lock:
            if forced or cls in ("dispatch", "commit"):
                mech.append("PROC-PROCEED-FORCE-BLOCKED-LOCK")
            if cls in ("skip_done", "out_of_scope") and not gate_path:
                mech.append("PROC-PROCEED-SILENT-SKIP-LOCK")

    return _uniq(mech)


def main() -> int:
    if not FIXTURES_DIR.is_dir():
        print("FAIL: fixtures dir missing", file=sys.stderr)
        return 1
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
        try:
            trace = json.loads(trace_path.read_text(encoding="utf-8"))
            exp = parse_expected(exp_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, ValueError) as exc:
            print(f"FAIL {fix.name}: parse error: {exc}")
            failed += 1
            continue

        mech = detect(trace)

        if exp["expected_verdict"] == "PASS":
            if mech:
                print(f"FAIL {fix.name}: expected PASS got mech={mech}")
                failed += 1
            else:
                print(f"PASS {fix.name}")
            continue

        if set(mech) != set(exp["fail_ids"]):
            print(
                f"FAIL {fix.name}: mech={sorted(mech)} "
                f"expected_fail_ids={sorted(exp['fail_ids'])}"
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

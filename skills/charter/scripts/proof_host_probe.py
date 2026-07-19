#!/usr/bin/env python3
"""DOM/host hard-gate probe for proof-before-accept (EXECUTION_WIRING Rule 2b).

Measures primary product host geometry and emits JSON with at least
``host_client_height`` and ``blank_canvas``. Fail the gate when
``host_client_height <= 0`` or ``blank_canvas`` is true while chrome may PASS.

Stdlib only for self-check / dry-run. Live mode optionally uses Playwright
when installed; otherwise exits with a clear error (use --self-check).

  # Contract / CI smoke (no browser, no network):
  python3 skills/charter/scripts/proof_host_probe.py --self-check \
    --out gate-captures/PHF-probe-self-check.json

  # Live (requires Playwright):
  python3 skills/charter/scripts/proof_host_probe.py \
    --url "$PROOF_URL" \
    --selector "$PROOF_HOST_SELECTOR" \
    --out gate-captures/<CODE>-ACCEPT-proof-host.json

Pass metric: host_client_height > 0 AND blank_canvas == false.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from typing import Any


REQUIRED_FIELDS = ("host_client_height", "blank_canvas")

# Built-in fixtures for --self-check / --dry-run (no browser).
SELF_CHECK_CASES: list[dict[str, Any]] = [
    {
        "id": "healthy-host",
        "host_client_height": 711,
        "blank_canvas": False,
        "expect_pass": True,
    },
    {
        "id": "zero-height",
        "host_client_height": 0,
        "blank_canvas": False,
        "expect_pass": False,
    },
    {
        "id": "blank-canvas-class",
        "host_client_height": 400,
        "blank_canvas": True,
        "expect_pass": False,
    },
]


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def gate_pass(host_client_height: int, blank_canvas: bool) -> bool:
    return host_client_height > 0 and blank_canvas is False


def _base_record(
    *,
    mode: str,
    url: str | None,
    selector: str | None,
    host_client_height: int,
    blank_canvas: bool,
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    record: dict[str, Any] = {
        "mode": mode,
        "url": url,
        "selector": selector,
        "host_client_height": int(host_client_height),
        "blank_canvas": bool(blank_canvas),
        "pass": gate_pass(int(host_client_height), bool(blank_canvas)),
        "finished": _now_iso(),
    }
    if extra:
        record.update(extra)
    return record


def run_self_check() -> dict[str, Any]:
    """Exercise gate logic and emit required JSON fields without a browser."""
    case_results: list[dict[str, Any]] = []
    logic_ok = True
    for case in SELF_CHECK_CASES:
        actual = gate_pass(case["host_client_height"], case["blank_canvas"])
        ok = actual == case["expect_pass"]
        if not ok:
            logic_ok = False
        case_results.append(
            {
                "id": case["id"],
                "host_client_height": case["host_client_height"],
                "blank_canvas": case["blank_canvas"],
                "expect_pass": case["expect_pass"],
                "actual_pass": actual,
                "ok": ok,
            }
        )

    # Primary capture record uses the healthy fixture so ACCEPT can show
    # required fields on a runnable command when no live host exists.
    healthy = SELF_CHECK_CASES[0]
    summary = _base_record(
        mode="self-check",
        url=None,
        selector=None,
        host_client_height=healthy["host_client_height"],
        blank_canvas=healthy["blank_canvas"],
        extra={
            "self_check_logic_ok": logic_ok,
            "self_check_cases": case_results,
            "note": (
                "Dry-run / self-check: no live browser. "
                "Required fields present; gate logic exercised. "
                "Live ACCEPT still needs --url/--selector with a browser backend."
            ),
        },
    )
    summary["pass"] = logic_ok
    return summary


def _measure_live(url: str, selector: str) -> dict[str, Any]:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        raise RuntimeError(
            "Live mode requires Playwright (`pip install playwright` and "
            "`playwright install`). Use --self-check when no browser is available."
        ) from exc

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page()
            page.goto(url, wait_until="domcontentloaded", timeout=60_000)
            handle = page.query_selector(selector)
            if handle is None:
                return _base_record(
                    mode="live",
                    url=url,
                    selector=selector,
                    host_client_height=0,
                    blank_canvas=True,
                    extra={"error": "selector_not_found", "backend": "playwright"},
                )
            height = handle.evaluate("el => el.clientHeight")
            blank = handle.evaluate(
                """el => {
                  const cls = (el.className && el.className.toString)
                    ? el.className.toString() : '';
                  const canvas = el.tagName === 'CANVAS'
                    ? el
                    : el.querySelector('canvas');
                  const blankClass = /blank-canvas|blank_canvas|is-blank/i.test(cls)
                    || (el.getAttribute('data-blank-canvas') === 'true');
                  if (blankClass) return true;
                  if (!canvas) return false;
                  return (canvas.clientHeight || 0) <= 0 || (canvas.clientWidth || 0) <= 0;
                }"""
            )
            return _base_record(
                mode="live",
                url=url,
                selector=selector,
                host_client_height=int(height or 0),
                blank_canvas=bool(blank),
                extra={"backend": "playwright"},
            )
        finally:
            browser.close()


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Measure proof host clientHeight / blank_canvas for Rule 2b."
    )
    ap.add_argument("--url", default=None, help="page URL (live mode)")
    ap.add_argument(
        "--selector",
        default=None,
        help="CSS selector for primary product host (live mode)",
    )
    ap.add_argument("--out", default=None, help="write JSON capture path")
    ap.add_argument(
        "--self-check",
        action="store_true",
        help="stdlib dry-run: emit required JSON fields; exercise gate fixtures",
    )
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="alias for --self-check (no live browser)",
    )
    args = ap.parse_args()

    self_check = bool(args.self_check or args.dry_run)

    if self_check:
        summary = run_self_check()
    else:
        if not args.url or not args.selector:
            print(
                "error: live mode requires --url and --selector "
                "(or pass --self-check / --dry-run)",
                file=sys.stderr,
            )
            return 2
        try:
            summary = _measure_live(args.url, args.selector)
        except RuntimeError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2

    for field in REQUIRED_FIELDS:
        if field not in summary:
            print(f"error: missing required field {field!r}", file=sys.stderr)
            return 2

    print("=== SUMMARY ===", flush=True)
    print(json.dumps(summary, indent=2), flush=True)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            json.dump(summary, fh, indent=2)
            fh.write("\n")

    if self_check:
        return 0 if summary.get("self_check_logic_ok") else 1
    return 0 if summary.get("pass") else 1


if __name__ == "__main__":
    raise SystemExit(main())

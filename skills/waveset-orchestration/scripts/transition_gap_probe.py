#!/usr/bin/env python3
"""Generic user-visible-gap probe for a measured transition (deploy, recycle, cutover).

Polls a LIVENESS endpoint and a REAL USER endpoint at a fixed cadence and records
the max contiguous window where the real endpoint returns non-2xx while liveness
stays 2xx. That window is the user-visible gap. Optionally fires a sparse mutating
call (e.g. a create) to exercise a write path, throttled to respect quotas.

Dependency-free (stdlib only). Run it inside ONE long-blocking command alongside
the transition trigger so the process is not reaped (see EXECUTION_WIRING.md):

  python3 transition_gap_probe.py --base https://svc --real-path /api/x/status \
    --seconds 360 --out gate_captures/gap.json &
  PROBE=$!; sleep 6; <trigger transition>; <poll to completion>; wait $PROBE

Pass = max_gap_while_live_up_ms == 0.
"""

from __future__ import annotations

import argparse
import json
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone


def _request(url: str, method: str = "GET", body: bytes | None = None, timeout: float = 6.0) -> int:
    try:
        headers = {"Content-Type": "application/json"} if body is not None else {}
        req = urllib.request.Request(url, data=body, method=method, headers=headers)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status
    except urllib.error.HTTPError as exc:
        return exc.code
    except Exception:
        return 0


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True, help="base URL, no trailing slash")
    ap.add_argument("--live-path", default="/health", help="liveness endpoint (expected 2xx throughout)")
    ap.add_argument("--real-path", required=True, help="real user endpoint whose 2xx defines serveability")
    ap.add_argument("--mutate-path", default=None, help="optional POST path fired sparsely (e.g. a create)")
    ap.add_argument("--mutate-body", default="{}", help="JSON body for --mutate-path")
    ap.add_argument("--mutate-every-s", type=int, default=30, help="sparse mutate cadence (quota-aware)")
    ap.add_argument("--seconds", type=int, default=360)
    ap.add_argument("--cadence-ms", type=int, default=500)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    base = args.base.rstrip("/")
    live_url = f"{base}{args.live_path}"
    real_url = f"{base}{args.real_path}"
    mutate_url = f"{base}{args.mutate_path}" if args.mutate_path else None
    mutate_body = args.mutate_body.encode("utf-8")
    cadence = args.cadence_ms / 1000.0
    deadline = time.monotonic() + args.seconds

    samples = live_up = real_2xx = 0
    gap_events: list[dict] = []
    gap_start: float | None = None
    gap_first: int | None = None
    max_gap_ms = 0.0
    mutate_attempts = mutate_2xx = 0
    mutate_non2xx: list[dict] = []
    last_mutate = 0.0

    print(f"[{_now_iso()}] gap probe start base={base} live={args.live_path} real={args.real_path} seconds={args.seconds}", flush=True)

    while time.monotonic() < deadline:
        tick = time.monotonic()
        ls = _request(live_url)
        rs = _request(real_url)
        samples += 1
        l_ok = 200 <= ls < 300
        r_ok = 200 <= rs < 300
        live_up += 1 if l_ok else 0
        real_2xx += 1 if r_ok else 0

        if l_ok and not r_ok:
            if gap_start is None:
                gap_start, gap_first = tick, rs
                print(f"[{_now_iso()}] GAP open: real={rs} live={ls}", flush=True)
        elif gap_start is not None:
            dur = (tick - gap_start) * 1000.0
            max_gap_ms = max(max_gap_ms, dur)
            gap_events.append({"duration_ms": round(dur, 1), "first_status": gap_first})
            print(f"[{_now_iso()}] GAP close: duration_ms={round(dur, 1)}", flush=True)
            gap_start = gap_first = None

        if mutate_url and tick - last_mutate >= args.mutate_every_s:
            last_mutate = tick
            code = _request(mutate_url, method="POST", body=mutate_body)
            mutate_attempts += 1
            if 200 <= code < 300:
                mutate_2xx += 1
            else:
                mutate_non2xx.append({"t": _now_iso(), "status": code})
            print(f"[{_now_iso()}] mutate -> {code} (live={ls} real={rs})", flush=True)

        elapsed = time.monotonic() - tick
        if elapsed < cadence:
            time.sleep(cadence - elapsed)

    if gap_start is not None:
        dur = (time.monotonic() - gap_start) * 1000.0
        max_gap_ms = max(max_gap_ms, dur)
        gap_events.append({"duration_ms": round(dur, 1), "first_status": gap_first})

    summary = {
        "base": base,
        "samples": samples,
        "live_up_pct": round(100.0 * live_up / max(samples, 1), 2),
        "real_2xx_pct": round(100.0 * real_2xx / max(samples, 1), 2),
        "max_gap_while_live_up_ms": round(max_gap_ms, 1),
        "gap_event_count": len(gap_events),
        "gap_events": gap_events,
        "mutate_attempts": mutate_attempts,
        "mutate_2xx": mutate_2xx,
        "mutate_non2xx": mutate_non2xx,
        "finished": _now_iso(),
    }
    print("=== SUMMARY ===", flush=True)
    print(json.dumps(summary, indent=2), flush=True)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            json.dump(summary, fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

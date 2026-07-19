# PHF-W1c — adversarial

lane: PHF
wave: W1c
date: 2026-07-18 (America/New_York)
repo_state_verified_against: `538437cad76764fd989cd028f64927b1ae839292`
model: cursor-grok-4.5-high-fast
status: discovery complete

## Attack surface

Close named PBB gap (contract-only Rule 2b) without reopening PBB or
importing product-look lane fixtures into wavves evals.

## Adversarial cases

| id | attack | expected defense |
|---|---|---|
| A1 | Claim Rule 2b live while only docs cite a missing script | Ship real `skills/charter/scripts/proof_host_probe.py`; Rule 2b cites that path |
| A2 | Self-check always emits PASS / ignores zero height | Self-check must include a FAIL fixture (`host_client_height <= 0` or `blank_canvas: true`) and assert gate logic |
| A3 | Live mode silently invents heights without a browser | Live without Playwright (or equivalent) must error; no fabricated live metrics |
| A4 | Treat DOM green as ACCEPT-complete under `visual_accept: yes` | Playbook + Rule 2b state capture-then-grade required; DOM green ≠ done |
| A5 | Port product-look lane vocab into wavves mechanical checker | PHF-EVAL defer; closed wavves vocab stays PROC-* method ids only |
| A6 | Rewrite PBB-ACCEPT as FAIL because probe was missing | Forbidden; PBB PASS stands; gap was disclosed non-blocking |
| A7 | Hand-authored proof-host JSON at ACCEPT | Rule 2b already: hand-authored summaries FAIL; verdict must cite command + measured numbers |
| A8 | Absolute chrome freeze with no proof-serving allowlist | Already FAIL in playbook; do not regress |

## Originating-mod alignment check

From `ORIGINATING-MOD-FEEDBACK.md` (`538437c`):

- Method match yes; keep C+D+B+E — honor
- Product-look = product-look lane — honor (no port)
- Ship probe before claiming Rule 2b live shared tool — this lane
- Capture-then-grade for `visual_accept: yes` — harden docs
- Do not block PBB as shipped — honor

## ACCEPT readiness risks (for PHF-ACCEPT later)

1. Probe runnable (`--self-check` at minimum) with required JSON fields
2. Capture under `gate-captures/` from the named command
3. Playbook + Rule 2b language audited for A4
4. PBB mechanical regression still 4/4; paragraph-tunnel 6/6 (ACCEPT wave)
5. No product-look fixture corpus added

## Commit file list (this finding)

- `wavves/lanes/20260718_proof-host-followon/findings/PHF-adversarial.md`

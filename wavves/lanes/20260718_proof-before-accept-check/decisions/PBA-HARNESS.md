# PBA — HARNESS

- **Date:** 2026-07-18
- **Lane:** wavves/lanes/20260718_proof-before-accept-check/
- **repo_state_verified_against:** af0c0788cb2dbb865cbce6721fcdcbf6642b11d4
- **Question:** What is the runnable Proof gate?
- **Options considered:**
  - A: Screenshot-vs-reference required (hard)
  - B: DOM / primary product host metrics hard; screenshot optional operator step
  - C: Assertion-only in ACCEPT prose
- **Pick:** B
- **Rationale:** Operator `¯\_(ツ)_/¯` / proceed as recommended. C struck (unrunnable / process-PASS).
- **Implications for BUILD:** Name `python3 evals/check_proof_before_accept.py` for mechanical PROC-* fixtures; document DOM/host harness command + JSON schema in EXECUTION_WIRING (fail if primary product host height ≤ 0 or blank-canvas class while chrome PASS). Screenshot-vs-reference is optional when `visual_accept: yes` and environment supports it; not the sole hard gate.

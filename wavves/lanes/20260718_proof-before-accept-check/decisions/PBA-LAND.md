# PBA — LAND

- **Date:** 2026-07-18
- **Lane:** wavves/lanes/20260718_proof-before-accept-check/
- **repo_state_verified_against:** af0c0788cb2dbb865cbce6721fcdcbf6642b11d4
- **Question:** Where does proof-before-accept land, and does it block BUILD unlock?
- **Options considered:**
  - E1: C+D+B+E (charter+wiring, playbook+evals, mod-check proof-bar, mod-decide AUTH sync unlock)
  - E2: C+D+B only (ACCEPT-time bar; drop unlock claim)
  - A: also ship `/proof-gate` slash skill
- **Pick:** E1 — **C + D + B + E**; defer A
- **Rationale:** Operator `¯\_(ツ)_/¯` / proceed as recommended.
- **Implications for BUILD:** Ship charter ACCEPT template fields + EXECUTION_WIRING harness rule; playbook + mechanical evals; mod-check proof-bar lens; mod-decide AUTH sync requires `proof_job` on `proof_required: yes` before BUILD unlock. No `/proof-gate` skill in v0.

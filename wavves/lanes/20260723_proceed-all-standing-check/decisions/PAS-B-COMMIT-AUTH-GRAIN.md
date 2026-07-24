# PAS — COMMIT-AUTH-GRAIN

- **Date:** 2026-07-23
- **Lane:** `wavves/lanes/20260723_proceed-all-standing-check/`
- **repo_state_verified_against:** `7aecdfb50d8d6fc53fa00a08b021e4cd9926aa67`
- **Question:** When proceed-all-standing classifies multiple `commit` rows with
  explicit `files:` lists, does one all-standing authorize utterance cover every
  land, or does each land need its own this-turn authorize / `operator_gate`?
- **Options considered:**
  - A: One all-standing authorize covers every `commit` row that already has `files:`
  - B: Each `commit` row needs its own “ship it” / per-land `operator_gate` when multi-repo or >1 land
  - C: Hybrid: single-repo lands covered by one authorize; cross-repo lands always per-land gate
- **Pick:** C
- **Rationale:** Operator `¯\_(ツ)_/¯` + “all three” on O0 recommended next;
  queue lean was C (AUTH-10 file-list discipline; avoid blanket multi-repo push).
- **Implications for BUILD:** Proceed-all-standing commit class must treat
  same-repo multi-land as one authorize when `files:` present; any land whose
  paths span another repo id / foreign tree → `operator_gate` until per-land
  authorize this turn.

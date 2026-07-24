# PAS — SCOPE-FALLBACK

- **Date:** 2026-07-23
- **Lane:** `wavves/lanes/20260723_proceed-all-standing-check/`
- **repo_state_verified_against:** `7aecdfb50d8d6fc53fa00a08b021e4cd9926aa67`
- **Question:** When the trigger names no lanes and INDEX has zero active
  lanes, empty queue + stop vs refuse mode with message?
- **Options considered:**
  - A: Empty queue + stop (write empty standing file; no moves)
  - B: Refuse mode with operator-facing message (no standing file)
- **Pick:** A
- **Rationale:** FR default lean; operator shrug proceeded residual decide
  after COMMIT-AUTH-GRAIN C in the same “all three” pass.
- **Implications for BUILD:** Empty inventory path must write
  `wavves/standing/<date>_<label>.md` with zero rows and stop; not an error
  refuse that skips the persist step.

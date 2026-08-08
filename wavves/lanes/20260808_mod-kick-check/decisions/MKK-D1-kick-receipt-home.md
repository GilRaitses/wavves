# MKK-D1 — kick-receipt-home

- **Date:** 2026-08-08
- **Lane:** `wavves/lanes/20260808_mod-kick-check/`
- **repo_state_verified_against:** `d327b66` (registry tip; FR revise `6e5076a`)
- **Question:** Where does the durable kick receipt live?
- **Options considered:**
  - A: `wavves/handoffs/KICK_*.md` + mirror under active lane `findings/`
  - B: Lane-only `moderator_handoffs/` (new seam)
  - C: New dir `wavves/kicks/`
- **Pick:** A
- **Rationale:** House `wavves/handoffs/` already holds durable cross-thread artifacts; avoid inventing `moderator_handoffs/` or `wavves/kicks/`. Lane mirror keeps the check/BUILD lane self-contained.
- **Implications for BUILD:** KICK-06 writes `wavves/handoffs/KICK_<YYYYMMDD>_<HHMM>.md` and, when a lane is active, mirrors to `lanes/<lane>/findings/KICK_RECEIPT.md`. Do not create `wavves/kicks/` or `moderator_handoffs/`.

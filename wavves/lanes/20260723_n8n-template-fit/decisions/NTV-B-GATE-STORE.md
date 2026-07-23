# NTV — GATE-STORE

- **Date:** 2026-07-23
- **Lane:** `wavves/lanes/20260723_n8n-template-fit/`
- **repo_state_verified_against:** `de75b4c4118c78dcc0164fdaa916bbc53f99225f`
- **Question:** Where does pass/block evidence land?
- **Options considered:**
  - A: Google Sheets
  - B: n8n Data Table
  - C: binary / Drive log file
- **Pick:** B
- **Rationale:** Operator bare shrug (AUTH-10 proceed as recommended). Lean was B.
- **Implications for BUILD:** Gate capture writes pass/block rows to an n8n Data Table. Stickies document table columns. No Google Sheets or Drive required for v0 evidence path. Strip any personal table IDs before submit.

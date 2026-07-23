# NTV — V0-SCOPE

- **Date:** 2026-07-23
- **Lane:** `wavves/lanes/20260723_n8n-template-fit/`
- **repo_state_verified_against:** `de75b4c4118c78dcc0164fdaa916bbc53f99225f`
- **Question:** Which ADAPTs ship in the first Free template?
- **Options considered:**
  - A: Core only (alignment packet + fan-out + proof gate + Data Table evidence)
  - B: Core + monotonic term_id
  - C: Core + paragraph-tunnel subflow
- **Pick:** A
- **Rationale:** Operator bare shrug (AUTH-10 proceed as recommended). Lean was A.
- **Implications for BUILD:** v0 Free pack is core governed wave accept only. Do not ship term_id rotation or paragraph-tunnel in the first template. Those may be separate later Free templates toward paid eligibility.

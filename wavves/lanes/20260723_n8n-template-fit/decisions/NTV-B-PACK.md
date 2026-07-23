# NTV — PACK

- **Date:** 2026-07-23
- **Lane:** `wavves/lanes/20260723_n8n-template-fit/`
- **repo_state_verified_against:** `de75b4c4118c78dcc0164fdaa916bbc53f99225f`
- **Question:** Single workflow vs parent + charge sub-workflows?
- **Options considered:**
  - A: One workflow (simpler import)
  - B: Parent orch + Execute Workflow charges (clearer triad)
- **Pick:** B
- **Rationale:** Operator: "duh B" (with shrug). Matches lean B.
- **Implications for BUILD:** Ship a parent orchestrator workflow plus charge sub-workflows invoked via Execute Workflow. Stickies must document import order (charges then parent, or pack zip if used). Do not flatten into a single graph. Do not copy competitor 8578 layout.

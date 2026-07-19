# PBA — LENS

- **Date:** 2026-07-18
- **Lane:** wavves/lanes/20260718_proof-before-accept-check/
- **repo_state_verified_against:** af0c0788cb2dbb865cbce6721fcdcbf6642b11d4
- **Question:** How does mod-check gain the proof-bar hunt?
- **Options considered:**
  - A: Fifth default lens on every mod-check
  - B: Default lens when waveset/artifact is `proof_required: yes` or product/visitor FR; otherwise optional fifth
  - C: Playbook-only hunt; no SKILL.md lens change
- **Pick:** B
- **Rationale:** Operator `¯\_(ツ)_/¯` / proceed as recommended (avoids forcing proof-bar on pure research checks).
- **Implications for BUILD:** Patch `skills/mod-check/SKILL.md` to document `proof-bar` as conditional default; playbook still teaches the hunt. Not a silent fifth lens on every check.

# PTG — LAND

- **Date:** 2026-07-15
- **Lane:** wavves/lanes/20260715_paragraph-tunnel-gate-check/
- **repo_state_verified_against:** f2fb8ce144b68d820b0992f5075a2cbbf44673d2
- **Question:** Where does paragraph tunnel land in wavves?
- **Options considered:**
  - A: New skill `/paragraph-tunnel`
  - B: Extension to mod-check adversarial lens + charter tunneled-field step
  - C: Playbook fragment under skills/wavves/playbooks/ + eval fixture
  - A+C: Slash skill plus playbook/eval in one BUILD
- **Pick:** C + dispatch STEPS hook (not a new slash skill yet)
- **Rationale:** Operator `¯\_(ツ)_/¯` / proceed as recommended. B struck (phase leak). Defer standalone skill A until C proves out.
- **Implications for BUILD:** Ship playbook + evals/fixtures; document STEPS order in dispatch templates; no `/paragraph-tunnel` skill in v0; do not touch mod-check runtime.

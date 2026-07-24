# NTVB-INT return

```yaml
charge: NTVB-INT
git_actions_by_runner: none
commit_file_list:
  - pack/03-parent-orchestrator.json
  - pack/README.md
  - findings/NTVB-INT-return.md
status: done
proof_path_nodes:
  - Merge Charge Returns
  - Proof Merge Complete
  - IF Outcome Pass
  - Append Proof Gate Row
  - Emit Pass Rollup
parent_workflow_name: "Parent Orchestrator — Proof-Gated Wave Accept"
```

## Summary

Parent orchestrator implements proof_job: Manual Trigger → Set Fields →
parallel Execute Workflow (Charge A ‖ Charge B) → Merge (append) → named
Code proof check → IF on `outcome === pass` → Data Table insert → pass
rollup. Block path writes `Append Block Gate Row` then `Emit Block Rollup`
(no success accept).

Charge workflow names wired as placeholders for importer select:
`Charge Research A — Wave Packet`, `Charge Research B — Wave Packet`.
Stickies from `STICKIES.md` embedded (yellow overview + six step notes).
README INT finalize section filled; import order unchanged (charges →
table → parent → credentials → wire).

## Checks

- `python3 -m json.tool pack/03-parent-orchestrator.json` → EXIT 0
- No secrets / `sk-` / absolute home paths in owned files
- Did not rewrite charge JSON 01/02; did not run ACCEPT; did not submit

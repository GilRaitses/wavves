# Pickup playbook

Route: hydrate as moderator, then charter or reconcile as needed.

```
- [ ] 1. Read <repo>/wavves/INDEX.md.
- [ ] 2. Read the newest rotation file named by INDEX.md.
- [ ] 3. Ack assigned identity (O0.R<N>) and the rotation filename before
        acting.
- [ ] 4. Verify claimed positions and commit hashes are reachable from HEAD.
        Record gaps; never silently execute stale pickups.
- [ ] 5. Read README.md for each active lane in INDEX.md.
- [ ] 6. **Mandatory reconcile branch** for any in-flight wave orch (do this
        before “report and wait”). For each active dispatch / orch notify:
        remasure leave-act + disk artifacts, then take exactly one branch:
        - `yield_awaiting_children` → same-turn remasure
          `findings/<wave>-orch-checkpoint.md` and named child outs. If
          children COMPLETE and next integrate/ACCEPT is due → Task-resume
          orch (or re-dispatch from checkpoint). Never step-log-and-park.
          If rollup+gate (or hard FAIL / legal operator_gate) already on
          disk → treat as `return_to_O0` (next bullet).
        - `return_to_O0` (or yield remasure found rollup+gate) → reconcile
          gate captures vs summary; land orch `commit_file_list` per repo
          protocol; update registry/INDEX. Do not wait for a second notify.
        - hard FAIL / illegal early-exit → record fail; resume from
          checkpoint only as **fail remediation** (re-dispatch or repair);
          do not invent PASS.
        Nested charge-worker Task completions may not surface as O0 notices;
        disk remasure is authority (Cursor harness gap).
- [ ] 7. Report: current identity, active lanes, running dispatches, blocked
        decisions and recommended next action.
- [ ] 8. If the operator named new bounded work, route to charter-lane. If they
        asked to rotate, route to rotate.
```

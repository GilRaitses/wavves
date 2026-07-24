```yaml
charge: NTVB-W1d
git_actions_by_runner: none
commit_file_list:
  - pack/GATE-TABLE-SCHEMA.md
  - pack/README.md
  - findings/NTVB-W1d-return.md
status: done
columns:
  - outcome:string          # pass|block
  - proof_check_id:string
  - proof_check_name:string
  - recorded_at:date
  - wave_run_id:string      # generic; not term_id
  - reason:string
  - merge_fingerprint:string  # optional
  - topic:string              # optional
```

## Summary for orch

Wrote Data Table schema for proof_job evidence (`NTV-GATE-STORE = B`) and
import-order draft README with credential placeholders, Free-template notes,
and `## INT finalize (TBD)` slots for parent name + Execute Workflow IDs.

No charge JSON, DESCRIPTION/STICKIES, or parent orchestrator written (out of
ownership). No git. No n8n.io submit.

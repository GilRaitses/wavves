# WOF — CHECKPOINT-FILENAME

- **Date:** 2026-07-23
- **Lane:** wavves/lanes/20260723_wave-orchestrator-fanout-check/
- **repo_state_verified_against:** 7aecdfb50d8d6fc53fa00a08b021e4cd9926aa67
- **Question:** Checkpoint path for yield_awaiting_children?
- **Pick:** **A — `findings/<wave>-orch-checkpoint.md`**
- **Rationale:** FR resume contract; matches RLI-W2 missing-checkpoint failure
  (orch returned after W2a launch with no checkpoint on disk). Lane-specific
  alternate paths require an explicit waveset override; default is this name.
- **Implications:** OF-04/OF-05 paste and eval fixtures use this filename.
  Missing file + yield → `PROC-ORCH-NO-RESUME-CONTRACT`.

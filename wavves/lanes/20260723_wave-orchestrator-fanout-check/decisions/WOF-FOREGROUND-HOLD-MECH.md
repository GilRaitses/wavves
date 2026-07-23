# WOF — FOREGROUND-HOLD-MECH

- **Date:** 2026-07-23
- **Lane:** wavves/lanes/20260723_wave-orchestrator-fanout-check/
- **repo_state_verified_against:** 7aecdfb50d8d6fc53fa00a08b021e4cd9926aa67
- **Question:** Keep `PROC-ORCH-FOREGROUND-HOLD` mechanical when synthetic
  traces encode poll/blocking await, or always review-only?
- **Pick:** **A — mechanical when trace field present; else review-only**
- **Rationale:** Operator sleep drive-through after RLI-W2 orch LAUNCH-AND-EXIT
  recurrence; matches FR lean. Eval can assert when
  `orch_poll_or_blocking_await: true` is present; unlabeled traces stay
  review-only fixtures.
- **Implications:** OF-07 fixtures must include at least one mechanical
  FOREGROUND-HOLD case with the trace field and one labeled review-only case.

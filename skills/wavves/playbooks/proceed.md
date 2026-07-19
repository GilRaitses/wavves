# Proceed playbook

Route: **wavves** (`/wavves proceed`)

Execute the ordered **recommended_actions** block from a mod-check verdict,
mod-decide completion, or lane reconcile return (AUTH-10).

```
- [ ] 1. Locate the source verdict or reconcile file. Read `recommended_actions`
        in order. If absent, infer from verdict prose and stop if ambiguous.
- [ ] 2. For each `commit` action: stage listed files only. Commit and push
        only when the operator explicitly asked or said "proceed as recommended"
        / "ship it" in this turn.
- [ ] 3. For each `dispatch` action: read the named `dispatch_file`, verify
        AUTH-05 gate (waveset synced after mod-decide). Dispatch to background.
        Do not poll.
- [ ] 4. For each `operator_gate` action: surface the gate to the operator and
        pause until they respond. Do not skip approval gates.
- [ ] 5. Report what ran, what is blocked on operator input, and landing
        commit hash when commits occurred.
```

Trigger language: `proceed as recommended`, `/wavves proceed`, `ship it`, or
**¯\_(ツ)_/¯** (standing operator alias = proceed as recommended in sequence)
after a verdict with `recommended_actions`.

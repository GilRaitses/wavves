# Check playbook

Route: **mod-check** (`/mod-check`)

```
- [ ] 1. Verify <repo>/wavves/ exists. If missing, run bootstrap first.
- [ ] 2. Read wavves/INDEX.md and the current rotation file if one exists.
- [ ] 3. Read the mod-check skill (skills/mod-check/SKILL.md) in full.
- [ ] 4. Confirm the operator's artifact path exists. Record branch,
        repo_state_verified_against and landing_commit_hash when given.
- [ ] 5. Run the mod-check workflow: lane home, registry entry, one
        adversarial parallel wave, reconcile to a GO | REVISE | BLOCK verdict.
- [ ] 6. Dispatch to background. Do not poll. Reconcile on return notice.
- [ ] 7. Report verdict, top blockers, lane home and recommended next step.
        Do not write the implementation plan unless the operator asks.
```

Lane types this playbook covers:

| type | operator says |
|:-----|:--------------|
| spec check | check the spec, review the design before the plan |
| plan check | sanity-check the implementation plan before build |
| adversarial wave | adversarial review, parallel reviewers, /mod-check |

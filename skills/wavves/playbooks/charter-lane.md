# Charter lane playbook

Route: **charter** (`/charter`)

```
- [ ] 1. Verify <repo>/wavves/ exists. If missing, run bootstrap first.
- [ ] 2. Read wavves/INDEX.md and the current rotation file if one exists.
- [ ] 3. Read the charter skill (skills/charter/SKILL.md) in full.
- [ ] 4. Carry the operator's task verbatim into the charter intent section.
- [ ] 5. Run the charter workflow: lane home, registry entry, dispatch.
- [ ] 6. Dispatch to background. Do not poll. Reconcile on return notice.
- [ ] 7. Report lane code, home path, dispatch status and any operator gates.
```

Lane types this playbook covers (same charter skill, different operator framing):

| type | operator says |
|:-----|:--------------|
| read-only audit | audit, review, inventory, no commits |
| bug fix | reproduce, root cause, fix, verify with gates |
| flaky CI | flakes, stability, rerun gate |
| refactor | migrate callers, behavior identical |
| feature | new behavior, feature flag, acceptance gate |
| security pass | audit auth, CSRF, session, read-only unless approved |
| overnight lane | stepping away, land with gates, no deploy without approval |

# Decide playbook

Route: **mod-decide** (`/mod-decide`)

```
- [ ] 1. Verify <repo>/wavves/ exists. If missing, run bootstrap first.
- [ ] 2. Read wavves/INDEX.md and the current rotation file if one exists.
- [ ] 3. Read the mod-decide skill (skills/mod-decide/SKILL.md) in full.
- [ ] 4. Locate the check lane / findings. Build the ordered decision queue
        from named open calls. Do not invent forks.
- [ ] 5. Walk decisions one at a time. On each pick, write
        decisions/<CODE>-<slug>.md and append to the Locked decisions draft.
- [ ] 6. When the operator says locks are complete, emit the Locked
        decisions paste and the recommended /charter invocation(s).
- [ ] 7. Do not dispatch BUILD unless the operator asks in the same turn.
```

Lane types this playbook covers:

| type | operator says |
|:-----|:--------------|
| post-check locks | navigate the decisions, lock before charter |
| decision packet | open calls, product picks, /mod-decide |
| pre-BUILD gate | ready to charter after picks |

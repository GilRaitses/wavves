# Kick playbook

Route: **mod-kick** (`/mod-kick`)

Cross-environment exit. Not rotate. The **pickup** playbook stays
rotate-hydrate only.

```
- [ ] 1. Read skills/mod-kick/SKILL.md in full.
- [ ] 2. Resolve kick-target default from active lane repos: primary (or sole
        listed). No foreign hardcode.
- [ ] 3. Ask: Kick target repo? A=default single, B=named single, C=multi
        (MULTI_REPO_AUTH), D=leash (LEASH_AUTH + ≤8 files / ≤256 KiB).
        Bare shrug accepts A only.
- [ ] 4. Build lane-owned publish allowlist for this stream only.
- [ ] 5. Publish allowlist to kick-target; verify origin sync. Or LOCAL_ONLY
        with LOCAL_ONLY_AUTH (same-machine paste only).
- [ ] 6. Write wavves/handoffs/KICK_<YYYYMMDD>_<HHMM>.md (+ lane mirror).
- [ ] 7. Emit paste one-liner / short block (≤12 lines / ≤2000 chars).
```

Cue table:

| Cue | Route |
|---|---|
| hand to another environment / other machine / readback elsewhere | **kick** |
| fresh thread / token velocity / O0.R(N+1) | **rotate** + pickup hydrate |

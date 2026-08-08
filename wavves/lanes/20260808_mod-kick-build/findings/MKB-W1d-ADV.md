# MKB-W1d ADV — jargon / rotate-collapse hunt

- **lane:** `20260808_mod-kick-build`
- **when:** 2026-08-08T17:45:00-04:00 (America/New_York)
- **scope:** new kick skill, playbook, public surfaces, CHANGELOG, plugin meta

## Findings

| Check | Result |
|---|---|
| Product UX uses **leash** / `LEASH_AUTH` | PASS — skill + playbook + fixtures |
| No promotional `vendor` / `VENDOR_*` in index/README/usage/router | PASS |
| Ban mentions of vendor remain only in lock / skill non-negotiables | PASS (meta; not product path name) |
| Kick ≠ rotate documented | PASS — cue tables in skill, playbook, usage, index |
| Pickup stays rotate-hydrate | PASS — playbook + router row wording |
| Shrug cannot widen to MULTI/LEASH | PASS — D5 + fixture `mod-kick-shrug-widen` |

## Verdict

ADV clear for ACCEPT. No remediation required.

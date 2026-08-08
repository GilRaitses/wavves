# Locked decisions draft — mod-kick (MKK)

- **lane:** `20260808_mod-kick-check`
- **artifact:** `feature-requests/20260808_mod-kick.md`
- **repo_state_verified_against:** `d327b66`
- **status:** **locks complete** — awaiting commit + re-check/BUILD charter
- **mod_decide_complete_at:** 2026-08-08T17:34:00-04:00

## Program intent

Ship `/mod-kick` as cross-environment exit (git-published kick-target + paste),
distinct from `/mod-rotate` and from the `pickup` hydrate playbook. Prefer
single-repo; multi-repo / **leash** only with explicit auth. Publish allowlist +
proof harness required before BUILD ACCEPT.

## Meta (PBA)

```yaml
proof_required: yes
proof_job: >-
  Live /mod-kick on a throwaway allowlisted lane surface publishes to the
  kick-target remote, origin sync verifies, paste contract fields present,
  and evals/check_mod_kick.py PASS on fixture corpus including
  PROC-KICK-NO-PUBLISH, MULTI-SILENT, LEASH-SILENT, LOCAL-ONLY-ABUSE,
  UNRELATED-PUSH, SHRUG-WIDEN, LEASH-UNBOUNDED.
proof_reference: evals/check_mod_kick.py + gate-captures from live smoke
chrome_freeze:
  freeze: [skills/mod-kick/SKILL.md, skills/wavves/playbooks/kick.md, router/usage/AGENTS rows]
  proof_serving_allowlist: [evals/check_mod_kick.py, evals/fixtures/mod-kick/, wavves/handoffs/KICK_*.md]
visual_accept: no
visual_accept_rationale: CLI/git publish proof; no visitor DOM surface
```

## Locks

- **D1 receipt home:** A — `wavves/handoffs/KICK_*.md` + lane `findings/KICK_RECEIPT.md` mirror
- **D2 commit protocol:** A — `/mod-kick` = publish auth for allowlist only
- **D3a copy-in term:** **leash** / `LEASH_AUTH` (ban vendor / `VENDOR_*`)
- **D3 leash thin threshold:** A — ≤8 files AND ≤256 KiB AND no secret globs; else multi-repo
- **D4 LOCAL_ONLY:** A — same-machine fence + `LOCAL_ONLY_AUTH`
- **D5 shrug:** A — shrug accepts single-repo default only (never multi/leash)

## Queue

All D1–D5 **LOCKED**.

# MKK — mod-kick-check

## Intent

Adversarial sanity-check of `feature-requests/20260808_mod-kick.md`.
No build. No implementation plan. **mod-decide locks complete 2026-08-08.**

## Artifact

- path: `feature-requests/20260808_mod-kick.md`
- landing_commit_hash: `6e5076aca6fa3aa957a4970d936bde69c3cc4583` (post-MKK revise; decide records after)
- branch: `main`
- repo_state_verified_against: `d327b66` (pre-decide tip; remeasure at BUILD charter)
- index: `feature-requests/README.md` row FR-20260808-mod-kick
- locks: `decisions/LOCKED-DECISIONS.md`

## Meta (proof)

```yaml
proof_required: yes
proof_job: >-
  Live /mod-kick publish + origin sync + paste contract; evals/check_mod_kick.py
  PASS on fixtures (NO-PUBLISH, MULTI-SILENT, LEASH-SILENT, LOCAL-ONLY-ABUSE,
  UNRELATED-PUSH, SHRUG-WIDEN, LEASH-UNBOUNDED).
proof_reference: evals/check_mod_kick.py + live smoke gate-captures
chrome_freeze:
  freeze: [skills/mod-kick/SKILL.md, skills/wavves/playbooks/kick.md, router/usage/AGENTS]
  proof_serving_allowlist: [evals/check_mod_kick.py, evals/fixtures/mod-kick/, wavves/handoffs/KICK_*.md]
visual_accept: no
visual_accept_rationale: CLI/git publish proof; no visitor DOM
```

## Locked decisions (do NOT reopen)

- D1 receipt: `wavves/handoffs/KICK_*.md` + lane `findings/KICK_RECEIPT.md` mirror
- D2: `/mod-kick` = publish auth for allowlist only
- D3a: term **leash** / `LEASH_AUTH` (ban vendor / `VENDOR_*`)
- D3: leash ≤8 files AND ≤256 KiB AND no secret globs; else multi-repo
- D4: LOCAL_ONLY = same-machine + `LOCAL_ONLY_AUTH`
- D5: shrug accepts single-repo default only (never multi/leash)

## Locked (check discipline)

- read-only reviewers for W1
- distinguish kick vs mod-rotate vs pickup playbook
- no invent of BUILD plan inside check

## Waves

### Wave 1 — adversarial check (parallel, high-reasoning) — DONE REVISE

- MKK-W1a…W1e + MKK-verdict.md

### Gate

- MKK-VERDICT: REVISE applied + decide complete → BUILD unlock via `/charter` after commit/re-check as AUTH-10 directs

## Out of scope (this check lane)

- writing the implementation plan inside check
- commits / push / deploy unless operator AUTH-10
- chartering BUILD inside mod-decide

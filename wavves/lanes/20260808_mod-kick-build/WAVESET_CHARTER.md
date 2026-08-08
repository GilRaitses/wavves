# MKB — mod-kick-build

## Intent

BUILD and ship `/mod-kick` (cross-environment kick-out) on production repo
`wavves` (`/Users/gilraitses/wavves_build` → `github.com/GilRaitses/wavves`),
including public surfaces: `examples/usage.md`, `README.md`, `index.html`
(wavves.aimez.ai), `CHANGELOG`, plugin version, AGENTS, router.

## Artifact / authority

- FR: `feature-requests/20260808_mod-kick.md`
- Check: `wavves/lanes/20260808_mod-kick-check/` (REVISE → locks)
- Locks: copy from `../20260808_mod-kick-check/decisions/LOCKED-DECISIONS.md`
- `repo_state_verified_against`: `3d91e48a6e525b20ce9c079f5c14d219ec0cc6b0`

## Meta (proof)

```yaml
proof_required: yes
proof_job: >-
  evals/check_mod_kick.py PASS on fixtures; live /mod-kick smoke on throwaway
  allowlisted surface with origin sync + paste contract (or LOCAL_ONLY labeled
  same-machine only if remote blocked — must not claim cross-env).
proof_reference: evals/check_mod_kick.py + gate-captures/MKB-ACCEPT*
chrome_freeze:
  freeze: [skills/mod-kick/SKILL.md, skills/wavves/playbooks/kick.md]
  proof_serving_allowlist: [evals/, wavves/handoffs/KICK_*.md, gate-captures/]
visual_accept: no
visual_accept_rationale: CLI/git publish proof
```

## Locked decisions (do NOT reopen)

- D1 receipt: `wavves/handoffs/KICK_*.md` + lane `findings/KICK_RECEIPT.md`
- D2: `/mod-kick` = publish auth for allowlist only
- D3a: **leash** / `LEASH_AUTH` (ban vendor / `VENDOR_*`)
- D3: ≤8 files AND ≤256 KiB AND no secret globs; else multi-repo
- D4: LOCAL_ONLY = same-machine + `LOCAL_ONLY_AUTH`
- D5: shrug accepts single-repo default only (never multi/leash)
- Kick ≠ rotate; `pickup` playbook remains rotate-hydrate only
- Production repo is this wavves repo; bump plugin to **0.5.0**

## Waves

### W1 — skill + playbook + evals (parallel charges)

- MKB-W1a → `skills/mod-kick/SKILL.md` (+ optional thin scripts)
- MKB-W1b → `skills/wavves/playbooks/kick.md`
- MKB-W1c → `evals/check_mod_kick.py` + `evals/fixtures/mod-kick-*/`
- MKB-W1d ADV → findings hunt for vendor jargon / rotate collapse

### W2 — public surfaces (serialized INT editor preferred)

- Router `skills/wavves/SKILL.md` leave-act + playbook row
- `examples/usage.md`, `README.md`, `wavves/AGENTS.md`
- `index.html` (wavves.aimez.ai usage grid + invocable tables)
- `CHANGELOG.md` + `.cursor-plugin/plugin.json` → 0.5.0
- FR status → shipped (when ACCEPT PASS)

### W3 — ACCEPT

- Run `python3 evals/check_mod_kick.py`
- Live smoke or honest LOCAL_ONLY same-machine smoke with labeled paste
- Gate capture under `gate-captures/`

## Out of scope

- Substack publish / social post (O0 announcement pack under `announcements/`)
- Marketplace listing submission
- Force-updating every consumer clone of local plugin (document re-copy path)

## Remediations

Cap 2. Escalate to O0 if proof_job cannot run.

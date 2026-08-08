# MKB-ACCEPT gate capture

```yaml
lane: 20260808_mod-kick-build
wave: ACCEPT
when: 2026-08-08T17:43:00-04:00
verdict: PASS
proof_required: yes
proof_job: |
  evals/check_mod_kick.py PASS on fixtures; LOCAL_ONLY same-machine smoke
  with receipt + paste contract (remote publish deferred to O0 — orch must
  not git commit/push). Must not claim cross-env.
proof_reference: evals/check_mod_kick.py + gate-captures/MKB-ACCEPT.md + wavves/handoffs/KICK_20260808_1743.md
visual_accept: no
repo_state_verified_against: d8467343d2e6a0ca6ef4b799d41958886225481f
plugin_version: "0.5.0"
```

## Evidence

### Eval harness

```text
$ python3 evals/check_mod_kick.py
PASS mod-kick-desktop-authority
PASS mod-kick-leash-silent
PASS mod-kick-leash-unbounded
PASS mod-kick-local-only-abuse
PASS mod-kick-multi-silent
PASS mod-kick-no-publish
PASS mod-kick-pass-single
PASS mod-kick-rotate-collapse
PASS mod-kick-secret-leak
PASS mod-kick-shrug-widen
PASS mod-kick-unrelated-push
PASS mod-kick-wrong-default

All 12 fixtures PASS
```

### Live smoke

- Path: **LOCAL_ONLY** + `LOCAL_ONLY_AUTH` (orch cannot push; honest label)
- Receipt: `wavves/handoffs/KICK_20260808_1743.md`
- Lane mirror: `findings/KICK_RECEIPT.md`
- Smoke surface: `findings/smoke-local-only.txt`
- Paste: same-machine only; no remote-pull instruction

### ADV

`findings/MKB-W1d-ADV.md` — clear (leash term; no product vendor jargon; kick≠rotate)

## Gaps

1. Cross-env `origin` sync proof deferred until O0 lands `commit_file_list` and a follow-up `/mod-kick` (non-LOCAL_ONLY) can run.
2. Local plugin install `~/.cursor/plugins/local/wavves/` may need re-copy after O0 lands — orch did not copy (document only).

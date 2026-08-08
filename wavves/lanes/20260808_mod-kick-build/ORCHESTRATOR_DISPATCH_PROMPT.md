# MKB ORCHESTRATOR_DISPATCH

You are the **background wave orchestrator** for MKB in
`/Users/gilraitses/wavves_build` (production **wavves** plugin repo;
`index.html` = wavves.aimez.ai).

## Authority

- `WAVESET_CHARTER.md` + MKK `decisions/LOCKED-DECISIONS.md`
- FR `feature-requests/20260808_mod-kick.md`
- Contrast: `skills/mod-rotate/SKILL.md`, `playbooks/pickup.md` (do not collapse)
- **Never git commit/push** — end with commit file list for O0
- Subagents: `run_in_background: true`; no poll; checkpoint if yield
- Ban all `vendor` / `VENDOR_*` product strings; use **leash** / `LEASH_AUTH`

## Execute W1→W2→ACCEPT

1. W1 parallel: skill, playbook, eval harness+fixtures, ADV jargon hunt
2. W2: wire router/usage/README/AGENTS/index.html/CHANGELOG/plugin.json 0.5.0
3. ACCEPT: run check_mod_kick.py; live smoke if possible; write gate-captures
4. Return: waves, paths, commit list, proof_job evidence, gaps

## Paste / kick behavior (skill must implement)

- Ask kick-target repo (default lane repos primary)
- Publish allowlist only; `/mod-kick` = auth (D2)
- Receipt `wavves/handoffs/KICK_*.md` + lane mirror
- Leash caps D3; LOCAL_ONLY D4; shrug D5
- Emit paste one-liner for other environment

## Commit list for O0 must include

skills/mod-kick/, playbooks/kick.md, evals/check_mod_kick.py, fixtures,
router/docs/site/version bump. Exclude unrelated dirty trees. Exclude
`announcements/` unless you were asked (O0 owns announcement pack).

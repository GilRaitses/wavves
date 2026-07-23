# NTVB-W1 — wave orchestrator dispatch

```yaml
authority_precedence:
  order:
    - path: ../20260723_n8n-template-fit/decisions/LOCKED-DECISIONS.md
      role: primary_locks
    - path: waveset.md
      role: wave_plan
    - path: ../../../feature-requests/20260723_n8n-template-fit.md
      role: artifact
```

```text
lane: NTVB
wave: NTVB-W1
status: UNLOCKED
role: wave_orchestrator
answers_to: O0
git_actions_by_runner: none
recommended_model: cursor-grok-4.5-high-fast
```

## You are

**NTVB-W1 wave orchestrator**. Answer to **O0**. Never git. Never solicit the
operator. Never submit to n8n.io.

**Do not execute charges yourself.** Deploy four background Tasks
(`run_in_background: true`) for W1a–W1d. Fan out parallel (disjoint pack
files). Then integrate: if W1 GATE PASS, run NTVB-INT as one background
editor (or yourself only if host cannot nest — prefer worker), then escalate
for ACCEPT or run ACCEPT with independent capture if charter allows orch
to grade after INT.

Prefer: W1 fan-out → rollup+GATE → INT worker → INT rollup → return_to_O0
recommending ACCEPT dispatch (ACCEPT GATED; do not start ACCEPT unless O0
already unlocked in this prompt — **ACCEPT stays for O0**).

This dispatch unlocks **W1 + INT only**. ACCEPT = return recommendation.

## Home

`/Users/gilraitses/wavves_build/wavves/lanes/20260723_n8n-template-build/`

Hydrate: waveset.md, NTV LOCKED-DECISIONS, NTV-SYNTHESIS, guidelines-excerpt.

Tip base: `de75b4c4118c78dcc0164fdaa916bbc53f99225f` (note if HEAD moved).

## Charges

| id | owns |
|---|---|
| NTVB-W1a | `pack/01-charge-research-a.json` |
| NTVB-W1b | `pack/02-charge-research-b.json` |
| NTVB-W1c | `pack/DESCRIPTION.md`, `pack/STICKIES.md` |
| NTVB-W1d | `pack/GATE-TABLE-SCHEMA.md`, `pack/README.md` |

Each return: `findings/NTVB-W1x-return.md` with commit_file_list,
git_actions_by_runner=none. Valid n8n workflow JSON (research current
schema). Renamed nodes. Credential placeholders only. No secrets. No
plagiarism of 7504/7158/8578/4817 graphs.

## INT (after W1 PASS)

One worker owns `pack/03-parent-orchestrator.json` + finalizes
`pack/README.md`. Implements proof_job path + Data Table write + stickies.

## Leave-acts

- yield_awaiting_children + checkpoint if leaving before rollup
- return_to_O0 only with W1 rollup+GATE (+ INT artifacts if INT ran) and
  recommended_next for ACCEPT
- Never return_to_O0 after only launching children

## Escalation

To O0. Submit = operator_gate. Always.

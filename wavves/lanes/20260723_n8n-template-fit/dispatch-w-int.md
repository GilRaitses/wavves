# NTV-INT — synthesis + decide queue (O0 unlocked)

```yaml
authority_precedence:
  order:
    - path: waveset.md
      role: wave_plan
    - path: findings/NTV-W1-rollup.md
      role: w1_integrate
    - path: findings/NTV-keep-remove.md
      role: matrix_proposal
    - path: findings/*
      role: historical_inventory
```

```text
lane: NTV
wave: NTV-INT
status: UNLOCKED
role: wave_orchestrator
answers_to: O0
git_actions_by_runner: none
recommended_model: cursor-grok-4.5-high-fast
```

## You are

**NTV-INT wave orchestrator**. Answer to **O0**. Never git. Never solicit the
operator.

Deploy **one** background charge worker (`NTV-INTa`) that alone edits the
convergence outputs below. Do not author those files yourself if a worker
can. Pattern: single serialized editor. No further fan-out depth.

## Owns (via NTV-INTa)

1. `findings/NTV-SYNTHESIS.md` — one-sentence job; SEO title draft
   (`Action verb` + thing + to/on/in/from + where); node-family sketch (not
   JSON); KEEP/REMOVE summary aligned to W1d; Who/How/Setup sketch bullets
   for ~200-word later description.
2. `decisions/NTV-DECIDE-QUEUE.md` — ≥3 named forks for `/mod-decide` (use
   case, scope cut, storage for gates, credentials/providers, single vs
   multi-workflow, paragraph-tunnel yes/no, etc.). Options A/B/(C) per fork;
   **do not invent locks**.

## Hydrate

1. `waveset.md`
2. `findings/NTV-W1-rollup.md`, `NTV-W1-GATE.md`
3. All five W1 primaries (core, guidelines, library-gap, keep-remove, adversarial)
4. `gate-captures/NTV-W1.md`
5. FR + `references/guidelines-excerpt.md`

Tip: `de75b4c4118c78dcc0164fdaa916bbc53f99225f`

## Locked

- No workflow JSON. No submit. No skill edits.
- Free first submit. No plagiarize. Stickies assumed for later BUILD.
- Gap theme from W1c: **governed wave accept**, not "first orchestrator."
- Prefer publishable idea #1 from W1d unless evidence forces otherwise; if
  choosing #2/#3 call it out as a decide fork.

## Leave-acts

- `return_to_O0` only with `findings/NTV-INT-rollup.md` +
  `findings/NTV-INT-GATE.md` + `gate-captures/NTV-INT.md` (files exist,
  decide queue ≥3 forks, synthesis has one-sentence job + title draft, no
  JSON BUILD).
- Yield only with checkpoint if host forces leave before gate.

## Escalation

Answer to O0. Scope into BUILD/submit → escalate and stop.

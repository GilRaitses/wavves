---
name: mod-decide
description: >-
  Navigate open product and design decisions after a check return, lock them
  into decisions/*.md, and produce a Locked decisions paste for a BUILD
  charter. Use for /mod-decide, "lock decisions", "navigate the open calls",
  "decision packet" or "ready to charter after picks". No build. No re-check.
disable-model-invocation: true
---

# mod-decide

Operator-facing decision gate between **`/mod-check`** and **`/charter`**.

After an adversarial check returns `GO` / `REVISE` / `BLOCK` with named open
calls, O0 does **not** charter BUILD while forks are still open. This skill
walks those calls one at a time, records each pick under `decisions/`, and
emits a **Locked decisions** block ready to paste into `waveset.md`.

Sibling skills:

- `wavves` (`/wavves`) routes here via the **decide** playbook.
- `mod-check` (`/mod-check`) is the prior step (adversarial review).
- `charter` (`/charter`) is the next step (BUILD), only after locks exist.
- `wavves-init` (`/wavves-init`) is home setup only.

## When to use

The check lane (or equivalent findings) left **open product or design
calls** that a build agent must not pick silently. Typical cues: "navigate
the decisions", "lock before charter", "decision packet", `/mod-decide`.

## Non-negotiables

1. **One decision at a time.** Present options in one line each, optional
   recommendation, then wait for the operator pick before the next call.
2. **Invoke once per queue.** `/mod-decide` starts the decision queue. While
   Mod is already asking for the next pick in the same thread, the operator
   answers with `Pick: …` only — they do not re-slash before every decision.
   Re-invoke only in a fresh chat or if the thread never ran decide.
3. **No BUILD charter inside this skill.** Do not run `/charter` until the
   operator says the locks are complete.
4. **No re-litigation of settled technical findings.** If the check already
   verified a fact (e.g. point-in-polygon renders nothing), treat it as
   grounding to lock, not as an open debate, unless the operator reopens it.
5. **Write durable records.** Each pick lands in
   `wavves/lanes/<lane>/decisions/<CODE>-<slug>.md`. Maintain a running
   Locked decisions draft the operator can paste into BUILD.
6. **Separate lanes stay separate.** If two features have independent open
   calls (e.g. DSO and GEX), finish or explicitly park one before mixing
   locks into a single BUILD charter. Prefer one BUILD charter per feature.
7. **No commit / push / deploy** unless the operator explicitly asks.

## Workflow

```
- [ ] 1. Verify <repo>/wavves/ exists. If missing, run /wavves-init bootstrap first.
- [ ] 2. Locate the check lane (or operator-named findings). Read the verdict
        and the named open calls. Record repo_state_verified_against.
- [ ] 3. Build an ordered decision queue. Product calls before mechanical
        confirmations. Do not invent new forks the check did not surface
        unless the operator adds them.
- [ ] 4. For each call: state options (one line each), optional lean, wait
        for pick. On pick, write decisions/<CODE>-<slug>.md and append to
        the Locked decisions draft.
- [ ] 5. When the operator says locks are complete, emit the final Locked
        decisions paste and the recommended /charter invocation(s). Do not
        dispatch BUILD unless they ask in the same turn.
- [ ] 6. Update the check lane README or registry note: status awaiting
        BUILD charter, locks path listed.
```

## Decision record shape

```markdown
# <CODE> — <slug>

- **Date:** <YYYY-MM-DD>
- **Lane:** <check lane home>
- **repo_state_verified_against:** <hash>
- **Question:** <one sentence>
- **Options considered:**
  - A: ...
  - B: ...
- **Pick:** <A|B|...>
- **Rationale:** <operator wording, verbatim when given>
- **Implications for BUILD:** <what the charter must lock / gate>
```

## Locked decisions paste (output)

Emit a fenced block the operator can drop into `/charter`:

```text
Locked decisions (do NOT reopen):
- <pick 1, one line>
- <pick 2, one line>
...

Grounding (already verified — do not rediscover):
- <settled technical finding 1>
- <settled technical finding 2>
```

## Recommended next charter shape

After locks are complete, point the operator at `/charter` (or `/wavves`
charter) with:

- `repo_state_verified_against` from the check landing
- the Locked decisions paste
- the Grounding paste
- one feature per lane when scopes are disjoint
- gated integration + acceptance
- no commits/deploy without an explicit ask

## Related

- Prior step: `/mod-check`
- Next step: `/charter` BUILD
- Lifecycle guide: `examples/usage.md` → "From check to BUILD"

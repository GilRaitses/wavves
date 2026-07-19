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
2. **No BUILD charter inside this skill.** Do not run `/charter` until the
   operator says the locks are complete.
3. **No re-litigation of settled technical findings.** If the check already
   verified a fact (e.g. point-in-polygon renders nothing), treat it as
   grounding to lock, not as an open debate, unless the operator reopens it.
4. **Write durable records.** Each pick lands in
   `wavves/lanes/<lane>/decisions/<CODE>-<slug>.md`. Maintain a running
   Locked decisions draft the operator can paste into BUILD.
5. **Separate lanes stay separate.** If two features have independent open
   calls (e.g. DSO and GEX), finish or explicitly park one before mixing
   locks into a single BUILD charter. Prefer one BUILD charter per feature.
6. **No commit / push / deploy** unless the operator explicitly asks.

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
- [ ] 5b. **Authority sync (AUTH-01).** Patch authority surfaces so locks
        propagate before W2+ dispatch:
        - `waveset.md` — Locked decisions section and gated-waves table
        - active `dispatch-w{N}.md` — inline locks (retire or mark historical
          prior `dispatch.md` when superseded)
        - `wavves/registry.yml` — `status`, `note`, `mod_decide_complete_at`,
          `waveset_synced_at`, `active_dispatch`
        - **Proof fields (PBA-LAND E).** When the feature or check lane will
          charter an execution lane with visitor/product surface, ensure
          Locked decisions and the synced `waveset.md` carry
          `proof_required: yes|no|n/a`. If `proof_required: yes`, AUTH sync
          FAILS (block BUILD unlock / W2 dispatch) until `proof_job` appears
          in the Locked decisions paste and in `waveset.md` Meta, along with
          `proof_reference`, `chrome_freeze` (freeze list + proof-serving
          allowlist), and `visual_accept` (with rationale if `no` or if
          `proof_reference: none`). Dropping `proof_job` from the paste after
          decide is a sync failure, not a soft warning.
        Show a diff preview or ask O0 to confirm if waveset has intentional
        draft edits. **Block W2 dispatch** when `waveset.md` is older than the
        newest `decisions/*-B-*.md` (or lane decision records) until sync passes.
- [ ] 6. Update the check lane README or registry note: status awaiting
        BUILD charter, locks path listed.
- [ ] 7. Emit **recommended_actions** (AUTH-10) — ordered block for O0:
        commit file list, `/charter` or dispatch invocation, operator gates.
        Operator may invoke `/wavves proceed` to execute the list.
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
- `proof_required` and, when `yes`, `proof_job` (+ three companion fields)
  present in Locked decisions and waveset Meta before BUILD dispatch
- one feature per lane when scopes are disjoint
- gated integration + acceptance
- no commits/deploy without an explicit ask

## Related

- Prior step: `/mod-check`
- Next step: `/charter` BUILD
- Lifecycle guide: `examples/usage.md` → "From check to BUILD"

---
name: mod-check
description: >-
  Run an adversarial sanity-check wave of parallel subagents against a written
  spec or plan before implementation. Use for /mod-check, "check the spec",
  "adversarial review of the design", "sanity-check wave" or "review before we
  write the plan". Read-only. No build wave. Reports blockers and gaps.
disable-model-invocation: true
---

# mod-check

Adversarial sanity-check wave for a **written artifact** (spec, design note,
alignment packet or plan) **before** implementation planning or build.

This is a specialized charter: one discovery/adversarial wave of parallel
high-reasoning reviewers, no build, no integration. O0 stays operator-facing.
Findings land under a lane home. The return is a go / revise / block verdict
with named gaps, not a soft "looks fine."

Sibling skills:

- `wavves` (`/wavves`) routes here via the **check** playbook.
- `mod-decide` (`/mod-decide`) is the next step when the return leaves open
  product or design calls to lock before BUILD.
- `charter` (`/charter`) is the full multi-wave lane. Use that when locks are
  done (or none were needed), not when forks are still open.
- `wavves-init` (`/wavves-init`) is home setup only.

## When to use

The operator has a landed spec or plan and wants parallel adversarial review
before writing the implementation plan or starting build. Typical cues:
"check the spec", "sanity-check wave", "adversarial review", "review before
we write the plan", `/mod-check`.

## Non-negotiables

1. **Read-only.** Reviewers write findings only. No code edits, no commits,
   no plan authoring inside this skill.
2. **Ground against repo state.** Use the operator's
   `landing_commit_hash` / `repo_state_verified_against` when given. Open the
   real spec path. Cite real files the spec claims to touch.
3. **Parallel, disjoint lenses.** Each subagent owns one findings file and
   one review lens. No shared authorship of the same finding.
4. **High-reasoning for every member.** Spec review is judgment work.
5. **Honest verdict.** `GO`, `REVISE` or `BLOCK`. Named gaps with evidence.
   A conclusion without a cited path or contradiction is not a finding.
6. **No commit / push / deploy** unless the operator explicitly asks.

## Workflow

```
- [ ] 1. Verify <repo>/wavves/ exists. If missing, run /wavves-init bootstrap first.
- [ ] 2. Confirm the artifact path exists. Record branch +
        repo_state_verified_against (and landing_commit_hash if given).
- [ ] 3. Name the lane: short code (e.g. CHK) + kebab label from the spec
        slug + date. Home: wavves/lanes/<YYYYMMDD>_<label>/
- [ ] 4. Write lane home: README.md, waveset.md, dispatch.md. Scope is
        "adversarial check only — no build, no implementation plan."
- [ ] 5. Register the lane in wavves/registry.yml (status: chartered).
- [ ] 6. Dispatch ONE wave of parallel high-reasoning reviewers (default 4
        lenses below; add proof-bar when proof_required: yes or
        product/visitor FR). Background preferred. Do not poll.
- [ ] 7. On return: reconcile findings **once** after all parallel lenses
        complete (AUTH-06). Do not prompt the operator per lens unless one
        failed. Write findings/<CODE>-verdict.md with scoped verdict (AUTH-04).
- [ ] 8. Report to the operator: verdict, top blockers, path to findings,
        and **recommended_actions** (AUTH-10). Do not start the implementation
        plan unless they ask.
```

## Default parallel lenses (Wave 1 only)

Dispatch these as disjoint subagents unless the operator narrows the set:

| Wave id | Lens | Owns | Hunts for |
|:--------|:-----|:-----|:----------|
| `<CODE>-W1a` | grounding | `findings/<CODE>-grounding.md` | claims that don't match repo files, wrong paths, stale `repo_state_verified_against`, missing cited seams |
| `<CODE>-W1b` | contradictions | `findings/<CODE>-contradictions.md` | internal conflicts, phase-boundary leaks, mutually exclusive requirements |
| `<CODE>-W1c` | completeness | `findings/<CODE>-completeness.md` | missing acceptance criteria, unowned edges, silent assumptions, absent rollback / non-goals |
| `<CODE>-W1d` | adversarial | `findings/<CODE>-adversarial.md` | failure modes, unsafe defaults, "works on happy path only", gates that can't actually run |

### Conditional fifth lens: proof-bar (PBA-LENS)

Dispatch `<CODE>-W1e` **proof-bar** as a default fifth parallel lens when the
artifact or its waveset Meta sets `proof_required: yes`, or when the
artifact is a product/visitor feature request that will charter an execution
lane. Otherwise keep the four-lens default; operators may still name
proof-bar as an optional fifth domain lens.

| Wave id | Lens | Owns | Hunts for |
|:--------|:-----|:-----|:----------|
| `<CODE>-W1e` | proof-bar | `findings/<CODE>-proof-bar.md` | ACCEPT criteria that can PASS without measuring `proof_job`; chrome-only waves with no frozen proof_job; `proof_reference: none` / `visual_accept: no` without rationale on proof_required:yes; debt-close treated as product done; missing named DOM/host or mechanical proof harness |

proof-bar owns its findings file alone. It does not replace grounding,
contradictions, completeness, or adversarial. Playbook
`skills/wavves/playbooks/proof-before-accept.md` teaches the same hunt for
BUILD lanes.

For research-only, mod-check-of-check, plugin-meta, or outbound-copy-only
artifacts with `proof_required: no` or `n/a`, do not force proof-bar unless
the operator asks.

Other domain fifth lenses (security, perf, migration blast radius) remain
operator-named and stay disjoint from proof-bar ownership.

## waveset.md shape (check lane)

```markdown
# <CODE> — <label>

## Intent
Adversarial sanity-check of <artifact path>. No build. No implementation plan.

## Artifact
- path: <path>
- landing_commit_hash: <hash or n/a>
- branch: <branch>
- repo_state_verified_against: <hash>

## Locked
- read-only reviewers
- high-reasoning model tier for every wave member
- verdict must be GO | REVISE | BLOCK with named gaps

## Waves
### Wave 1 — adversarial check (parallel, high-reasoning)
- <CODE>-W1a grounding → findings/<CODE>-grounding.md
- <CODE>-W1b contradictions → findings/<CODE>-contradictions.md
- <CODE>-W1c completeness → findings/<CODE>-completeness.md
- <CODE>-W1d adversarial → findings/<CODE>-adversarial.md

### Gate
- <CODE>-VERDICT: O0 reconciles the four findings into
  findings/<CODE>-verdict.md. Pass metric: every blocking gap is named with
  evidence, or verdict is GO with zero blockers.

## Out of scope
- writing the implementation plan
- code changes
- commits / push / deploy
```

## Verdict rules

| Verdict | When |
|:--------|:-----|
| **GO** | No blocking gaps. Residual nits may be listed as non-blocking. |
| **REVISE** | Spec is salvageable; named edits required before plan. |
| **BLOCK** | Phase boundary wrong, ungrounded critical claim, or contradiction that makes a plan unsafe. |

O0 writes the verdict file. Wave members do not grade each other.

## Scoped verdict schema (AUTH-04)

Verdict files must differentiate lane-wide REVISE from wave-scoped blocks:

```yaml
verdict: GO | REVISE | BLOCK
blocks_w2: false
blocks_w3: false
blocks_w4: false
blocks_w5: false
blockers:
  - id: string
    wave: w2 | w3 | w4 | w5
    evidence_path: string
    summary: string
```

A lane may be **REVISE** overall while `blocks_w4: true` and `blocks_w2: false`.
"Proceed as recommended" must map to an unambiguous next step.

## Mandatory gate before W2+ (AUTH-05)

When `registry.status` matches `mod-decide-complete*` and `waveset.md` is older
than the newest `decisions/*.md`, require mod-check PASS or AUTH-01 authority
sync before W2 dispatch.

## Operator return shape

Keep it short:

1. Verdict (`GO` / `REVISE` / `BLOCK`) plus scoped `blocks_w2`…`blocks_w5`
2. Top blockers (bullets with finding file refs)
3. Lane home path
4. **Recommended actions (ordered)** — commit files, dispatch, operator gates.
   Invocable via `/wavves proceed` (AUTH-10).

## Related

- Open product/design calls after a return: `/mod-decide`
- Full multi-wave build after locks: `/charter` or `/wavves` with the build task
- Home missing: `/wavves-init` first
- Lifecycle: `examples/usage.md` → "From check to BUILD"

# PUO-W1b — contradictions

```text
lens: contradictions
wave_id: PUO-W1b
model: cursor-grok-4.5-high-fast
artifact: feature-requests/20260720_pre-unlock-options-mod-check.md
check_repo_state_verified_against: 26ad2d2afbb9196f2b690000f6a50f1cabfe20e5
verdict_lean: REVISE
escalation: O0 only
git: none performed
```

## Hydrated (this lens)

- artifact; lane `waveset.md` / `dispatch.md`
- `skills/mod-check/SKILL.md` (AUTH-04, AUTH-05)
- `skills/charter/SKILL.md` (reconcile / registry fields)
- `skills/wavves/playbooks/proceed.md`; `skills/wavves/playbooks/check.md`
- `feature-requests/README.md`
- Foreign pax RWC/RLW illustration only (unlock sequence narrative)

## Verdict lean (this lens)

**REVISE.** Intent is coherent (new AUTH-11, not stretch AUTH-05). Several
internal conflicts would let BUILD pick opposite gates: waive vs heuristic,
AUTH-04 fixed `blocks_wN` vs free `blocks_<options_wave>`, "B required" vs
still-open operator Accept, and REVISE-applied clear vs mandatory re-check
wording. Not BLOCK: conflicts are editable without re-scoping the product.

O0 owns the lane verdict. This file does not grade sibling lenses.

## CX-* conflicts

### CX-01 — Explicit waive vs implicit heuristic still fires

| | |
|---|---|
| **Claim A** | Waive only with operator `pre_unlock_mod_check: waived` + one-line reason in LOCKED. |
| **Claim B path** | Playbook sketch: route when `required` **(or heuristic matches)**. Implicit need when ≥2 of 4 signals. |
| **Conflict** | A wave can be `waived` and still match the heuristic. Proceed text does not say waive wins. Agents may re-route to check after an explicit waive, or honor waive and skip a heuristic hit. |
| **Severity** | high |
| **Lean** | REVISE — lock precedence: `waived` beats heuristic; `required` beats absence; heuristic only when flag unset. |

### CX-02 — AUTH-11a auto-`required` vs false-positive risk control

| | |
|---|---|
| **Claim A** | AUTH-11a: if any wave is `options-only` / options memo / unlock-before-DECIDE, set `pre_unlock_mod_check: required`. |
| **Claim B path** | Risks: false positive if every GATED W2 treated as options; require options/memo language or explicit flag. |
| **Conflict** | AUTH-11a already treats three phrasings as sufficient for `required`. Risk text implies a narrower detector. "GATED" alone is banned, but "unlock-before-DECIDE" can still tag non-memo gated waves. |
| **Severity** | medium |
| **Lean** | REVISE — one detector definition shared by AUTH-11a, heuristic, and Risks (closed phrase list + optional explicit flag). |

### CX-03 — AUTH-11c `blocks_<options_wave>` vs AUTH-04 `blocks_w2`…`blocks_w5`

| | |
|---|---|
| **Claim A** | AUTH-04 / live mod-check: scoped flags are `blocks_w2`…`blocks_w5` only. |
| **Claim B path** | AUTH-11c: verdict must set `blocks_<options_wave>` for unlock safety; AUTH-11e adds `options_wave_id`. |
| **Conflict** | Free-form `blocks_RLW-W2` (or similar) is not in the live schema. Mapping `options_wave_id` → `blocks_wN` is unspecified. Proceed AUTH-11d looks for registry status strings, not `blocks_*` flags. Two unlock-safety signals with no join rule. |
| **Severity** | high |
| **Lean** | REVISE — require AUTH-04 `blocks_wN` for the options wave index; registry `options_wave_id` is documentation only, or extend schema explicitly. |

### CX-04 — Lean B "required" vs Operator decision still open

| | |
|---|---|
| **Claim A** | Where it lands: option B lean **required**; D evals **strong**. |
| **Claim B path** | Operator decision: Accept / revise / reject, then `/mod-check` this FR before BUILD. |
| **Conflict** | "Required" reads as already locked product shape while Accept is still open. BUILD agents may treat B+D as decided and skip mod-decide forks (heuristic threshold, waive rules, status vocabulary). |
| **Severity** | medium (phase-boundary leak) |
| **Lean** | REVISE — mark B/D as proposal leans pending Accept; list open calls for mod-decide. |

### CX-05 — "GO or REVISE-applied" unlock clear vs "re-check on drift only"

| | |
|---|---|
| **Claim A** | AUTH-11b: do not treat unlock as next dispatch until GO or REVISE-applied. |
| **Claim B path** | Risks: `verdict-revise-applied` + synced waveset clears; re-check only on waveset drift. |
| **Conflict** | AUTH-11b can be read as requiring a fresh GO after every REVISE apply. Risks say apply+sync is enough. "REVISE-applied" mechanical meaning (who marks it, which files) is undefined, so both readings stay live. |
| **Severity** | medium |
| **Lean** | REVISE — one clear rule: unlock allowed on `verdict-go` **or** `verdict-revise-applied` with waveset sync hash/mtime match; re-check iff sync broken. |

### CX-06 — AUTH-11d sibling-check statuses vs live registry vocabulary

| | |
|---|---|
| **Claim A** | Live registry statuses in use: `chartered`, `check-revise`, `mod-decide-complete-awaiting-build`, `completed`, … (`wavves/registry.yml`). |
| **Claim B path** | AUTH-11d: clear when sibling check is `verdict-go` / `verdict-revise-applied` against waveset mtime. |
| **Conflict** | Proposed statuses collide with / ignore existing `check-revise` and AUTH-05's `mod-decide-complete*` gate. Proceed step 3 already checks AUTH-05; AUTH-11d adds a second gate without stating order or whether both must pass. |
| **Severity** | high |
| **Lean** | REVISE — extend status enum explicitly; order AUTH-11 then AUTH-05 (or combine into one pre-dispatch checklist). |

### CX-07 — Option A rejected vs AUTH-05 still on the proceed path

| | |
|---|---|
| **Claim A** | Option A (extend AUTH-05 only) is weak / wrong trigger. |
| **Claim B path** | Live `proceed.md` step 3 still runs AUTH-05 on every dispatch; AUTH-11d adds another proceed branch. |
| **Conflict** | Not fatal, but FR never says AUTH-05 remains for mod-decide sync while AUTH-11 covers options unlock. Implementers may fold AUTH-11 into AUTH-05 (rejected A) or leave AUTH-05 and invent a parallel undocumented gate. |
| **Severity** | low–medium |
| **Lean** | REVISE — one sentence: AUTH-05 unchanged; AUTH-11 is an additional pre-unlock gate. |

### CX-08 — Charter reconcile `recommended_actions` vs proceed source scope

| | |
|---|---|
| **Claim A** | `proceed.md` today: sources are mod-check verdict, mod-decide completion, or lane reconcile return (AUTH-10). |
| **Claim B path** | AUTH-11b: charter reconcile emits `recommended_actions` including `/mod-check` first. |
| **Conflict** | Charter skill reconcile duties do not today mandate AUTH-10 `recommended_actions` blocks. FR assumes reconcile returns are already proceed-shaped. If reconcile only writes prose `recommended_next_for_O0: unlock …`, proceed step 1 "if absent, infer… stop if ambiguous" can skip AUTH-11d. |
| **Severity** | high |
| **Lean** | REVISE — require machine-readable AUTH-10 actions on options-unlock recommends, or teach proceed to parse `unlock` + options-wave ids from reconcile prose with a fail-closed rule. |

## Lens verdict

**REVISE** (not BLOCK, not GO).

Highest-severity conflicts are CX-01 (waive/heuristic), CX-03 (blocks_*
schema), CX-06 (status vocabulary vs AUTH-05), and CX-08 (proceed source
shape). Resolve those before BUILD charter; mod-decide can lock the open
calls from CX-04.

## Commit file list (orchestrator)

- `wavves/lanes/20260723_pre-unlock-options-check/findings/PUO-contradictions.md`

No git actions performed.

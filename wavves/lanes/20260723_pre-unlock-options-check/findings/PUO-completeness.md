# PUO-W1c — completeness

```text
lens: completeness
wave_id: PUO-W1c
model: cursor-grok-4.5-high-fast
artifact: feature-requests/20260720_pre-unlock-options-mod-check.md
check_repo_state_verified_against: 26ad2d2afbb9196f2b690000f6a50f1cabfe20e5
verdict_lean: REVISE
escalation: O0 only
git: none performed
```

## Hydrated (this lens)

- artifact; lane `waveset.md` / `dispatch.md` / `README.md`
- `skills/mod-check/SKILL.md`; `skills/charter/SKILL.md`
- `skills/wavves/playbooks/proceed.md`; `skills/wavves/playbooks/check.md`;
  `skills/wavves/playbooks/charter-lane.md`
- `feature-requests/README.md`; `examples/usage.md` (From check to BUILD)
- `wavves/registry.yml`; `wavves/failure_log.yml`
- `evals/README.md` (+ fixture layout)
- Foreign pax RLW/RWC illustration only

## Verdict lean (this lens)

**REVISE.** Problem, AUTH-11 sketch, heuristic seed, and proceed paste are
enough for `/mod-decide`. The FR is not complete enough to charter BUILD:
no acceptance criteria, no non-goals, no mechanical definition of
`verdict-go` / `verdict-revise-applied` / sync, no sibling-lane discovery
rule, no rollback/stop, and option D evals have no fixture home. Not BLOCK:
product shape is named; gaps are fillable edits.

O0 owns the lane verdict.

## Blocking gaps

### B1 — No acceptance criteria / pass metric for AUTH-11

**Evidence:** FR has Problem, Feature sketch, Where it lands, Risks,
Operator decision. No Acceptance / AC table.

**Missing:**

| element | specified | missing |
|---|---|---|
| ACs per AUTH-11a–e | sketch rows | checkable pass/fail per surface |
| fail id wired to ACCEPT | `PROC-UNLOCK-NO-CHECK` named | detector + fixture + gate-capture path |
| negative AC | Risks prose | "GATED-only W2 does not force check" as AC |
| docs AC | usage.md mention | README / CHANGELOG / SKILL When-to-use bullets |

**Why blocking:** BUILD ACCEPT can green on prose edits alone.

**Needed edit:** Add Acceptance section with runnable checks (fixture or
harness) citing `PROC-UNLOCK-NO-CHECK`.

### B2 — Registry / status schema for clear signals incomplete

**Evidence:** AUTH-11d/e propose `verdict-go`, `verdict-revise-applied`,
`pre_unlock_mod_check`, `pre_unlock_check_lane`, `options_wave_id`.
Live `wavves/registry.yml` has none of these; charter optional-fields list
omits them.

**Missing:** field types; allowed status enum; who writes transitions
(O0 only); relationship to existing `check-revise` /
`mod-decide-complete*`; whether `pre_unlock_mod_check` lives in registry,
waveset Meta, or both (AUTH-11a says both).

**Why blocking:** Proceed cannot remasure a status that has no schema.

**Needed edit:** Freeze field table + status enum + single writer.

### B3 — "Synced to waveset mtime" undefined

**Evidence:** AUTH-11d "against current waveset mtime"; Risks "synced
waveset"; live registry already has `waveset_synced_at` (AUTH-05 neighbor).

**Missing:** mtime vs content hash vs `waveset_synced_at`; timezone; which
file's mtime (waveset only vs LOCKED too); behavior when filesystem mtime
moves without content change; multi-repo lane clocks.

**Why blocking:** False clear (stale GO) and false block (touch-only mtime)
both available.

**Needed edit:** Prefer recorded sync hash/`waveset_synced_at` over raw
mtime; define remasure algorithm in proceed step.

### B4 — Sibling check lane discovery unowned

**Evidence:** AUTH-11d "no sibling check lane is verdict-go / …".

**Missing:** how to find the sibling (registry `pre_unlock_check_lane`?
`depends_on`? name heuristic `*-mod-check`?); multiple check lanes;
check in another repo; missing lane → fail-closed vs charter-check-now.

**Why blocking:** Proceed either invents a lane or skips the gate.

**Needed edit:** Require `pre_unlock_check_lane` when `required`, or
fail-closed with operator_gate to charter check.

### B5 — AUTH-11c artifact bundle missing-file behavior

**Evidence:** Default bundle: `waveset.md` + `LOCKED-DECISIONS.md` + latest
`*-RECONCILE.md` (+ gate JSON).

**Missing:** if LOCKED or RECONCILE absent; multiple `*-RECONCILE.md`;
which gate JSON; whether check is BLOCK vs REVISE when bundle incomplete;
proof-bar lens yes/no for this trigger (`proof_required` default for
plugin-meta).

**Why blocking:** mod-check runners will invent bundle substitutes.

**Needed edit:** Bundle required-vs-optional table + incomplete-bundle
verdict rule.

### B6 — Option D evals lean "strong" without fixture shape

**Evidence:** Where it lands D; `evals/` has sibling checkers
(`check_proof_before_accept.py`, fixtures under `evals/fixtures/`).

**Missing:** fixture id/path; input artifact shape (fake waveset +
reconcile recommending unlock); expected FAIL `PROC-UNLOCK-NO-CHECK`;
runner entry in `evals/run_fixtures.py` / README; whether D is v0 ACCEPT
or follow-on.

**Why blocking:** "Strong" eval can be deferred forever while BUILD ships.

**Needed edit:** Lock D in or out of v0 ACCEPT with named fixture stub.

### B7 — Non-goals / rollback / stop rules absent

**Evidence:** Problem lists RLW-class gaps (ACs, non-goals, rollback, stop)
that RWC required before options unlock. This FR does not apply that bar
to itself.

**Missing:** non-goals (e.g. not gating BUILD unlock, not replacing
AUTH-05, not auto-dispatching mod-check without O0); rollback if AUTH-11
false-blocks trivial memos; stop if heuristic ambiguous.

**Why blocking:** Same class of incompleteness the FR exists to prevent.

**Needed edit:** Add Non-goals + Rollback + Stop sections.

## Non-blocking gaps

### N1 — Heuristic scoring edge cases

≥2 of 4 listed, but no worked examples (RLW would score how?), no tie-break
when signals conflict, no guidance for research lanes with GATED memos that
are not ranking options.

### N2 — `examples/usage.md` path named, README/CHANGELOG not

Playbook sketch cites usage path; shipped siblings usually touch README /
CHANGELOG. Unowned.

### N3 — Interaction with proceed-all-standing (PAS) unstated

If standing queue classifies an unlock-options item as `dispatch`, AUTH-11
must apply. FR silent. Cross-FR note is enough (non-blocking if PAS not
shipped).

### N4 — Charter write-time vs reconcile-time flag

AUTH-11a sets flag at charter write; waves can become options-only later.
No recompute rule.

### N5 — Fail id not in `failure_log.yml` shape guidance

Proposed id is fine for FR stage; BUILD should say when O0 appends it.

## What is already complete enough

- Trigger story (reconcile recommends unlock-options without check).
- Surface list (charter, mod-check, proceed, registry).
- Waive requires explicit operator line (directionally).
- Option A correctly rejected as wrong AUTH-05 trigger.
- Foreign illustration names the load-bearing RWC→unlock sequence.

## Commit file list (orchestrator)

- `wavves/lanes/20260723_pre-unlock-options-check/findings/PUO-completeness.md`

No git actions performed.

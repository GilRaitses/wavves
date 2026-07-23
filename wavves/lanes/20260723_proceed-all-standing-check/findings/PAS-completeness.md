# PAS-W1c — completeness

- **Lens:** completeness
- **Artifact:** `feature-requests/20260723_proceed-all-standing.md`
- **Repo state (dispatch):** `73b09bad223ed004a2e8f10443f48196cbbbf396`
- **Hydrated:** waveset.md, dispatch.md, artifact;
  `skills/wavves/playbooks/proceed.md`, `skills/wavves/SKILL.md`,
  `skills/wavves/playbooks/pickup.md`, `skills/wavves/playbooks/layover.md`,
  `feature-requests/README.md`,
  `wavves/handoffs/20260723_set-key_docs_version_bump.md`,
  `evals/README.md` (+ fixture layout / sibling checkers),
  `skills/mod-check/SKILL.md` (lens hunt list)
- **Lens verdict recommendation:** **REVISE**
- **Blocker count:** 6 blocking gaps; 4 non-blocking
- **statement:** read-only; no git; no code edits outside this findings file
- **Escalation:** O0 only

## Verdict (this lens only)

REVISE. Problem, triggers, fail ids, and most move rules are clear enough for
`/mod-decide`. The FR is not yet complete enough to charter BUILD: standing
queue schema and persistence are forked, `out_of_scope` has no move rule,
router wiring in `skills/wavves/SKILL.md` is unnamed, eval fixture homes and
runner are unnamed, Acceptance can green without locking those edges, and
multi-repo / empty-lane behavior is unowned.

O0 owns the lane verdict. Not BLOCK: intent and non-widen of bare shrug are
already product-shaped. Not GO: BUILD would invent schema, wiring, and eval
shape.

---

## Blocking gaps

### B1 — Standing queue schema holes (BUILD unlock)

**Evidence:** PS-02: ordered list of `{id, source_path, class, action}` with
`class` ∈ five values; persist under `wavves/standing/<YYYYMMDD>_<label>.md`
**(or)** lane `standing.md`. Return card (PS-06) adds land hash / gate path /
blocked reason, which are not in the schema tuple.

**Missing for charter:**

| element | specified | missing |
|---|---|---|
| field set | four names | types, required vs optional, max lengths |
| `action` | listed | proposed vs taken; closed vocab vs free text |
| post-move fields | return card only | whether queue file gains `result`, `land_hash`, `gate_path`, `blocked_reason` |
| ordering | "Ordered list" | remasure sort key (registry order? operator paste? severity?) |
| persistence home | two alternatives with "or" | single locked path; create-dir rule; overwrite vs append; one file per pass vs per day |
| empty inventory | — | write empty queue + stop, or refuse mode |

**Why blocking:** BUILD cannot lock waveset acceptance against an OR persistence
path and a four-field tuple that omits the return-card fields the mode must emit.

**Needed edit:** Freeze one persistence home; expand schema to cover return
card columns; define empty-queue behavior.

### B2 — `out_of_scope` class has no move rule

**Evidence:** PS-02 includes `out_of_scope` in the class enum. PS-04 Move rules
cover only `dispatch`, `commit_land`, `operator_gate`, `skip_done`. Non-goals
forbid cross-lane "do everything in the registry" without named scope, but
never say what the agent does when an inventoried item is classified
`out_of_scope`.

**Gap:** Unowned edge: list-and-skip? omit from queue? surface in return card
with no mutation? operator must re-scope?

**Why blocking:** Without a move rule, agents will either invent work outside
scope or silently drop items. Completeness requires parity with the other four
classes.

**Needed edit:** Add PS-04 bullet: `out_of_scope` → cite scope boundary, no
dispatch/commit, include in return card as not-moved.

### B3 — Router wiring (`skills/wavves/SKILL.md`) not named

**Evidence:** Product surface claims "`/wavves` routing". Triggers propose
`/wavves proceed all standing`. Live router
(`skills/wavves/SKILL.md` Routing table, proceed row) only names
`proceed as recommended`, `/wavves proceed`, execute verdict actions.
Playbook list points at `playbooks/proceed.md` only. Acceptance requires
playbook docs + README/usage/index, **not** an explicit SKILL.md routing /
description / playbook-row edit. Next step says "BUILD into proceed playbook
(+ optional thin leaf)" and never names the router file.

**Gap:** Unowned whether BUILD patches SKILL.md routing table (and
frontmatter description), only proceed.md, and/or a new leaf skill. Sibling
shipped products (set-key, paragraph-tunnel, proof-before-accept) all touch
router and/or named playbook rows; this FR leaves the seam implicit.

**Why blocking:** Without a named wiring surface, Acceptance can PASS on
proceed.md alone while `/wavves proceed all standing` still routes to bare
proceed (AUTH-10 recommended_actions only) — the defect the FR exists to fix.

**Needed edit:** Add PS row + Acceptance bullet: update
`skills/wavves/SKILL.md` proceed route (and description if needed); lock
playbook-only vs optional leaf as a mod-decide call.

### B4 — Eval fixture homes and runner unnamed

**Evidence:** Acceptance lists three eval/fixture behaviors (blocked lock →
operator_gate; dispatchable → background; PASS → skip_done). `evals/README.md`
shows three harness families: lens-keyword `run_fixtures.py`, disjoint
`check_paragraph_tunnel.py` (`evals/fixtures/paragraph-tunnel-*/`), disjoint
`check_proof_before_accept.py` (`evals/fixtures/proof-before-accept-*/`).
No `proceed-all-standing` prefix, checker script, or fixture layout exists
today. FR never names home, prefix, `input.md`/`expected.md` vs mechanical
checker, or pass command.

**Gap:** Acceptance can be "documented" without a runnable corpus. Using
`run_fixtures.py` alone would only tripwire lens wording, not proceed-mode
classification.

**Why blocking:** Same class of hole PBA/PTG hit: BUILD AC must name fixture
home + assertion mechanism or the mode ships without a gate.

**Needed edit:** Name e.g. `evals/fixtures/proceed-all-standing-*/` +
stdlib checker (or explicit defer of mechanical checker with lane-local
fixtures and a later wave). Map each of the three AC bullets to a case id
and expected class.

### B5 — Acceptance bullets insufficient for BUILD charter

**Evidence:** Seven Acceptance checkboxes (doc split, queue-on-disk, three
fixtures, docs index, mod-check before BUILD).

**Missing AC (testable):**

| missing AC | why it matters |
|---|---|
| SKILL.md route lists proceed-all-standing triggers | closes B3 |
| Bare shrug alone does not invent standing inventory | core non-widen; waveset Locked but not Acceptance |
| `out_of_scope` appears in return card with no mutation | closes B2 |
| Empty / no-active-lane inventory → defined stop | closes B6 |
| Fail ids emitted or documented (`PROC-PROCEED-NO-STANDING-QUEUE`, `PROC-PROCEED-FORCE-BLOCKED-LOCK`) | proposed in Problem; never in Acceptance |
| Return card columns match PS-06 | sketch only |
| Persistence path frozen | currently OR |

**Why blocking:** A BUILD waveset copied from these bullets can green on prose
and three narrative fixtures while router, empty-lane, and out_of_scope edges
remain inventable.

### B6 — Multi-repo / no active lane edge unowned

**Evidence:** PS-03 inventory sources: "active program/lane set", registry +
active_dispatch, lane dispatch/waveset, gates, open FRs, optional operator
paste. Non-goals: no cross-lane everything without operator-named scope;
default scope = "current conversation's program / named lanes." Layover
playbook (`skills/wavves/playbooks/layover.md`) is the multi-repo preflight
surface and is never mentioned. Pickup hydrates active lanes from INDEX but
is not named as a seam for standing inventory.

**Gaps:**

1. **No active lane / empty registry:** mode behavior unset (refuse? write
   empty standing file? fall back to operator paste only?).
2. **Multi-repo workspace:** whether standing inventory may cross sibling
   repos from a `.code-workspace`, or stays single-repo (invoking
   `wavves/` home only). Silent assumption today: single-repo.
3. **How "current conversation's program" is remasured** when operator did
   not name a lane this turn.

**Why blocking:** BUILD agents will invent scope. Multi-repo invent risks
cross-repo dispatch/commit; empty-lane invent risks chat-memory queue (the
stated fail mode).

**Needed edit:** Lock default scope = invoking repo's `wavves/` +
operator-named lanes only; multi-repo = out of scope or layover-only report;
empty active set → write empty queue + stop (or require paste + verify).

---

## Non-blocking gaps

### N1 — Open calls for mod-decide incomplete / mislisted

**Evidence:** Next: "`/mod-decide` any open calls (queue path, bare-shrug
non-widen, persistence path)".

**Present as decide-worthy:** persistence path (home OR); landing shape
(playbook-only vs thin leaf) implied but not listed as a call.

**Mislisted:** bare-shrug non-widen is already locked in PS-05 and waveset
Locked; it should be a BUILD invariant / AC, not an open product fork.

**Absent from the open-call list (should be explicit):**

1. Persistence home (keep)
2. Landing: playbook-only vs optional leaf skill (add)
3. Eval home + runner (add; or defer with named non-goal)
4. `out_of_scope` move rule (add if not patched in FR)
5. Multi-repo / empty-lane policy (add)
6. Queue ordering key (add if not frozen in schema)

### N2 — Rollback / disable absent

**Evidence:** Completeness lens hunts absent rollback. Non-goals cover
auto-unlock, polling, replacing decide/check, unbounded registry sweep. No
disable flag, no "bad standing file → ignore and re-inventory", no revert of
playbook mode if mis-trigger widens shrug.

**Call:** Soft: add Non-goals or Rollback note — wrong standing file must not
authorize commit; operator can discard `wavves/standing/*` and re-run; bare
shrug path remains AUTH-10-only if mode withdrawn.

### N3 — Interaction with pickup / AUTH-10 proceed coexistence thin

**Evidence:** proceed.md today executes `recommended_actions` only. FR adds a
second mode. Pickup reports standing state but is not named as consumer or
non-overlap. Whether all-standing may run when a verdict `recommended_actions`
block also exists (merge? prefer all-standing? refuse?) is unset.

**Call:** Non-blocking if B3 locks router precedence: all-standing scope wins
over bare recommended_actions for that turn; else document merge rule.

### N4 — Foreign evidence pins as BUILD hard-deps

**Evidence:** Originating table cites pax dispatch-w27, IWD-V3 gate, TOP PASS;
`evidence_verified_against` names pax/klosr hashes. Dispatch says do not
require live pax/klosr for PASS grounding.

**Call:** Completeness flag only: Acceptance fixtures must be repo-local
synthetics, not hard-deps on pax paths. Already implied by non-goals /
dispatch; state once under Acceptance or Non-goals.

---

## Silent assumptions (call out)

1. "Current conversation's program / named lanes" is remasureable from disk
   (INDEX/registry) without chat memory — unstated algorithm.
2. Operator paste list is optional enrichment; disk remasure always wins
   (stated directionally in PS-03; not AC).
3. `commit_land` under all-standing inherits the same operator-ask bar as
   proceed.md step 2 (partially stated; file list ownership unset).
4. Background dispatch needs a named `dispatch_file` / AUTH-05 sync the same
   as bare proceed (unstated; proceed.md step 3 exists but mode sketch does
   not cite it).
5. Single-repo invoking home is enough (multi-repo unowned; see B6).
6. Three narrative eval bullets imply a mechanical or fixture harness will
   exist in-repo (homes unnamed; see B4).

---

## Non-goals coverage

**Present and useful:** no auto-unlock of hard locks; no polling background
runners; no replacing mod-decide/mod-check; no unbounded registry sweep
without named scope.

**Still thin:**

- No explicit non-goal for multi-repo standing invent (layover remains audit)
- No rollback/disable
- No statement that foreign pax/klosr pins are illustration-only for BUILD
- Optional leaf skill deferred in Next prose but not listed under Non-goals
  for v0

---

## Hunt checklist (dispatch-specific)

| hunt | result |
|---|---|
| Acceptance sufficient for BUILD charter? | **No** (B5) |
| Standing queue schema fully specified? | **No** (B1) |
| Router wiring (`SKILL.md`) named? | **No** (B3) |
| Eval fixture homes named? | **No** (B4) |
| Open calls for mod-decide explicit? | **Partial** (N1) |
| `out_of_scope` move rules? | **Absent** (B2) |
| Multi-repo / no active lane covered? | **No** (B6) |
| Rollback / non-goals gaps? | Thin (N2) |

---

## Covered adequately (for this lens)

- Problem vs AUTH-10-only proceed; chat-memory fail mode named
- Two proposed fail ids with plain-language definitions
- Trigger table distinguishing bare shrug vs all-standing scope
- PS-04 move rules for four of five classes (dispatch / commit_land /
  operator_gate / skip_done)
- Inventory source list (registry, active_dispatch, gates, FRs, paste verify)
- Return card column sketch (PS-06)
- Non-goals skeleton (locks, polling, decide/check, scope)
- Explicit Next path: mod-check → mod-decide → charter BUILD
- Originating evidence table as illustration (classes match enum)
- FR indexed in `feature-requests/README.md` as ready-for-mod-check
- Sibling handoff correctly parks this FR as separate check/decide/charter

---

## Recommended FR edits (for O0 / mod-decide; not applied)

1. Freeze standing queue schema + single persistence home; align return-card
   fields; define empty-queue stop.
2. Add `out_of_scope` move rule (cite + no mutation + return-card row).
3. Name `skills/wavves/SKILL.md` as a BUILD wiring target; lock playbook-only
   vs optional leaf via mod-decide.
4. Name eval fixture prefix + runner (or explicit defer); map three AC cases
   to case ids / expected class.
5. Expand Acceptance: bare-shrug non-widen AC; router row; out_of_scope;
   empty active lane; fail-id documentation or emission.
6. Lock multi-repo = out of scope (invoking repo only) and empty-lane stop.
7. Rewrite Next open calls: drop bare-shrug (already locked); keep
   persistence + landing + eval + scope edges.
8. (Non-blocking) Add rollback/disable note; state foreign pins are
   illustration-only for BUILD fixtures.

---

## Commit file list (for O0; no git performed)

- Write: `wavves/lanes/20260723_proceed-all-standing-check/findings/PAS-completeness.md`
- Exclude: none
- **No git actions performed.**

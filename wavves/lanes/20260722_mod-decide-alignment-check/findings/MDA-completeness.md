# MDA-W1c — completeness

- **Lens:** completeness
- **Artifact:** `feature-requests/20260722_mod-decide-decision-alignment.md`
- **Repo state (dispatch):** `26ad2d2afbb9196f2b690000f6a50f1cabfe20e5`
- **Hydrated:** waveset.md, dispatch.md, artifact;
  `skills/mod-decide/SKILL.md`, `skills/wavves/playbooks/decide.md`,
  `examples/usage.md` (decide sections), `feature-requests/README.md`,
  `evals/README.md` (+ fixture / checker layout),
  `skills/mod-check/SKILL.md` (lens hunt list)
- **Lens verdict recommendation:** **REVISE**
- **Blocker count:** 5 blocking gaps; 4 non-blocking
- **statement:** read-only; no git; no code edits outside this findings file
- **Escalation:** O0 only

## Verdict (this lens only)

REVISE. Problem, fail ids, per-option template, and DA-01..DA-07 sketch are
clear enough for `/mod-decide` on landing shape. The FR is not complete
enough to charter BUILD: no Acceptance section, eval homes/runner unnamed,
standing-intent source when charter/waveset silent is unowned, Locked paste
/ AUTH-01 field merge unspecified, and option A/B/C/D landing is not an
explicit open-call list.

O0 owns the lane verdict. Not BLOCK: defect class is real and templates are
product-shaped. Not GO: BUILD would invent AC, fixture harness, and
authority surfaces.

---

## Blocking gaps

### B1 — No Acceptance criteria section

**Evidence:** FR has Problem, Feature sketch, Where it lands, Risks,
Operator decision. No Acceptance / Done-when checklist.

**Missing for charter:**

| element | status |
|---|---|
| Skill presents exit_criteria on every hold/ban/pause option | absent AC |
| Lean Hold-no-exit → fail / refuse | absent AC |
| Program alignment stanza + per-option program_tag | absent AC |
| Grain check on admit/hold/build-scope calls | absent AC |
| Locked paste includes program_intent + unlocks_next | absent AC |
| Playbook + examples anti-loop text | absent AC |
| Fixtures emit named fail ids | absent AC (DA-07 sketch only) |

**Why blocking:** BUILD waveset copied from DA rows can green on prose
patches with no remasureable ACCEPT.

**Needed edit:** Add Acceptance bullets mapped 1:1 to DA-01..DA-07 (and
landing pick).

### B2 — Eval fixture homes and runner unnamed

**Evidence:** DA-07 names two behaviors and fail ids.
`evals/README.md` shows lens-keyword `run_fixtures.py` plus mechanical
checkers (`check_paragraph_tunnel.py`, `check_proof_before_accept.py`).
No `mod-decide` / `decide-alignment` prefix exists.

**Gap:** Unowned whether DECIDE-ALIGN uses keyword tripwire (known weak),
a new `check_mod_decide_alignment.py`, or lane-local fixtures deferred.

**Why blocking:** Same class as PBA/PAS: ACCEPT without a named harness is
process-PASS.

**Needed edit:** Name e.g. `evals/fixtures/decide-hold-no-exit/` +
`decide-grain-mismatch/` and checker (or explicit defer with non-goal).

### B3 — Standing-intent source when waveset/charter silent

**Evidence:** DA-02: 2–4 bullets from waveset/charter/prior locks
(verbatim cites). DA-03: operator intent from charter or prior message.

**Gaps:**

1. No prior locks / empty waveset Locked → refuse decide? invent intent
   from chat? park alignment?
2. "Prior message" re-admits chat memory as intent authority.
3. Conflict among waveset vs charter vs operator utterance: no precedence.

**Why blocking:** Without a remasure rule, program_tag theater cites
whatever the agent remembers (the originating failure mode, inverted).

**Needed edit:** Lock precedence: waveset Locked → decisions/*.md →
operator paste this turn. If none, emit `program_intent: unset` and ban
aligns tags until operator supplies cites; no transcript search.

### B4 — Locked paste / decision record / AUTH-01 schema incomplete

**Evidence:** DA-05 adds `program_intent` + per-pick `unlocks_next`.
Templates add `exit_criteria`, `program_tag`. Live skill paste and
decision record omit them. AUTH-01 already requires proof_* fields when
applicable.

**Missing:** Field list on decision `*.md`; Locked paste fenced shape;
registry/waveset sync keys; whether `unlocks_next` is required on
non-hold picks; interaction with proof_required block.

**Why blocking:** BUILD cannot patch skill + AUTH sync without inventing
schema.

**Needed edit:** Spec decision record + Locked paste + AUTH-01 checklist
deltas in the FR.

### B5 — Landing shape (A/B/C/D) and open calls not listed for mod-decide

**Evidence:** Where it lands table leans B required, D companion.
Operator decision Accept/revise/reject. No "Next: `/mod-decide` open
calls" list.

**Absent explicit calls:**

1. Landing: B only vs B+D vs docs-only A (C insufficient is a reject, not a
   pick)
2. Eval harness: mechanical checker vs keyword fixtures vs defer
3. Grain invent override vs operator-added fork only (see contradictions
   CX-01)
4. Intent precedence when disk silent (B3)

**Why blocking:** Phase leak: "B required" can skip decide; BUILD then
guesses D and eval shape.

**Needed edit:** Next section with open calls; demote author lean to
recommendation.

---

## Non-blocking gaps

### N1 — Triggers / when grain check applies

**Evidence:** DA-03: "When the call is admit/hold/build-scope." No cue
list for classifying a call into that class vs ordinary product fork.

**Call:** Soft: closed cue list (admit, hold, ban, pause, build-scope,
supersede) or "any call whose options include Hold/Ban/Pause."

### N2 — Rollback / disable absent

**Evidence:** Risks mention longer turns. No disable flag, no "alignment
stanza wrong → operator discard and re-decide."

**Call:** Soft non-goal: bad program_intent must not auto-charter BUILD;
operator can reject lean and re-run decide.

### N3 — Option C "Registry flags only" undefined

**Evidence:** Where it lands C: Registry flags only / insufficient.

**Call:** Either drop C or name which registry keys (none exist today for
decide-alignment). Non-blocking if C stays rejected example.

### N4 — Foreign IWD pins as BUILD hard-deps

**Evidence:** Source evidence + DA-07 Midtown wording. Dispatch:
illustration only.

**Call:** Acceptance fixtures must be repo-local synthetics with generic
grain labels. State under Non-goals or Acceptance.

---

## Silent assumptions (call out)

1. "Hygiene exits already exist (freeze wire, check PASS)" is remasureable
   from Grounding paste / named artifact paths.
2. Letter options A/B/C/D remain the presentation form (skill does not
   require letters today; convention only).
3. DA-06 anti-loop applies only to admit/build-scope after PASS, not to
   all decide sessions.
4. Fail ids land in skill text and/or `failure_log.yml` (append owner is
   O0 at reconcile; FR never says which).
5. Single-repo plugin home is enough (no multi-repo decide).

---

## Non-goals coverage

**Present (thin):** over-fit risk called; hold still allowed with exit;
docs-only/registry-only called insufficient via landing table.

**Still thin:**

- No explicit non-goal: foreign pax paths not required for ACCEPT
- No non-goal: auto-lock prefer-aligns
- No rollback/disable
- No statement that invent-fork ban is amended or preserved

---

## Hunt checklist (dispatch-specific)

| hunt | result |
|---|---|
| Acceptance sufficient for BUILD charter? | **No** (B1) |
| Eval fixture homes named? | **No** (B2) |
| Standing-intent remasure rule? | **No** (B3) |
| Locked paste / AUTH schema specified? | **No** (B4) |
| Open calls for mod-decide explicit? | **No** (B5) |
| Rollback / non-goals gaps? | Thin (N2, N4) |
| Triggers for grain-check class? | Thin (N1) |

---

## Covered adequately (for this lens)

- Problem: indefinite-hold bias, grain mismatch, lean without alignment
- Two proposed fail ids with plain-language definitions
- Per-option and lean templates (required shapes)
- DA-01..DA-07 target map across skill / playbook / examples / evals
- Landing table with author lean
- Risks (length, over-fit, hold-with-exit allowed)
- Explicit Operator path: mod-check this FR before BUILD charter
- FR indexed `ready-for-mod-check`; MDA lane chartered at pin `26ad2d2…`

---

## Recommended FR edits (for O0 / mod-decide; not applied)

1. Add Acceptance mapped to DA-01..DA-07 + landing pick.
2. Name eval fixture prefix + runner (or defer).
3. Lock intent precedence; ban transcript invent for program_intent.
4. Spec decision record + Locked paste + AUTH-01 field deltas.
5. Add Next open calls; mark B/D as author lean until decide locks.
6. Resolve grain invent vs do-not-invent (with contradictions CX-01).
7. (Non-blocking) Grain cue list; rollback note; foreign pins
   illustration-only for fixtures.

---

## Commit file list (for O0; no git performed)

- Write: `wavves/lanes/20260722_mod-decide-alignment-check/findings/MDA-completeness.md`
- Exclude: none
- **No git actions performed.**

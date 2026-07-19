# PBA-W1c — completeness

- **Lens:** completeness
- **Artifact:** `feature-requests/20260718_proof-before-accept.md`
- **Repo state (dispatch):** `af0c0788cb2dbb865cbce6721fcdcbf6642b11d4`
- **Hydrated:** waveset.md, dispatch.md, artifact; `skills/charter/SKILL.md`,
  `skills/charter/EXECUTION_WIRING.md`, `skills/mod-check/SKILL.md`,
  `evals/README.md`, `feature-requests/README.md`,
  `skills/wavves/playbooks/paragraph-tunnel.md` (shape reference);
  `skills/mod-decide/SKILL.md`, `docs/purpose-gates.md` (boundary)
- **Lens verdict recommendation:** **REVISE**
- **Blocker count:** 5 blocking gaps; 4 non-blocking

## Verdict (this lens only)

REVISE. The problem and option set are clear enough to salvage. The FR is not
complete enough to charter BUILD: mandatory fields lack schema and pass
metrics, product-lane scope is undefined, the visual gate is not runnable as
specified, BUILD acceptance items can green without closing PROC-PASS-NO-PROOF,
and option E vs the recommended C+D+B combo is an unlocked product fork.

O0 owns the lane verdict.

## Shape reference (paragraph-tunnel)

`skills/wavves/playbooks/paragraph-tunnel.md` ships with: closed fail vocab,
numbered dispatch STEPS, capture path convention, loop cap, model lock, lane
types covered, and a disjoint mechanical checker under `evals/`. The PBA FR
names fail ids and landing options but does not yet match that completeness
bar for fields, steps, harness, or fixture harness choice.

---

## Blocking gaps

### B1 — Product / visitor / UX lane classifier unset

**Evidence:** Feature sketch §1: "every product/UX lane must declare…";
§3: "block BUILD unlock when `proof_job` missing on visitor/product lanes";
Non-goals: "Mandating visual gates for pure research/read-only check lanes."

**Gap:** No rule names how a waveset is classified as product/UX/visitor vs
research/read-only/check. Charter today types lanes as "execution vs
research/read-only" (`skills/charter/SKILL.md` waveset sections) and has
`lane_type: multi-repo`, not visitor/product. Boundary cases unowned:
homepage/docs-only, skill-doc lanes, outbound copy, check-of-product-spec,
INT-only wiring, layover.

**Why blocking:** Without a classifier, the mod-decide/charter gate in §3
cannot be applied consistently; BUILD agents will invent the boundary.

**Needed edit:** Define classifier (fields on waveset, keywords, or explicit
`proof_required: yes|no|n/a` with allowed n/a rationales) and list exempt
lane types.

### B2 — `proof_*` fields not charter-ready (schema / location / pass metric)

**Evidence:** Feature sketch §1 lists four names with one-line glosses only:
`proof_job`, `proof_reference`, `chrome_freeze`, `visual_accept`.

**Missing for charter:**

| field | specified | missing |
|---|---|---|
| `proof_job` | "one sentence, operator-facing" | waveset section; max length; who grades satisfaction at ACCEPT; pass = measured how |
| `proof_reference` | "path/URL/figure class or `none` with rationale" | what "figure class" means; required path existence check; `none` rationale template |
| `chrome_freeze` | "what must not change until Proof ACCEPT" | freeze mechanism (lock text vs file checksum vs git); violation detector |
| `visual_accept` | "screenshot/capture required: yes/no" | capture path convention; harness command; comparison rule vs reference; FAIL ids mapping |

**Why blocking:** A BUILD charter cannot lock or enforce fields that have no
home, no validation, and no ACCEPT pass metric. This is the completeness
failure the FR itself targets (process docs without Proof measurement).

### B3 — Visual / blank-canvas gate not runnable as written

**Evidence:** Feature sketch §4: "runnable visual gate: capture screenshot
(or named DOM proof markers) and fail ACCEPT if proof markers absent or map
host height 0 / blank black-canvas class." Acceptance item 2 asks for a
"visual gate named" in fixtures.

**Gap vs EXECUTION_WIRING:** Wiring Rule 2 requires pass metric before run,
JSON/log under `gate-captures/`, and a named reproducible command. Current
wiring examples are transition-gap probes (`scripts/transition_gap_probe.py`),
not screenshots or DOM markers. FR names neither command, script path,
dependencies, capture schema, nor how "blank black-canvas class" is detected
(CSS class string vs visual heuristic).

**Why blocking:** Adversarial/ACCEPT gates that stay prose-only recreate
PROC-NO-VISUAL / unrunnable-gate (evals fixture
`unrunnable-gate-narrowed-adversarial-lens`). BUILD acceptance cannot claim a
visual gate without a harness shape.

**Needed edit:** Name harness approach (stdlib DOM probe vs browser capture),
pass metric, capture filenames, and loop/escalation; or explicitly defer
screenshot tooling to a later wave and define a minimal DOM/height check for
v0.

### B4 — BUILD acceptance items are not all testable / can PASS without Proof

**Evidence:** Acceptance (BUILD) items 1–4.

| # | text | testability |
|---|---|---|
| 1 | Template/playbook "documents" the four fields | Doc presence only; can PASS with no enforcement at charter/ACCEPT time |
| 2 | Fixtures under `evals/fixtures/` show PROC-PASS-NO-PROOF FAIL and PASS with proof fields + visual gate named | Harness choice unset: `run_fixtures.py` is a lens-keyword tripwire (`evals/README.md`), not ACCEPT-criteria structure review; paragraph-tunnel uses a separate mechanical checker. FR does not say which runner or fixture prefix |
| 3 | mod-check/playbook "instructions require hunting" process-only ACCEPT | Prose instruction check only; same keyword-survival limit as current corpus |
| 4 | No install from FR folder | Process meta; not a Proof test |

**Why blocking:** Acceptance as written can green on documentation and lens
wording while PROC-PASS-NO-PROOF remains open in real ACCEPT templates. Item
2 must specify fixture shape, fail assertion, and runner (new checker vs
extend an existing one).

**Needed edit:** Hard, checkable AC: e.g. charter template contains required
keys; fixture `input.md` with process-only ACCEPT → mechanical FAIL with
`PROC-PASS-NO-PROOF`; PASS fixture includes proof fields + named gate
command/capture path; optional third fixture for chrome-only wave.

### B5 — Recommended combo C+D+B leaves option E unlocked

**Evidence:** Options table: E = "Mention in `mod-decide` AUTH sync:
proof_job must appear in waveset locks" lean **strong**. Recommended combo:
**C + D + B**. Sketch §3 also says "mod-decide / charter gate — block BUILD
unlock when proof_job missing."

**Gap:** Whether BUILD patches `mod-decide` AUTH sync (E) is an open product
fork. Sketch §3 implies a mod-decide gate; recommended combo omits E. Owner
of the BUILD-unlock block (charter only vs mod-decide AUTH-01) is unset.

**Why blocking:** Unowned edge between check→decide→charter. Agents will
either skip E or implement it silently.

**Needed edit:** Lock include-E or defer-E with rationale; if deferred, name
how §3's "mod-decide / charter gate" is satisfied by C alone.

---

## Non-blocking gaps

### N1 — Problem names bake→visitor consumer contract; BUILD does not deliver it

**Evidence:** Problem symptom 4: "No bake→visitor consumer contract"; Feature
sketch and Acceptance omit consumer-contract deliverables.

**Call:** Either add a BUILD item / non-goal, or state explicitly that
consumer contract is out of scope for this FR (pax/klosr or later playbook).

### N2 — Rollback / migration for existing lanes absent

**Evidence:** Completeness lens hunts absent rollback. Non-goals cover
replacements and klosr Proof-1, not backfill or revert of the method change.

**Call:** State whether historical wavesets must gain proof fields, and
rollback if visual harness flakes (disable flag, remediation cap, escalate).

### N3 — Fail vocabulary vs ACCEPT ownership incomplete

**Evidence:** Default fail vocabulary table; sketch §2–4 spread responsibility
across mod-check lens, charter template, EXECUTION_WIRING, evals.

**Call:** Non-blocking if B2–B4 land: add a one-line owner per fail id
(proof-bar lens vs ACCEPT harness vs charter template check).

### N4 — Deferred A and "playbook outgrows one file" trigger vague

**Evidence:** "Defer standalone skill (A) unless the playbook outgrows one
file."

**Call:** Optional size/trigger criterion; not required for first BUILD if
D is locked.

---

## Silent assumptions (call out)

1. Screenshot or browser automation is available in ACCEPT runners (unstated;
   may be false in this plugin repo).
2. "Figure class" and "blank black-canvas class" are shared house vocabulary
   (not defined in wavves_build surfaces hydrated here).
3. Keyword/instruction edits plus fixtures are enough to prevent
   process-only ACCEPT PASS (contradicted by `evals/README.md` known
   limitation unless a structure/harness check is added).
4. RFU/CRE/BETA evidence paths under pax are illustrative only for this FR
   (BUILD lands in wavves_build; klosr Proof is non-goal). Completeness does
   not re-litigate grounding of those citations.

---

## Non-goals coverage

Present and useful: does not replace purpose-gates / public-copy-gates /
paragraph-tunnel; no visual mandate for pure research/read-only check lanes;
no klosr Proof-1 inside wavves_build.

Still thin: no explicit non-goal for historical lane backfill, consumer
contract, or standalone `/proof-gate` in v0 (A is deferred in options, not
listed under Non-goals).

---

## proof_job fields: charter readiness summary

| ready to lock in BUILD waveset? | verdict |
|---|---|
| Field names | yes |
| Field semantics / schema / home section | **no** (B2) |
| When required (lane classifier) | **no** (B1) |
| ACCEPT measurement + capture | **no** (B3) |
| Eval assertion of FAIL/PASS | **no** (B4) |
| mod-decide vs charter unlock owner | **no** (B5) |

---

## Recommended FR edits (for O0 / mod-decide; not applied here)

1. Add lane classifier + exempt list.
2. Specify waveset home + validation for the four fields; ACCEPT pass metrics.
3. Specify v0 visual/DOM harness command, capture path, PROC-BLANK-CANVAS /
   PROC-NO-VISUAL detection.
4. Rewrite BUILD acceptance as mechanical checks; name eval runner and
   fixture prefix; at least one structure FAIL and one PASS.
5. Lock E in or out of the BUILD combo; align sketch §3 with that lock.
6. (Non-blocking) Park or scope consumer contract; add rollback/backfill note.

---

## Commit file list (for O0; no git performed)

- Write: `wavves/lanes/20260718_proof-before-accept-check/findings/PBA-completeness.md`
- Exclude: none
- **No git actions performed.**

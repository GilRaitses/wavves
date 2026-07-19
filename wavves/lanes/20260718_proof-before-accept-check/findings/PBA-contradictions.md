# PBA-W1b — contradictions

- **Lens:** contradictions (internal conflicts, phase-boundary leaks, mutually exclusive requirements)
- **Artifact:** `feature-requests/20260718_proof-before-accept.md`
- **repo_state_verified_against (lane):** `af0c0788cb2dbb865cbce6721fcdcbf6642b11d4`
- **Evidence hydrated:** FR; pax doctrine
  `.ddb/decisions/pax_multi_surface_proof_then_consume_doctrine_v1_20260718.yaml`;
  RFU lane `wavves/lanes/20260718_route-first-ux/`; `skills/mod-check/SKILL.md`;
  `skills/mod-decide/SKILL.md`; `skills/charter/SKILL.md`;
  `skills/charter/EXECUTION_WIRING.md`; `evals/README.md`;
  `skills/wavves/playbooks/check.md`; `feature-requests/README.md`;
  `docs/purpose-gates.md`
- **Lens verdict recommendation:** **REVISE**
- **Blocking contradictions:** 3
- **Non-blocking contradictions:** 5

## Verdict (this lens only)

**REVISE.** The FR's intent matches the pax Proof-then-consume doctrine, but the
recommended combo **C+D+B**, the BUILD-unlock claim, the research-lane
exemption, and `chrome_freeze` are not simultaneously satisfiable as written.
Salvageable by naming phase ownership and closing the open option forks before
BUILD. Not GO. Not BLOCK: no claim that the method itself is impossible once
ownership and lane-type predicates are locked.

Escalate open product forks to O0 (then `/mod-decide`), not to wave peers.

---

## Blocking

### CX-1 — BUILD-unlock gate claimed; combo C+D+B omits the unlock surface

**Conflict type:** phase-boundary leak + mutually exclusive surface assignment

| claim | path |
|---|---|
| Sketch step 3: "mod-decide / charter gate — **block BUILD unlock** when `proof_job` missing on visitor/product lanes" | FR § Feature sketch, item 3 |
| Option E: mod-decide AUTH sync so `proof_job` appears in waveset locks (lean: strong) | FR § Where it lands |
| Recommended combo: **C + D + B** (charter+wiring + playbook/evals + mod-check lens); E not included | FR § Where it lands |
| Option C: harden charter **ACCEPT** template + `EXECUTION_WIRING.md` visual rule | FR § Where it lands |
| mod-decide is the gate between check and BUILD unlock; AUTH-01 syncs locks into `waveset.md` before W2+ | `skills/mod-decide/SKILL.md` workflow steps 5–5b |
| ACCEPT is Wave 4 of a BUILD charter, after unlock and build | `skills/charter/SKILL.md` Wave structure § Wave 4 |

**Why blocking:** "Block BUILD unlock" is a **pre-BUILD / mod-decide** control.
Combo **C** hardens **ACCEPT** (late BUILD). Omitting **E** leaves the
BUILD-unlock claim unwired. A plan that ships C+D+B cannot meet sketch item 3
as stated.

**Resolve (product fork for O0 / mod-decide):** either (1) add **E** to the
required combo and keep the unlock claim, or (2) drop "block BUILD unlock"
and restate the hard bar as ACCEPT-only under C.

---

### CX-2 — Product/UX mandatory fields vs research/check exemption (no type predicate)

**Conflict type:** mutually exclusive requirements + unowned classifier

| claim | path |
|---|---|
| Charter mandatory fields for **every product/UX lane** (`proof_job`, `proof_reference`, `chrome_freeze`, `visual_accept`) | FR § Feature sketch, item 1 |
| Non-goal: do **not** mandate visual gates for pure research/read-only check lanes | FR § Non-goals |
| Charter lane `type` today: **execution vs research/read-only** only | `skills/charter/SKILL.md` waveset sections (~L119) |
| Motivating RFU lane typed `research-discovery` yet ran W2 build + ACCEPT PASS on process/shell criteria | pax `wavves/lanes/20260718_route-first-ux/waveset.md` (type + RFU-ACCEPT) |
| Doctrine accept_bar requires `proof_job_visible` + `visual_screenshot_vs_reference_class` for visitor proof | pax doctrine yaml `binding.accept_bar` |

**Why blocking:** "Product/UX" is not a charter type. Without a predicate
(visitor/product vs research/check vs plugin-meta), **C** either (a) applies
visual/proof fields to research/check lanes and violates the non-goal, or (b)
skips lanes that look like research but ship visitor chrome (RFU-shaped),
recreating `PROC-PASS-NO-PROOF`. The research exemption and the universal
product/UX mandate cannot both be enforced from current type vocabulary.

**Resolve:** lock a lane-class rule (e.g. visitor/product execution lanes
require proof fields; mod-check / research-discovery / plugin-meta exempt)
before BUILD writes the charter template.

---

### CX-3 — Absolute `chrome_freeze` vs delivering `proof_job`

**Conflict type:** mutually exclusive requirements (underspecified freeze)

| claim | path |
|---|---|
| `chrome_freeze`: "what must not change until Proof ACCEPT" | FR § Feature sketch, item 1 |
| Fail id `PROC-CHROME-THRASH`: new IA/chrome wave with no frozen `proof_job` | FR § Default fail vocabulary |
| Doctrine freeze is **selective**: no IA/residual visitor lanes **except those that unblock Proof-1** until Proof-1 ACCEPT with visual evidence | pax doctrine yaml `binding.proof_1.chrome_freeze` |
| Product BUILD waves that close a proof job often must change visitor chrome/IA | RFU W2 IA ship + ACCEPT path (pax RFU waveset) |

**Why blocking:** Read as absolute freeze, `chrome_freeze` forbids the chrome
edits needed to make `proof_job` visible. Doctrine already uses
freeze-except-proof-serving. The FR field does not import that carve-out, so
BUILD agents can treat freeze and proof delivery as exclusive.

**Resolve:** define `chrome_freeze` as freeze of non-proof-serving chrome, with
an allowlist of seams that may change to unblock `proof_job`.

---

## Non-blocking

### CX-4 — Check-lane Next treats C+D+B as starting locks; FR leaves A–E for mod-decide

**Conflict type:** phase-boundary leak (check → decide → BUILD)

| claim | path |
|---|---|
| Options A–E are "for mod-decide" | FR § Where it lands |
| Intake lifecycle: `/mod-check` → `/mod-decide` → `/charter` | `feature-requests/README.md` |
| Check waveset Next: if GO → `/charter` BUILD with C+D+B as **starting locks** | `wavves/lanes/20260718_proof-before-accept-check/waveset.md` § Next |

**Why non-blocking for the FR text itself:** the leak is in the check lane's
Next guidance, not only in the FR. Still unsafe if O0 follows waveset Next
and skips mod-decide while E vs not-E and A deferred remain open (feeds CX-1).

**Resolve:** O0 treat C+D+B as a lean, not a lock, until `/mod-decide` (or
explicit operator paste) closes A–E.

---

### CX-5 — Option B "fifth **default** lens" vs mod-check fifth-lens rule

**Conflict type:** requirement vs current skill contract

| claim | path |
|---|---|
| B: extend mod-check with a fifth **default** lens `proof-bar` | FR § Where it lands |
| Default parallel lenses are four; "Add a fifth lens only when the operator names a domain" | `skills/mod-check/SKILL.md` Default parallel lenses |
| Eval tripwire reads the live "Default parallel lenses" table for keyword survival | `evals/README.md` Known limitation |

**Why non-blocking:** BUILD can amend the skill (that is the point of B), but
the FR must say it **replaces** the "fifth only when operator names domain"
rule for `proof-bar`, and that eval fixtures / repeat-trial convention for
lens-table edits apply. Otherwise implementers keep the old fifth-lens rule
and B never becomes default.

---

### CX-6 — Acceptance §3 softens B; recommended combo includes B

**Conflict type:** internal strength mismatch

| claim | path |
|---|---|
| Acceptance §3: "`mod-check` **(or playbook check)** instructions require hunting process-only ACCEPT criteria" | FR § Acceptance |
| Recommended combo includes **B** (mod-check lens) alongside required **D** (playbook + evals) | FR § Where it lands |

**Why non-blocking:** A BUILD can PASS Acceptance §3 via D alone and skip B,
while the recommended combo presents B as co-equal. Clarify whether B is
required for FR ACCEPT or only recommended.

---

### CX-7 — `PROC-BLANK-CANVAS` map-host rule vs general wavves landing + klosr non-goal

**Conflict type:** domain leak into general method

| claim | path |
|---|---|
| Fail vocab / wiring: map host height 0 / blank black-canvas class | FR § Default fail vocabulary; Feature sketch item 4 |
| Product surface: wavves skills / charter ACCEPT / playbooks + evals | FR header |
| Non-goal: not implementing klosr Proof-1 inside wavves_build | FR § Non-goals |
| Doctrine evidence includes blank-map hotfix klosr `c76e19b` | pax doctrine yaml `evidence.blank_map_hotfix` |

**Why non-blocking:** Motivating evidence is map-specific; generalizing the
fail id is fine if scoped as an **example class** (product host empty while
chrome PASS), not as a hard map-height rule in every wavves ACCEPT. As written,
EXECUTION_WIRING addition can overfit klosr.

---

### CX-8 — Escape hatches (`proof_reference: none`, `visual_accept: no`) vs `PROC-PASS-NO-PROOF`

**Conflict type:** fail mode vs allowed field values

| claim | path |
|---|---|
| `proof_reference` may be `none` with rationale; `visual_accept` yes/no | FR § Feature sketch, item 1 |
| `PROC-PASS-NO-PROOF`: ACCEPT/check greens without measuring `proof_job` | FR § Default fail vocabulary |
| Doctrine: visual screenshot vs reference class is **required** on accept_bar | pax doctrine yaml `binding.accept_bar.required` |

**Why non-blocking:** Escape hatches are needed for non-visual lanes, but
without a hard rule that visitor/product lanes cannot use `none`/`no` to skip
measurement, the fail id is advisory. Tie escapes to the lane-class predicate
from CX-2.

---

### CX-9 — FR status string vs feature-requests lifecycle enum

**Conflict type:** metadata inconsistency (docs only)

| claim | path |
|---|---|
| FR status: `in-mod-check` | FR header |
| Lifecycle enum: `draft` → `ready-for-mod-check` → `chartered` → `shipped` / `wontfix` | `feature-requests/README.md` |

**Why non-blocking:** does not affect BUILD correctness. Align status token
when O0 next edits the FR.

---

## Combo C+D+B stress (summary)

| piece | phase | conflict with |
|---|---|---|
| **C** charter ACCEPT + EXECUTION_WIRING visual rule | BUILD ACCEPT | Sketch "block BUILD unlock"; research exemption without predicate; map-specific blank-canvas |
| **D** playbook + evals | docs / check tripwire | Acceptance §3 can satisfy without B |
| **B** mod-check `proof-bar` default lens | pre-BUILD check | Current "fifth lens only if operator names domain"; not an ACCEPT harness |
| **E** (omitted) mod-decide AUTH sync | BUILD unlock | Sketch item 3 claims this job |

C+D+B is coherent only if sketch item 3 is rewritten to ACCEPT-time under C,
lane class is locked (CX-2), and `chrome_freeze` is selective (CX-3).
Otherwise the combo and the sketch disagree.

---

## Out of scope for this lens

- Grounding of pax paths / commit hashes (PBA-W1a)
- Missing acceptance edges / rollback (PBA-W1c)
- Failure-mode inventiveness beyond internal conflict (PBA-W1d)
- Implementation plan or skill patches

## Escalation

To **O0 only.** Recommended: open mod-decide queue for CX-1 (include E or
drop unlock claim), CX-2 (lane-class predicate), CX-3 (`chrome_freeze`
carve-out). Non-blocking CX-4–CX-9 can ride in the same packet.

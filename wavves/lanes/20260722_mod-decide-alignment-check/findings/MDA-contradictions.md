# MDA-W1b — contradictions lens

- **Artifact:** `feature-requests/20260722_mod-decide-decision-alignment.md`
- **Repo pin:** `26ad2d2afbb9196f2b690000f6a50f1cabfe20e5`
- **Hydrated:** artifact; `skills/mod-decide/SKILL.md`;
  `skills/wavves/playbooks/decide.md`; `examples/usage.md` (decide /
  From check to BUILD); waveset Locked; `feature-requests/README.md`
- **Lens:** internal conflicts, phase-boundary leaks, mutually exclusive
  requirements
- **Git:** none. Commits: none.

## CX-* conflicts

### CX-01 — Grain invent vs "do not invent forks"

| | |
|---|---|
| **Claim A** | Live mod-decide Workflow step 3 / Non-negotiable spirit: build queue from named open calls; do not invent forks the check did not surface unless the operator adds them. |
| **Claim B path** | FR DA-03: if operator intent names successor coverage, default option set **must include** that BUILD path as a first-class pick even when the presented set is only hold/eval/train N. |
| **Conflict** | Alignment feature requires inventing a coverage-BUILD option the check queue omitted. Faithful BUILD of DA-03 violates today's invent ban unless the FR patches that non-negotiable. |
| **Severity** | high |
| **Lean** | REVISE — state override: grain check may add one operator-intent-aligned pick, cite charter/waveset/prior lock; or require operator to add the fork before decide presents it. |

### CX-02 — Ban lean Hold-no-exit vs operator may pick Hold

| | |
|---|---|
| **Claim A** | DA-01: Ban leans that are hold-with-no-exit. Fail id `PROC-DECIDE-HOLD-NO-EXIT` on recommend/lean Hold without exit. |
| **Claim B path** | Risks: "Operator may still pick hold — allowed if exit_criteria named." Non-negotiable today: wait for operator pick (any letter). |
| **Conflict** | Mostly consistent if ban applies only to **lean/recommend**, not to operator pick. FR never says whether presenting Hold without exit_criteria is also banned, or only leaning it. Agents can still **surface** Hold-no-exit as option A and omit lean. |
| **Severity** | medium |
| **Lean** | REVISE — lock: every hold/ban/pause **option** requires exit_criteria; lean ban is additional. Operator pick of Hold still needs named exit on the written option. |

### CX-03 — Program alignment "before first call" vs one-call presentation

| | |
|---|---|
| **Claim A** | DA-02: Program alignment stanza **before the first call**; each option tags aligns/defers/conflicts. |
| **Claim B path** | Non-negotiable 1 + usage paste: for each call, options one line each, optional lean, wait. DA-05 adds `program_intent` on Locked draft; option D adds operator-facing "alignment card" in Locked paste. |
| **Conflict** | Three surfaces (pre-call stanza, Locked draft fields, Locked paste card) without authority order. BUILD can implement one and claim DA-02/DA-05/D done while the others stay empty. |
| **Severity** | medium |
| **Lean** | REVISE — one authority: stanza once per decide session; per-option tags on each call; Locked paste carries `program_intent` summary; option D is that paste block or is dropped. |

### CX-04 — Lean prefer-aligns vs operator authority / hygiene hold

| | |
|---|---|
| **Claim A** | DA-04: prefer options that `aligns` when hygiene exits already exist; hygiene lean to hold only with exit **and** explicit "defers standing intent." |
| **Claim B path** | Skill: optional recommendation then wait; judgment calls belong to the operator (`wavves/AGENTS.md`). |
| **Conflict** | "Prefer" can be read as auto-pick or as lean-only. If BUILD hardens prefer into default pick without wait, it breaks one-at-a-time operator gate. |
| **Severity** | low–medium |
| **Lean** | REVISE — prefer = lean text rule only; never auto-lock. |

### CX-05 — Where-it-lands B required vs D strong companion vs Operator Accept

| | |
|---|---|
| **Claim A** | Where it lands: B = patch skill + playbook + evals is **required**; D = alignment card **strong companion to B**. |
| **Claim B path** | Operator decision: Accept / revise / reject, then mod-check before BUILD. Status already `ready-for-mod-check`. |
| **Conflict** | Product lean B is written as settled requirement while Operator decision and lifecycle still treat scope (A/B/C/D) as open. Phase leak: BUILD charter may skip `/mod-decide` on landing shape because FR already says B required. |
| **Severity** | medium (phase-boundary) |
| **Lean** | REVISE — mark B/D as FR author lean for mod-decide, not Locked; or move landing shape into explicit open calls. |

### CX-06 — DA-07 Midtown/IWD fixtures vs generic grain labels

| | |
|---|---|
| **Claim A** | Risks: keep grain labels generic (fixtures-rail / coverage-build / claim-surface / park). |
| **Claim B path** | DA-03 / DA-07 prose: "supersede Midtown N", "coverage BUILD", IWD admit vocabulary in fail fixtures. |
| **Conflict** | Eval acceptance tied to Midtown/IWD nouns fights the anti-overfit risk. Consumer repos without Midtown will not remasure those fixtures as written. |
| **Severity** | medium |
| **Lean** | REVISE — fixtures use generic standing-intent strings; IWD names stay in FR Originating evidence only. |

### CX-07 — Anti-loop "must not re-open hygiene" vs decide queue from check open calls

| | |
|---|---|
| **Claim A** | DA-06: after check/wire PASS, admit/build-scope decide must not re-open hygiene. |
| **Claim B path** | Workflow: queue from named open calls in the check return. A check that still lists hygiene as an open call would force re-open. |
| **Conflict** | Unowned: does DA-06 override a check-named hygiene call, park it, or fail the decide session? |
| **Severity** | medium |
| **Lean** | REVISE — if wire/check PASS is in Grounding, hygiene calls are parked with exit cite, not re-walked as product forks. |

### CX-08 — Locked paste "do NOT reopen" vs new interpretability fields

| | |
|---|---|
| **Claim A** | Current Locked paste header: picks only; BUILD must not reopen. |
| **Claim B path** | DA-05: add `program_intent` + per-pick `unlocks_next` to draft (and D's card). |
| **Conflict** | Not fatal, but paste consumers (`/charter`, AUTH-01 sync) have no schema for the new fields. Proof fields (PBA-LAND E) already overload the same paste. Unspecified merge can drop proof fields or drop alignment fields. |
| **Severity** | medium |
| **Lean** | REVISE — extend Locked paste schema explicitly; AUTH-01 sync checklist names the new keys. |

## Lens verdict

**REVISE** (not BLOCK, not GO).

Core problem (hold-without-exit, grain mismatch) is coherent. Blocking for
faithful BUILD if unaddressed: CX-01 (invent vs grain), CX-03 (triple
alignment surface), CX-08 (Locked paste / AUTH sync schema). Must-clear in
FR or `/mod-decide`: CX-02, CX-05, CX-06, CX-07. CX-04 is wording.

## Commit file list (findings only; no git)

- `wavves/lanes/20260722_mod-decide-alignment-check/findings/MDA-contradictions.md`

## Escalation

O0 only. No operator solicit.

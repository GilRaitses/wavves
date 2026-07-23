# PUO-W1a — grounding

```text
lens: grounding
wave_id: PUO-W1a
model: cursor-grok-4.5-high-fast
artifact: feature-requests/20260720_pre-unlock-options-mod-check.md
artifact_sha256: 70802628e1981abf0638d8e202d7ae5c8f09f40d188e852328e813af238205c5
artifact_bytes_lines: 4870 bytes / 98 lines
check_repo_state_verified_against: 26ad2d2afbb9196f2b690000f6a50f1cabfe20e5
verdict_lean: REVISE
escalation: O0 only
git: none performed
```

## Verdict lean (this lens)

**REVISE.** In-repo product seams match the FR problem: AUTH-05 is
mod-decide sync only, and `proceed` has no unlock-options → check route.
Foreign pax RLW/RWC paths remasure as originating illustration and support
the failure story. The FR tip pin `pax 07c00007f` does not remasure on disk
text, and several evidence cites are lane-relative without home prefixes.
Fix those pins before BUILD treats originating evidence as closed.

Foreign pax paths are illustration only (dispatch rule). They are not a
grounding BLOCK for in-repo BUILD targets.

## Claims vs evidence

| claim (FR / waveset) | evidence_path | match |
|---|---|---|
| Artifact exists; status `ready-for-mod-check` | `feature-requests/20260720_pre-unlock-options-mod-check.md` | yes |
| FR indexed at same status | `feature-requests/README.md` (FR-20260720-pre-unlock-options-mod-check row) | yes |
| INDEX + registry list PUO check lane at pin `26ad2d2a…` | `wavves/INDEX.md`; `wavves/registry.yml` (PUO); lane `waveset.md` / `README.md` / `dispatch.md` | yes |
| Today AUTH-05 gates W2+ after mod-decide when waveset older than newest decisions | `skills/mod-check/SKILL.md` §Mandatory gate before W2+ (AUTH-05) | yes |
| AUTH-05 is not an options-unlock / pre-unlock mod-check gate | same; no `pre_unlock` / unlock-options language in AUTH-05 | yes |
| `proceed` executes AUTH-10 actions; AUTH-05 only on dispatch; no unlock-options → check first | `skills/wavves/playbooks/proceed.md` steps 1–3 | yes |
| `check` playbook is generic mod-check; no unlock-options trigger | `skills/wavves/playbooks/check.md` | yes |
| `mod-check` When-to-use omits reconcile→unlock-options cue | `skills/mod-check/SKILL.md` §When to use | yes |
| AUTH-04 scoped `blocks_w2`…`blocks_w5` exists (FR AUTH-11c extends use) | `skills/mod-check/SKILL.md` §Scoped verdict schema | yes |
| Charter has no `pre_unlock_mod_check` / options-memo unlock gate | `skills/charter/SKILL.md` (grep: no `pre_unlock`, no options-unlock gate) | yes (absent = gap FR proposes to close) |
| Target playbook `charter-lane.md` exists | `skills/wavves/playbooks/charter-lane.md` | yes |
| `examples/usage.md` has "From check to BUILD" (FR wants reconcile→check→unlock path) | `examples/usage.md` | yes (section exists; unlock-options path not present) |
| Registry optional fields today lack `pre_unlock_*` / `options_wave_id` | `wavves/registry.yml`; `skills/charter/SKILL.md` registry optional fields list | yes (absent) |
| Registry statuses include `check-revise`, `mod-decide-complete*`, not `verdict-go` / `verdict-revise-applied` | `wavves/registry.yml` status values | yes (proposed strings absent) |
| Fail id `PROC-UNLOCK-NO-CHECK` proposed only | `wavves/failure_log.yml` (empty list `[]`) | n/a (proposed) |
| Eval home available for option D | `evals/README.md`, `evals/fixtures/`, `evals/run_fixtures.py` | yes (pattern; no PUO fixture yet) |
| RWC verdict REVISE + `blocks_w2: true` + B1–B5 | foreign `…/20260720_rlw-charter-mod-check/findings/RWC-verdict.md` | yes (illustration) |
| Options unlock memo after REVISE; not DECIDE/BUILD | foreign `…/20260720_rl-win-track/decisions/RLW-W2-OPTIONS-UNLOCK.md` | yes (illustration) |
| W2 gate `PASS_WITH_GAPS`; DECIDE/BUILD still false | foreign `…/20260720_rl-win-track/gate-captures/RLW-W2.json` | yes (illustration) |
| W1 reconcile recommended bare `unlock W2` | foreign `RLW-W1-RECONCILE.md` now says `unlock W2 options memo under entry conditions`; bare wording attested by OPTIONS-UNLOCK `supersedes:` line | partial (historical; see G2) |
| `evidence_verified_against: pax 07c00007f` | string only in this FR under wavves_build; not cited in pax lane docs opened for this check | **no** |

## Named gaps

### GAP-PUO-G1 — FR tip pin `07c00007f` does not remasure

- **severity:** REVISE (evidence honesty)
- **claim:** `evidence_verified_against: pax 07c00007f tip at FR authoring`
- **evidence_path:** `feature-requests/20260720_pre-unlock-options-mod-check.md` (lines 15–16);
  foreign RLW/RWC artifacts cite other hashes (`53d3ff6f…`, `fca01e31…`,
  `57f94a25…`) not `07c00007f`
- **note:** Git not run (dispatch ban). O0 should replace or drop the pin so
  originating evidence matches remasureable disk.

### GAP-PUO-G2 — "Bare unlock W2" is historical, not current RECONCILE text

- **severity:** note (precision; non-blocking if labeled historical)
- **claim:** RLW W1 reconcile recommended bare `unlock W2`
- **evidence_path:** foreign `…/rl-win-track/findings/RLW-W1-RECONCILE.md`
  (`recommended_next_for_O0: unlock W2 options memo under entry conditions`);
  foreign `…/decisions/RLW-W2-OPTIONS-UNLOCK.md` (`supersedes: bare "unlock W2"
  wording in RLW-W1-RECONCILE (pre-RWC revise)`)
- **note:** Problem list is still load-bearing. Cite the supersedes line (or
  a frozen pre-revise excerpt) so BUILD does not hunt a bare string on tip.

### GAP-PUO-G3 — Lane-relative foreign cites without home prefixes

- **severity:** note
- **claim / pointers:** `findings/RWC-verdict.md`,
  `decisions/RLW-W2-OPTIONS-UNLOCK.md`, `gate-captures/RLW-W2.json`
- **evidence_path:** FR Source evidence list; actual homes are RWC for
  verdict and RLW for unlock + gate JSON
- **note:** Illustration-only. Prefer full foreign paths or explicit
  `(RWC)` / `(RLW)` prefixes so readers do not invent a single home.

### GAP-PUO-G4 — Proposed registry status strings not on live schema

- **severity:** note (forward-looking; completeness owns the schema hole)
- **claim:** proceed clears on sibling check `verdict-go` /
  `verdict-revise-applied`
- **evidence_path:** FR AUTH-11d; live `wavves/registry.yml` statuses
  (`chartered`, `check-revise`, `mod-decide-complete-awaiting-build`,
  `completed`, …)
- **note:** Grounding confirms absence. BUILD must define the status
  vocabulary; do not assume those strings already mean something.

## What is already sound

- Gap vs AUTH-05 / proceed is real on live plugin files.
- Option A lean (extend AUTH-05 only) matches wrong-trigger reading of
  AUTH-05 text.
- AUTH-11 target surfaces exist: `skills/charter/SKILL.md`,
  `skills/mod-check/SKILL.md`, `skills/wavves/playbooks/proceed.md`,
  `skills/wavves/playbooks/check.md`, `skills/wavves/playbooks/charter-lane.md`,
  `examples/usage.md`, `wavves/registry.yml`.
- Foreign RWC→options-unlock sequence remasures for illustration.

## Commit file list (orchestrator)

- `wavves/lanes/20260723_pre-unlock-options-check/findings/PUO-grounding.md`

No git actions performed.

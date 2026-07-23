# PAS-W1a — grounding

```text
lens: grounding
wave_id: PAS-W1a
model: cursor-grok-4.5-high-fast
artifact: feature-requests/20260723_proceed-all-standing.md
artifact_sha256: ea8d3e59ee6ff897ceb57c4797963a8b77cea7800120bbd605125e1fb9ea57f2
artifact_bytes_lines: 100
check_repo_state_verified_against: 73b09bad223ed004a2e8f10443f48196cbbbf396
verdict_lean: REVISE
escalation: O0 only
git: none performed
```

## Verdict lean (this lens)

**REVISE.** Core product-surface claims match the live proceed / wavves seams.
One FR evidence pin (`wavves fd12cb8` for set-key docs handoff) does not
remasure against the sibling handoff’s own recorded hashes. Fix that pin
(or drop it) before BUILD charter treats originating evidence as closed.

Foreign pax/klosr/IWD paths are originating-session illustration only; BUILD
acceptance targets in-repo inventory surfaces and fixtures, so those foreign
paths are not a grounding BLOCK.

## Claims vs evidence

| claim (FR / waveset) | evidence_path | match |
|---|---|---|
| Artifact path `feature-requests/20260723_proceed-all-standing.md` exists; status `ready-for-mod-check` | `feature-requests/20260723_proceed-all-standing.md` | yes |
| FR indexed in feature-requests README at same status | `feature-requests/README.md` (FR-20260723-proceed-all-standing row) | yes |
| INDEX lists FR + PAS check lane | `wavves/INDEX.md` (`feature_requests.open`, `active_lanes` PAS) | yes |
| Check lane `repo_state_verified_against` / landing hash `73b09bad…` consistent across lane docs + registry | `wavves/lanes/20260723_proceed-all-standing-check/waveset.md`, `README.md`, `dispatch.md`; `wavves/registry.yml` (PAS) | yes |
| Today `/wavves proceed` executes ordered `recommended_actions` only (no all-standing mode) | `skills/wavves/playbooks/proceed.md` | yes |
| Bare shrug alias = proceed as recommended (AUTH-10 sequence), not all-standing | `skills/wavves/playbooks/proceed.md` (trigger language) | yes |
| wavves router has proceed playbook row; no proceed-all-standing route yet | `skills/wavves/SKILL.md` (Routing table + playbook list) | yes |
| pickup playbook is hydrate/resume, not standing-queue execute | `skills/wavves/playbooks/pickup.md` | yes (no FR false claim) |
| Sibling set-key docs handoff present; names this FR as separate | `wavves/handoffs/20260723_set-key_docs_version_bump.md` | yes |
| Evidence table pin wavves `17539cb` for `/set-key` skill land | handoff `repo_state_verified_against` / “Skill code … at `17539cb`” | yes (prefix match of full `17539cb913c…`) |
| `evidence_verified_against` wavves `fd12cb8` (set-key docs handoff) | handoff cites handoff land `e437b9b` and feature `17539cb`; string `fd12cb8` absent elsewhere under wavves_build (grep) | **no** |
| PS-03 inventory source `registry.yml` + `active_dispatch` exist as house surfaces | `wavves/registry.yml` (field `active_dispatch` present) | yes (path shorthand; see gap) |
| Proposed persist path `wavves/standing/<…>.md` | directory `wavves/standing/` | n/a (proposed; absent today) |
| Proposed fail ids `PROC-PROCEED-*` | `wavves/failure_log.yml` (empty list) | n/a (proposed) |
| Eval/fixture acceptance pattern available in-repo | `evals/README.md` + `evals/fixtures/` | yes |
| pax `4a7d6c91d`, pax `.cursor/rules/shrug-means-proceed.mdc`, `dispatch-w27.md`, `findings/IWD-V3-TRAIN-BUSY-OPERATOR-GATE.md`, klosr remasure | foreign / originating illustration (dispatch: do not require under wavves_build) | n/a (illustration) |

## Named gaps

### GAP-PAS-G1 — FR evidence pin `fd12cb8` does not remasure

- **severity:** REVISE (evidence honesty)
- **claim:** `evidence_verified_against: … wavves fd12cb8 (set-key docs handoff)`
- **evidence_path:** `feature-requests/20260723_proceed-all-standing.md` (lines 18–19);
  `wavves/handoffs/20260723_set-key_docs_version_bump.md` (header
  `repo_state_verified_against: 17539cb9…`; paste “handoff land e437b9b;
  feature code 17539cb”)
- **note:** No in-repo text cites `fd12cb8`. Sibling handoff’s remasureable
  pins are `17539cb` (feature) and `e437b9b` (handoff land). Git not run
  (dispatch ban); cannot resolve short hash via history. O0 should replace
  or drop `fd12cb8` so originating evidence matches disk.

### GAP-PAS-G2 — PS-03 `registry.yml` path shorthand

- **severity:** note (precision; non-blocking if BUILD scopes to wavves home)
- **claim:** inventory remasures `registry.yml` status + `active_dispatch`
- **evidence_path:** `feature-requests/20260723_proceed-all-standing.md` (PS-03);
  live file `wavves/registry.yml`
- **note:** Repo-root relative path is `wavves/registry.yml`. Skill-relative
  `playbooks/proceed.md` cite is acceptable from the wavves skill tree
  (`skills/wavves/playbooks/proceed.md` exists).

### GAP-PAS-G3 — Foreign evidence paths (illustration; not BUILD hard-dep)

- **severity:** note
- **claim / pointers:** pax shrug rule; `dispatch-w27.md`;
  `findings/IWD-V3-TRAIN-BUSY-OPERATOR-GATE.md`; pax/klosr pins
- **evidence_path:** FR Source evidence + Evidence pointers table;
  dispatch hydrate rule (foreign pins not required for PASS)
- **note:** BUILD sketch targets `skills/wavves/playbooks/proceed.md`,
  optional leaf, `wavves/standing/` or lane `standing.md`, and evals
  fixtures for class behavior. Acceptance does not require those foreign
  files to exist under wavves_build. Flag only: do not charter BUILD steps
  that open pax/klosr paths as mandatory remasure.

## Hydration opened (must-cite list)

| path | opened |
|---|---|
| `feature-requests/20260723_proceed-all-standing.md` | yes |
| `wavves/lanes/20260723_proceed-all-standing-check/waveset.md` | yes |
| `wavves/lanes/20260723_proceed-all-standing-check/dispatch.md` | yes |
| `skills/wavves/playbooks/proceed.md` | yes |
| `skills/wavves/SKILL.md` | yes |
| `skills/wavves/playbooks/pickup.md` | yes |
| `feature-requests/README.md` | yes |
| `wavves/handoffs/20260723_set-key_docs_version_bump.md` | yes |
| `evals/README.md` (fixture pattern) | yes |

## Commit file list

- This findings file only:
  `wavves/lanes/20260723_proceed-all-standing-check/findings/PAS-grounding.md`
- No git performed (status / add / commit / push none).

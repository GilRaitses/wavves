# WOF-W1a — grounding

```text
lens: grounding
wave_id: WOF-W1a
model: cursor-grok-4.5-high-fast
artifact: feature-requests/20260723_wave-orchestrator-fanout.md
artifact_sha256: a06e0436c637431e5cd67d86e5056d5ef2ce52427bc2efd644affdb0f91c1d31
artifact_bytes_lines: 7429 bytes / 119 lines
check_repo_state_verified_against: 26ad2d2afbb9196f2b690000f6a50f1cabfe20e5
verdict_lean: REVISE
escalation: O0 only
git: none performed
```

## Verdict lean (this lens)

**REVISE.** Problem claims about O0 background / no-poll and thin wave-subagent
wording remasure against live charter, wavves-init Roles, README, and set-key
densify note. Sketch row OF-01 names the wrong primary seams for the existing
three-roles definition (`skills/wavves/SKILL.md` + "README Roles"); those
tables live in `skills/charter/SKILL.md` and the wavves-init `AGENTS.md`
template. Fix the target list before BUILD charter treats OF-01 as closed.

Foreign pax IWD paths are illustration only; not a grounding BLOCK.

## Claims vs evidence

| claim (FR / waveset) | evidence_path | match |
|---|---|---|
| Artifact path exists; status `ready-for-mod-check` | `feature-requests/20260723_wave-orchestrator-fanout.md` | yes |
| FR indexed at same status | `feature-requests/README.md` (FR-20260723-wave-orchestrator-fanout) | yes |
| INDEX lists FR + WOF check lane | `wavves/INDEX.md` (`feature_requests.open`, `active_lanes` WOF) | yes |
| Check pin `26ad2d2…` consistent across lane docs + registry | `waveset.md`, `README.md`, `dispatch.md`; `wavves/registry.yml` (WOF) | yes (stated; git not remasured) |
| O0 dispatches background; never blocks polling | `skills/charter/SKILL.md` (roles + Dispatch mechanics); `skills/wavves-init/SKILL.md` Roles; `wavves/AGENTS.md`; playbooks `charter-lane.md` / `proceed.md` / `check.md` | yes |
| Dispatches label paste target as orchestrator | `skills/charter/SKILL.md` (dispatch declares "this lane's orchestrator") | yes |
| `AGENTS.md` mentions wave subagents one bounded disjoint task | `wavves/AGENTS.md`; `skills/wavves-init/SKILL.md` §2 (near-exact wording) | yes |
| Three roles already defined (collapse risk) | charter table: O0 / Dispatched orchestrator / Parallel subagents; init+home: O0 / Dispatched orchestrators/runners / Wave subagents | yes (vocab ≠ FR's wave orchestrator / charge worker) |
| `/wavves` SKILL alone states the three roles | `skills/wavves/SKILL.md` | **no** (router only; no Roles block) |
| README has a "Roles" section naming the triad | `README.md` ("What wavves tracks": Moderator/O0 only) | **no** (heading/triad absent) |
| Older etiquette: orchestrator owns completion / mid-dispatch empty return | `feature-requests/20260718_proof-before-accept_ORIGINATING-MOD-FEEDBACK.md` (§ Discovery notes); also `wavves/lanes/20260718_proof-host-followon/decisions/PHF-ETIQUETTE.md` | yes (source phrasing differs slightly; see gap) |
| densify/set-key aside for background follow-ups | `skills/set-key/SKILL.md` step 10 | yes |
| Proceed/charter playbooks already say dispatch background + do not poll | `skills/wavves/playbooks/charter-lane.md` step 6; `proceed.md` step 3 | yes (OF-09 additive line still open) |
| Proposed fail ids `PROC-ORCH-*` / `PROC-MOD-FOREGROUND-HOLD` | `wavves/failure_log.yml` (`[]`); no matching `evals/fixtures/` | n/a (proposed) |
| Eval/fixture pattern available for OF-07 | `evals/README.md` + `evals/fixtures/` | yes |
| OF-05 default `role: wave_orchestrator` paste in plugin | in-repo dispatch templates under `skills/` | n/a (proposed; pax illustration only) |
| Lane bind / W29 role / early exit | pax `OPERATOR_ORCHESTRATION.md`, `dispatch-w29.md` (`role: wave_orchestrator`; critical path a→(b‖c)→d) | n/a (illustration; files exist under pax, not required here) |
| `evidence_verified_against` pax `20782d2d7` | foreign pin; not remasured under wavves_build | n/a (illustration) |

## Named gaps

### GAP-WOF-G1 — OF-01 primary targets miss the live three-roles seams

- **severity:** REVISE (wrong / incomplete paths)
- **claim:** OF-01 targets `skills/wavves/SKILL.md` + README Roles for O0 /
  wave orchestrator / charge worker
- **evidence_path:** FR sketch OF-01; live roles in `skills/charter/SKILL.md`
  ("The three roles"); `skills/wavves-init/SKILL.md` §2; `wavves/AGENTS.md` §2;
  `skills/wavves/SKILL.md` (no Roles); `README.md` (no "Roles" heading; O0 row
  only under "What wavves tracks")
- **note:** OF-05/OF-06/OF-08 partially cover charter/init/AGENTS, but OF-01 as
  written would let a BUILD agent skip the authoritative charter Roles table.
  Rename or expand targets: charter SKILL + wavves-init AGENTS template +
  README tracking table (+ optional router mention). Keep vocabulary rename
  (Dispatched orchestrator / Wave subagents → wave orchestrator / charge
  worker) explicit so portable homes do not keep two triads.

### GAP-WOF-G2 — Mid-dispatch etiquette paraphrase vs source wording

- **severity:** note (precision; non-blocking if BUILD cites the source file)
- **claim:** Older etiquette “orchestrator owns completion; no empty
  mid-dispatch return”
- **evidence_path:** `feature-requests/20260718_proof-before-accept_ORIGINATING-MOD-FEEDBACK.md`
  lines 101–104 ("Mid-dispatch empty returns… orchestrator owns completion;
  no return until RECONCILE+GATE")
- **note:** Intent matches. Acceptance item that resolves the wording conflict
  should quote the source phrase, not only the FR paraphrase.

### GAP-WOF-G3 — Foreign pax evidence (illustration; not BUILD hard-dep)

- **severity:** note
- **claim / pointers:** pax IWD `OPERATOR_ORCHESTRATION.md`, `dispatch-w29.md`,
  pin `20782d2d7`, W29a-only early exit narrative
- **evidence_path:** FR Source evidence + Evidence pointers; dispatch hydrate
  rule (foreign pins not required under wavves_build)
- **note:** Spot-check outside repo confirms path shape and
  `role: wave_orchestrator` on pax disk. BUILD acceptance must target in-repo
  skills/playbooks/AGENTS/evals, not mandatory opens of pax paths. Acceptance
  line "pax home synced when shipped" stays a ship-time operator action, not a
  wavves_build remasure gate.

### GAP-WOF-G4 — Landing pin not remasured under GIT BAN

- **severity:** note
- **claim:** `landing_commit_hash` / `repo_state_verified_against`
  `26ad2d2afbb9196f2b690000f6a50f1cabfe20e5`
- **evidence_path:** lane `waveset.md` / `README.md` / `dispatch.md`;
  `wavves/registry.yml` WOF row
- **note:** Pins are internally consistent. This lens did not run git; O0 may
  remasure HEAD if needed before verdict land.

## Hydration opened (must-cite list)

| path | opened |
|---|---|
| `feature-requests/20260723_wave-orchestrator-fanout.md` | yes |
| `wavves/lanes/20260723_wave-orchestrator-fanout-check/waveset.md` | yes |
| `wavves/lanes/20260723_wave-orchestrator-fanout-check/dispatch.md` | yes |
| `skills/wavves/SKILL.md` | yes |
| `skills/charter/SKILL.md` | yes |
| `skills/wavves/playbooks/charter-lane.md` | yes |
| `skills/wavves/playbooks/proceed.md` | yes |
| `skills/wavves-init/SKILL.md` | yes |
| `README.md` | yes |
| `feature-requests/README.md` | yes |
| `feature-requests/20260718_proof-before-accept_ORIGINATING-MOD-FEEDBACK.md` | yes |
| `skills/set-key/SKILL.md` (densify aside) | yes |
| `wavves/AGENTS.md` | yes |

## Commit file list

- This findings file only:
  `wavves/lanes/20260723_wave-orchestrator-fanout-check/findings/WOF-grounding.md`
- No git performed (status / add / commit / push none).

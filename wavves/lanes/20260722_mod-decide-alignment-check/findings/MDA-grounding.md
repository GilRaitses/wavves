# MDA-W1a — grounding

```text
lens: grounding
wave_id: MDA-W1a
model: cursor-grok-4.5-high-fast
artifact: feature-requests/20260722_mod-decide-decision-alignment.md
artifact_sha256: 8a37545fa29d74fdb80a643cc03fff6254c7d9e536a5ab8757b49995853e8bd0
artifact_bytes_lines: 5301 bytes / 93 lines
check_repo_state_verified_against: 26ad2d2afbb9196f2b690000f6a50f1cabfe20e5
verdict_lean: GO
escalation: O0 only
git: none performed
```

## Verdict lean (this lens)

**GO.** Product-surface claims match live `mod-decide` seams in this repo:
optional lean, no exit criteria, no program-alignment stanza, no grain
check, Locked paste without `program_intent` / `unlocks_next`. FR index,
lane pin, and hydrate targets remasure. Foreign pax IWD paths are
illustration only; they remasure under pax at the cited hash and are not
BUILD hard-deps for wavves_build.

## Claims vs evidence

| claim (FR / waveset) | evidence_path | match |
|---|---|---|
| Artifact exists; status `ready-for-mod-check` | `feature-requests/20260722_mod-decide-decision-alignment.md` | yes |
| FR indexed at same status | `feature-requests/README.md` (FR-20260722-mod-decide-decision-alignment row) | yes |
| Check lane pin `26ad2d2…` across lane docs + registry | `waveset.md`, `README.md`, `dispatch.md`; `wavves/registry.yml` (MDA) | yes |
| INDEX lists MDA active lane | `wavves/INDEX.md` (`active_lanes` MDA) | yes |
| Today mod-decide: options one line each, optional lean/recommendation, wait | `skills/mod-decide/SKILL.md` Non-negotiables §1; Workflow step 4 | yes |
| No required exit / unlock line for hold/ban/pause | full `skills/mod-decide/SKILL.md` (absent) | yes (gap is real) |
| No Program alignment stanza / `aligns\|defers\|conflicts` tags | same | yes (gap is real) |
| No grain check (fixtures-rail / coverage-build / claim-surface) | same | yes (gap is real) |
| Locked paste = pick lines + Grounding only; no `program_intent` / `unlocks_next` | `skills/mod-decide/SKILL.md` Locked decisions paste | yes |
| Decision record shape lacks those fields | `skills/mod-decide/SKILL.md` Decision record shape | yes |
| Decide playbook: walk picks, AUTH sync, no anti-loop after wire/check PASS | `skills/wavves/playbooks/decide.md` | yes |
| `examples/usage.md` From check to BUILD: decide locks, no hygiene-anti-loop | `examples/usage.md` §From check to BUILD | yes |
| Proposed fail ids not in failure_log yet | `wavves/failure_log.yml` (`[]`) | n/a (proposed) |
| Eval fixture pattern exists in-repo | `evals/README.md` + `evals/fixtures/` | yes (homes for DECIDE-ALIGN unnamed) |
| IWD-D5 pick D full admit; IWD-D6 pick B coverage BUILD; TRAIN-WIRE PASS; pin `2c04e8b…` | foreign pax (illustration): `…/decisions/IWD-D5-…`, `IWD-D6-…`, `findings/IWD-W2R-TRAIN-WIRE.md`; pax commit `2c04e8b27` | yes (illustration) |
| Those IWD paths under wavves_build | local `wavves/lanes/20260722_island-wide-discovery/` | **no** (expected; foreign) |

## Named gaps

### GAP-MDA-G1 — Source evidence omits foreign repo root (note)

- **severity:** note (illustration hygiene; non-blocking per dispatch)
- **claim:** Source evidence lists
  `wavves/lanes/20260722_island-wide-discovery/findings/IWD-W2R-TRAIN-WIRE.md`
  and `decisions/IWD-D5-…` / `IWD-D6-…` without a pax root prefix
- **evidence_path:** FR lines 7–15; absent under wavves_build; present under
  pax lane home; `evidence_verified_against` pax `2c04e8b273f6e949a0774d514a97de81f40b3105`
  remasures as TRAIN-WIRE land commit
- **note:** Dispatch: foreign pax illustration only. BUILD acceptance must
  not require those paths under wavves_build. Optional FR tidy: prefix
  `pax:` (or absolute root) on each citation.

### GAP-MDA-G2 — Eval target named only as "evals" (note)

- **severity:** note (completeness owns detail)
- **claim:** DA-07 "evals" fixtures for two fail ids
- **evidence_path:** FR DA-07; live `evals/` has
  `run_fixtures.py`, `check_paragraph_tunnel.py`,
  `check_proof_before_accept.py`; no decide-alignment prefix
- **note:** Grounding confirms the parent `evals/` surface exists. Fixture
  home / checker choice is a completeness/decide call, not a false path.

## Hydration opened (must-cite list)

| path | opened |
|---|---|
| `feature-requests/20260722_mod-decide-decision-alignment.md` | yes |
| `wavves/lanes/20260722_mod-decide-alignment-check/waveset.md` | yes |
| `wavves/lanes/20260722_mod-decide-alignment-check/dispatch.md` | yes |
| `skills/mod-decide/SKILL.md` | yes |
| `skills/wavves/playbooks/decide.md` | yes |
| `examples/usage.md` (decide / From check to BUILD) | yes |
| `feature-requests/README.md` | yes |
| `wavves/registry.yml` (MDA) | yes |
| `wavves/INDEX.md` | yes |
| `evals/README.md` | yes |
| foreign pax IWD-D5 / IWD-D6 / IWD-W2R-TRAIN-WIRE (illustration) | yes |

## Commit file list

- This findings file only:
  `wavves/lanes/20260722_mod-decide-alignment-check/findings/MDA-grounding.md`
- No git performed (status / add / commit / push none).

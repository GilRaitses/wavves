# PBB — proof-before-accept-build

## Meta

| field | value |
|---|---|
| lane code | PBB |
| label | proof-before-accept-build |
| owner | O0 |
| type | execution |
| proof_required | n/a |
| status | w1-w2-complete; pause before INT |
| home | `wavves/lanes/20260718_proof-before-accept-build/` |
| repo_state_verified_against | `517dd85190cf93cf744434338dec4b1eb1d859c5` |
| remediation_loop_cap | 2 |
| depends_on | [PBA] |
| conflicts_with | [] |
| active_dispatch | dispatch-w1.md |

```yaml
lane_type: single-repo
repos:
  - id: wavves
    path: <repo-root>
    role: lane_home_and_product
commit_plan:
  order: [wavves]
  note: O0 sole git actor. Runners never git.
```

## Intent

Ship proof-before-accept: playbook + mechanical eval harness, charter
ACCEPT/`proof_required` template fields, EXECUTION_WIRING runnable DOM/host
rule, mod-check conditional proof-bar lens, mod-decide AUTH sync note.
Defer `/proof-gate` slash skill.

## Grounding

| path | role |
|---|---|
| `feature-requests/20260718_proof-before-accept.md` | FR under build |
| `wavves/lanes/20260718_proof-before-accept-check/decisions/LOCKED-DECISIONS.md` | locks authority |
| `skills/wavves/playbooks/paragraph-tunnel.md` | playbook + STEPS shape |
| `evals/check_paragraph_tunnel.py` | mechanical checker shape |
| `skills/charter/{SKILL.md,EXECUTION_WIRING.md}` | C land |
| `skills/mod-check/SKILL.md` | B land (conditional lens) |
| `skills/mod-decide/SKILL.md` | E land (AUTH sync) |

**Root cause:** ACCEPT can green on process/shell gates while product Proof
is unset (visitor rebuild / product-look / beta visitor lanes). Method needs runnable PROC-* detection + charter
fields, not docs alone.

## Locked decisions (do NOT reopen)

- PBA-LAND: C+D+B+E; defer slash-skill A
- PBA-CLASSIFIER: waveset field proof_required: yes|no|n/a
- PBA-HARNESS: DOM/host-metrics hard + mechanical check_proof_before_accept.py; screenshot optional
- PBA-FREEZE: non-proof-serving freeze + proof-serving allowlist
- PBA-OPTOUT: none/no require rationale on proof_required:yes
- PBA-LENS: proof-bar conditional default for proof_required:yes / product-visitor FRs

## Wave structure

### PBB-W1 — discovery (parallel, read-only)

- PBB-W1a playbook-shape → findings/PBB-playbook-shape.md
- PBB-W1b eval-harness-design → findings/PBB-eval-harness.md
- PBB-W1c charter-wiring-seams → findings/PBB-charter-wiring.md (where to patch C+E)
- PBB-W1d adversarial → findings/PBB-adversarial.md (build footguns; no process-PASS ACCEPT)

### PBB-W2 — build (parallel, NEW files preferred; skill patches as findings drafts)

- PBB-W2a → `skills/wavves/playbooks/proof-before-accept.md`
- PBB-W2b → `evals/check_proof_before_accept.py` + `evals/fixtures/proof-before-accept-*/`
- PBB-W2c → findings drafts for charter SKILL + EXECUTION_WIRING patches (apply in INT)
- PBB-W2d → findings drafts for mod-check proof-bar + mod-decide AUTH sync (apply in INT); update `evals/README.md` + FR index status

Do **not** overload `evals/run_fixtures.py` or paragraph-tunnel fixtures.

### PBB-INT — integration (SINGLE editor) — GATED

Apply skill patches: charter SKILL.md + EXECUTION_WIRING.md; mod-check SKILL.md;
mod-decide SKILL.md; wavves SKILL.md router row for proof-before-accept playbook.
No other shared-file editors in parallel.

### PBB-ACCEPT — acceptance — GATED

1. `python3 evals/check_proof_before_accept.py` → PASS all fixtures; capture JSON under `gate-captures/PBB-ACCEPT-proof.json`
2. Spot-check playbook + EXECUTION_WIRING name harness, classifier, freeze allowlist, opt-out rationale
3. Confirm no `/proof-gate` skill directory
4. Confirm paragraph-tunnel surfaces untouched

## Acceptance criteria

- [ ] Playbook exists and matches locks
- [ ] Mechanical checker runnable with zero network/LLM; fixtures include PROC-PASS-NO-PROOF FAIL + PASS
- [ ] Charter/`proof_required` + four fields documented; EXECUTION_WIRING has named harness rule
- [ ] mod-check documents conditional proof-bar; mod-decide AUTH sync mentions proof_job
- [ ] Router lists proof-before-accept playbook
- [ ] Captures cite measured runner output

## Gated waves

| wave | gate |
|---|---|
| PBB-INT | O0 approval before shared skill-file edits |
| PBB-ACCEPT | O0 approval; independent evaluator preferred |

## Model routing

| role | recommended_model_tier | reason | expected_context | cost_caveat |
|---|---|---|---|---|
| lane orchestrator | cursor-grok-4.5-high-fast | plan + gates | lane home + locks + skills + evals | highest; keep bounded |
| discovery runners | cursor-grok-4.5-high-fast | Grok lock | owned finding only | summarize paths |
| build runners | cursor-grok-4.5-high-fast | Grok lock | owned new files only | validate locally |
| adversarial gate | cursor-grok-4.5-high-fast | defect judgment | after W2 artifacts | run on artifacts |
| acceptance gate | cursor-grok-4.5-high-fast | final verify | captures only | cite numbers |

**model_enforcement:** every Task/subagent launch MUST set `model: cursor-grok-4.5-high-fast`. No Claude/Composer fallback.

## Escalation

Runner answers to O0 only. Pause on INT/ACCEPT. Never solicit the human
operator directly. Never git.

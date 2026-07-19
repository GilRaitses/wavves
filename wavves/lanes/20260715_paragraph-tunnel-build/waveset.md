# PTB — paragraph-tunnel-build

## Meta

| field | value |
|---|---|
| lane code | PTB |
| label | paragraph-tunnel-build |
| owner | O0 |
| type | execution |
| status | chartered |
| home | `wavves/lanes/20260715_paragraph-tunnel-build/` |
| repo_state_verified_against | `f2fb8ce144b68d820b0992f5075a2cbbf44673d2` |
| remediation_loop_cap | 2 |
| depends_on | [PTG] |
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

Ship the wavves product surface for the paragraph tunnel: a **playbook** plus
**runnable eval fixtures/harness**, per PTG locks. Defer `/paragraph-tunnel`
slash skill. Do not extend mod-check as a mid-render gate.

## Grounding

| path | role |
|---|---|
| `feature-requests/20260715_paragraph-tunnel-gate.md` | FR under build |
| `wavves/lanes/20260715_paragraph-tunnel-gate-check/decisions/LOCKED-DECISIONS.md` | locks authority |
| `skills/wavves/playbooks/*.md` | playbook shape to match |
| `skills/wavves/SKILL.md` | router INT target |
| `evals/fixtures/` + `evals/run_fixtures.py` | existing corpus (lens-wording tripwire — **do not overload**) |
| originating product repo outbound copy lane P2-TUNNEL decision + gate-captures | live vocab/evidence (read-only) |

**Root cause:** outbound mid-render paragraphs fail human review while prose
lint passes; product needs a reusable tunnel playbook and a **mechanical**
acceptance harness (not LLM self-grade alone).

## Locked decisions (do NOT reopen)

- PTG-LAND: C + dispatch STEPS hook; strike B; defer slash-skill A
- PTG-INVOKE: lane runner; after render; before prose_lint; field named in waveset
- PTG-MODEL: cursor-grok-4.5-high-fast for adversarial and rewrite (Grok only)
- PTG-EVAL: evals/fixtures/paragraph-tunnel-* runnable; include FIXTURE/STANDIN cases
- PTG-FAIL-CAP: after loop 1 still FAIL → operator REVISE; no auto-pass
- PTG-VOCAB: PN-* + STANDIN/RESEARCH-META/FALSEFACT; alias map to P2-*
- PTG-JUDGE: separate re-adversarial capture + sibling freeze checksum
- PTG-HASH: split evidence_verified_against vs landing_commit_hash in FR

## Wave structure

### PTB-W1 — discovery (parallel, read-only)

- PTB-W1a playbook-shape → findings/PTB-playbook-shape.md
- PTB-W1b eval-harness-design → findings/PTB-eval-harness.md
- PTB-W1c vocab-port → findings/PTB-vocab-port.md (PN-* + aliases from outbound copy lane)
- PTB-W1d adversarial → findings/PTB-adversarial.md (build footguns)

### PTB-W2 — build (parallel, NEW files preferred)

- PTB-W2a → `skills/wavves/playbooks/paragraph-tunnel.md` (+ WIRING note in findings)
- PTB-W2b → `evals/check_paragraph_tunnel.py` (stdlib mechanical checker)
- PTB-W2c → `evals/fixtures/paragraph-tunnel-*/` at least:
  - one-fact PASS
  - stack/gloss/because FAIL
  - compare FAIL
  - FIXTURE FAIL
  - STANDIN FAIL
- PTB-W2d → patch FR hash hygiene + feature-requests index status; update `evals/README.md` section for tunnel fixtures (disjoint from lens-wording runner)

Do **not** overload `evals/run_fixtures.py` for tunnel cases.

### PTB-INT — integration (SINGLE editor) — GATED

Wire router: add playbook row to `skills/wavves/SKILL.md` (route table +
playbook list). No other shared-file editors in parallel.

### PTB-ACCEPT — acceptance — GATED

1. `python3 evals/check_paragraph_tunnel.py` → PASS all fixtures; capture JSON under `gate-captures/PTB-ACCEPT-tunnel.json`
2. Spot-check playbook documents: order render → tunnel → lint; fail-cap escalate; Grok model lock; judge/freeze rules
3. Confirm no `/paragraph-tunnel` skill directory created
4. Confirm mod-check SKILL.md untouched

## Acceptance criteria

- [ ] Playbook exists and matches locks (invoke order, vocab, fail-cap, judge, Grok)
- [ ] Mechanical tunnel checker runnable with zero network/LLM
- [ ] Fixtures include FIXTURE and STANDIN fail cases (not only outbound three-shop happy path)
- [ ] Router lists paragraph-tunnel playbook
- [ ] FR hash fields split per PTG-HASH
- [ ] Captures cite measured runner output

## Gated waves

| wave | gate |
|---|---|
| PTB-INT | O0 approval before shared SKILL.md edit |
| PTB-ACCEPT | O0 approval; independent evaluator preferred |

## Model routing

| role | recommended_model_tier | reason | expected_context | cost_caveat |
|---|---|---|---|---|
| lane orchestrator | cursor-grok-4.5-high-fast | plan + gates; house Grok lock | lane home + locks + playbooks + evals | highest; keep bounded |
| discovery runners | cursor-grok-4.5-high-fast | Grok lock (no fast exception this lane) | owned finding only | summarize paths |
| build runners | cursor-grok-4.5-high-fast | Grok lock | owned new files only | validate locally |
| adversarial gate | cursor-grok-4.5-high-fast | defect judgment | after W2 artifacts | run on artifacts |
| acceptance gate | cursor-grok-4.5-high-fast | final verify | captures only | cite numbers |

**model_enforcement:** every Task/subagent launch MUST set `model: cursor-grok-4.5-high-fast`. No Claude/Composer fallback.

## Escalation

Runner answers to O0 only. Pause on INT/ACCEPT. Never solicit the human
operator directly. Never git.

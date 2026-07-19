# PHF — proof-host-followon

## Meta

| field | value |
|---|---|
| lane code | PHF |
| label | proof-host-followon |
| owner | O0 |
| type | execution |
| proof_required | n/a |
| status | w1-w2-complete-pause-accept |
| active_dispatch | dispatch-w1.md (W1+W2 done; pause PHF-ACCEPT) |
| home | `wavves/lanes/20260718_proof-host-followon/` |
| repo_state_verified_against | `538437cad76764fd989cd028f64927b1ae839292` |
| remediation_loop_cap | 2 |
| depends_on | [PBB] |
| conflicts_with | [] |

```yaml
lane_type: single-repo
repos:
  - id: wavves
    path: /Users/gilraitses/wavves_build
    role: lane_home_and_product
commit_plan:
  order: [wavves]
  note: O0 sole git actor. Runners never git.
```

## Intent

Close the named PBB gap: ship a runnable DOM/host probe and harden
proof-before-accept docs so `visual_accept: yes` cannot treat DOM green as
done. Do not reopen PBB. Do not port pax VPB product-look into wavves.

## Grounding

| path | role |
|---|---|
| `feature-requests/20260718_proof-before-accept_ORIGINATING-MOD-FEEDBACK.md` | originating-mod locks source (`538437c`) |
| `skills/charter/EXECUTION_WIRING.md` Rule 2b | contract to make live |
| `skills/wavves/playbooks/proof-before-accept.md` | harden visual_accept path |
| `skills/charter/scripts/transition_gap_probe.py` | stdlib harness shape reference |

## Locked decisions (do NOT reopen)

- PHF-SCOPE: S2 — probe + playbook/docs harden; no VPB port; PBB stays shipped
- PHF-PROBE: stdlib `skills/charter/scripts/proof_host_probe.py`; JSON `host_client_height` + `blank_canvas`
- PHF-EVAL: defer screenshot+rubric fixtures to pax VPB
- PHF-ETIQUETTE: park orchestrator empty-return note outside this BUILD

## Wave structure

### PHF-W1 — discovery (parallel, read-only)

- PHF-W1a probe-shape → findings/PHF-probe-shape.md
- PHF-W1b playbook-harden → findings/PHF-playbook-harden.md
- PHF-W1c adversarial → findings/PHF-adversarial.md

### PHF-W2 — build

- PHF-W2a → ship probe script + minimal self-check / fixture path
- PHF-W2b → wire EXECUTION_WIRING Rule 2b to real command; harden playbook
- PHF-W2c → findings draft for any shared skill INT only if needed

### PHF-INT — GATED (if shared skill edits remain)

Single editor for EXECUTION_WIRING / playbook if not applied in W2.

### PHF-ACCEPT — GATED

1. Probe runnable; emits required JSON fields; capture under gate-captures/
2. Playbook states: visual_accept:yes ⇒ capture-then-grade; DOM green ≠ done
3. Rule 2b cites real command (not contract-only)
4. No product-look fixture corpus added; PBB mechanical regression still PASS

## Acceptance criteria

- [ ] `proof_host_probe.py` exists and is stdlib / documented deps
- [ ] EXECUTION_WIRING Rule 2b names the real path
- [ ] Playbook visual_accept:yes path hardened
- [ ] PBB checker regression 4/4; paragraph-tunnel 6/6
- [ ] No VPB product-look port; no PBB reopen

## Gated waves

| wave | gate |
|---|---|
| PHF-INT | O0 if shared skill files need single editor |
| PHF-ACCEPT | O0; independent evaluator preferred |

## Model routing

| role | recommended_model_tier | reason |
|---|---|---|
| every wave member | cursor-grok-4.5-high-fast | house Grok lock |

**model_enforcement:** `model: cursor-grok-4.5-high-fast`. No Claude/Composer.

## Escalation

Runner → O0 only. Pause on INT/ACCEPT. Never git.

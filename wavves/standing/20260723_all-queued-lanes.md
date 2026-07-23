# Standing queue — 20260723_all-queued-lanes

- **Built:** 2026-07-23 (America/New_York)
- **Trigger:** `¯\_(ツ)_/¯` + all-standing scope (“all queued lanes to the end”)
- **Scope formula:** INDEX `active_lanes` non-completed + `feature_requests.open` ready-for-mod-check / revised-after-PAS (this repo only)
- **Remasure base:** `wavves/INDEX.md`, `wavves/registry.yml`, lane homes, `feature-requests/README.md`
- **repo_state_verified_against:** `26ad2d2afbb9196f2b690000f6a50f1cabfe20e5` (tip at inventory)

| id | source_path | class | proposed_action | result | land_hash / gate_path | blocked_reason |
|---|---|---|---|---|---|---|
| WOF | `wavves/lanes/20260723_wave-orchestrator-fanout-check/` | operator_gate | revise FR / mod-decide after REVISE | gated | `findings/WOF-verdict.md` | check complete; blocks_w2; no BUILD |
| PAS-FR | `feature-requests/20260723_proceed-all-standing.md` | operator_gate | `/mod-decide` residual (COMMIT-AUTH-GRAIN → SCOPE-FALLBACK) | gated | `findings/PAS-verdict.md` | FR revised; BUILD blocked until decide locks |
| PAS-lane | `wavves/lanes/20260723_proceed-all-standing-check/` | skip_done | cite PAS-VERDICT REVISE | skip_done | `findings/PAS-verdict.md` | check wave complete |
| FR-PUO | `feature-requests/20260720_pre-unlock-options-mod-check.md` | operator_gate | revise FR after REVISE | gated | `findings/PUO-verdict.md` | blocks_w2 |
| FR-IPB | `feature-requests/20260719_ip-before-cutover.md` | operator_gate | revise FR after REVISE | gated | `findings/IPB-verdict.md` | blocks_w2 |
| FR-MDA | `feature-requests/20260722_mod-decide-decision-alignment.md` | operator_gate | revise FR after REVISE | gated | `findings/MDA-verdict.md` | blocks_w2 |
| PAS-DECIDE | `.../decisions/PAS-DECIDE-QUEUE.md` | operator_gate | Pick COMMIT-AUTH-GRAIN A\|B\|C | gated | `decisions/PAS-DECIDE-QUEUE.md` | awaiting operator Pick |
| FR-VOICE | `feature-requests/20260718_voice-library-lora.md` | operator_gate | park until AVP-ACCEPT | gated | FR status parked-pending-apollo-proof | hard park; no BUILD invent |
| FR-SETKEY | `feature-requests/20260723_set-key.md` | skip_done | shipped v0.4.0 | skip_done | README shipped row | — |
| PTB | `wavves/lanes/20260715_paragraph-tunnel-build/` | skip_done | ACCEPT PASS | skip_done | `gate-captures/PTB-ACCEPT.md` | — |
| PTG | `wavves/lanes/20260715_paragraph-tunnel-gate-check/` | skip_done | locks + BUILD done | skip_done | `decisions/LOCKED-DECISIONS.md` | — |
| PBA | `wavves/lanes/20260718_proof-before-accept-check/` | skip_done | mod-decide complete; PBB shipped | skip_done | `decisions/LOCKED-DECISIONS.md` | registry status stale vs PBB completed |
| PBB | `wavves/lanes/20260718_proof-before-accept-build/` | skip_done | ACCEPT PASS | skip_done | `gate-captures/PBB-ACCEPT.md` | — |
| PHF | `wavves/lanes/20260718_proof-host-followon/` | skip_done | ACCEPT PASS | skip_done | `gate-captures/PHF-ACCEPT.md` | — |
| SELF | `wavves/lanes/20260709_wavves-self-improvement/` | skip_done | ACCEPT PASS | skip_done | registry completed | — |
| LAYOVER | `wavves/lanes/20260709_layover-preflight/` | skip_done | ACCEPT PASS | skip_done | registry completed | — |

## Execution order (this pass)

1. Persist this queue (done).
2. Non-gate moves: charter+background-dispatch PUO / IPB / MDA checks.
3. Surface operator_gates: PAS mod-decide residual #1; voice park.
4. WOF: do not invent verdict; integrate on lens notify.
5. No BUILD charter for PAS/WOF/PUO/IPB/MDA until their checks clear.

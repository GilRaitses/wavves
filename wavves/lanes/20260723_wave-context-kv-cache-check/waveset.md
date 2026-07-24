# KVC — wave-context-kv-cache-check

| Meta | |
|---|---|
| lane code | KVC |
| type | check / read-only |
| `repo_state_verified_against` | `de75b4c4118c78dcc0164fdaa916bbc53f99225f` |
| `proof_required` | n/a — FR check; no visitor Proof |
| artifact | `feature-requests/20260723_wave-context-kv-cache.md` |

## Intent

Adversarial sanity-check of the context/KV-cache FR before decide/BUILD.
Wire scope is WOF checkpoint + PAS remasure + mod-rotate hydration only.

## Locked

- read-only; no skill edits; no git
- Model: `cursor-grok-4.5-high-fast`
- Ban treating FR as transformer KV isomorphism or RotatE
- Ban expanding scope to PUO/IPB/MDA
- Verdict GO | REVISE | BLOCK with named gaps
- O0 dispatches orch only; orch fans out lenses

## Waves

### KVC-W1 — parallel lenses

| id | lens | owns |
|---|---|---|
| KVC-W1a | grounding | `findings/KVC-grounding.md` |
| KVC-W1b | contradictions | `findings/KVC-contradictions.md` |
| KVC-W1c | completeness | `findings/KVC-completeness.md` |
| KVC-W1d | adversarial | `findings/KVC-adversarial.md` |

### KVC-VERDICT

Orch writes `findings/KVC-verdict.md` after all four returns. Pause; return_to_O0.

## Grounding seams

- artifact FR
- WOF FR leave-acts / checkpoint (`feature-requests/20260723_wave-orchestrator-fanout.md`)
- PAS FR stale-queue / standing (`feature-requests/20260723_proceed-all-standing.md`)
- `skills/mod-rotate/SKILL.md`, `skills/wavves-init/SKILL.md` §4–5
- RTH synthesis pointer (illustration): `lanes/20260723_mod-rotate-theory-research/findings/RTH-SYNTHESIS.md`
- HF blog is external analogy only: https://huggingface.co/blog/not-lain/kv-caching

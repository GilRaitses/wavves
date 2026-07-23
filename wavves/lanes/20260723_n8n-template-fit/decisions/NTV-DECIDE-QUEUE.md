# NTV — mod-decide queue (pre-auth)

- **Date:** 2026-07-23
- **Lane:** `wavves/lanes/20260723_n8n-template-fit/`
- **repo_state_verified_against:** `de75b4c4118c78dcc0164fdaa916bbc53f99225f`
- **Status:** **complete** — 5/5 locked; see `LOCKED-DECISIONS.md`
- **Source:** W1 PASS + O0-remediated `findings/NTV-SYNTHESIS.md` (INTa never landed)

Forks below are named by W1 rollup / keep-remove / adversarial / library-gap.
Do not invent new product calls mid-walk unless the operator adds them.

## Queue (product before mechanical)

| # | call | question | options (summary) | evidence |
|---|---|---|---|---|
| 1 | **NTV-JOB** | What practical job is the Free template? | **LOCKED A** — see `NTV-B-JOB.md` | W1d ideas; W1c gap; W1e practical-use risk |
| 2 | **NTV-PACK** | Single workflow vs parent + charge sub-workflows? | **LOCKED B** — see `NTV-B-PACK.md` | W1d triad ADAPT; W1c 8578 competitor (do not copy) |
| 3 | **NTV-GATE-STORE** | Where does pass/block evidence land? | **LOCKED B** — see `NTV-B-GATE-STORE.md` | W1d disk-gate ADAPT; W1b Set Fields / strip IDs |
| 4 | **NTV-LLM** | Default LLM credential surface for v0? | **LOCKED C** — see `NTV-B-LLM.md` | W1b credentials must; plug-and-play |
| 5 | **NTV-V0-SCOPE** | Which ADAPTs ship in first Free template? | **LOCKED A** — see `NTV-B-V0-SCOPE.md` | W1d matrix; W1e low-effort / overclaim |

## Already locked (do not re-open in this walk)

- Research/decide-prep charter: no submit this lane
- First submit pricing: **Free**
- No plagiarize; stickies mandatory at BUILD; no hardcoded keys
- Slash skills + `wavves/` standing home: **REMOVE / Cursor-only**
- Gap claim: governed wave accept, not "first orchestrator"

## AUTH-01 preflight (runs only after locks complete)

| surface | ready? | note |
|---|---|---|
| `decisions/*-B-*.md` per pick | pending picks | write on each operator pick |
| `decisions/LOCKED-DECISIONS.md` | stub next | paste when walk done |
| `waveset.md` Locked section | pending AUTH-01 | sync after complete |
| `dispatch-w{N}.md` for BUILD | N/A until `/charter` BUILD | research dispatch stays historical |
| `registry.yml` `mod_decide_complete_at` | pending | set on complete |
| `proof_required` for BUILD charter | pre-declared | BUILD visitor template → expect `proof_required: yes` + `proof_job` in paste (PBA-LAND E) |

## Next operator act

Locks complete. `/charter` BUILD when ready (see `LOCKED-DECISIONS.md`).
NTV-ACCEPT research gate optional; not required to charter BUILD.

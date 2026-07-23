# NTVB — n8n-template-build

| Meta | |
|---|---|
| lane code | NTVB |
| owner | O0; dispatched orch NTVB-W1 |
| type | execution |
| depends_on | NTV mod-decide complete |
| `repo_state_verified_against` | `de75b4c4118c78dcc0164fdaa916bbc53f99225f` |
| `proof_required` | yes |
| `proof_job` | After parallel charges merge, a named proof check must write a pass or block row to the Data Table before the accept/rollup path can emit success. |
| `proof_reference` | `pack/GATE-TABLE-SCHEMA.md` + parent workflow proof/IF nodes |
| `chrome_freeze` | freeze `skills/`, `index.html`, `wavves/` standing home except this lane and NTV research lane; allowlist = `pack/**`, this lane `findings/`, `gate-captures/`, `decisions/` |
| `visual_accept` | no — n8n canvas/stickies; no GitHub Pages DOM Proof |
| artifact | `feature-requests/20260723_n8n-template-fit.md` |
| locks | `../20260723_n8n-template-fit/decisions/LOCKED-DECISIONS.md` |
| active_dispatch | `dispatch-w1.md` |

## Intent

BUILD the Free n8n template pack: parent orchestrator + charge sub-workflows,
Data Table gate evidence, stickies, listing description. Ready for operator
submit (submit itself remains operator-gated).

## Locked decisions (do NOT reopen)

Paste from NTV `LOCKED-DECISIONS.md`:

```text
- NTV-JOB = A — bounded parallel research → proof-gated accept
- NTV-PACK = B — Parent orch + Execute Workflow charges
- NTV-GATE-STORE = B — n8n Data Table evidence
- NTV-LLM = C — Generic LangChain chat-model credential
- NTV-V0-SCOPE = A — Core only; no term_id; no paragraph-tunnel
- Free first submit; Cursor slash/home/plugin = REMOVE
- BUILD musts: stickies, credentials, Set Fields, originality, SEO title, strip IDs
- 4817 = description shape only; do not copy graph
- Competitors 7504/7158/8578 = gap refs only; do not copy
```

## Grounding

- NTV W1 PASS + locks: `wavves/lanes/20260723_n8n-template-fit/`
- Guidelines: `.../n8n-template-fit/references/guidelines-excerpt.md`
- Synthesis job: `.../n8n-template-fit/findings/NTV-SYNTHESIS.md`
- n8n workflow export schema: fetch current docs; use valid importable JSON

## Pack layout (owned under this lane)

```text
pack/
  README.md                 # import order + credentials
  01-charge-research-a.json
  02-charge-research-b.json
  03-parent-orchestrator.json
  DESCRIPTION.md            # ~200w listing copy + SEO title
  GATE-TABLE-SCHEMA.md      # Data Table columns for proof rows
  STICKIES.md               # yellow + step sticky markdown to paste/embed
```

## Wave structure

### NTVB-W1 — parallel build (disjoint files)

| id | owns |
|---|---|
| NTVB-W1a | `pack/01-charge-research-a.json` + `findings/NTVB-W1a-return.md` |
| NTVB-W1b | `pack/02-charge-research-b.json` + `findings/NTVB-W1b-return.md` |
| NTVB-W1c | `pack/DESCRIPTION.md` + `pack/STICKIES.md` + `findings/NTVB-W1c-return.md` |
| NTVB-W1d | `pack/GATE-TABLE-SCHEMA.md` + `pack/README.md` (import order draft) + `findings/NTVB-W1d-return.md` |

Charges A/B: Execute Workflow Trigger → Set (read locks) → AI Agent (generic
chat model) → structured return fields. Renamed nodes. No hardcoded keys.
Placeholder sticky text OK if STICKIES.md is canonical.

### NTVB-INT — parent + wire (single editor, after W1)

Owns `pack/03-parent-orchestrator.json`; updates `pack/README.md` with final
workflow names/IDs. Parent: trigger → Set Fields (topic, locks, proof_job) →
parallel Execute Workflow (A‖B) → Merge → proof Code/IF → Data Table append →
rollup. Sticky nodes in parent JSON. GATED: orch may proceed INT after W1
rollup without O0 if W1 GATE PASS; else escalate.

### NTVB-ACCEPT — GATED

Independent grader. Runnable:
1. `python3 -m json.tool` on all three workflow JSON files (EXIT 0)
2. ripgrep: no API key patterns / `sk-` / personal emails / `/Users/` in pack/
3. Checklist vs guidelines musts (stickies present in parent or STICKIES.md;
   Set Fields; Free; SEO title in DESCRIPTION)
4. proof_job: parent graph contains proof check + Data Table write path
   (node names cited); schema file non-empty
Capture `gate-captures/NTVB-ACCEPT.md` + `gate-captures/NTVB-ACCEPT.json`

Remediation loop cap: 2.

## Acceptance criteria

1. Pack importable in principle (valid JSON; documented import order).
2. Role triad visible: parent orch vs two charge workflows.
3. proof_required measured (schema + parent proof/IF/Data Table path).
4. No Cursor residue (no `/wavves`, no plugin install steps as requirements).
5. DESCRIPTION ~200 words with Who/How/Setup/Requirements/Customize.
6. git_actions_by_runner: none; commit file list for O0.

## Gated waves

- NTVB-W1: unlocked
- NTVB-INT: auto if W1 GATE PASS; else O0
- NTVB-ACCEPT: GATED O0
- **n8n website submit: operator-gated** (never by runners)

## Model routing

| role | tier | reason |
|---|---|---|
| wave orch | high-reasoning (`cursor-grok-4.5-high-fast`) | fan-out + gates |
| W1a/b JSON | balanced | n8n graph authoring |
| W1c/d docs | fast | copy + schema |
| INT parent | high-reasoning | wiring + stickies in JSON |
| ACCEPT | high-reasoning | independent grade |

## Escalation

Answer to O0 only. Credential/submit boundaries → escalate and stop.

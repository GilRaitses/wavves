# Pack import guide

## Creator Portal upload

Use **`coordinate-parallel-research-agents-openai-data-tables.json`** (portal title + renamed nodes).
Prior: `coordinate-parallel-research-proof-gated-accept.json`.
Charges are embedded. Modular `01`/`02`/`03` remain repo source for local multi-file import.

Free n8n template: bounded parallel research charges → merge → proof-gated
accept with Data Table evidence (`NTV-GATE-STORE = B`).

Pricing: **Free**. No Cursor install, slash skills, or plugin steps.

Credential and personal values stay in your n8n instance. This pack ships
placeholders only; no secrets in repo JSON.

## Pack files

| File | Role |
|---|---|
| `01-charge-research-a.json` | Charge sub-workflow A — `Charge Research A — Wave Packet` |
| `02-charge-research-b.json` | Charge sub-workflow B — `Charge Research B — Wave Packet` |
| `03-parent-orchestrator.json` | Parent orch — `Parent Orchestrator — Proof-Gated Wave Accept` |
| `GATE-TABLE-SCHEMA.md` | Data Table columns for proof rows |
| `STICKIES.md` | Yellow + step sticky markdown (canonical) |
| `DESCRIPTION.md` | Listing copy + SEO title |
| `SUBMIT-coordinate-parallel-research-proof-gated-accept.json` | **Creator Portal upload** (single file; charges embedded) |
| `README.md` | This import guide |

## Import order

1. **Import charges first**
   - Import `01-charge-research-a.json`
   - Import `02-charge-research-b.json`
   - Confirm each has Execute Workflow Trigger → Set (locks) → AI Agent
     (generic LangChain chat model) → structured return fields
   - Save both so the parent can resolve them by name/ID
2. **Create the proof Data Table**
   - Follow `GATE-TABLE-SCHEMA.md` (table name: `wavves_proof_gate`)
   - Columns: `outcome`, `proof_check_id`, `proof_check_name`, `recorded_at`,
     `wave_run_id`, `reason`, optional `merge_fingerprint`, optional `topic`
3. **Import parent**
   - Import `03-parent-orchestrator.json`
   - Graph: Manual Trigger → Set Fields → parallel Execute Workflow (A‖B) →
     Merge → Proof Merge Complete → IF Outcome Pass → Data Table append →
     pass/block rollup
4. **Attach LLM credentials**
   - On each charge AI / LangChain chat-model node, attach a **generic**
     LangChain chat-model credential (`NTV-LLM = C`)
   - Charge A node: **Chat Model Credential Slot**
   - Charge B node: **Generic Chat Model**
   - Importer picks provider (OpenAI, Anthropic, etc.). No hardcoded API keys
5. **Set Fields on parent**
   - Node: **Set Fields — Topic Locks Proof**
   - `topic` — research topic for the wave
   - `locks` — alignment / lock packet text (no secrets)
   - `proof_job` — named proof check requirement
   - `wave_run_id` defaults to `$execution.id`
6. **Point Execute Workflow nodes at charge workflows**
   - See **INT finalize** below
7. **Stickies**
   - Parent JSON already embeds yellow overview + step stickies from
     `STICKIES.md` (canonical paste source if you need to re-paste)
8. **Data Table node on parent**
   - Point **Append Proof Gate Row** / **Append Block Gate Row** at
     `wavves_proof_gate` (see `GATE-TABLE-SCHEMA.md`)
9. **Smoke run**
   - Manual Trigger once with a safe test topic
   - Confirm a proof row appears (`pass` or `block`) before treating rollup
     success as valid
   - Do not submit to n8n.io from runners; submit is operator-gated

## Credentials notes

| Surface | What to attach | What not to do |
|---|---|---|
| Charge A **Chat Model Credential Slot** | Generic LangChain chat-model credential | Hardcode keys in HTTP or Set nodes |
| Charge B **Generic Chat Model** | Same credential family (provider of choice) | Hardcode keys |
| Data Table | Project-scoped table; no external Sheet/Drive for v0 | Store API keys in table rows |
| Parent HTTP (if any later) | Credential reference only | Inline `Authorization` secrets |

Strip personal emails, absolute home paths, and `sk-` style keys before
any community publish. ACCEPT scans pack/ for those patterns.

## Free template

- First submit pricing: Free (lane lock)
- No paid-template requirements in this pack
- No community-node dependency planned for v0

## INT finalize

Parent and charge wiring after W1 GATE PASS.

| Item | Value |
|---|---|
| Parent workflow name | `Parent Orchestrator — Proof-Gated Wave Accept` |
| Parent workflow id (post-import) | Set by n8n on import; not committed |
| Charge A workflow name | `Charge Research A — Wave Packet` |
| Charge A workflow id | Set after import; wire parent **Execute Workflow — Charge A** |
| Charge B workflow name | `Charge Research B — Wave Packet` |
| Charge B workflow id | Set after import; wire parent **Execute Workflow — Charge B** |
| Proof Data Table name | `wavves_proof_gate` (create from `GATE-TABLE-SCHEMA.md`) |
| Named proof check node name | `Proof Merge Complete` (`proof_check_id` = `proof_merge_complete`) |

### Attach Execute Workflow targets after import

1. Open parent **Execute Workflow — Charge A**.
2. Source: Database. Select list or paste ID for
   **Charge Research A — Wave Packet** (replace `PLACEHOLDER_CHARGE_A_WORKFLOW_ID`).
3. Open **Execute Workflow — Charge B**.
4. Select or paste ID for **Charge Research B — Wave Packet**
   (replace `PLACEHOLDER_CHARGE_B_WORKFLOW_ID`).
5. Keep both on the parallel fan-out into **Merge Charge Returns**
   (A → merge input 0, B → merge input 1).
6. Confirm charge input mappings:
   - A: `topic`, `locks`, `charge_role`, `proof_job`, `research_brief`
   - B: `topic`, `proof_job`, `packet_id`

### Data Table

Create `wavves_proof_gate` using columns and types in `GATE-TABLE-SCHEMA.md`.
Parent append nodes use name mode `wavves_proof_gate`; re-select the table
in the UI if import does not resolve it.

### Stickies

Yellow overview (`color` 4) and step stickies (`color` 2) are embedded in
`03-parent-orchestrator.json`. Canonical text remains in `STICKIES.md` if
you need to paste again after a canvas reset.

### Credential attach (charges)

Attach your LangChain chat-model credential on both charge chat-model nodes
before the first live run. Parent has no LLM node.

## Commit file list note (for O0)

Runners do not git. When O0 lands INT, include at least:

```text
wavves/lanes/20260723_n8n-template-build/pack/03-parent-orchestrator.json
wavves/lanes/20260723_n8n-template-build/pack/README.md
wavves/lanes/20260723_n8n-template-build/findings/NTVB-INT-return.md
```

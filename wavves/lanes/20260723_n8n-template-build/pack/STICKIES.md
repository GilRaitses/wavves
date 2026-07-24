# STICKIES (canonical for SUBMIT / single-file upload)
Creator Portal path uses the SUBMIT JSON stickies below.
Modular `01`/`02`/`03` import is repo-source only.

## Sticky — Template overview

## Coordinate parallel research agents to a proof-gated accept in n8n

**Pricing:** Free

**Governed wave accept** (not a CEO/orchestrator demo): alignment packet + role triad + independent gate evidence.

1. **Set Fields** on the parent: `topic`, locks, and `proof_job`.
2. Parent fans out **two embedded charge sub-workflows** in parallel (`Execute Workflow` parameter/JSON → A ‖ B).
3. Merge returns → **named proof check** → write **pass or block** row to an **n8n Data Table**.
4. Accept / rollup emits success only after a pass row. Block stops the accept path.

**Evidence store (v0):** Data Table only (not Sheets/Drive).
**LLM:** Default chat-model nodes are OpenAI-compatible LangChain slots. Attach your chat credential; swap the model node if you use another provider.
**Upload:** This file is a **single** Creator Portal / Import JSON. Charges are already embedded. Do not import separate charge files for the portal upload path.

## Sticky — Setup credentials

## Setup credentials

1. After import, open **Execute Workflow — Charge A** (embedded graph) → node **Chat Model Credential Slot** → attach your chat-model credential.
2. Open **Execute Workflow — Charge B** → node **Chat Model Credential Slot** → attach the same (or another) chat-model credential.
3. Default node type is OpenAI-compatible (`lmChatOpenAi`). To use Anthropic/other, replace that model node with the matching LangChain chat-model node and attach its credential.
4. Do **not** paste API keys into Set Fields, HTTP bodies, or sticky text.

## Sticky — Set Fields

## Set Fields

On **Set Fields — Topic Locks Proof**, fill:

- `topic` — research question for both charges
- `locks` — bounded constraints both charges must respect
- `proof_job` — alignment text for the named proof check (v0 gate logic is `Proof Merge Complete`)

These values are the alignment packet. Do not hardcode secrets here.

## Sticky — Import order

## Import / upload (single JSON)

1. Import **this one workflow JSON** (Creator Portal upload or n8n Import from File).
2. Create Data Table **wavves_proof_gate** with the columns listed in **Sticky — Proof + Data Table**.
3. Attach chat-model credentials on both embedded charge **Chat Model Credential Slot** nodes.
4. Edit **Set Fields — Topic Locks Proof**.
5. Run **Start Wave Run** once.

Repo modular files `01`/`02`/`03` are source-only; not required for this upload path.

## Sticky — Wire Execute Workflow

## Embedded charges (no database wire)

Charges A and B are **already embedded** (`Execute Workflow` → source **parameter** / workflow JSON).

1. Do **not** point these nodes at separate imported workflows.
2. Open each Execute Workflow node only to reach the embedded chat-model credential slots.
3. Keep A and B on the **parallel** path into **Merge Charge Returns**.

Role triad: parent orchestrates; charges research; neither charge owns the gate.

## Sticky — Proof + Data Table

## Proof check + Data Table

After Merge:

1. **Proof Merge Complete** (named check, id `proof_merge_complete`) sets `outcome` to `pass` or `block`.
2. **IF Outcome Pass** → **Append Proof Gate Row** or **Append Block Gate Row**.
3. Accept / rollup emits success **only** after a pass row.

### Create table `wavves_proof_gate` before first run

| Column | Type | Required |
|---|---|---|
| `outcome` | string | yes (`pass` or `block`) |
| `proof_check_id` | string | yes |
| `proof_check_name` | string | yes |
| `recorded_at` | date | yes |
| `wave_run_id` | string | yes |
| `reason` | string | yes |
| `merge_fingerprint` | string | no |
| `topic` | string | no |

No `term_id` column (v0). Re-select the table on the Append nodes if name mode does not resolve after import.

## Sticky — Run once

## Run once

1. Confirm: Data Table `wavves_proof_gate` exists, credentials attached on both charge **Chat Model Credential Slot** nodes, Set Fields filled.
2. Click **Start Wave Run** → Execute workflow.
3. Inspect charge returns, proof `outcome`, and the Data Table row.
4. On pass, read the rollup. On block, fix charge returns or proof inputs and re-run.


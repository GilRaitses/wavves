# GATE-TABLE-SCHEMA — proof_job Data Table

Lock: `NTV-GATE-STORE = B` (n8n Data Table evidence).
Lock: `NTV-V0-SCOPE = A` (no `term_id` column).

**proof_job:** After parallel charges merge, a named proof check must write a
pass or block row to this table before the accept/rollup path can emit success.

Suggested table name: `wavves_proof_gate` (importer may rename; parent Data
Table node must point at the same table).

## Columns

Create these columns exactly (names are snake_case; n8n requires letter start,
letters/numbers/underscores only, max 63 chars). Types match n8n Data Table:
`string` | `number` | `boolean` | `date`.

| # | Column name | Type | Required on write | Purpose |
|---|---|---|---|---|
| 1 | `outcome` | string | yes | `pass` or `block` (exact lowercase). Rollup IF reads this. |
| 2 | `proof_check_id` | string | yes | Stable id of the named proof check (e.g. `proof_merge_complete`). |
| 3 | `proof_check_name` | string | yes | Short human label for the same check (sticky / UI). |
| 4 | `recorded_at` | date | yes | When the proof row was written (ISO datetime from the workflow). |
| 5 | `wave_run_id` | string | yes | Generic wave/run identifier for this execution. **Not** `term_id` (v0 excludes term identity). Source from Set Fields or `$execution.id`. |
| 6 | `reason` | string | yes | Brief evidence summary (why pass or block). Keep short; no secrets. |
| 7 | `merge_fingerprint` | string | no | Optional hash or compact fingerprint of the merged charge returns. Empty string if unused. |
| 8 | `topic` | string | no | Optional research topic from Set Fields. Empty string if unused. |

### Value contracts

| Field | Allowed values / notes |
|---|---|
| `outcome` | Only `pass` or `block`. Parent proof IF: success path requires `outcome === "pass"`. |
| `proof_check_id` | Non-empty. Same id the parent proof Code/IF node names. |
| `wave_run_id` | Non-empty per run. Do not store Cursor term ids or absolute home-directory paths. |
| `reason` | One short sentence or phrase. No API keys, emails, or absolute home paths. |
| `merge_fingerprint` | Optional. If present, opaque string (e.g. sha256 prefix of merged JSON). |
| `topic` | Optional. Mirrors parent Set Fields `topic`. |

### Out of scope (v0)

- No `term_id` column.
- No paragraph-tunnel fields.
- No credential or model-key columns.

## Create-table steps (importer)

1. In n8n: open **Data tables** (project scope) → **Create data table**.
2. Name: `wavves_proof_gate` (or match whatever INT documents after wiring).
3. Add columns in the order above; set each **type** as listed.
4. Save. Note the table id/name for the parent workflow **Data Table** append node.
5. Do not paste secrets into sample rows. A dry-run may insert one `block` row with
   `reason` = `importer dry-run` and delete it after smoke test if desired.
6. Parent graph (INT): after Merge → named proof check → IF → **append one row**
   with all required columns filled → only then emit accept/rollup success when
   `outcome` is `pass`.

## Example row (illustrative)

| outcome | proof_check_id | proof_check_name | recorded_at | wave_run_id | reason | merge_fingerprint | topic |
|---|---|---|---|---|---|---|---|
| `pass` | `proof_merge_complete` | Merge + proof check | `2026-07-23T17:00:00.000Z` | `run_manual_001` | Both charges returned structured fields; proof check passed | `a3f1c9…` | `governed wave accept` |

| outcome | proof_check_id | proof_check_name | recorded_at | wave_run_id | reason | merge_fingerprint | topic |
|---|---|---|---|---|---|---|---|
| `block` | `proof_merge_complete` | Merge + proof check | `2026-07-23T17:05:00.000Z` | `run_manual_002` | Charge B missing required return fields | | `governed wave accept` |

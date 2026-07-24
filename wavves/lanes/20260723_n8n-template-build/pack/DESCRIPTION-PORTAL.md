# Creator Portal listing copy (operator form)

## Title
Coordinate parallel research agents with OpenAI and n8n Data Tables

## Quick overview
This workflow runs a manual research wave in n8n, sending the same topic and constraints to two parallel LangChain agents (OpenAI-compatible chat models), then proof-checks that both returned usable findings and records a pass/block decision in an n8n Data Table before emitting an accept rollup.

## How it works
1. Starts when you manually trigger the workflow.
2. Sets the wave packet fields (topic, locks, proof job text, and a run ID) used to govern the run.
3. Runs two embedded sub-workflows in parallel that each use a LangChain agent with an OpenAI-compatible chat model to produce research outputs for Charge A (findings with sources/claims) and Charge B (adversarial gaps/risks).
4. Merges both charge results and performs a proof check that marks the wave as pass only if both charges return a usable status and non-empty findings.
5. Writes the proof outcome (pass or block) plus metadata to the n8n Data Table `wavves_proof_gate`.
6. Emits a final rollup object that sets `accept=true` only on pass, or `accept=false` with a block reason otherwise.

## Setup
1. Attach your OpenAI (or OpenAI-compatible) chat model credentials to the Chat Model Credential Slot inside both embedded charge sub-workflows.
2. Create an n8n Data Table named `wavves_proof_gate` with the required columns (outcome, proof_check_id, proof_check_name, recorded_at, wave_run_id, reason, and optional merge_fingerprint and topic) and reselect it in the insert nodes if name lookup does not resolve after import.
3. Update the topic, locks, and proof job text in the Set Fields step before each run.

## Portal AI note
n8n AI sticky rewrite ([auto-annotate template](https://n8n.io/workflows/13868-auto-generate-sticky-notes-and-rename-nodes/)) suggested selecting database sub-workflows. That is incorrect for this pack: charges are embedded as Execute Workflow parameter JSON. Upload JSON keeps portal-style stickies but corrects that step.

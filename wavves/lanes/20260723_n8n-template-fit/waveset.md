# NTV — n8n-template-fit

| Meta | |
|---|---|
| lane code | NTV |
| owner | O0 (moderator) |
| type | research / decide-complete (awaiting BUILD charter) |
| `repo_state_verified_against` | `de75b4c4118c78dcc0164fdaa916bbc53f99225f` |
| `proof_required` | yes — for the **BUILD** execution lane (n8n template pack); this research lane itself has no visitor DOM Proof |
| `proof_job` | After parallel charges merge, a named proof check must write a pass or block row to the Data Table before the accept/rollup path can emit success. |
| `proof_reference` | Data Table gate row schema in BUILD stickies; none until BUILD lands columns |
| `chrome_freeze` | freeze Cursor skills/, wavves/ standing home (except lane), index.html; allowlist = n8n workflow JSON pack + sticky text + Set Fields + Data Table schema under BUILD lane |
| `visual_accept` | no — deliverable is n8n template JSON / canvas, not GitHub Pages DOM |
| artifact | `feature-requests/20260723_n8n-template-fit.md` |
| locks | `decisions/LOCKED-DECISIONS.md` |
| `mod_decide_complete_at` | 2026-07-23T13:51:00-04:00 |
| `waveset_synced_at` | 2026-07-23T13:51:00-04:00 |
| active_dispatch | null |

## Intent

Operator (verbatim intent): charter the n8n version of wavves; decide what it
needs to be to fit the template library and what to remove. Ground against
n8n submission guidelines and a published template example. Do not BUILD or
submit workflow JSON in this lane.

## Grounding (verified)

| seam | path / URL | role |
|---|---|---|
| FR | `feature-requests/20260723_n8n-template-fit.md` | intent + out-of-scope |
| wavves product identity | `README.md` (core ideas) | keep-candidate source |
| roles / fan-out | `skills/charter/SKILL.md` Roles + OF-10 | O0 / wave orch / charge |
| standing home | `wavves/AGENTS.md`, `wavves/INDEX.md` | Cursor-disk hydration (likely REMOVE or ADAPT hard) |
| router skills | `skills/wavves/SKILL.md`, `mod-check`, `mod-decide`, `mod-rotate` | Cursor slash surface |
| guidelines (operator paste) | FR + this waveset Locked; Notion URL below | publish gates |
| example template | https://n8n.io/workflows/4817-composestitch-separate-images-together-using-n8n-and-gemini-ai-image-editing/ | description shape |
| guidelines URL | https://n8n.notion.site/Template-submission-guidelines-9959894476734da3b402c90b124b1f77 | authority link |
| submit UX | `references/submit-template-modal.png` | Free, AI review, JSON upload |
| repo n8n inventory | search at charter: **zero** `*n8n*` files; no workflow JSON | root constraint |

**Root constraint.** Full Cursor plugin cannot be the template. The lane must
name a **publishable n8n workflow** (practical use case + sticky-documented
graph) that carries only the wavves ideas that survive n8n's product and
review constraints. Everything else is REMOVE or "Cursor plugin only."

## Locked decisions (do NOT reopen)

Authority: `decisions/LOCKED-DECISIONS.md` (AUTH-01 synced).

1. **NTV-JOB = A** — Free template job: bounded parallel research →
   proof-gated accept.
2. **NTV-PACK = B** — Parent orchestrator + Execute Workflow charge
   sub-workflows.
3. **NTV-GATE-STORE = B** — Evidence in n8n Data Table.
4. **NTV-LLM = C** — Generic LangChain chat-model credential.
5. **NTV-V0-SCOPE = A** — Core only; no term_id; no paragraph-tunnel in v0.
6. First submit pricing: **Free**.
7. Slash skills, `wavves/` standing home, plugin install: **REMOVE /
   Cursor-only**.
8. BUILD musts: sticky notes, credentials (no hardcoded keys), Set Fields,
   originality, SEO title form, personal-ID strip.
9. Do **not** plagiarize (including example 4817 graph); competitors are
   gap references only.
10. This research lane does not submit or BUILD workflow JSON; BUILD is a
    separate `/charter` after these locks.
11. ROLE-COLLAPSE + git bans for orch/runners unchanged.
12. Model for judgment lenses: `cursor-grok-4.5-high-fast`.

## Wave structure

### NTV-W1 — discovery (parallel, read-only)

| id | lens | owns |
|---|---|---|
| NTV-W1a | wavves-core inventory | `findings/NTV-wavves-core.md` — list README + skill concepts that could map; cite paths |
| NTV-W1b | guidelines checklist | `findings/NTV-guidelines-checklist.md` — mandatory vs optional gates from operator paste + example page sections |
| NTV-W1c | library gap | `findings/NTV-library-gap.md` — what published n8n multi-agent/orchestrator templates already cover; gap wavves could fill (cite URLs; no copying) |
| NTV-W1d | keep-remove matrix | `findings/NTV-keep-remove.md` — every major wavves surface → KEEP / ADAPT (n8n native) / REMOVE with one-line why |
| NTV-W1e | adversarial | `findings/NTV-adversarial.md` — rejection risks, Cursor residue, low-effort traps, overclaim vs "orchestrator" templates |

Fan-out: all five parallel (disjoint files). Pattern: `(a‖b‖c‖d‖e)` then orch
rollup.

### NTV-INT — synthesis + decide queue (GATED; after W1)

Single serialized editor after O0 unlock. Writes:
- `findings/NTV-SYNTHESIS.md` — recommended template shape (one sentence job),
  title draft, node-family sketch (not full JSON), KEEP/REMOVE summary
- `decisions/NTV-DECIDE-QUEUE.md` — named forks for `/mod-decide` (use case,
  scope cut, storage, credentials, single vs multi-workflow, etc.)

Do **not** invent locks. Queue only.

### NTV-ACCEPT — research accept (GATED)

Independent of synthesis author. Capture `gate-captures/NTV-ACCEPT.md`:
- All five W1 files exist with path/URL evidence
- Matrix covers README core ideas + charter triad + standing home + mod-*
- Decide queue has ≥3 named forks
- No workflow JSON claimed built; no plagiarism of example 4817 graph
- Remediation loop cap: 2

## Acceptance criteria

1. Checklist marks sticky notes, credentials, originality, SEO title, Set
   Fields, personal-ID strip as **must** for BUILD.
2. KEEP/REMOVE matrix states REMOVE (or Cursor-only) for slash skills and
   `wavves/` disk home unless a concrete n8n ADAPT is named.
3. Library-gap lens cites ≥2 existing orchestrator/multi-agent templates or
   official playbook pages with URLs.
4. Synthesis proposes one practical use case with broad appeal (guidelines),
   not "port the Cursor plugin."
5. Commit file list for O0 only; git_actions_by_runner=none.

## Gated waves and operator involvement

- NTV-W1: unlocked at charter (research)
- NTV-INT: GATED on O0 after W1 rollup (and after clearing W1e FAIL if any)
- NTV-ACCEPT: GATED
- Any n8n submit or credential use: **operator-gated**, out of this lane

## Model routing and token discipline

| role | recommended_model_tier | reason | expected_context | expected_file_reads | cost_caveat |
|---|---|---|---|---|---|
| lane / wave orch | high-reasoning (`cursor-grok-4.5-high-fast`) | fan-out + rollup + decide queue | bounded lane home + FR | waveset, dispatch, five returns | keep chat short; files win |
| NTV-W1a inventory | fast | path cites from README/skills | local markdown | README, charter, AGENTS | summarize, do not paste skills whole |
| NTV-W1b checklist | fast | mechanical gate extract | guidelines paste + example | FR, example URL fetch | Notion may be thin; use operator paste |
| NTV-W1c library gap | balanced | web + originality judgment | few competitor URLs | web search/fetch only | no cloning workflows |
| NTV-W1d matrix | high-reasoning | product cut calls as proposals | W1a+b inputs via orch after | own file only at write; read seams | proposals not locks |
| NTV-W1e adversarial | high-reasoning | rejection / honesty | all seams | findings siblings read-only after exist | FAIL must name evidence |
| NTV-INT | high-reasoning | synthesis | W1 pack | five findings | GATED |
| NTV-ACCEPT | high-reasoning | independent grade | captures | synthesis + W1 | no authorship of INT |

## Escalation (operator-protection catch)

Wave orch and charge workers answer to **O0**, not the human operator. Pause
and escalate to O0 on locked-decision conflict, scope expand into BUILD/submit,
credential boundaries, or plagiarism uncertainty. Do not solicit the operator
directly from runners.

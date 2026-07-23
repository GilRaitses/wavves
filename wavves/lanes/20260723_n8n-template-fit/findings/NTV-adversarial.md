# NTV-adversarial: rejection and honesty risks

| Meta | |
|---|---|
| charge | NTV-W1e |
| tip | `de75b4c4118c78dcc0164fdaa916bbc53f99225f` |
| mode | research only; no BUILD/submit |
| sibling matrix | **missing at write time** (`findings/NTV-keep-remove.md` not on disk) |
| other siblings | `NTV-library-gap.md`, `NTV-guidelines-checklist.md`, `NTV-wavves-core.md` also absent |

Honesty judgment below uses the waveset **root constraint** and Acceptance #2 when the matrix is absent. Re-grade against the matrix when W1d lands.

## 1. Rejection risks (n8n review)

Grounded in `references/guidelines-excerpt.md` (operator paste of submission guidelines).

| risk | why it fails review | wavves-specific trap |
|---|---|---|
| Low effort | Guidelines demand high quality, renamed nodes, stickies, plug-and-play for new users | Porting "the Cursor plugin" as a thin HTTP/AI agent chain without a concrete job |
| Incomplete stickies | Yellow full description + step stickies are mandatory | Documenting slash skills or `wavves/` paths in stickies instead of runnable n8n steps |
| Hardcoded keys | Ban pattern: keys in HTTP nodes; must use credentials + Set Fields | Pasting Cursor/API secrets from local `.env` into workflow JSON for "demo" |
| Thin description | Need ~200 words + Who / How it works / Setup / Requirements / Customize; SEO title form | Title or body that only says "wavves for n8n" with no actionable setup |
| Not a practical use case | Broad appeal + specificity required | Process meta ("moderator layer for agents") with no operator outcome (e.g. ticket triage, research fan-out with deliverable) |
| Personal IDs / non-portable paths | Strip personal IDs; assume new user | Sticky or Set Fields pointing at `/Users/.../wavves_build` or a private lane home |
| Paid too early | Free until ≥3 high-quality templates | Irrelevant to first Free submit; still a later ban risk if commerce claims precede eligibility |

**Example 4817** is description **shape** only (sections, length, setup clarity). Copying its graph, nodes, or Gemini image pipeline is plagiarism adjacency (section 3), not a success pattern.

## 2. Cursor residue (must not ship as the template)

`README.md` defines wavves as a **Cursor plugin**: slash skills, marketplace/`/add-plugin`, standing disk home under `wavves/`, playbooks (`/wavves`, `/charter`, `/mod-check`, `/mod-decide`, `/mod-rotate`, `/shrug`, etc.), charge/orch Task fan-out, eval harness paths.

Waveset **root constraint** (verbatim intent): the full Cursor plugin cannot be the template. Publishable surface is a sticky-documented n8n workflow that carries only ideas that survive n8n product and review. Everything else is REMOVE or "Cursor plugin only."

### Residue classes that fail honesty if kept as n8n nodes

| residue | README / waveset cue | if treated as n8n node or required install | honesty |
|---|---|---|---|
| Slash skills (`/wavves`, `/charter`, `/mod-*`, `/shrug`, …) | Usage + Skills tables in `README.md` | Fake "skill" nodes or sticky "run `/mod-check`" with no n8n equivalent | **FAIL** (fiction) |
| Plugin install (`/add-plugin wavves`, `~/.cursor/plugins/local/wavves/`) | Installation section | Template setup that requires Cursor plugin install | **FAIL** (wrong product surface) |
| Standing home (`wavves/AGENTS.md`, `INDEX.md`, `registry.yml`, `rotations/`) | Standing home + What wavves tracks | Requiring that disk layout inside n8n Cloud/self-host as the workflow contract | **FAIL** unless a named ADAPT (e.g. Data Store / Google Drive folder schema) is concrete and documented |
| Charge / Task fan-out as Cursor Tasks | Roles triad in README | Nodes labeled "charge worker" that only call LLM with Cursor role prose | Overclaim + low effort unless mapped to real n8n branching/sub-workflows |
| Eval / failure_log / `evals/check_*.py` | Orchestration fail ids | Shipping Python harness as template dependency | Wrong audience; incomplete stickies |

Acceptance #2 already requires the KEEP/REMOVE matrix to state REMOVE (or Cursor-only) for slash skills and `wavves/` disk home unless a concrete n8n ADAPT is named. A matrix that KEEP's those as nodes without ADAPT is an honesty FAIL regardless of description polish.

## 3. Plagiarism adjacency

Locked decisions #3 and #10: do not plagiarize or resell another creator's workflow; existing multi-agent / orchestrator templates are originality **competitors**, not copy sources.

| adjacency | risk |
|---|---|
| Clone of example [4817](https://n8n.io/workflows/4817-composestitch-separate-images-together-using-n8n-and-gemini-ai-image-editing/) graph or Gemini stitch pipeline | Ban-class; 4817 is description shape only |
| Near-copy of published "orchestrator / worker / CSO" multi-agent templates | Review rejects as non-original; library already crowded (W1c should cite; file missing here) |
| Reskin of competitor Cursor-to-n8n "agent swarm" graphs | Same ban/originality risk |
| Lifting sticky text or title patterns from a paid template | Still theft of creator work |

Safe: original graph + original stickies; borrow only **section headings and length discipline** from 4817's public description page.

## 4. Overclaim vs existing "orchestrator" / multi-agent templates

Without `NTV-library-gap.md` on disk, this lens states the overclaim class from waveset Locked #10 and README positioning only.

| overclaim | why it dies in review or market |
|---|---|
| "First multi-agent orchestrator on n8n" | False category claim; library and blogs already sell orchestrator-worker patterns |
| "wavves for n8n" as identity without a single job sentence | Reads as product port, not a practical template |
| Claiming Raft/Kubernetes/Erlang rotation fidelity inside a few LLM nodes | Analogy from README becomes unearned technical claim |
| Equating Cursor Task fan-out with n8n sub-workflows | Different runtime; must ADAPT or REMOVE |
| "Disk gate captures" without a runnable check the importer can execute | Stickies about honesty gates are not gates |

Gap-worthy direction (proposal only, not a lock): a **narrow, named job** that uses a subset of wavves ideas (bounded parallel branches, written acceptance criteria, pass/fail artifact before merge) implemented with native n8n nodes, credentials, and stickies. That competes on originality of the job + graph, not on the word "orchestrator."

## 5. Honesty verdict

**Verdict: PASS** (charter / root-constraint honesty), with **matrix not yet verifiable**.

| check | result | evidence |
|---|---|---|
| Would the locked charter ship slash-skill fiction as n8n nodes? | **No** | Waveset root constraint: full Cursor plugin cannot be the template; Acceptance #2 requires REMOVE/Cursor-only for slash skills and standing home unless concrete ADAPT named; FR states Cursor plugin is not drop-in |
| Would a KEEP/REMOVE matrix shipping slash skills as nodes FAIL? | **Yes, by rule** | Same Acceptance #2; this charge fails honesty if such a matrix appears |
| Matrix on disk at W1e write? | **No** | `findings/NTV-keep-remove.md` absent; critique is risk-class only |
| Other rejection risks remaining after honesty PASS? | **Yes** | Practical use case still undefined; stickies, credentials, originality, thin description, and orchestrator overclaim remain open for INT / decide queue |

**PASS meaning.** The locked research charter correctly bans Cursor residue as the publishable graph. This is **not** a claim that a future BUILD would pass n8n review. It is **not** clearance of W1d: when `NTV-keep-remove.md` lands, orch must re-check that every slash skill and the standing home are REMOVE or named ADAPT. Any KEEP of `/wavves`-class surfaces as fake nodes flips this verdict to **FAIL**.

**Failed gates to report plainly.** Sibling findings W1a–W1d were missing at write time, so library-gap URL cites and matrix row coverage could not be adversarially graded here. That is an incomplete W1 pack condition for ACCEPT, not a PASS on those lenses.

## 6. Escalation note for orch / O0

No operator solicit. If W1d matrix KEEP's slash skills or requires Cursor plugin install as template setup, treat as honesty FAIL and escalate to O0 before NTV-INT unlock. If matrix correctly REMOVEs those surfaces, keep this PASS and still surface section 1 rejection risks in rollup.

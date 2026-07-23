# NTV-wavves-core: wavves concept inventory for n8n template fit

Lane: `20260723_n8n-template-fit` (NTV). Charge: NTV-W1a. Research only.
Tip base cited in waveset: `de75b4c4118c78dcc0164fdaa916bbc53f99225f`.
Full KEEP/REMOVE matrix is NTV-W1d; this file only lists concepts with a one-line `map_hint`.

Root constraint from waveset Grounding: a publishable n8n workflow cannot be the full Cursor plugin. Slash skills and disk hydration under `wavves/` are expected Cursor-heavy unless a concrete n8n ADAPT is named later.

---

## 1. README core ideas

### Alignment packets
- **what:** Each lane home carries scope, grounded facts, locked decisions, file boundaries, and acceptance checks.
- **paths:** `README.md` (core ideas); lane example `wavves/lanes/20260723_n8n-template-fit/waveset.md`; layout under `README.md` Project layout (`waveset.md`, `decisions/`, `findings/`).
- **map_hint:** ADAPT candidate (sticky notes + workflow description as the alignment surface; not a repo lane tree).

### Bounded waves
- **what:** A dispatched sub-orchestrator runs focused waves of parallel workers with strict ownership while the operator-facing thread stays small.
- **paths:** `README.md` (core ideas; What wavves tracks); `skills/charter/SKILL.md` (Roles, Fan-out + background, OF-10).
- **map_hint:** KEEP candidate (n8n parallel branches or sub-workflows as wave fan-out, with a single integrate step).

### Disk gate captures
- **what:** A lane advances after a runnable harness writes pass or block evidence under `gate-captures/`, graded by someone who did not author the work under review; failed gates stay failed; remediation loops are capped.
- **paths:** `README.md` (core ideas; Manual harness inspection); lane dirs such as `wavves/lanes/*/gate-captures/` (examples exist under layover-preflight, wavves-self-improvement, paragraph-tunnel-build); this lane plans `gate-captures/NTV-ACCEPT.md` per `waveset.md`.
- **map_hint:** ADAPT candidate (n8n execution data, binary pass/fail nodes, or written artifact to storage; not Cursor `gate-captures/` paths).

### Proof-before-accept
- **what:** Product lanes declare a named proof job; process-only ACCEPT cannot clear when `proof_required: yes`.
- **paths:** `README.md` (core ideas; Paragraph tunnel and proof-before-accept); `skills/wavves/playbooks/proof-before-accept.md`; `evals/check_proof_before_accept.py`; `skills/charter/scripts/proof_host_probe.py`; Meta fields in `skills/charter/SKILL.md` / lane `waveset.md`.
- **map_hint:** KEEP candidate (named measurable outcome before a final Accept/Done branch).

### Paragraph tunnel
- **what:** Mid-render structural gate for one outbound field (adversarial review, capped rewrite, mechanical fixtures); not a voice clone.
- **paths:** `README.md`; `skills/wavves/playbooks/paragraph-tunnel.md`; `evals/check_paragraph_tunnel.py`; routed from `skills/wavves/SKILL.md` (paragraph-tunnel playbook).
- **map_hint:** ADAPT candidate (optional AI rewrite + validate node on one text field; niche for a first Free template).

### Rotation with term identity
- **what:** Overloaded thread hands off via a rotation file that assigns the successor a monotonic term identity so stale instructions are recognizable and provenance survives.
- **paths:** `README.md` (core ideas); `skills/mod-rotate/SKILL.md`; `wavves/AGENTS.md` (Identity and rotation terms; Rotation contract); `wavves/rotations/` (directory exists; empty at inventory time); `wavves/INDEX.md` (`current_rotation`).
- **map_hint:** likely Cursor-only for chat-term handoff; ADAPT candidate only if template models session/run id or incarnation fields in durable store.

### Standing home
- **what:** Fresh instances hydrate from files (index, home contract, rotations, registry, step log), never from transcripts.
- **paths:** `README.md` (core ideas; Project layout; What wavves tracks Home); `wavves/AGENTS.md`; `wavves/INDEX.md`; `wavves/registry.yml`; `wavves/step-log.md`; `wavves/rotations/`; bootstrap via `skills/wavves/SKILL.md` playbook bootstrap / `wavves-init` (cited in README Skills).
- **map_hint:** likely Cursor-only as a repo tree; ADAPT candidate as n8n static data, Data Tables, or external store for "current run state."

### Authority propagation
- **what:** After mod-decide, locks sync to `waveset.md`, `dispatch-w{N}.md`, and the registry so later waves do not re-litigate settled decisions; scoped mod-check verdicts and `/wavves proceed` execute ordered recommended actions.
- **paths:** `README.md` (core ideas; Usage proceed/shrug); `skills/mod-decide/SKILL.md`; `skills/mod-check/SKILL.md`; `skills/wavves/playbooks/proceed.md`; `wavves/registry.yml`; lane `dispatch-w{N}.md` pattern in README.
- **map_hint:** ADAPT candidate (locked fields written once, then read by later nodes; "proceed" as an execute-actions branch).

---

## 2. Role triad (O0 / wave orchestrator / charge worker)

### O0 (operator-facing moderator)
- **what:** Charters lanes, background-dispatches wave orchestrators, reconciles on notify, lands git; then releases the operator window (`O0_release_window`). Does not execute charge work inline when a dispatch fits; does not poll.
- **paths:** `README.md` (What wavves tracks); `skills/charter/SKILL.md` (The three roles; Moderator background etiquette; OF-10); `wavves/AGENTS.md` (The three roles).
- **map_hint:** ADAPT candidate (human approval / Wait node / webhook resume as O0; git land stays Cursor or out of template).

### Wave orchestrator
- **what:** Background Task under O0; fans out charge workers; integrates; writes rollup+gate (or hard FAIL / operator_gate). No early `return_to_O0`. Yield requires `findings/<wave>-orch-checkpoint.md`.
- **paths:** `README.md`; `skills/charter/SKILL.md` (Roles; Leave-acts; Fan-out + background; OF-10); fail ids and checker note in README (`evals/check_wave_orchestrator_fanout.py`).
- **map_hint:** KEEP candidate (central workflow or Execute Workflow that fans out and merges).

### Charge worker
- **what:** One background Task per charge id; one bounded disjoint task; never git; never solicit the operator; escalate via orch to O0.
- **paths:** `README.md`; `skills/charter/SKILL.md` (Roles); this charge's own contract matches NTV-W1a in `waveset.md` Wave structure.
- **map_hint:** KEEP candidate (parallel worker branches or sub-workflows with disjoint outputs).

### ROLE-COLLAPSE ban (related)
- **what:** O0 dispatches only the wave orchestrator; orch fans out charges; orch writes rollup/gate. Locked in this lane.
- **paths:** `wavves/lanes/20260723_n8n-template-fit/waveset.md` Locked decisions item 7; `skills/charter/SKILL.md` fail id `PROC-ORCH-ROLE-COLLAPSE`.
- **map_hint:** KEEP candidate as a design rule for the template graph (do not collapse roles into one mega-agent node without an orch step).

---

## 3. Standing home pieces

### `wavves/AGENTS.md` (home contract)
- **what:** Stable governance and hydration contract for the standing home; roles, etiquette locks, rotation terms, skill lifecycle.
- **paths:** `wavves/AGENTS.md`; created by bootstrap per `README.md` What each skill does (`/wavves-init`).
- **map_hint:** likely Cursor-only (IDE/repo governance).

### `wavves/INDEX.md` (fast pickup)
- **what:** Fast pickup surface: current identity, rotation pointer, active lanes, next files to read.
- **paths:** `wavves/INDEX.md`; described in `README.md` Project layout.
- **map_hint:** ADAPT candidate (a single "status" record or sticky summary of active runs).

### `wavves/registry.yml` (lane map)
- **what:** Map of every chartered lane and status; authority sync target after decide.
- **paths:** `wavves/registry.yml`; `README.md` What wavves tracks.
- **map_hint:** ADAPT candidate (n8n Data Table / DB row per "lane" or job).

### `wavves/rotations/` (handoff files)
- **what:** Handoff files with term identity (`O0.R1`, `O0.R2`, ...); directory may be empty until first rotate.
- **paths:** `wavves/rotations/`; `skills/mod-rotate/SKILL.md`; `wavves/AGENTS.md` Rotation contract.
- **map_hint:** likely Cursor-only unless template needs durable handoff between human sessions.

### `wavves/step-log.md` (append-only trace)
- **what:** Append-only synthesis / step trace for the home.
- **paths:** `wavves/step-log.md`; `README.md` Project layout; `wavves/AGENTS.md` Hydration stack.
- **map_hint:** ADAPT candidate (append execution log / audit trail in n8n).

### Related home pieces (secondary)
- **`wavves/failure_log.yml`:** Observed process fail ids. Path: `wavves/failure_log.yml`. map_hint: ADAPT candidate (error log) or Cursor-only if tied to skill fail ids.
- **`wavves/skills/proposed/` and `wavves/skills/accepted/`:** Draft then operator-approved project skills. Paths: `wavves/skills/proposed/`, `wavves/skills/accepted/` (README Moderator and skill flow). map_hint: likely Cursor-only.
- **Lane home:** `wavves/lanes/<date>_<label>/` with `waveset.md`, `dispatch-w{N}.md`, `findings/`, `gate-captures/`, `decisions/`. map_hint: ADAPT candidate as workflow folders / sticky structure, not git paths.

---

## 4. mod-* surfaces and router `/wavves`

### Router `/wavves` (`skills/wavves`)
- **what:** Default entry; checks home; matches a playbook; reads and runs the leaf skill. Playbooks include bootstrap, charter, check, decide, layover, set-key, paragraph-tunnel, proof-before-accept, rotate, pickup, proceed.
- **paths:** `skills/wavves/SKILL.md`; `skills/wavves/playbooks/*.md`; `README.md` Usage and Components.
- **map_hint:** likely Cursor-only (slash routing). ADAPT as a single webhook entry that branches by intent string if the template needs one front door.

### `/mod-check`
- **what:** Read-only adversarial parallel sanity-check of a landed spec or plan; returns scoped verdict (`GO` / `REVISE` / `BLOCK`, `blocks_w2`…`blocks_w5`) with `recommended_actions`.
- **paths:** `skills/mod-check/SKILL.md`; `README.md` What each skill does; playbook `skills/wavves/playbooks/check.md` (via router).
- **map_hint:** KEEP/ADAPT candidate (parallel review agents + merge verdict); Cursor slash surface itself is Cursor-only.

### `/mod-decide`
- **what:** Walks open product/design calls one at a time; writes `decisions/*.md`; syncs authority surfaces; emits Locked decisions paste for BUILD. No BUILD inside the skill.
- **paths:** `skills/mod-decide/SKILL.md`; `README.md`; lane `decisions/` pattern.
- **map_hint:** ADAPT candidate (human-in-the-loop picks + write locks to store); Cursor slash is Cursor-only.

### `/mod-rotate`
- **what:** Writes a rotation file with term identity and emits a one-line paste for a fresh thread.
- **paths:** `skills/mod-rotate/SKILL.md`; `README.md`; `wavves/rotations/`.
- **map_hint:** likely Cursor-only (chat thread handoff).

### Adjacent router surfaces (inventory, not core matrix drivers)
- **`/charter`:** Lane home + dispatch + gates. `skills/charter/SKILL.md`. map_hint: ADAPT (create job record + spawn orch) / Cursor slash Cursor-only.
- **`/wavves proceed`:** Execute ordered `recommended_actions` from a verdict; all-standing phrases widen. `skills/wavves/playbooks/proceed.md`. map_hint: ADAPT candidate (action executor branch).
- **`/shrug`:** Thin alias; bare AUTH-10 proceed; closed all-standing phrase widens. `README.md`; `skills/shrug/SKILL.md` (cited in README Components). map_hint: likely Cursor-only.
- **`/layover`, `/set-key`, `/wavves-init`:** Workspace audit, secret paste helper, home bootstrap. map_hint: likely Cursor-only for a first n8n template.

---

## 5. Gates / proof / rotation as concepts

### Gates (runnable evidence)
- **what:** Runnable checks with JSON + log (or equivalent) evidence on disk; independent grader; capped remediation; hand-written summary is not a gate capture.
- **paths:** `README.md` Manual harness inspection; `skills/charter/SKILL.md` Workflow step on harnesses / EXECUTION_WIRING references; example lane `gate-captures/` dirs under `wavves/lanes/`.
- **map_hint:** KEEP candidate as a product idea (must produce rerunnable evidence); storage ADAPT to n8n-native artifacts.

### Proof (named job before accept)
- **what:** Explicit `proof_required` classifier and named proof job; process-only ACCEPT insufficient when proof is required.
- **paths:** `skills/wavves/playbooks/proof-before-accept.md`; `evals/check_proof_before_accept.py`; charter Meta rules in `skills/charter/SKILL.md`; this lane uses `proof_required: n/a` in `waveset.md` (research).
- **map_hint:** KEEP candidate for any product-shaped template; skip or n/a for research-only graphs.

### Rotation (term identity handoff)
- **what:** Monotonic successor identity on handoff; hydrate from files; stale-term artifacts are historical.
- **paths:** `skills/mod-rotate/SKILL.md`; `wavves/AGENTS.md` sections 4–5; `README.md` core ideas.
- **map_hint:** likely Cursor-only for moderator chat; optional ADAPT as run incarnation / lock version fields.

---

## 6. Compact map_hint rollup (for W1d, not the matrix)

| Cluster | Dominant hint |
|---|---|
| Role triad + bounded waves + ROLE-COLLAPSE | KEEP / ADAPT into graph shape |
| Proof-before-accept + gates (idea) | KEEP / ADAPT evidence sink |
| Alignment packets + authority locks + proceed actions | ADAPT |
| Paragraph tunnel | ADAPT (optional / niche) |
| Standing home disk tree, slash router, mod-rotate paste, shrug, set-key, layover | likely Cursor-only unless a named n8n store ADAPT exists |
| Rotation term identity | likely Cursor-only; thin ADAPT if session id needed |

No workflow JSON proposed. No KEEP/REMOVE locks claimed. Escalate to O0 only if W1d needs a path re-verify against a different tip.

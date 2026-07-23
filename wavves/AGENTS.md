# wavves standing contract — wavves_build

This repo is the wavves plugin's own source (skills, playbooks, homepage,
marketplace metadata). A charter here builds or repairs the plugin itself,
not a downstream project. Read this file, `INDEX.md` and the newest
`rotations/` file (if one exists) before any substantive write.

## 1. Hydration stack (read in this order)

1. This file (`wavves/AGENTS.md`) and `wavves/INDEX.md`. No separate root
   `AGENTS.md` exists in this repo, so this file is the full governance
   surface for wavves' own writes here.
2. `wavves/rotations/` — newest file is the current position. None exists
   yet; this is the O0.R1 bootstrap term.
3. `wavves/registry.yml` — every chartered lane, status, home path.
4. The lane homes named by `INDEX.md`'s `active_lanes`.
5. `wavves/step-log.md` — append-only synthesis trace.
6. `wavves/skills/proposed/` and `wavves/skills/accepted/` — evidence-backed
   drafts and operator-approved project instructions. Never auto-installed.

Fresh instances hydrate from these files, never from chat transcripts.
Transcripts are keyword-search-only, and only when a rotation file cites one.

## 2. The three roles (never collapse)

- **O0 (this thread)** is operator-facing: charters lanes, background-
  dispatches **wave orchestrators**, reconciles on notify, lands git.
  Never executes charge work inline when a dispatch fits. Never polls.
  After deploy: release the operator window (`O0_release_window`).
- **wave orchestrator** fans out **charge workers**, integrates, writes
  rollup+gate. Illegal: `return_to_O0` after only launching children;
  solo multi-charge BUILD; poll. Yield requires
  `findings/<wave>-orch-checkpoint.md`.
- **charge worker** takes one bounded disjoint task each, no shared-file
  collisions; never git; escalate to O0 via the wave orch.

**Moderator (O0) background etiquette**

1. Dispatch wave orchestrators background.
2. `O0_release_window` after charter + deploy (+ AUTH/git if that is the land).
3. No poll / “check again shortly.”
4. Reconcile then land on notify; do not re-do charge work in O0.
5. Resume is fail remediation only (from `findings/<wave>-orch-checkpoint.md`).
6. Brief note of what was backgrounded; progress theater is a fail
   (`PROC-MOD-PROGRESS-THEATER`). Inline BUILD / foreground await →
   `PROC-MOD-FOREGROUND-HOLD`.

Canonical fan-out + leave-acts: `skills/charter/SKILL.md` Roles.

## 3. Etiquette locks (carried into every charter and dispatch)

Portable locks (unchanged from the wavves-init template):

- Honesty. Modeled-not-measured labeling, no reassurance bias, failed gates
  reported as failed, evidence transcribed not asserted. Visual claims
  require looking at rendered output before claiming done.
- Anomalies. Check actual values against baselines before calling a warning
  benign. Say plainly when something is unknown; require a citable source
  before calling a behavior expected or safe.
- Returns. Never trust a return that arrives implausibly fast or with
  implausibly low output volume. When a defect invalidated earlier output,
  re-run the full pass and overwrite the poisoned artifacts.
- Reporting. Report the full result distribution alongside any gate
  statistic. Claims trace to findings files, quoted verbatim. Cross-domain
  analogies are labeled as analogies.
- Adversarial gates. Independent evaluator with no authorship of the work
  under review, runnable checks, evidence to `gate-captures/`, capped
  remediation loops, then escalate.
- Prose gates. Plain, direct, observation-driven language. No filler,
  synthetic-contrast framing, or promotional tone. No double dashes or em
  dashes in operator-facing prose; use plain punctuation instead.
- Git. Runners never commit. O0 commits per repo protocol below and treats
  work as incomplete until push is verified.
- Git concurrency. Record the dispatch base commit. Never land commits on a
  branch a dispatched agent is actively editing.
- Cross-actor artifacts. An artifact meant for another actor is published to
  shared repo state before cross-actor use.
- Judgment calls that belong to the operator are never inferred by agents.
  Operator-gated actions always pause for the operator.
- Escalations. At an access or permission boundary, transcribe the block
  evidence, record resolution options, stop.
- Outbound deliverables. Leak-scan before anything leaves the house
  (credentials, internal paths, private facts).
- Skill lifecycle. Lane orchestrators draft project skills only as proposals
  under `wavves/skills/proposed/`. The moderator reviews and asks the
  operator before promoting to `wavves/skills/accepted/` or editing an
  installed skill under `skills/` at repo root.
- Model routing. Record recommended model tiers before dispatch.

## House bindings for wavves_build (filled in concretely)

- **Repo identity.** This is the wavves Cursor plugin's own source repo
  (`.cursor-plugin/plugin.json`, `skills/`, `README.md`, `LICENSE`,
  `index.html`, `CNAME`, `assets/`). Lanes chartered here edit the plugin's
  own skill files, homepage, or docs. There is no separate consuming
  project; wavves is bootstrapping its own home to develop itself.
- **Gated surfaces.** `git push` to `origin/main` is the operator-gated
  mutation, because it is also the publish surface for the GitHub Pages
  homepage (`index.html` + `CNAME`) and the source of truth for the plugin
  marketplace listing. No commit or push happens unless the operator
  explicitly asks.
- **Skill-file edits are lane-scoped, not silent.** Any edit to an
  **installed, already-shipped skill file** under `skills/*/SKILL.md` is
  itself a gated mutation: draft it as a new file or a clearly-marked patch
  in the lane's `findings/`, get it verified per the lane's acceptance
  criteria, then let O0 apply it to the real skill file only after the gate
  passes and only as part of the reconciled return.
- **No production infra, no destructive infra locks needed.** This repo has
  no servers, databases, or deployed services beyond the static GitHub Pages
  site. The only irreversible action is a push to `main`.
- **Timezone.** America/New_York (UTC-4 as of this bootstrap) for all dates
  and times unless an artifact states otherwise.
- **Prose style.** Plain, direct, observation-driven. No smug narrative
  devices, no double dashes, no hedging filler ("might", "could lead to",
  "perhaps"). This applies to every operator-facing return, README, and
  homepage copy this house produces.

## 4. Identity and rotation terms

Term identity `O0.R<N>`, assigned by handoff, never self-chosen. This
instance takes `O0.R1` by the bootstrap act itself (recorded in
`step-log.md`'s first entry). Every later identity comes from a rotation
file's "Successor identity" block. Stale-term artifacts are historical
record only; the newest rotation file and this file govern on conflict.

## 5. Rotation contract

An outgoing orchestrator writes
`rotations/rotation-r<NN>-<YYYYMMDD>-<HHMM>.md` (NN = outgoing term) naming
successor identity, positions with commit hashes, active background
dispatches, blocked items, uncommitted local state, and operator-pending
decisions, then returns a commit plan. Commits and pushes only when the
operator explicitly asks (see gated surfaces above).

## 6. Skills that implement the system

- `wavves` (`/wavves`) — default entry, playbook routing.
- `charter` (`/charter`) — chartering and dispatching lanes.
- `mod-check` (`/mod-check`) — adversarial sanity-check of a landed spec or
  plan before implementation.
- `mod-decide` (`/mod-decide`) — locking open calls after a check return,
  before a BUILD charter.
- `mod-rotate` (`/mod-rotate`) — producing the next rotation handoff.
- `wavves-init` (`/wavves-init`) — this file's own bootstrap skill.

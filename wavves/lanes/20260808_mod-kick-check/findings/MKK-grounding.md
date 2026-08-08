# MKK-W1a grounding

- **lens:** grounding
- **artifact:** `feature-requests/20260808_mod-kick.md` (**WORKING-TREE / uncommitted**; `git status` shows `??`)
- **repo:** `/Users/gilraitses/wavves_build` branch `main`
- **HEAD measured:** `b7ce95f075e89183a49e0486b6764ec299aeecac` (matches waveset `repo_state_verified_against`)
- **scope:** claims vs live seams; paths; hashes; FR index; foreign apps evidence

## Verified (no gap)

| claim / seam | evidence |
|---|---|
| Check HEAD pin is live | `git rev-parse HEAD` = `b7ce95f…aeecac`; waveset L13 matches |
| Contrast product `/mod-rotate` exists and is same-O0 continuity | `skills/mod-rotate/SKILL.md` (rotation file / O0.R(N+1) / same-orchestrator paste); FR Problem + non-goals match |
| Router has rotate + pickup (hydrate) today; no `/mod-kick` yet | `skills/wavves/SKILL.md` routing table; leaf table ends at `mod-rotate` |
| Usage grid lists `/mod-rotate`, not kick | `examples/usage.md` Skills / Playbooks / Quick reference |
| Standing AGENTS lists rotate, not kick | `wavves/AGENTS.md` §6 |
| Eval fixture pattern for new PROC-* ids exists | `evals/README.md` (disjoint harnesses: proceed-all-standing, proof-before-accept, wave-orch) |
| Cited hydrate seams resolve | `skills/mod-rotate/SKILL.md`, `skills/wavves/SKILL.md`, `skills/wavves-init/SKILL.md`, `examples/usage.md`, `wavves/AGENTS.md`, `evals/README.md`, `feature-requests/README.md`, `feature-requests/20260723_proceed-all-standing.md` |
| FR does not claim `skills/mod-kick/` already shipped | Product surface says **new** skill + playbook (targets, not present files) |
| Playbook dir convention (house) | Live playbooks under `skills/wavves/playbooks/` (`kick.md` absent; expected pre-BUILD) |

## Named gaps

### G-ARTIFACT-WT — FR not on origin/main

- **Claim surface:** waveset Artifact block + dispatch NOTE
- **Measured:** `feature-requests/20260808_mod-kick.md` is `??` (untracked). Not in `b7ce95f`.
- **Gap:** Any reviewer or successor that rehydrates at HEAD alone cannot read the artifact. Working-tree check is allowed by waveset, but publication of the FR itself is not done.

### G-INDEX-WT — index row only in dirty README

- **Claim:** waveset L14 `index: feature-requests/README.md row FR-20260808-mod-kick`; FR id `FR-20260808`
- **Measured:** Working-tree `feature-requests/README.md` has the row (`M`, +1 line). `git show HEAD:feature-requests/README.md` ends at FR-20260724-gate-outcome-invocables; **no** FR-20260808 row at HEAD.
- **Gap:** Index match is true only against the uncommitted README, not against `repo_state_verified_against`. Waveset does not label the index row as working-tree.

### G-APPS-HASH — `e6f25cf…` unverifiable from this repo

- **Claim:** FR L17–18 `evidence_verified_against: apps e6f25cf70016af3c78cfb31fcc4c4628c6f7f488` (CCR W0–W5 land; kick paste validated)
- **Measured:** In `wavves_build`, `git cat-file -t e6f25cf70016af3c78cfb31fcc4c4628c6f7f488` → fatal (object absent). Same hash **is** a commit in `/Users/gilraitses/applications-for-jobs` (`CCR W0–W5: …`).
- **Gap:** Source-evidence pin is foreign-repo-only. Unlike `feature-requests/20260723_proceed-all-standing.md` (which labels outside-repo pins **illustration only**), this FR presents the apps hash as verified evidence without that label and without an auth/path model for BUILD consumers of wavves_build alone.
- **Dispatch alignment:** dispatch L31–33: apps CCR is illustration only; flag foreign-repo hard-deps. This pin is currently over-claimed for a wavves_build-only rehydrate.

### G-DEFAULT-UX-APPS — default pickup hardcodes foreign repo

- **Claim:** FR Default operator UX L66 `[default: applications-for-jobs]`
- **Measured:** `applications-for-jobs` is not a lane `repos:` entry in this plugin repo; wavves_build AGENTS identity is the plugin source (`wavves/AGENTS.md` house bindings).
- **Gap:** UX sketch teaches a foreign default as if it were the house default. Illustration bleed into the product template. Risks BUILD agents baking apps as default without lane `repos:` primary logic (KICK-02 text is correct; the UX block contradicts it by example).

### G-PASTE-CCR — paste contract hardcodes apps CCR read-order

- **Claim:** Paste contract L79–80 MUST include ordered read list `(return / rankings / queue / adversarial / Ready drafts)`
- **Measured:** Those names are not wavves lane/file conventions (`waveset`, `findings/`, `rotations/`, `gate-captures/`). They match originating apps CCR session vocabulary.
- **Gap:** Minimum paste contract is not grounded as a portable wavves product seam. Treat as originating-session example or parameterize by lane artifact types.

### G-RECEIPT-SEAMS — invented receipt / vendor paths

- **Claim:** KICK-06 `<lane>/moderator_handoffs/KICK_<YYYYMMDD>_<HHMM>.md` or `wavves/kicks/`; KICK-04 `desktop_staging` / `findings/deps/`
- **Measured:** No `moderator_handoffs/`, `wavves/kicks/`, `desktop_staging/`, or `findings/deps/` under wavves_build. Existing continuity homes: `wavves/rotations/`, `wavves/handoffs/` (e.g. `20260723_set-key_docs_version_bump.md`), lane `findings/`.
- **Gap:** Receipt/vendor targets are proposed without binding to an existing house path (Open call 1 acknowledges the fork, but the sketch still asserts `moderator_handoffs` as if named). Grounding requires either map to `wavves/handoffs/` / lane `findings/` or mark paths as **new seams to create** under decide.

### G-PICKUP-NAME-COLLISION — “pickup” already means rotate-hydrate

- **Claim:** Feature name / framing “cross-environment pickup”; KICK-07 register next to `/mod-rotate`
- **Measured:** Router `pickup` playbook = hydrate from **rotation** paste (`skills/wavves/playbooks/pickup.md`; `skills/wavves/SKILL.md` L45). Distinct from proposed `/mod-kick`.
- **Gap:** Not a false path, but product language “pickup” already owns a playbook. FR distinguishes rotate vs kick well; it does **not** distinguish kick vs existing `pickup` playbook in router/usage targets. Successor agents may route `/wavves pickup` to the wrong leaf.

### G-PLAYBOOK-PATH — shorthand OK, full path unstated

- **Claim:** Product surface `playbooks/kick.md`
- **Measured:** House playbooks live at `skills/wavves/playbooks/*.md`. Peer FRs often use the same shorthand (`playbooks/proceed.md`).
- **Gap:** Mild. Prefer explicit `skills/wavves/playbooks/kick.md` (as proof-before-accept / WOF FRs sometimes do) so BUILD does not invent repo-root `playbooks/`.

## Non-gaps (explicit)

- Missing `skills/mod-kick/SKILL.md` / `kick.md` today = expected for `ready-for-mod-check`, not a grounding miss.
- `repo_state_verified_against` on the **check lane** is not stale vs measured HEAD.
- FR index **id string** `FR-20260808-mod-kick` matches filename slug when the dirty README is included.
- KICK-08 fail ids are proposed; no claim they already exist in `evals/fixtures/`.

## Lens lean

**REVISE**

Blockers for GO on grounding alone: label or drop foreign apps `e6f25cf` pin (or cite illustration-only + path); fix Default UX default to lane-primary not hard-coded apps; de-apps the paste-contract MUST list; name receipt paths against house seams or mark new; cite FR + index as working-tree; disambiguate kick vs router `pickup`.

No pure path-fabrication of cited hydrate seams; contrast with `/mod-rotate` is grounded. Not **BLOCK** unless O0 treats unverifiable foreign evidence + apps-shaped paste MUST as hard gates for this check.

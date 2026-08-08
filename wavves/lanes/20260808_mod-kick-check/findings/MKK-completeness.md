# MKK-W1c — completeness

- **Lens:** completeness
- **Artifact:** `feature-requests/20260808_mod-kick.md` (working-tree;
  uncommitted at check; `git status` shows `??`)
- **Repo state (dispatch):** `b7ce95f075e89183a49e0486b6764ec299aeecac`
- **Hydrated:** waveset.md, dispatch.md, full FR;
  `evals/README.md`, `examples/usage.md`,
  `skills/mod-rotate/SKILL.md`, `skills/wavves/SKILL.md` (routing table),
  `skills/wavves/playbooks/rotate.md`, `wavves/AGENTS.md` (rotate row),
  `.cursor-plugin/plugin.json`, `README.md` (install paths),
  `feature-requests/README.md` index row, `skills/mod-check/SKILL.md`
  (completeness hunt list)
- **Lens verdict recommendation:** **REVISE**
- **Blocker count:** 7 blocking gaps; 4 non-blocking
- **statement:** read-only; no git; wrote only this findings file
- **Escalation:** O0 only

## Verdict (this lens only)

REVISE. Problem, kick-vs-rotate split, three PROC-KICK fail ids, and the
default UX sketch are product-shaped enough for `/mod-decide`. The FR is not
complete enough to charter BUILD: thin-deps threshold is an open call while
VENDOR is already a ship surface; Acceptance can green without locking open
calls; lane vs no-lane applicability is unowned; paste readback constraints
are prose-only; Cursor slash leaf / plugin install surfaces are incomplete;
eval fixture homes are unnamed; rollback is absent.

O0 owns the lane verdict. Not BLOCK: intent and non-collapse with rotate are
already clear. Not GO: BUILD would invent thresholds, when-to-kick, paste
limits, and plugin ship edges.

---

## Blocking gaps

### B1 — Thin-deps threshold undefined while VENDOR ships (ship-blocker)

**Evidence:** KICK-04 offers `VENDOR_INTO_PICKUP` for “thin tracked deps (few
files, already cited by hash).” Non-goals: “thin deps only; else multi-repo
auth.” Open call #3 asks for max size / file-count threshold. Acceptance
requires multi/vendor auth lines and KICK-01…08, **not** a frozen threshold.
No fail id for over-threshold silent vendor (only `PROC-KICK-VENDOR-SILENT`
= vendor without auth).

**Gap:** “Thin” is undefined. File-count, total bytes, path-globs, and
“already cited by hash” are not measurable. BUILD can implement any heuristic
and still check the Acceptance box for KICK-04.

**Why blocking:** Open call #3 is the ship gate for option D in the UX and
for non-goal “not silent vendoring of large secondary trees.” Leaving it
unlocked while VENDOR remains in the required sketch means Acceptance cannot
fail an over-wide vendor. Same class as PAS standing-schema OR-paths: decide
must freeze before BUILD, or VENDOR must leave v0 Acceptance.

**Needed edit:** Freeze numeric/path threshold (or defer VENDOR to post-v0
with explicit non-goal). Add AC: over-threshold → refuse vendor, require
MULTI_REPO_AUTH (named fail id optional). Map open call #3 out of “optional
decide” into **BUILD unlock**.

### B2 — Acceptance insufficient for BUILD charter

**Evidence:** Six Acceptance checkboxes (KICK-01…08, default UX, multi/vendor
auth, LOCAL_ONLY, rotate diff in usage, three eval fixtures).

**Missing AC (testable):**

| missing AC | why it matters |
|---|---|
| Thin-deps threshold locked (or VENDOR deferred) | closes B1 |
| Receipt home frozen (lane vs `wavves/kicks/`) | open call #1; KICK-06 OR |
| Commit/push protocol locked per repo class | open call #2; KICK-01 forks |
| When kick applies: active lane vs no-lane / mid-wave / INT-only | closes B3 |
| Paste max length / line count / readback constraints | closes B4 |
| `skills/mod-kick/SKILL.md` frontmatter + `disable-model-invocation: true` | closes B5 |
| Plugin meta: `.cursor-plugin/plugin.json` keywords + version; CHANGELOG; README/usage/AGENTS rows; local install re-copy note | closes B5 |
| Playbook path frozen as `skills/wavves/playbooks/kick.md` | product surface says bare `playbooks/kick.md` |
| Eval fixture home + runner named | closes B6 |
| Fail ids appear in skill/playbook (not only FR Problem) | fixtures assert them |
| Rollback / bad-kick recovery rule | closes B7 |

**Why blocking:** A BUILD waveset copied from today’s bullets can green on
skill prose + three narrative fixtures while thresholds, applicability,
paste limits, and plugin install remain inventable.

### B3 — When kick applies (lane vs no-lane) unowned

**Evidence:** Problem: “After a waveset lands (or INT is ready).” KICK-02
default = “lane `repos:` primary (or sole dirty repo)” — lane-shaped.
KICK-06 receipt: `<lane>/moderator_handoffs/…` **or** `wavves/kicks/` when
no lane. UX default example: `applications-for-jobs`. No trigger table. No
rule for mid-wave kick, check-only lane, empty dirty tree, or kick with no
active registry lane. Open call #1 only asks receipt home, not applicability.

**Gaps:**

1. **No active lane:** Is `/mod-kick` valid? What surfaces are “lane-owned”
   to publish (KICK-01)? What is the default pickup repo without `repos:`?
2. **Mid-wave / before INT:** Allowed, refused, or LOCAL_ONLY-only?
3. **Trigger phrases:** Only `/mod-kick`, or also natural language (“hand
   off to another environment”)? Unowned → router invent.
4. **Relationship to pickup playbook:** Successor hydrate path unnamed
   (`/wavves hydrate` vs raw file list). Completeness: kick paste contract
   does not say which leaf the successor must invoke.

**Why blocking:** BUILD agents will invent scope. No-lane path is mentioned
only as a receipt OR, not as a product mode with publish rules.

**Needed edit:** Applicability table (lane active / no lane / mid-wave) +
refuse conditions; freeze default-repo algorithm for no-lane; name successor
entry command.

### B4 — Paste length / readback constraints underspecified

**Evidence:** KICK-05: “paste-ready one-liner (and optional short block)…
Optimized for read-aloud.” Paste contract lists five must-include fields +
optional second line for MULTI/VENDOR. No max characters, no max lines, no
max path count in the read-order list, no TTS/voice truncation rule, no
ban on secrets/local absolute paths in the paste body. Ordered-read example
(“return / rankings / queue / adversarial / Ready drafts”) is CCR-shaped,
not a general schema.

**Gap:** Product identity includes phone / voice readback / non-visual
discuss. Without measurable paste limits, BUILD can emit multi-paragraph
dumps that fail the originating ask while still matching the five bullets.

**Why blocking for this product:** Read-aloud is not a soft preference; it
is in Problem + KICK-05. Completeness requires a pass metric (e.g. ≤N chars
or ≤2 lines for the one-liner; long body only in receipt on disk).

**Needed edit:** Freeze paste schema: one-liner max length; optional block
max lines; read-order = paths relative to pickup repo only; secrets never in
paste; full lists live in receipt if over limit.

### B5 — Cursor slash leaf + plugin install path incomplete

**Evidence:** Product surface names `mod-kick` skill + `playbooks/kick.md` +
router/usage/AGENTS. Option B required: skill + playbook + router/usage/
AGENTS + evals. Live plugin: `.cursor-plugin/plugin.json` points
`"skills": "./skills/"` (no `commands/` directory in this repo; slash leaves
are skill folders). Sibling leaves (`mod-rotate`, `shrug`, `set-key`) use
YAML frontmatter + `disable-model-invocation: true`. README install:
marketplace `/add-plugin wavves` or copy to `~/.cursor/plugins/local/wavves/`.
Shipped siblings bump `plugin.json` version + keywords + CHANGELOG (e.g.
0.4.1 shrug). FR Acceptance never names frontmatter, plugin.json, version,
CHANGELOG, README skill inventory, or reinstall/reload after land.
Playbook path is relative-ambiguous (`playbooks/kick.md` vs
`skills/wavves/playbooks/kick.md`).

**Gap:** `/mod-kick` will not appear for operators until the skill leaf lands
**and** the installed plugin copy is refreshed. FR treats “skill lands” as
done without the install/version seam. Bare playbook path can land in the
wrong tree.

**Why blocking:** Unowned ship edge: repo main can claim Acceptance while
local/marketplace plugin still has no `/mod-kick`. Same class as PAS B3
(router wiring unnamed) — surface named in sketch, missing from AC.

**Needed edit:** AC bullets: `skills/mod-kick/SKILL.md` with
`disable-model-invocation: true`; playbook at
`skills/wavves/playbooks/kick.md`; patch `skills/wavves/SKILL.md` routing +
description; `examples/usage.md` + `wavves/AGENTS.md`;
`.cursor-plugin/plugin.json` keywords + version bump; CHANGELOG; README note
that local installs must re-copy / reload plugin.

### B6 — Eval fixture homes and runner unnamed

**Evidence:** KICK-08 + Acceptance: three fixtures for
`PROC-KICK-NO-PUBLISH`, `PROC-KICK-MULTI-SILENT`, `PROC-KICK-VENDOR-SILENT`.
`evals/README.md`: lens-keyword `run_fixtures.py` is **not** a behavioral
kick checker; disjoint mechanical harnesses use prefixes
(`paragraph-tunnel-*`, `proof-before-accept-*`, `wave-orch-fanout-*`,
`proceed-all-standing-*` pattern from sibling FRs). FR never names
`evals/fixtures/mod-kick-*/` (or similar), checker script, or pass command.

**Gap:** Acceptance can be “documented” without a runnable corpus. Dropping
cases into `run_fixtures.py` only tripwires lens wording, not publish/auth
behavior.

**Why blocking:** Same hole PAS/PBA hit. BUILD AC must name fixture home +
assertion mechanism (mechanical checker preferred for PROC-* ids) or
explicitly defer with a named non-goal and lane-local fixtures.

**Needed edit:** Name e.g. `evals/check_mod_kick.py` +
`evals/fixtures/mod-kick-*/` mapping each fail id; or defer mechanical
checker with explicit post-v0 non-goal and still require fixture specs under
lane/evals.

### B7 — Rollback / recovery absent

**Evidence:** Completeness hunt includes absent rollback / non-goals.
Non-goals cover: not rotate substitute; not Desktop-only; not auto-send;
not silent large vendor. No rollback for: publish already pushed then paste
wrong; VENDOR_INTO_PICKUP copied bad paths; LOCAL_ONLY paste used then
operator wants remote kick; receipt written with wrong hash; disable/withdraw
`/mod-kick` mis-trigger.

**Gap:** After a bad kick, BUILD has no recovery rule (revert vendor commit?
supersede receipt? emit corrected paste only?). Non-goals do not say kick
never force-pushes or never mutates foreign remotes beyond pickup.

**Why blocking (soft-hard):** For a product whose first act is commit+push
(KICK-01), missing rollback is a completeness fail on the publish edge.
Not as hard as B1–B6 if open call #2 locks “emit plan first” for ask-only
repos — still must state: wrong receipt → write superseding KICK_*; vendor
mistakes → operator-gated revert, no silent rewrite of history.

**Needed edit:** Short Rollback section: supersede receipt; never force-push;
LOCAL_ONLY does not authorize later silent push; vendor revert is
operator-gated.

---

## Non-blocking gaps

### N1 — Open calls listed but incomplete / under-ranked

**Evidence:** Open calls (1) receipt home (2) auto-commit vs plan-first
(3) thin-deps threshold.

**Present and decide-worthy:** all three.

**Under-ranked:** #3 is a ship-blocker for VENDOR (see B1), not a soft
prefer. #1–#2 are BUILD unlocks; Acceptance does not say “locks required
before charter.”

**Absent from open-call list (should be explicit):**

1. Lane vs no-lane applicability (B3)
2. Paste length / readback limits (B4)
3. Eval home + runner (B6)
4. Plugin version / install refresh (B5)
5. Successor entry command (`/wavves hydrate` vs paste-only file read)
6. Whether shrug/proceed may accept default pickup (KICK-02) without
   widening AUTH-10 / proceed-all-standing semantics

### N2 — Paste contract silently CCR-shaped

**Evidence:** Paste must-include #2: “return / rankings / queue / adversarial
/ Ready drafts.” Originating evidence is apps CCR. Product claims general
cross-environment exit.

**Call:** Generalize to “ordered paths relative to pickup repo (lane return
/ findings / locks as applicable)” or mark v0 apps-only (non-goal widen).

### N3 — Default UX hard-codes `applications-for-jobs`

**Evidence:** Default operator UX proposes
`Pickup repo? [default: applications-for-jobs]`. Dispatch: do not
hard-depend on applications-for-jobs paths for BUILD without auth model.

**Call:** Treat as illustration only; AC must use synthetic/local fixture
repos. Completeness flag: default algorithm = lane primary / sole dirty,
not a foreign repo name.

### N4 — Interaction with `/mod-rotate` and pickup coexistence thin

**Evidence:** Non-goals: not a rotate substitute. KICK-07: document diff in
usage grid. No rule for same-turn rotate+kick, or kick while rotation file
unpushed. Pickup playbook (`examples/usage.md` hydrate row) never cited as
successor seam.

**Call:** Non-blocking if B3 names successor entry and non-goals add
“kick does not assign O0.R(N+1).”

---

## Silent assumptions (call out)

1. Active lane always has a `repos:` primary (or sole dirty repo is obvious).
2. “Publish first” can stage “lane-owned surfaces” without a file inventory
   rule (what is in / out of the kick commit).
3. Successor has git remote access to the pickup repo at the cited hash.
4. Shrug / proceed may accept the proposed default pickup (KICK-02) without
   a kick-specific auth token — may collide with bare-shrug AUTH-10.
5. CCR read-order labels generalize to all lanes.
6. `desktop_staging` / `findings/deps/` are valid vendor targets in every
   pickup repo layout.
7. Three eval fixtures imply an in-repo harness will exist (homes unnamed;
   see B6).
8. Skill file alone makes `/mod-kick` invocable in operator Cursor without
   plugin reinstall (see B5).
9. Working-tree FR is ready-for-mod-check while still uncommitted (honest per
   dispatch; not a product gap).

---

## Non-goals coverage

**Present and useful:** not rotate substitute; not Desktop-only authority;
not auto-submit/send; not silent large vendor.

**Still thin / absent:**

- No rollback / supersede-receipt rule (B7)
- No explicit non-goal: kick does not assign rotation term identity
- No explicit non-goal: foreign apps CCR paths are illustration-only for
  BUILD fixtures
- No explicit defer of VENDOR if threshold stays open
- No statement that kick does not widen bare shrug into multi-repo auth
- Plugin install / version bump not listed as ship surface or non-goal

---

## Hunt checklist (dispatch-specific)

| hunt | result |
|---|---|
| Missing acceptance criteria? | **Yes** (B2) |
| Unowned edges? | **Yes** — lane/no-lane, receipt OR, commit protocol, paste limits, plugin meta (B3–B5) |
| Silent assumptions? | **Yes** (list above) |
| Absent rollback / non-goals coverage? | **Yes** — rollback absent; non-goals thin (B7) |
| Thin-deps threshold undefined as ship-blocker? | **Yes** (B1) |
| Cursor command leaf missing / incomplete? | **Partial** — skill named; frontmatter + plugin install/version AC missing (B5). Repo has no `commands/`; leaf = `skills/mod-kick/`. |
| Plugin install path? | **Absent from FR/AC** (B5); README documents marketplace + `~/.cursor/plugins/local/wavves/` |
| When kick applies (lane vs no-lane)? | **Unowned** (B3) |
| Paste length / readback constraints? | **Underspecified** (B4) |
| Open calls coverage? | **Listed but under-ranked / incomplete** (N1) |

---

## Covered adequately (for this lens)

- Problem: environment exit vs same-O0 rotate; fail ids proposed with
  plain-language definitions
- Feature sketch KICK-01…08 covers publish-first, single question, multi
  auth, vendor offer, paste, receipt, router, evals
- Default UX A–D options named
- Paste contract minimum field list (content, not length)
- Explicit non-goals skeleton (rotate / Desktop / auto-send / large vendor)
- Where it lands: option B required; alias-to-rotate rejected
- Open calls correctly park three forks for `/mod-decide` (need ranking)
- FR indexed in `feature-requests/README.md` as ready-for-mod-check
- Diff-from-rotate called out for usage grid (KICK-07)

---

## Recommended FR edits (for O0 / mod-decide; not applied)

1. Freeze thin-deps threshold **or** defer VENDOR from v0 Acceptance; treat
   open call #3 as BUILD unlock.
2. Expand Acceptance with: applicability table; paste limits; receipt home;
   commit protocol; skill frontmatter; playbook full path; plugin.json /
   version / CHANGELOG / reinstall; eval home+runner; rollback note.
3. Add applicability: lane vs no-lane vs mid-wave refuse rules; successor
   entry command.
4. Name `evals/check_mod_kick.py` + `evals/fixtures/mod-kick-*/` (or defer).
5. Generalize paste read-order; mark apps CCR labels as illustration.
6. Rewrite open calls: promote threshold + receipt + commit protocol; add
   applicability, paste limits, eval home, plugin ship, shrug-accept rule.
7. Add Rollback: supersede receipt; no force-push; vendor revert gated.

---

## Commit file list (for O0; no git performed)

- Write: `wavves/lanes/20260808_mod-kick-check/findings/MKK-completeness.md`
- Exclude: none
- **No git actions performed.**

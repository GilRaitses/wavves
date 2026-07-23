# WOF-W1c — completeness

- **Lens:** completeness
- **Artifact:** `feature-requests/20260723_wave-orchestrator-fanout.md`
- **Repo state (dispatch):** `26ad2d2afbb9196f2b690000f6a50f1cabfe20e5`
- **Hydrated:** waveset.md, dispatch.md, artifact;
  `skills/wavves/SKILL.md`, `skills/charter/SKILL.md`,
  `skills/wavves/playbooks/charter-lane.md`,
  `skills/wavves/playbooks/proceed.md`,
  `skills/wavves-init/SKILL.md` (Roles template),
  `README.md`, `feature-requests/README.md`,
  `feature-requests/20260718_proof-before-accept_ORIGINATING-MOD-FEEDBACK.md`,
  `evals/README.md`, `skills/set-key/SKILL.md` (densify aside),
  `skills/mod-check/SKILL.md` (lens hunt list),
  `wavves/failure_log.yml` (header only)
- **Lens verdict recommendation:** **REVISE**
- **Blocker count:** 6 blocking gaps; 4 non-blocking
- **statement:** read-only; no git; no code edits outside this findings file
- **Escalation:** O0 only

## Verdict (this lens only)

REVISE. Problem, four fail ids, three-role split, and moderator etiquette
are product-shaped enough for `/mod-decide`. The FR is not complete enough
to charter BUILD: eval fixture homes are unnamed, Acceptance omits
`PROC-ORCH-FOREGROUND-HOLD` from the eval bullet, dispatch-template and
charter-skill wiring homes are unowned, the wavves-init AGENTS path is not
filesystem-named, OF-09 playbook edits are sketch-only, and the
mid-dispatch vs background conflict is an Acceptance checkbox without
resolved text.

O0 owns the lane verdict. Not BLOCK: intent and non-goals skeleton are
clear. Not GO: BUILD would invent eval shape, paste-template home, and
role-table landing surfaces.

---

## Blocking gaps

### B1 — Eval fixture homes and runner unnamed

**Evidence:** OF-07: "Fixture: fake 3-charge dispatch → assert ≥2 parallel
workers after first PASS; assert no early orchestrator return; assert no
solo multi-charge BUILD." Acceptance: eval/fixture for three fail ids.
`evals/README.md` shows three harness families (`run_fixtures.py`,
`check_paragraph_tunnel.py` / `paragraph-tunnel-*`,
`check_proof_before_accept.py` / `proof-before-accept-*`). No
wave-orchestrator-fanout prefix, checker script, or fixture layout exists
today. FR never names home, prefix, `input.md`/`expected.md` vs mechanical
checker, or pass command.

**Gap:** Acceptance can green on narrative prose. Live Task fan-out is not
assertable by the current keyword tripwire alone; without a named home,
BUILD invents or skips the gate.

**Why blocking:** Same class of hole PBA/PTG/PAS hit: BUILD AC must name
fixture home + assertion mechanism (or explicit defer with a named
non-goal).

**Needed edit:** Name e.g. `evals/fixtures/wave-orch-fanout-*/` + stdlib
checker (or explicit defer). Map each Acceptance eval bullet to a case id
and expected fail id / PASS shape. State that mechanical PASS ≠ live Cursor
Task fan-out judgment.

### B2 — `PROC-ORCH-FOREGROUND-HOLD` missing from eval Acceptance

**Evidence:** Problem names four fail ids:
`PROC-ORCH-SOLO-BUILD`, `PROC-ORCH-EARLY-EXIT`,
`PROC-ORCH-FOREGROUND-HOLD`, `PROC-MOD-FOREGROUND-HOLD`.
Acceptance docs bullet: "README + SKILL name … and the four fail ids"
(covers docs). Acceptance eval bullet lists only
`PROC-ORCH-EARLY-EXIT`, `PROC-ORCH-SOLO-BUILD`, and
`PROC-MOD-FOREGROUND-HOLD`. OF-07 asserts early-exit and solo-build only;
no fixture assertion for orchestrator/worker foreground BUILD hold.

**Gap:** Docs can name all four while eval never covers
`PROC-ORCH-FOREGROUND-HOLD`. OF-03 (background rule for workers + wave
orchestrator launches) has no matching AC case.

**Why blocking:** Completeness of fail-id coverage requires parity: if the
id is product, either name an eval case or explicitly defer it with reason.

**Needed edit:** Add `PROC-ORCH-FOREGROUND-HOLD` to the eval Acceptance
bullet and OF-07, or mark it docs-only / deferred under Non-goals with a
cite.

### B3 — Dispatch paste template filesystem home unnamed

**Evidence:** OF-05: Default "You are" block with `role: wave_orchestrator`,
"Do not execute charges yourself", critical-path `a → (b‖c) → d`.
Acceptance: "Dispatch paste template includes fan-out + background +
no-early-exit." Product surface says "charter/dispatch templates" without a
path. Live paste guidance lives mainly in `skills/charter/SKILL.md`
(dispatch mechanics, three-role table) and per-lane `dispatch-w{N}.md`
files; no single template file is named.

**Gap:** Unowned whether BUILD edits charter skill prose, adds a snippet
under `skills/wavves/playbooks/`, ships a `dispatch-template.md`, or only
documents an example in README.

**Why blocking:** Without a named home, Acceptance can PASS on README prose
while live dispatches keep solo-builder paste blocks.

**Needed edit:** Lock one landing path (recommend: default block in
`skills/charter/SKILL.md` Dispatch mechanics + one canonical example
snippet path) and put that path in Acceptance.

### B4 — Router / wiring seam: `skills/charter/SKILL.md` unowned

**Evidence:** Sketch OF-01 names `skills/wavves/SKILL.md` + README Roles.
OF-09 names proceed/charter playbooks (one line each). Live three-role
table and O0 background/reconcile rules that agents actually hydrate sit in
`skills/charter/SKILL.md` ("The three roles", Dispatch mechanics: "Then
continue or end the turn. reconcile on return."). Dispatch hydrate lists
charter skill as a seam; FR never puts it in the sketch table or
Acceptance.

**Gap:** Unowned whether BUILD patches charter skill (role rename to wave
orchestrator / charge worker, fan-out + no-early-exit + background), only
wavves skill + playbooks, or both. Acceptance "README + SKILL" is
ambiguous which SKILL.

**Why blocking:** Leaving charter skill untouched leaves the strongest
live orchestrator contract half-clear on fan-out (the originating O0.R3
gap). Acceptance can green without touching the seam that caused the fail.

**Needed edit:** Add OF row + Acceptance bullet: update
`skills/charter/SKILL.md` three-role table + dispatch mechanics for
fan-out / no-early-exit / worker background. Clarify "SKILL" in
Acceptance = wavves + charter (or list paths).

### B5 — Acceptance bullets insufficient for BUILD charter

**Evidence:** Seven Acceptance checkboxes. Sketch rows OF-01…09.

**Missing AC (testable):**

| missing AC | why it matters |
|---|---|
| `PROC-ORCH-FOREGROUND-HOLD` eval case (or explicit defer) | closes B2 |
| Named eval fixture prefix + pass command | closes B1 |
| Named dispatch paste template path | closes B3 |
| `skills/charter/SKILL.md` role + dispatch mechanics updated | closes B4 |
| OF-09: proceed.md + charter-lane.md one-liners present | sketch row with no AC |
| Mid-dispatch conflict: **resolved wording** frozen (not only "resolve") | AC is a process checkbox; BUILD needs the text |
| Filesystem AGENTS template path + live-home sync rule | closes B6 |
| Fail ids appended or cited in `wavves/failure_log.yml` shape (or non-goal) | proposed ids otherwise orphan |

**Why blocking:** A BUILD waveset copied from these bullets can green on
README/SKILL prose and a partial eval while charter skill, playbooks,
template path, and FOREGROUND-HOLD coverage remain inventable.

### B6 — AGENTS template path not filesystem-named; live home vs init fork

**Evidence:** OF-06: "`AGENTS.md` (plugin home template)". Acceptance:
"Home `AGENTS.md` Roles updated in wavves-init template (and pax home
synced when shipped)". Product name `wavves-init` is used; concrete path
`skills/wavves-init/SKILL.md` (section "What the standing AGENTS.md
contains" / "The three roles") is never written in the FR. Unowned:
whether this BUILD also patches live `wavves/AGENTS.md` in wavves_build
(and when), or only the init template for next installs. "pax home synced
when shipped" pulls a foreign repo into Acceptance while waveset Locked
says foreign pax evidence is illustration only.

**Gap:** BUILD file ownership for the Roles edit is ambiguous; pax sync as
Acceptance can block a wavves_build-only ship.

**Why blocking:** Completeness requires a named edit target and a clear
rule for already-initialized homes vs template-only.

**Needed edit:** Name `skills/wavves-init/SKILL.md` Roles section as the
template target. Lock live `wavves/AGENTS.md` in this repo: same BUILD vs
follow-on. Move "pax home synced when shipped" to Non-goals / operator
follow-on, not a wavves_build Acceptance hard gate.

---

## Non-blocking gaps

### N1 — Open calls for mod-decide absent / incomplete

**Evidence:** FR has no Next / open-calls section (unlike sibling
proceed-all-standing FR). Acceptance lists "Resolve wording conflict with
'no empty mid-dispatch return'" without framing it as a decide call.
Originating note
(`20260718_proof-before-accept_ORIGINATING-MOD-FEEDBACK.md`): "orchestrator
owns completion; no return until RECONCILE+GATE exist."

**Decide-worthy forks (should be explicit):**

1. Resolved etiquette text: workers background + orchestrator stays until
   rollup / integrate-on-notify (keep as decide until wording frozen in FR)
2. Eval home + runner vs explicit mechanical defer (add)
3. Dispatch template landing path (add; or freeze in FR)
4. Charter skill in-scope depth (add; or freeze in FR)
5. Live `wavves/AGENTS.md` same BUILD vs template-only (add)
6. Fresh-thread wave orchestrator allowed vs background-Task-only (add;
   see Silent assumptions)

**Call:** Add a Next / Open calls block for `/mod-decide` before BUILD
charter. Drop forks that get frozen by FR revise.

### N2 — Rollback / disable absent

**Evidence:** Completeness lens hunts absent rollback. Non-goals cover git
rules, auto-polling, max parallelism when shared write target, historical
dispatch rewrite, judgment pauses. No disable path if fan-out text causes
wrong depth (e.g. nested background orchestrators), no "revert skill prose
to prior Roles table" note, no failure_log regression append rule tied to
the four PROC-* ids.

**Call:** Soft: add Rollback note — operator can withdraw fan-out paste
requirements per lane; skill prose revert is ordinary skill lifecycle; new
fail ids append to `wavves/failure_log.yml` only when observed in a real
run (or document ids in skill without failure_log until first hit).

### N3 — Fresh-thread vs background Task for wave orchestrator unowned

**Evidence:** `skills/charter/SKILL.md` allows background subagent OR fresh
thread for dispatched orchestrator. FR OF-04: wave orchestrator must not
return until rollup. OF-08: O0 releases the operator window. If the wave
orchestrator is itself a fresh operator-facing thread, "stay until rollup"
occupies that chat for the full critical path.

**Gap:** Silent assumption that wave orchestrators are always
`run_in_background` Tasks. Fresh-thread path etiquette unset.

**Call:** Non-blocking if mod-decide locks background-Task-only for wave
orchestrators in v0; else document fresh-thread exception (stay for rollup
is not PROC-MOD-FOREGROUND-HOLD; charge workers still background).

### N4 — set-key densify cross-link not Acceptance-bound

**Evidence:** OF-08 requires cross-link so densify note is not the only
home for moderator etiquette. Acceptance requires etiquette block "not
buried under densify-only" but does not require the set-key pointer.

**Call:** Optional AC bullet: README/skill etiquette block is canonical;
`skills/set-key/SKILL.md` densify bullet links back. Non-blocking if OF-08
stays in sketch and BUILD waveset cites it.

---

## Silent assumptions (call out)

1. Charge independence is obvious from the dispatch table (no rule for
   "shared write target" beyond Non-goals max-parallelism exception).
2. Mechanism = Cursor Task / `run_in_background`; completion notifications
   reach the wave orchestrator so integrate-on-notify is real, not aspirational.
3. Wave orchestrator maps 1:1 onto today's "Dispatched orchestrator" role
   (rename/split), and "charge worker" maps onto "Wave subagents."
4. Critical-path shape `a → (b‖c) → d` is the default teaching example, not
   a required waveset topology.
5. O0 "release the window" is compatible with AUTH sync / git land in the
   same turn when that is the land (stated in etiquette point 2; not AC).
6. Mechanical or fixture harness will exist in-repo for OF-07 (homes
   unnamed; see B1).
7. "pax home synced when shipped" is operator follow-on, not a gate for
   wavves_build BUILD (contradicts Acceptance wording today; see B6).
8. Fresh-thread dispatched orchestrators are either forbidden or specially
   etiquette-bound (unowned; see N3).

---

## Non-goals coverage

**Present and useful:** no git-rule change; no auto-polling / session-
blocking waits; no forced max parallelism on shared write targets; no
mass rewrite of historical dispatches; gates still surface without
justifying foreground BUILD.

**Still thin:**

- No rollback / disable / skill-prose revert note
- No explicit non-goal that foreign pax paths are illustration-only for
  BUILD fixtures and for Acceptance (Acceptance currently asks for pax sync)
- No statement that live multi-agent Task fan-out cannot be fully proven by
  stdlib fixtures alone (known evals limitation; needs defer or hybrid AC)
- Fresh-thread wave orchestrator policy absent (see N3)

---

## Hunt checklist (dispatch-specific)

| hunt | result |
|---|---|
| Missing acceptance for BUILD charter? | **Yes** (B5) |
| Unowned edges (template / charter / playbooks)? | **Yes** (B3, B4, OF-09) |
| Silent assumptions called out? | **Yes** (list above) |
| Eval fixture homes named? | **No** (B1) |
| Router/wiring seams named? | **Partial** — wavves SKILL yes; charter SKILL no (B4) |
| Open calls for mod-decide explicit? | **No** (N1) |
| AGENTS template path named? | **Partial** — "wavves-init template" only; not `skills/wavves-init/SKILL.md` (B6) |
| `PROC-ORCH-FOREGROUND-HOLD` in Acceptance? | **Docs yes; eval no** (B2) |
| Rollback / non-goals gaps? | Thin (N2) |

---

## Covered adequately (for this lens)

- Problem: solo-builder, early-exit, foreground holds (orch + mod)
- Four proposed fail ids with plain-language definitions
- Six-point Moderator (O0) background etiquette block (OF-08 body)
- Three-role sketch: O0 → wave orchestrator → charge worker (OF-01)
- Fan-out / background / completion rules in sketch (OF-02…04)
- Non-goals skeleton (git, polling, shared-target parallelism, history,
  judgment pauses)
- Acceptance requires resolving mid-dispatch wording conflict (direction
  correct; text not frozen — see B5/N1)
- Originating evidence treated as illustration in waveset Locked
- FR indexed in `feature-requests/README.md` as ready-for-mod-check
- Explicit `/mod-check` before BUILD in Acceptance

---

## Recommended FR edits (for O0 / mod-decide; not applied)

1. Name eval fixture prefix + checker (or explicit defer); add
   `PROC-ORCH-FOREGROUND-HOLD` to eval AC / OF-07 or defer it.
2. Name dispatch paste template landing path; put path in Acceptance.
3. Own `skills/charter/SKILL.md` three-role + dispatch mechanics as a BUILD
   target; disambiguate "SKILL" in Acceptance.
4. Add OF-09 playbook one-liners to Acceptance
   (`playbooks/proceed.md`, `playbooks/charter-lane.md`).
5. Name `skills/wavves-init/SKILL.md` Roles section; lock live
   `wavves/AGENTS.md` sync rule; move pax sync out of Acceptance.
6. Freeze mid-dispatch vs background resolved wording in the FR body (not
   only an Acceptance checkbox).
7. Add Next / Open calls for `/mod-decide` (eval home, template path,
   charter depth, live AGENTS, fresh-thread policy).
8. (Non-blocking) Rollback note; set-key densify back-link AC; failure_log
   append policy for new PROC-* ids.

---

## Commit file list (for O0; no git performed)

- Write: `wavves/lanes/20260723_wave-orchestrator-fanout-check/findings/WOF-completeness.md`
- Exclude: none
- **No git actions performed.**

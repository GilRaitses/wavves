# MKK-W1e — proof-bar

```yaml
lens: proof-bar
wave_id: MKK-W1e
model: cursor-grok-4.5-high-fast
artifact: feature-requests/20260808_mod-kick.md
artifact_state: working-tree uncommitted (?? at check)
repo_state_verified_against: b7ce95f075e89183a49e0486b6764ec299aeecac
lane: wavves/lanes/20260808_mod-kick-check/
recommendation: REVISE
git: none (findings only; no FR edit; no commit)
```

## Scope of this lens

Hunts ACCEPT / eval criteria that can PASS without measuring a real
`proof_job`; chrome-only skill text with no frozen proof fields; missing
named harness for kick (publish verify + paste contract + fail-id fixtures);
debt-close treated as product done; whether KICK-08 evals alone suffice or
a live `/mod-kick` smoke is required. Does not invent a BUILD plan. Does
not re-litigate kick vs rotate product split.

Authority hydrated: `waveset.md`, `dispatch.md`, full FR Acceptance +
KICK-01…08, `skills/wavves/playbooks/proof-before-accept.md`,
`evals/README.md`. Contrast house plugin-meta Accept bars: PAS
(`check_proceed_all_standing.py`), WOF, PBA, GOI-proof-bar PB-01…03.

## Classifier (plugin-meta + runtime publish)

Kick ships a new slash skill + playbook + router/usage/AGENTS chrome +
eval fixtures inside wavves. Per `proof-before-accept.md` defaults,
plugin-meta is `proof_required: no` or `n/a` with one-line rationale; the
house Accept bar for that class is a **named stdlib mechanical fail-id
harness** (PAS / WOF / PBA pattern in `evals/README.md`), not DOM/host
`proof_host_probe`.

Kick is not pure docs: KICK-01’s product job is **publish-first** (push +
`origin` sync verify) before paste. That is a measurable runtime
`proof_job` even when `visual_accept: no`. Fixtures can seed synthetic
“paste while unpushed” receipts; they cannot alone prove live remote sync
or live slash-skill behavior. FR never declares `proof_required` /
`proof_job` / `proof_reference` / `chrome_freeze` / `visual_accept`.

## What is already on the right bar

1. **Closed fail ids** proposed: `PROC-KICK-NO-PUBLISH`,
   `PROC-KICK-MULTI-SILENT`, `PROC-KICK-VENDOR-SILENT` (FR Problem +
   KICK-08). Measurable vocab shape matches PAS/WOF.
2. **KICK-08** sketches three behavioral FAIL cases (paste without push;
   multi without auth; vendor without auth).
3. **Paste contract (minimum)** lists five successor fields (repo+hash,
   read-order, locks, next move, readback permission). Good candidate for
   a mechanical assert once harness exists.
4. **Non-goals** keep Desktop as supplement; kick authority is
   git-published pickup. Aligns with publish-first proof_job.
5. **Live corpus baseline** (`evals/check_*.py` at tip
   `b7ce95f…`): no kick checker yet. Expected pre-BUILD; FR must still
   **name** the home so ACCEPT cannot invent “fixtures somewhere.”

## Blocking gaps (proof-bar)

### PB-01 — ACCEPT can PASS without measuring a real proof_job

**Evidence:**

- FR Acceptance (done when shipped):
  - `/mod-kick` skill lands with KICK-01…08
  - default UX asks only for pickup repo
  - multi/vendor auth lines in receipt
  - paste refuses or LOCAL_ONLY-labels when not on remote
  - rotate diff in usage grid
  - “Eval fixtures for the three PROC-KICK fail ids”
- No Acceptance checkbox requires a named command PASS.
- No FR field names `proof_job` (one sentence) or freezes chrome vs
  proof-serving allowlist.
- First AC is surface land (skill chrome). Docs/usage grid greens are
  independent of publish verify.

**Why it fails this lens:** Same class as GOI PB-03 /
`PROC-PASS-NO-PROOF`: product completion can be claimed when skill text +
router rows + three fixture directories exist, without measuring publish
verify or paste-contract completeness. `evals/README.md` states mechanical
PASS ≠ live judgment; FR Acceptance does not even require mechanical PASS.

**Revise required:** Freeze one-line `proof_job` for BUILD Accept, e.g.
“`/mod-kick` refuses unlabeled paste until pickup remote sync PASS (or
LOCAL_ONLY-labeled), and emitted paste+receipt satisfy the paste contract
and auth lines.” Make harness PASS a hard Acceptance gate; chrome/docs
secondary.

### PB-02 — No named harness home (chrome-only skill text risk)

**Evidence:**

- KICK-08: “Fixture: … → FAIL …” prose only. **No** checker path, **No**
  fixture glob.
- Acceptance: “Eval fixtures for the three PROC-KICK fail ids” with no
  `python3 evals/check_….py`.
- Contrast PAS PS-10 + Acceptance: names
  `evals/check_proceed_all_standing.py` and
  `evals/fixtures/proceed-all-standing-*/`, and AC requires that command
  PASS.
- Contrast WOF OF-07 / PBA: named `check_wave_orchestrator_fanout.py` /
  `check_proof_before_accept.py` + fixture prefixes in `evals/README.md`.
- Tip corpus: `check_paragraph_tunnel.py`, `check_proceed_all_standing.py`,
  `check_proof_before_accept.py`, `check_public_copy.py`,
  `check_wave_orchestrator_fanout.py` only. No `check_mod_kick*` /
  `check_kick*`. No `skills/mod-kick/SKILL.md`, no
  `playbooks/kick.md` yet (chrome not shipped; FR still must name harness).

**Why it fails this lens:** Without a frozen harness path, BUILD ACCEPT
can PASS on skill + playbook + router chrome while never measuring
fail-id tripwires or paste-contract fields.

**Revise required:** Name checker + fixture prefix in KICK-08 and
Acceptance (PAS style). Example shape (lock exact names in FR / mod-decide):

- `evals/check_mod_kick.py`
- `evals/fixtures/mod-kick-*/` (or `kick-*`)
- Acceptance: `python3 evals/check_mod_kick.py` PASS

Harness scope must cover at least:

| measure | minimum fixture / assert |
|---|---|
| publish verify | paste emitted while pickup unpushed / not synced → FAIL `PROC-KICK-NO-PUBLISH`; LOCAL_ONLY path must label |
| paste contract | successor paste missing hash / read-order / locks / next / readback → FAIL (new id or fold under NO-PUBLISH/contract id) |
| fail-id fixtures | one case each for MULTI-SILENT and VENDOR-SILENT |

### PB-03 — KICK-08 evals alone do not suffice; live `/mod-kick` smoke required

**Evidence:**

- KICK-01 product job: push + verify `origin` sync before paste.
- `evals/README.md` known limitation (lens-wording / mechanical tripwire):
  PASS means fixture encoding still trips, not that a live agent run
  produces the verdict.
- PBA playbook: for `proof_required: yes` product Accept, mechanical
  checker alone is incomplete (host probe + capture). Kick is plugin-meta
  (no DOM), but publish-first is still a **live** remote/runtime seam.
- FR Acceptance never requires a live smoke: invoke `/mod-kick` (or
  scripted skill steps) against a disposable / labeled pickup, capture
  receipt + paste, remeasure remote hash sync (or LOCAL_ONLY label).

**Why it fails this lens:** Three synthetic fail-id fixtures can green
while live kick still emits paste against unpushed paths, or ships paste
that omits contract fields the fixture never asserted. Treating KICK-08
fixture green as product done is chrome/debt Accept.

**Revise required:** Split Accept bar explicitly:

1. **Mechanical (required):** named `check_mod_kick.py` PASS on fail-id +
   paste-contract fixtures.
2. **Live smoke (required for BUILD ACCEPT, review/live class):** one
   recorded `/mod-kick` (or equivalent step script) with receipt path,
   paste body, and publish remeasure (`origin` sync hash or LOCAL_ONLY
   label). Capture under lane `gate-captures/` or kick receipt. Do not
   ACCEPT on fixtures alone.
3. Label live smoke as review/live (not sole fixture-script green), same
   grain as PBA review/live ids vs mechanical.

### PB-04 — Debt-close / originating CCR treated as Accept evidence risk

**Evidence:**

- FR `evidence_verified_against`: apps CCR land + “kick paste pattern
  validated same session.” That is originating illustration, not BUILD
  Accept measurement.
- Open calls (receipt home; auto-commit vs plan-first; thin-deps
  threshold) are deferred to `/mod-decide`. Closing those calls without
  harness+smoke still leaves product unmeasured.
- Option B “required” lands skill+fixtures; without PB-01…03 locks,
  “FR open calls decided + skill file present” can be mistaken for done
  (`PROC-DEBT-AS-DONE` class).

**Why it fails this lens:** Originating ad-hoc one-liner success is debt
context, not proof_job evidence. Decide-locks alone are not Accept.

**Revise required:** State in FR Acceptance or BUILD Meta: originating CCR
evidence is illustration only; Accept = named harness PASS + live smoke
capture. Forbid treating decide closure or skill file presence alone as
ACCEPT-complete.

## Non-blocking / clear

- **DOM/host `proof_host_probe`:** Not required for this plugin-meta slash
  skill. Do not invent visual Accept for kick.
- **Fail-id vocab seed:** Three PROC-KICK ids are the right closed set for
  v0 mechanical coverage; expand only if paste-contract needs its own id.
- **Rotate contrast chrome:** Documenting rotate vs kick in usage grid is
  fine as secondary AC once harness+smoke are primary.
- **LOCAL_ONLY override:** Allowed by KICK-01 if labeled; smoke must prove
  unlabeled path still FAILs.
- **This check lane:** `waveset.md` correctly sets check-only / no BUILD;
  MKK itself needs no product `proof_job`. Gap is on the **artifact FR’s**
  future BUILD Accept bar.

## Lens verdict

| field | value |
|---|---|
| recommendation | **REVISE** |
| blocks BUILD charter until | PB-01 + PB-02 + PB-03 addressed in FR (or locked in mod-decide before BUILD); PB-04 stated as Accept rule |
| GO if | named harness + fixture glob; Acceptance requires checker PASS; paste-contract asserts named; live `/mod-kick` smoke required and not replaceable by KICK-08 alone; CCR evidence labeled illustration-only |
| BLOCK if | (not yet) FR claimed shipped Accept on chrome/fixtures with no revise path |

## Suggested FR edits (for O0 / revise; this lens does not edit the FR)

1. Expand KICK-08 to name `evals/check_mod_kick.py` +
   `evals/fixtures/mod-kick-*/` and map each PROC-KICK id → fixture case;
   add paste-contract incomplete case.
2. Replace Acceptance “Eval fixtures for the three PROC-KICK fail ids”
   with explicit `python3 evals/check_mod_kick.py` PASS + live smoke
   checkbox (receipt + remote sync or LOCAL_ONLY).
3. Add one-line BUILD Meta: `proof_required: n/a` (plugin-meta; no DOM) +
   frozen `proof_job` sentence for publish-first + paste contract;
   `visual_accept: no` with rationale.
4. Label `evidence_verified_against` CCR paste as illustration only for
   Accept.

## Escalate

Owned finding complete for O0 reconcile into `findings/MKK-verdict.md`.
No other files written. No commits. No human solicitation.

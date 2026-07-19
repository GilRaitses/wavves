# PBA-W1d — adversarial lens

```yaml
lens: adversarial
wave: PBA-W1d
artifact: feature-requests/20260718_proof-before-accept.md
repo_state_verified_against: af0c0788cb2dbb865cbce6721fcdcbf6642b11d4
model: cursor-grok-4.5-high-fast
git_actions: none
```

## Lens verdict (this lens only)

**REVISE**

The FR names a real failure mode (RFU-ACCEPT process green while Proof unset).
As written, BUILD can ship the pattern and still leave `PROC-PASS-NO-PROOF`
open: ACCEPT criteria are process-shaped, the visual gate is not runnable,
PROC-* ids have no detector, and product-lane defaults allow opt-out.

O0 owns the lane verdict. This file does not grade sibling lenses.

## Blocking failure modes

### FM-1 — BUILD acceptance recapitulates process-PASS

**Class:** happy-path-only gate / process-PASS loophole  
**Severity:** blocking

FR Acceptance (BUILD in wavves_build) requires:

1. docs name the four fields
2. eval fixtures demonstrate FAIL/PASS labels
3. mod-check or playbook instructions "require hunting"
4. no install from folder

None of those measure a felt Proof. A BUILD ACCEPT can green on charter
prose + fixture files + instruction text while no screenshot harness, no
DOM height check, and no closed fail-id detector exist. That is the same
shape as RFU-ACCEPT (`gate-captures/RFU-ACCEPT.json`: LAND-C, honesty,
e2e shell PASS; Proof job not among gates).

**Evidence:** FR §Acceptance items 1–4; RFU-ACCEPT.json `gates` object
(no `proof_job` / visual-vs-reference); pax doctrine `accept_bar.required`
includes `proof_job_visible` and `visual_screenshot_vs_reference_class`,
`insufficient_alone` includes `shell_mounts` and `e2e_land_c_only`.

**Required revise:** BUILD ACCEPT must name a runnable proof of the
pattern itself (at minimum: mechanical fixture checker that emits PROC-*
on seeded process-only ACCEPT criteria, plus a named visual/DOM harness
command that can FAIL). Docs-only ACCEPT is forbidden for this FR.

### FM-2 — Visual / blank-canvas gate is not runnable

**Class:** gate that can't actually run  
**Severity:** blocking

Feature sketch item 4 and land option C say EXECUTION_WIRING gains a
"runnable visual gate" (screenshot or DOM markers; fail on height 0 /
blank black-canvas). Today `skills/charter/EXECUTION_WIRING.md` has no
visual rule. The FR does not name:

- harness path / command
- pass metric (JSON fields)
- capture layout under `gate-captures/`
- who invokes it (ACCEPT subagent vs CI)
- how screenshot-vs-reference is compared (byte, human, LLM assert)

This matches the held `unrunnable-gate-narrowed-adversarial-lens` fixture
class and EXECUTION_WIRING Rule 2 ("If a capture is missing, hand-authored
or cannot be rerun from the named command, the gate is not accepted").

Screenshot capture is environment-dependent in Cursor; without a
dependency-free DOM/metric path (height, marker presence) the gate
defaults to assertion. "Or named DOM proof markers" without a hard fail
when markers are chrome-only recreates shell honesty PASS.

**Required revise:** Lock one named harness (command + JSON schema + FAIL
conditions) before BUILD. Prefer measurable DOM/host metrics as the hard
gate; treat screenshot-vs-reference as optional operator/visual step with
an explicit capture path, not as the only pass metric.

### FM-3 — PROC-* fail ids are not operable

**Class:** unsafe default / inoperable vocabulary  
**Severity:** blocking

| id | Operable today? | Gap |
|---|---|---|
| PROC-PASS-NO-PROOF | No | Requires judging whether ACCEPT criteria can green without proof_job; no regex/AST detector |
| PROC-CHROME-THRASH | No | "IA/chrome wave" and "frozen" are agent-classified |
| PROC-DEBT-AS-DONE | No | No residual/`blocked_on` schema in wavves_build ACCEPT |
| PROC-NO-VISUAL | Partial | Checkable only if `visual_accept: yes` is set and harness path empty |
| PROC-BLANK-CANVAS | No (in fixtures) | Needs live DOM/runtime; not fixture-static |

Contrast: paragraph-tunnel ships closed vocab + `evals/check_paragraph_tunnel.py`
that detects fail ids on fixture text (stdlib, no LLM). FR Acceptance item 2
asks for fixtures that "demonstrate" PROC-PASS-NO-PROOF FAIL. If those land
under `evals/run_fixtures.py` (lens-wording keyword tripwire), PASS only
means the lens table still contains a keyword — evals/README known
limitation. That does not catch process-only ACCEPT criteria.

**Required revise:** Either (a) ship a mechanical checker analogous to
`check_paragraph_tunnel.py` with closed detection rules for at least
PROC-PASS-NO-PROOF and PROC-NO-VISUAL on charter/ACCEPT fixture text, or
(b) mark PROC-CHROME-THRASH / PROC-DEBT-AS-DONE / PROC-BLANK-CANVAS as
review-only ids with separate live harness requirements, and forbid
calling BUILD ACCEPT "PASS" on review-only ids alone.

### FM-4 — Opt-out defaults keep process-PASS alive

**Class:** unsafe defaults  
**Severity:** blocking

- `proof_reference: none with rationale` — any one-liner rationale skips a
  reference class (doctrine requires `visual_screenshot_vs_reference_class`
  for visitor Proof).
- `visual_accept: yes/no` — no default. Default `no` (or silent omit)
  restores chrome-only ACCEPT.
- Mandatory fields apply to "every product/UX lane" and
  "visitor/product lanes". No taxonomy exists under `skills/` today
  (`proof_job` / `visual_accept` / `visitor` grep: zero hits). Non-goal
  exempts "pure research/read-only check lanes". Agents can reclassify a
  visitor chrome lane as research/check and skip fields.
- Acceptance item 3: "mod-check **(or playbook check)**" — the or-clause
  lets BUILD skip land option B (fifth lens) while still claiming ACCEPT.

**Required revise:** For lanes that touch a visitor/product surface
(define the classifier in charter template: e.g. waveset
`lane_class: visitor|product|research|check`), defaults must be
`visual_accept: yes` and `proof_reference` not `none` unless operator
lock. `none` requires operator-gated exception, not agent rationale.
Drop the or-clause: if recommended combo is C+D+B, Acceptance must require
B (or explicitly lock "B deferred" with a named residual fail id).

### FM-5 — DOM-marker / honesty path is a happy path that misses the bug

**Class:** works on happy path only  
**Severity:** blocking

RFU-ACCEPT already PASSed honesty labels, shell e2e, and LAND-C while the
operator reported empty product (height-0 map until klosr `c76e19b`). A gate
that only checks "named DOM proof markers present" or "honesty copy
present" can green the same empty shell. Doctrine lists
`honesty_toggle_copy_without_proof_job` under `insufficient_alone`.

FR sketch allows screenshot **or** DOM markers. Without requiring
proof_job-linked markers (or host geometry + reference check), BUILD can
implement the weaker arm and miss PROC-BLANK-CANVAS / PROC-PASS-NO-PROOF.

**Required revise:** Hard-fail when proof_job is set and either (a) host
geometry/blank class fails, or (b) no capture path exists when
`visual_accept: yes`. Marker-only PASS without geometry or visual capture
is insufficient for visitor/product lanes.

## Non-blocking failure modes

### FM-6 — Recommended land combo omits AUTH sync (E)

**Severity:** non-blocking (product fork for mod-decide)

Options: A defer, B strong, C required, D required, E strong. Recommended
BUILD combo is **C+D+B**. Option E (mod-decide AUTH sync: proof_job in
waveset locks) is not in the combo. mod-decide already has AUTH-01
waveset sync; without E, locks can omit proof_job after decide and charter
templates alone may not catch a paste that drops the field.

**Revise ask (non-blocking):** Add E to the recommended combo, or state
why charter template alone is sufficient when AUTH-01 patches waveset.

### FM-7 — chrome_freeze is declarative only

**Severity:** non-blocking

paragraph-tunnel freezes sibling checksums before rewrite. FR
`chrome_freeze` is a sentence field with no checksum, path list, or
diff gate. Thrash can continue while the field is filled.

**Revise ask:** At least require a path glob / surface list and a
"no unapproved path edits before Proof ACCEPT" check in ACCEPT dispatch.

### FM-8 — Fifth default lens conflicts with mod-check policy

**Severity:** non-blocking (skill-edit clarity)

`skills/mod-check/SKILL.md`: "Add a fifth lens only when the operator
names a domain." Option B wants a fifth **default** lens `proof-bar`.
Without editing that sentence, implementers may keep proof-bar optional.

**Revise ask:** Explicit skill patch: proof-bar is default for
visitor/product artifacts; research/check lanes remain four-lens.

### FM-9 — Map-specific blank-canvas wording overfits klosr

**Severity:** non-blocking

PROC-BLANK-CANVAS cites "map host height 0 or empty canvas / black-canvas
class". wavves_build ships skills/playbooks, not MapLibre. A wavves-native
BUILD may stub the id as N/A and never generalize to "primary product host
empty while chrome PASS."

**Revise ask:** Generalize the fail condition to primary product host /
proof surface; keep map height as one example binding for pax/klosr lanes.

### FM-10 — No debt/`blocked_on` seam in wavves_build

**Severity:** non-blocking

Doctrine: keep-debt must carry `blocked_on` in {Proof-1, workbench-consumer,
kill}; debt close is not product done. FR names PROC-DEBT-AS-DONE but
wavves ACCEPT templates have no residual schema. Without that seam the id
is slogan-only in this repo.

**Revise ask:** Either add residual `blocked_on` to charter ACCEPT
template, or scope PROC-DEBT-AS-DONE as pax-lane playbook guidance, not a
wavves_build mechanical ACCEPT id.

### FM-11 — Relationship to existing visual-verification rule unstated

**Severity:** non-blocking

House Cursor rule `visual-verification-required.mdc` already requires
looking at rendered output before claiming visual fixes. FR does not bind
EXECUTION_WIRING visual rule to that workflow or to purpose-gates PG11
("Runnable check evidence on disk"). Risk of duplicate, conflicting, or
ignored surfaces.

**Revise ask:** One sentence in playbook: Proof visual gate implements
the house visual-verification rule for ACCEPT; purpose-gates remain
copy-scoped (non-goal stands).

## Land options A–E (adversarial read)

| option | Adversarial note |
|---|---|
| A `/proof-gate` skill | Defer is fine; avoid a slash skill that asserts PASS without harness. |
| B mod-check `proof-bar` | Strong only if default + Acceptance requires it; else theater. |
| C charter + EXECUTION_WIRING | Required, but currently unrunnable until harness is named. |
| D playbook + evals | Required; must use mechanical fail-id checker, not lens-keyword tripwire alone. |
| E mod-decide AUTH sync | Strong; omitting it leaves waveset lock drop as a loophole. |

Recommended combo C+D+B is directionally right. Without harness + operable
ids + hard defaults, C+D+B still ships process-PASS.

## What would change REVISE → GO (this lens)

1. Named visual/DOM harness command + JSON fail conditions in the FR (or
   locked for mod-decide before BUILD).
2. Mechanical PROC-* detector for charter/ACCEPT fixtures (paragraph-tunnel
   analogy), with review-only ids labeled as such.
3. Hard defaults / lane_class classifier; no agent `none` / `visual_accept: no`
   without operator lock.
4. BUILD Acceptance requires those runnables, not docs-only green.
5. Drop "or playbook check" escape on mod-check lens, or lock B deferred
   with residual.

## Out of scope for this lens

- Grounding of pax paths (W1a)
- Internal FR contradictions (W1b)
- Completeness / missing edges inventory (W1c)
- Implementation plan or code

## Commit file list (orchestrator only)

- `wavves/lanes/20260718_proof-before-accept-check/findings/PBA-adversarial.md` (this file)

No git. Escalation to O0 only.

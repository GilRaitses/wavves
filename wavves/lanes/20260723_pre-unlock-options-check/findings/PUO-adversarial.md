# PUO-W1d — adversarial

```yaml
lens: adversarial
wave: PUO-W1d
artifact: feature-requests/20260720_pre-unlock-options-mod-check.md
repo_state_verified_against: 26ad2d2afbb9196f2b690000f6a50f1cabfe20e5
model: cursor-grok-4.5-high-fast
git_actions: none
```

## Lens verdict (this lens only)

**REVISE**

The FR names a real false-green (`PROC-UNLOCK-NO-CHECK`): reconcile says
`unlock W2` while charter is stale, and AUTH-05 / proceed do not force a
check. As written, BUILD can ship flag prose + a proceed sentence and still
leave the burn open: statuses are not remasureable, waive/heuristic
precedence is soft, sync-by-mtime is forgeable, and there is no mechanical
detector. Happy-path GO→unlock works; the originating RLW path still slips
through.

O0 owns the lane verdict. This file does not grade sibling lenses.

Foreign pax RLW/RWC is illustration of the burn only.

## Proposed fail ids (map)

| id | Covers | Operable in FR as written? |
|---|---|---|
| `PROC-UNLOCK-NO-CHECK` | options-wave unlock from reconcile recommend without mod-check GO or REVISE-applied synced to current waveset | Partial. Named; no detector; status/sync undefined |

### Missing fail ids (needed before BUILD ACCEPT)

| id | Why |
|---|---|
| `PROC-UNLOCK-STALE-GO` | Unlock proceeds on sibling check GO/REVISE-applied after waveset/LOCKED drift |
| `PROC-UNLOCK-WAIVE-ABUSE` | `pre_unlock_mod_check: waived` without LOCKED reason, or reason that does not name why check is unnecessary |
| `PROC-UNLOCK-HEURISTIC-MISS` | Options/memo unlock with flag unset and heuristic <2 while unlock language present in reconcile |
| `PROC-UNLOCK-MANUAL-BYPASS` | O0/dispatch unlocks options wave without going through proceed AUTH-11d (registry never blocks) |
| `PROC-UNLOCK-WRONG-SIBLING` | Cleared using an unrelated check lane verdict (wrong artifact / wrong waveset) |
| `PROC-UNLOCK-AUTH05-CONFUSION` | Treats AUTH-05 mod-decide sync PASS as sufficient for options unlock |

Keep `PROC-UNLOCK-NO-CHECK` as the umbrella false-green. Do not collapse
stale-GO or waive-abuse into it; they need separate fixtures.

## Blocking failure modes

### FM-1 — Soft proceed sentence, hard unlock still works

**Class:** happy-path-only / gate that cannot actually run  
**Severity:** blocking  
**Fail ids:** `PROC-UNLOCK-NO-CHECK`, `PROC-UNLOCK-MANUAL-BYPASS`

AUTH-11d is playbook prose. Charter dispatch and O0 can still paste
`dispatch-w2.md` and launch the options wave without `/wavves proceed`.
Registry has no `pre_unlock_mod_check: required` lock that dispatch
hydration refuses.

**Concrete BUILD footgun:** Implementer updates `proceed.md` only.
Operator says "unlock W2". Agent dispatches W2 from charter habit. Check
never runs. Fixture that only greps proceed.md for "mod-check" greens.

**Required revise:** Dispatch/charter hydration fail-closed when
`pre_unlock_mod_check: required` and clear signal absent. Proceed is not
the only door.

### FM-2 — Status strings never remasure → always "no sibling clear"

**Class:** unrunnable gate / or silent skip  
**Severity:** blocking  
**Fail ids:** `PROC-UNLOCK-NO-CHECK`

`verdict-go` / `verdict-revise-applied` are not live registry statuses
(`wavves/registry.yml`). BUILD may (a) never write them → permanent
route-to-check loop, or (b) match on verdict prose ("Verdict: **GO**")
without registry sync → false clear.

**Required revise:** Closed status enum + O0 transition rules; proceed
remasures registry fields, not chat.

### FM-3 — Mtime sync false clear after REVISE theater

**Class:** stale authority / originating RWC twin  
**Severity:** blocking  
**Fail ids:** `PROC-UNLOCK-STALE-GO`

Risks allow unlock after `verdict-revise-applied` + synced waveset.
If sync is filesystem mtime, touching `waveset.md` without closing B1–B5
class gaps clears the gate. Foreign RWC blocked bare unlock precisely
because charter text lagged reconcile.

**Illustration:** foreign `RWC-verdict.md` B1 (W1 still IN FLIGHT) +
`RLW-W2-OPTIONS-UNLOCK.md` entry conditions require real REVISE closes.

**Required revise:** Sync = content hash or AUTH-01/`waveset_synced_at`
after named blocker ids closed; not touch mtime.

### FM-4 — Heuristic miss on bare unlock language

**Class:** detector gap recreating the bug  
**Severity:** blocking  
**Fail ids:** `PROC-UNLOCK-HEURISTIC-MISS`, `PROC-UNLOCK-NO-CHECK`

Heuristic needs ≥2 of 4. A reconcile can say `recommended_next_for_O0:
unlock W2` (signal 4) with PASS_WITH_GAPS (signal 2) while the wave is not
yet labeled options-only and honesty locks are unnamed → score 2, or with
sloppy labeling score 1. AUTH-11a only helps if charter write already set
the flag.

**Illustration:** FR problem item 5 + foreign pre-revise bare unlock
superseded by OPTIONS-UNLOCK.

**Required revise:** Unlock-language in reconcile against a GATED wave is
alone sufficient to require check (or force operator waive). Do not rely
on ≥2 when signal 4 is present.

### FM-5 — Waive one-liner defeats the product

**Class:** unsafe default / social bypass  
**Severity:** blocking  
**Fail ids:** `PROC-UNLOCK-WAIVE-ABUSE`

Waive needs "one-line reason in LOCKED". No ban on reasons like "speed" or
"trivial". Latency risk section encourages waive for "trivial mechanical
memos" without a mechanical triviality test.

**Required revise:** Waive template must name why options/memo risk is
absent (no ranking, no honesty locks, no PASS_WITH_GAPS prior). Eval
fixture: waived without template → FAIL.

### FM-6 — Wrong sibling check lane clears unlock

**Class:** authority confusion  
**Severity:** blocking  
**Fail ids:** `PROC-UNLOCK-WRONG-SIBLING`

House may have many check lanes (PUO, PAS, WOF, …). AUTH-11d says
"sibling" without binding `pre_unlock_check_lane` or artifact path match.
A stale GO from another FR check can be cited.

**Required revise:** Clear only if check lane `artifact` or registry
`pre_unlock_check_lane` points at this lane's waveset/LOCKED bundle.

### FM-7 — AUTH-05 PASS treated as unlock license

**Class:** wrong gate / Option A regression  
**Severity:** blocking  
**Fail ids:** `PROC-UNLOCK-AUTH05-CONFUSION`

Proceed step 3 already checks AUTH-05 (mod-decide sync). Agents will
collapse AUTH-11 into "waveset synced" and unlock options after decide
hygiene alone. FR rejects Option A, but does not state a distinct fail
when AUTH-05 passes and AUTH-11 does not.

**Required revise:** Pre-dispatch checklist lists AUTH-11 and AUTH-05 as
separate rows; fixture where AUTH-05 ok + no options-check → FAIL
`PROC-UNLOCK-AUTH05-CONFUSION` or umbrella `PROC-UNLOCK-NO-CHECK` with
explicit case.

## Non-blocking adversarial notes

### N1 — Double-check fatigue

After REVISE apply, operators skip re-check even when waveset drifts.
Addressed if FM-3 sync is hash-based; still add a proceed log line naming
which check lane cleared unlock.

### N2 — Latency → check starvation

Mandatory mod-check on every options unlock may push agents to relabel
options waves as BUILD to skip the gate. Non-goal + detector: renaming
without removing unlock-before-DECIDE language still requires check.

### N3 — Eval-only D deferred

If D stays "strong" but out of v0, FM-1…FM-7 ship untested. Completeness
B6 owns the charter call; adversarial marks ACCEPT without detector as
false green.

## What is already sound

- Correct diagnosis: AUTH-05 ≠ options-unlock gate
  (`skills/mod-check/SKILL.md`, `skills/wavves/playbooks/proceed.md`).
- Foreign RWC REVISE with `blocks_w2: true` shows scoped verdict can hold
  unlock when used.
- Defense in depth idea (charter flag + reconcile actions + proceed route)
  is the right spine once fail-closed.

## Commit file list (orchestrator)

- `wavves/lanes/20260723_pre-unlock-options-check/findings/PUO-adversarial.md`

No git actions performed.

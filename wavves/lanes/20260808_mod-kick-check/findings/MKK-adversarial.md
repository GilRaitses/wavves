# MKK-W1d — adversarial lens

```yaml
lens: adversarial
wave: MKK-W1d
artifact: feature-requests/20260808_mod-kick.md
artifact_state: working-tree (uncommitted; ?? at check time)
repo_state_verified_against: b7ce95f075e89183a49e0486b6764ec299aeecac
model: cursor-grok-4.5
git_actions: none (owned findings file only)
```

## Lens verdict (this lens only)

**REVISE**

The FR names the right product fork (kick = cross-environment exit +
git-published pickup; rotate = same-O0-family continuity) and the right
spine fail ids for no-publish, silent multi-repo, and silent vendor. As
written, BUILD can still ship a happy-path skill that greens the three
named fixtures while reintroducing the originating failure modes through
`LOCAL_ONLY`, shrug-accepted wrong defaults, unbounded vendor, Desktop
staging as false authority, over-broad publish of dirty trees, and cue
collision with `/mod-rotate`. Secret hygiene (set-key standing) is absent
from the paste/vendor path.

O0 owns the lane verdict. This file does not grade sibling lenses.

## Proposed fail ids (map)

| id | Covers | Operable in FR as written? |
|---|---|---|
| `PROC-KICK-NO-PUBLISH` | paste while pickup paths local-only / unpushed | Partial. Named; Acceptance allows `LOCAL_ONLY`-label escape with no abuse detector |
| `PROC-KICK-MULTI-SILENT` | multi-remote hydration without recorded auth | Partial. Named; "hydration needs >1" is agent judgment with no disk remeasure rule |
| `PROC-KICK-VENDOR-SILENT` | vendor/copy without explicit auth | Partial. Named; no thin-deps threshold (open call 3); auth alone does not bound blast radius |

### Missing fail ids (needed before BUILD ACCEPT)

| id | Why |
|---|---|
| `PROC-KICK-LOCAL-ONLY-ABUSE` | `LOCAL_ONLY` paste used as cross-environment handoff (different machine / agent without shared FS) |
| `PROC-KICK-WRONG-DEFAULT` | proposed pickup default ≠ lane `repos:` primary (or sole listed repo); dirty-tree heuristic wins |
| `PROC-KICK-UNRELATED-PUSH` | publish stages/commits/pushes files outside the lane-owned allowlist for the kick stream |
| `PROC-KICK-SECRET-LEAK` | vendor or paste includes env secrets, `.env*`, credentials, or secret substrings (set-key hygiene) |
| `PROC-KICK-DESKTOP-AUTHORITY` | Desktop zip / `desktop_staging` cited as pickup authority instead of git-published hash |
| `PROC-KICK-ROTATE-COLLAPSE` | kick cues routed to `/mod-rotate` (or reverse); paste shape omits kick vs rotate distinction |
| `PROC-KICK-THIN-UNBOUNDED` | `VENDOR_INTO_PICKUP` without closed size/count/path-class threshold |
| `PROC-KICK-SHRUG-WIDEN` | bare shrug / proceed accepts a contested multi-repo or vendor offer without explicit MULTI/VENDOR auth lines |

Do not collapse `PROC-KICK-VENDOR-SILENT` (no auth) with
`PROC-KICK-THIN-UNBOUNDED` (auth present, blast radius unbounded) or
`PROC-KICK-SECRET-LEAK` (content class forbidden even with auth).

## Blocking failure modes

### FM-1 — `LOCAL_ONLY` defeats publish-first

**Class:** loophole / unsafe override default  
**Severity:** blocking  
**Fail ids:** `PROC-KICK-NO-PUBLISH` (weakened), `PROC-KICK-LOCAL-ONLY-ABUSE` (missing)

KICK-01: refuse paste until publish PASS **or** operator overrides with
`LOCAL_ONLY` labeled paste. Acceptance: "Paste refuses (or LOCAL_ONLY-labels)
when pickup not on remote." A fixture that only checks "paste without push
→ FAIL" will green if the agent stamps `LOCAL_ONLY:` and emits the
one-liner. That recreates the originating failure for the stated product
goal (successor in a **different environment** with repo access).

Contrast: `skills/mod-rotate/SKILL.md` scopes an unpublished handoff
explicitly to the **same machine** and says so in the paste. Kick FR has
no same-machine fence, no required auth token for the override, and no
rule that `LOCAL_ONLY` paste MUST refuse cross-env claims ("pull @ hash",
"different environment").

**Concrete BUILD footgun:** Push fails or operator is impatient. Agent
emits `LOCAL_ONLY: pull applications-for-jobs @ <local hash>…` for a phone
/ other-machine successor. Successor cannot see the work. Fail id
`PROC-KICK-NO-PUBLISH` marked PASS because the label was present.

**Required revise:** Close the override. Either (a) delete `LOCAL_ONLY`
from kick entirely (kick = publish or stop), or (b) allow `LOCAL_ONLY`
only with explicit operator phrase + paste banner that forbids other
machines + receipt field `scope: same_machine_only`, and add fixture
`PROC-KICK-LOCAL-ONLY-ABUSE`. Acceptance must not treat label-as-PASS as
equivalent to publish PASS.

### FM-2 — Wrong default pickup via dirty-tree heuristic + illustration leak

**Class:** unsafe default  
**Severity:** blocking  
**Fail ids:** `PROC-KICK-WRONG-DEFAULT` (missing)

KICK-02: default = lane `repos:` primary **or sole dirty repo**. UX sketch
hardcodes `[default: applications-for-jobs]` (CCR session illustration,
not a product default). Dirty ≠ authoritative. Multi-root Cursor
workspaces often have one dirty tree that is unrelated to the stream
being kicked.

Operator may "accept default with shrug / proceed" (KICK-02). That
collapses the only question into an unexamined dirty-repo pick.

**Concrete BUILD footgun:** Lane lists `repos: [applications-for-jobs]`.
`wavves_build` is dirty from this FR check. Agent proposes default =
`wavves_build` (sole dirty), shrug accepts, publish pushes plugin tree,
paste sends successor to the wrong remote.

**Required revise:** Default order locked: (1) lane `repos:` primary if
present and resolvable; (2) else sole repo in lane `repos:`; (3) else
**ask with no default** (do not invent from dirty). Dirty status may
annotate, never select. Remove CCR repo name from the default UX
template or mark it EXAMPLE-ONLY. Fixture: dirty-secondary vs clean
primary → default must be primary (`PROC-KICK-WRONG-DEFAULT`).

### FM-3 — Publish pushes unrelated dirty trees

**Class:** blast radius / auth downgrade  
**Severity:** blocking  
**Fail ids:** `PROC-KICK-UNRELATED-PUSH` (missing); open call 2 unresolved

KICK-01: "stage lane-owned surfaces per repo protocol, commit if protocol
allows … **push** pickup remotes." "Lane-owned" is undefined (no path
allowlist, no `files:` AUTH-10 shape). Open call 2 asks whether kick
auto-commits under apps-style push-to-main or always emits a plan when
protocol is commit-only-when-asked. Until that is locked, BUILD can
interpret kick as blanket authorize for every dirty path in the pickup
repo.

Contrast: proceed-all-standing FR closed `PROC-PROCEED-COMMIT-WITHOUT-AUTH`
with per-land `files:` lists. Kick has no equivalent.

**Concrete BUILD footgun:** Kick on apps repo with uncommitted resume
edits + unrelated WIP. Agent `git add -A`, commit, push, paste. Successor
inherits unrelated WIP as "published kick authority."

**Required revise:** Lock open call 2 before BUILD. Publish step must
take an explicit `files:` allowlist (lane surfaces + kick receipt only)
and refuse to stage paths outside it. Protocol fork: if repo is
commit-when-asked, emit plan + wait (no shrug-alone push). Fixture:
dirty unrelated path present → must remain unstaged (`PROC-KICK-UNRELATED-PUSH`).

### FM-4 — Vendor blast radius + secret leakage into paste

**Class:** secret hygiene / unbounded copy  
**Severity:** blocking  
**Fail ids:** `PROC-KICK-VENDOR-SILENT` (partial), `PROC-KICK-THIN-UNBOUNDED`
(missing), `PROC-KICK-SECRET-LEAK` (missing)

KICK-04 offers `VENDOR_INTO_PICKUP` for "thin tracked deps (few files,
already cited by hash)" with open call 3 still unset (max size /
file-count). Auth (`VENDOR_AUTH`) alone does not prevent copying
`.env.local`, `credentials.json`, Twilio sid files, or other set-key
targets into `findings/deps/` then committing them into the pickup remote.

Paste contract requires an ordered read list. If vendored secret paths
appear in that list (or absolute host paths), the one-liner leaks
inventory even when values are not echoed. Standing set-key rules
(`skills/set-key/SKILL.md`, `~/.cursor/rules/set-key.mdc`): never print,
log, or commit secrets; remeasure set/nchars only. Kick FR never cites
that seam.

**Concrete BUILD footgun:** Secondary repo holds a cited config plus
`.env.local`. Agent vendors "the deps folder," commits to pickup, paste
lists `findings/deps/.env.local`. Remote and chat both now carry secret
material. Fixture `PROC-KICK-VENDOR-SILENT` greens because `VENDOR_AUTH`
was recorded.

**Required revise:** Close open call 3 with numeric + path-class rules
(tracked, already hash-cited, max N files / max bytes, deny-globs:
`.env*`, `*secret*`, `*credential*`, `*.pem`, key material). Pre-vendor
and pre-paste leak-scan (AGENTS.md outbound deliverables lock). Paste
must never include secret paths or values. Fixture:
`PROC-KICK-SECRET-LEAK` + `PROC-KICK-THIN-UNBOUNDED`.

### FM-5 — Desktop / `desktop_staging` as false authority

**Class:** false authority  
**Severity:** blocking  
**Fail ids:** `PROC-KICK-DESKTOP-AUTHORITY` (missing)

Non-goals: "Not Desktop-only delivery; Desktop may be noted as local
supplement, but kick authority is **git-published** pickup." KICK-04 then
lists `desktop_staging` as a valid vendor target beside the pickup lane
home. A BUILD can vendor to Desktop, paste a Desktop path, and claim kick
done while remote pickup lacks the deps.

**Concrete BUILD footgun:** CCR-style Desktop zip noted in paste as
primary read; git hash is old. Other-environment successor has no
Desktop. Product claim (cross-env) fails silently.

**Required revise:** Vendor targets ⊆ pickup git tree only
(`<lane>/…` or `findings/deps/` under the pickup repo). Desktop may appear
only as optional same-machine supplement after a published hash, never as
read-order authority. Fixture: paste citing Desktop without reachable
origin hash → `PROC-KICK-DESKTOP-AUTHORITY` FAIL.

### FM-6 — Silent multi-repo via judgment + shrug

**Class:** happy-path auth theater  
**Severity:** blocking  
**Fail ids:** `PROC-KICK-MULTI-SILENT` (partial), `PROC-KICK-SHRUG-WIDEN` (missing)

KICK-03 gates multi-repo on "if hydration needs >1 remote." Need is not
remeasured from a disk list of required paths × owning remotes. An agent
can (a) silently assume one remote and omit required secondary paths, or
(b) list three remotes in the paste without `MULTI_REPO_AUTH` because
shrug "accepted default" was treated as blanket auth.

Dispatch note: do not widen kick into shrug/proceed-all-standing
(`feature-requests/20260723_proceed-all-standing.md`). KICK-02 still lets
shrug accept the pickup default. Without a closed rule, shrug can also
be read as accepting option C/D.

**Required revise:** Multi-repo detection = path inventory with owning
repo per path (disk). If >1 owning remote → stop and list; never proceed
on shrug alone. `MULTI_REPO_AUTH` / `VENDOR_AUTH` require explicit
operator tokens this turn (not bare shrug). Fixture:
`PROC-KICK-SHRUG-WIDEN`.

### FM-7 — Operator confusion kick vs rotate

**Class:** product collapse / cue collision  
**Severity:** blocking for router land; high for paste UX  
**Fail ids:** `PROC-KICK-ROTATE-COLLAPSE` (missing)

Both products emit a one-line paste. Rotate cues already include
"handoff", "fresh thread" (`skills/wavves/SKILL.md` leave-act table).
Kick originating ask is "push to me and give a one-liner" for another
environment. FR non-goals reject `/mod-rotate --kick` but do not give a
closed cue table or a mandatory paste prefix that cannot be mistaken for
rotate's `/wavves hydrate as O0.R…` form.

Kick paste contract (minimum) does not require a leading invocable
(`/mod-kick` receipt pointer or `/wavves kick …`). Rotate skill text
stresses leading `/wavves` because `disable-model-invocation: true`.
Kick can ship a prose one-liner that never invokes the plugin in the
successor environment.

**Concrete BUILD footgun:** Operator says "hand this off with a
one-liner." Router fires `/mod-rotate`. Paste assigns `O0.R(N+1)` in the
same orchestrator home. Cross-env successor with only the pickup remote
cannot hydrate rotation continuity. Or kick paste lacks slash command;
fresh thread never loads wavves.

**Required revise:** Closed cue table: kick = environment exit / other
machine / other agent with shared git only / "kick paste"; rotate =
same orchestrator family / term bump / token velocity. Paste MUST lead
with an explicit kick invocable or `/wavves kick …` and MUST state
`product: kick` (not rotate). Usage grid row must show both side by
side (KICK-07). Fixture: ambiguous "handoff one-liner" → must not emit
rotation file alone (`PROC-KICK-ROTATE-COLLAPSE`).

### FM-8 — Happy-path-only gates that cannot run

**Class:** unrunnable / chrome-only gate  
**Severity:** blocking for ACCEPT  
**Fail ids:** all of the above when fixtures stay prose-only

KICK-08 lists three fixtures by fail-id name only. No detector shape
(what string/receipt field must be present; what publish probe runs; how
`LOCAL_ONLY` is scored). Eval corpus pattern (`evals/README.md`, fixture
`unrunnable-gate-narrowed-adversarial-lens`) exists specifically to catch
gates described in prose without a harness. Acceptance checkboxes are
manual and do not name a command or pass metric for kick.

**Required revise:** For each fail id (named + missing above that stay
in scope), specify fixture `input.md` / `expected.md` detector:
receipt fields, paste banners, `git status`/`git rev-parse` probes, deny
path globs. `PROC-KICK-NO-PUBLISH` detector must FAIL on `LOCAL_ONLY`
cross-env paste, not PASS. W1e owns proof-bar detail; this lens only
flags that current KICK-08 cannot catch FMs 1–7.

## Non-blocking / watch items

- **Receipt home fork (open call 1):** dual homes (`<lane>/moderator_handoffs/`
  vs `wavves/kicks/`) risk successor reading the wrong receipt; not a
  security fail by itself if paste cites the absolute receipt path.
- **Foreign apps CCR evidence:** `evidence_verified_against` apps hash is
  illustration; BUILD must not hard-depend on `applications-for-jobs`
  paths (dispatch already notes this). Adversarial concern is the UX
  default leak (FM-2), not the citation itself.
- **Concurrent term push:** rotate skill has rebase/no-force rules; kick
  should inherit the same remote-rejected handling when publish races
  another term. Recommend cite-by-reference to mod-rotate git safety
  rather than inventing a third protocol.

## Lens lean summary

| Option | Meaning |
|---|---|
| GO | Only if FMs 1–8 closed in FR text before BUILD |
| **REVISE** | **This lens: close LOCAL_ONLY, default selection, publish allowlist, thin/secret/Desktop vendor rules, shrug auth, kick≠rotate cues, runnable fixtures** |
| BLOCK | Reserved if BUILD chartered with current FR unchanged and Acceptance treated as shippable |

## Seams read (this lens)

- `wavves/lanes/20260808_mod-kick-check/waveset.md`
- `wavves/lanes/20260808_mod-kick-check/dispatch.md`
- `feature-requests/20260808_mod-kick.md` (working-tree)
- `skills/mod-rotate/SKILL.md`
- `skills/set-key/SKILL.md` + `feature-requests/20260723_set-key.md`
- `skills/wavves/SKILL.md` (rotate leave-act row; no kick row yet)
- `examples/usage.md` (rotate rows only)
- `wavves/AGENTS.md` (outbound leak-scan; git)
- `feature-requests/20260723_proceed-all-standing.md` (shrug widen / commit auth contrast)
- `evals/README.md` + `evals/fixtures/unrunnable-gate-narrowed-adversarial-lens/expected.md`

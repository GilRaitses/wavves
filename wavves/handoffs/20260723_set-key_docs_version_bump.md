# Handoff — `/set-key` docs sync + FR officialize + version bump

```text
repo: /Users/gilraitses/wavves_build  (remote GilRaitses/wavves)
term: wavves product mod (fresh thread)
from: O0.R3 (pax operator thread)
date_america_new_york: 2026-07-23
repo_state_verified_against: 17539cb913c397f0469a6f6598c9774992935878
feature: /set-key
fr: feature-requests/20260723_set-key.md
local_plugin_mirror: ~/.cursor/plugins/local/wavves/  (rsync after land)
```

## One-line paste (fresh thread)

```text
/wavves You are the wavves product mod. Hydrate from wavves/handoffs/20260723_set-key_docs_version_bump.md (handoff land e437b9b; feature code 17539cb). Charge: (1) review FR-20260723 and make it official in the FR index lifecycle, (2) sync ALL public docs / usage grid / index.html / skill frontmatter with the landed /set-key skill, (3) bump version 0.3.0 → 0.4.0 (new public slash skill), fold CHANGELOG Unreleased into 0.4.0, commit+push main, rsync to ~/.cursor/plugins/local/wavves/. Do not reopen skill behavior unless a doc contradiction forces a tiny fix. Prefer cursor-grok-4.5-high-fast for any runners.
```

## What already landed (do not rebuild)

| path | state |
|---|---|
| `skills/set-key/SKILL.md` | landed |
| `skills/set-key/scripts/setkey_env.sh` | landed (executable) |
| `skills/wavves/playbooks/set-key.md` | landed |
| `skills/wavves/SKILL.md` | partial — routing + leaf table + playbook list have set-key; **description frontmatter still omits set-key** |
| `.cursor-plugin/plugin.json` | keyword `set-key` added; **version still `0.3.0`** |
| `README.md` | skills table has `/set-key`; **Version line still `0.3.0`**; numbered skill narrative + bottom inventory still miss set-key |
| `examples/usage.md` | skills table has `/set-key`; **playbooks table + quick examples still miss set-key** |
| `CHANGELOG.md` | Unreleased bullet only — **not cut as 0.4.0** |
| `feature-requests/20260723_set-key.md` | exists; status self-marked SHIPPED — **not yet in FR README index** |
| `index.html` | **no `/set-key` rows**; kicker/footer still v0.3.0 |
| klosr `setkey.sh` | landed separately on klosr `0e4fc98` (consumer helper; out of this repo) |
| standing rules | `~/.cursor/rules/set-key.mdc` + `pax/.cursor/rules/set-key.mdc` point at this FR |

## Charge (ordered)

### 1. Review FR → official

Read `feature-requests/20260723_set-key.md`.

- Confirm acceptance matches what shipped (skill + playbook + helper; never echo secret; remasure set/nchars).
- Set lifecycle status to **`shipped`** (official).
- Add row to `feature-requests/README.md` Index table.
- If anything in the FR contradicts the skill, fix the FR (or a one-line skill honesty fix) — do not expand scope into new secret backends.

### 2. Sync all docs with `/set-key`

Checklist (every row must pass a remasure grep for `set-key` / `/set-key` where applicable):

| surface | required edit |
|---|---|
| `README.md` | Version → `0.4.0`; add `/set-key` to numbered capabilities list; add to bottom skills inventory; add `set-key only:` example line |
| `examples/usage.md` | playbooks table row; quick-reference `set-key only:` line; optional short walkthrough if other leaves have one |
| `skills/wavves/SKILL.md` | description frontmatter lists `/set-key`; non-negotiable #2 leaf list includes `set-key` |
| `index.html` | skills table row; playbooks table row; command card (`when` / `not-this`); demo snippet; kicker + footer → v0.4.0 |
| `CHANGELOG.md` | cut `## 0.4.0 (2026-07-23)` from Unreleased; keep Unreleased empty or next-only |
| `.cursor-plugin/plugin.json` | `"version": "0.4.0"` |
| `evals/` | only if an inventory fixture enumerates slash skills; update if present |
| public-copy gates | run existing evals if doc edits touch gated copy |

### 3. Version bump (locked lean)

**Bump `0.3.0` → `0.4.0`.** Rationale: new public slash-invocable leaf skill (same class as prior minor bumps that added commands). Do not ship as 0.3.1.

Surfaces that must agree on `0.4.0`:

- `.cursor-plugin/plugin.json`
- `README.md` Version line
- `index.html` kicker + footer
- `CHANGELOG.md` section header

### 4. Land + mirror

1. Commit on `main` (message: ship `/set-key` docs + official FR + v0.4.0).
2. Push `origin/main`; verify synced.
3. Rsync product → local Cursor plugin:

```bash
rsync -a --delete \
  --exclude '.git' \
  /Users/gilraitses/wavves_build/skills/ \
  /Users/gilraitses/.cursor/plugins/local/wavves/skills/
cp /Users/gilraitses/wavves_build/.cursor-plugin/plugin.json \
  /Users/gilraitses/.cursor/plugins/local/wavves/.cursor-plugin/plugin.json
cp /Users/gilraitses/wavves_build/README.md \
  /Users/gilraitses/.cursor/plugins/local/wavves/README.md
cp /Users/gilraitses/wavves_build/CHANGELOG.md \
  /Users/gilraitses/.cursor/plugins/local/wavves/CHANGELOG.md
cp /Users/gilraitses/wavves_build/index.html \
  /Users/gilraitses/.cursor/plugins/local/wavves/index.html
cp /Users/gilraitses/wavves_build/examples/usage.md \
  /Users/gilraitses/.cursor/plugins/local/wavves/examples/usage.md
```

4. Remasure: `plugin.json` version `0.4.0`; `rg -n '/set-key' README.md examples/usage.md index.html skills/wavves/SKILL.md`.

## Out of scope

- Changing set-key runtime behavior beyond honesty fixes forced by docs
- pax IWD-W27 Google densify (separate lane; runner already dispatched)
- Marketplace publish / Cursor plugin store submission (unless operator asks)
- Self-embedding the landing commit hash inside this handoff after you land

## Completion report (return fields only)

```text
landing_commit_hash:
branch_at_start: main
push_origin_main: yes|no
version: 0.4.0
fr_status: shipped
docs_surfaces_touched: [list]
local_plugin_rsync: yes|no
grep_set_key_ok: yes|no
```

## Operator note

Skill code already on `main` at `17539cb`. This handoff is **docs + FR officialize + version cut** only. Standing operator phrase **set key** remains covered by alwaysApply rules even before the slash skill is rediscovered after rsync.

**Sibling FR (do not fold into this bump unless trivial):**  
`feature-requests/20260723_proceed-all-standing.md` — proceed-all-standing /
“queue all standing and move.” Separate `/mod-check` → decide → charter.

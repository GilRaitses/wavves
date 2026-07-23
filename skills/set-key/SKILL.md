---
name: set-key
description: >-
  Open an external Terminal.app window with a paste-and-return helper that
  writes a server-only env secret (default klosr GOOGLE_MAPS_API_KEY). Use for
  /set-key, "set key", "setkey", or named secrets (SID, client secret). Never
  prints the secret; remasures set/nchars only.
disable-model-invocation: true
---

# set-key

Operator paste helper for **server-only** env secrets. Cursor's integrated
shell is not a TTY for hidden `read -s`, so this skill always launches
**Terminal.app** with a small bash helper. The operator pastes the secret and
presses return. The agent remasures presence only.

## When to use

Cues: `/set-key`, **set key**, **setkey**, "open setkey for Google / SID /
client secret".

## Non-negotiables

1. **External Terminal only.** Use `osascript` → Terminal.app `do script` (or
   `open -a Terminal`). Do not ask the operator to paste into the Cursor shell.
2. **Never print, log, commit, or chat the secret value.** Remasure with
   `set=True/False` and `nchars=N` (and path + key name) only.
3. **Default target:** repo `/Users/gilraitses/klosr`, file `.env.local`,
   key `GOOGLE_MAPS_API_KEY`. Helper: prefer repo-local `setkey.sh` if present;
   else use `skills/set-key/scripts/setkey_env.sh`.
4. **Named secrets.** If the operator names another key (`TWILIO_ACCOUNT_SID`,
   client secret, etc.), pass `--key-name` / `--env-file` / `--repo` to the
   helper. Same paste UX.
5. **chmod 600** on the env file after write. Do not stage `.env.local`.
6. **After paste:** remasure; report path + key name + set/nchars; hint next
   step (restart Next / unlock densify) only if a standing wave needs it.

## Steps

```
- [ ] 1. Resolve repo, env file, key name (defaults above unless named).
- [ ] 2. Ensure helper exists and is executable.
- [ ] 3. Launch Terminal.app running the helper (title the tab set-key).
- [ ] 4. Tell the operator: paste + return in the external window.
- [ ] 5. When they say done (or on next turn), remasure without reading the
        value into chat. Report set/nchars only.
```

## Launch pattern (macOS)

```bash
HELPER="/Users/gilraitses/klosr/setkey.sh"   # or skills/set-key/scripts/setkey_env.sh
osascript <<APPLESCRIPT
tell application "Terminal"
  activate
  do script "printf '\\\\033]0;set-key\\\\007'; cd $(dirname \"$HELPER\") && exec bash \"$HELPER\""
end tell
APPLESCRIPT
```

For the generic helper with args:

```bash
bash skills/set-key/scripts/setkey_env.sh \
  --repo /Users/gilraitses/klosr \
  --env-file .env.local \
  --key-name GOOGLE_MAPS_API_KEY
```

## Remasure (never prints value)

```python
from pathlib import Path
p = Path("/Users/gilraitses/klosr/.env.local")
ok=False; n=0
for ln in p.read_text().splitlines():
    s=ln.strip()
    if not s or s.startswith("#") or "=" not in s: continue
    k,v=s.split("=",1)
    if k.strip()=="GOOGLE_MAPS_API_KEY":
        v=v.strip().strip('"').strip("'"); ok=bool(v); n=len(v)
print(f"ok set={ok} nchars={n} path={p.resolve()}")
```

## Out of scope

Cloud secret managers, CI inject, visitor-facing key exposure, committing env files.

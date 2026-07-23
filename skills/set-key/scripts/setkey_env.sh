#!/usr/bin/env bash
# Generic paste-and-return env writer for /set-key.
# Interactive TTY only for secrets. Agent must NOT pass secret on argv/env.
# On reject: env file UNCHANGED.

set -euo pipefail

REPO=""
ENV_FILE=".env.local"
KEY_NAME=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo) REPO="${2:-}"; shift 2 ;;
    --env-file) ENV_FILE="${2:-}"; shift 2 ;;
    --key-name) KEY_NAME="${2:-}"; shift 2 ;;
    *)
      echo "error: unknown arg: $1" >&2
      exit 1
      ;;
  esac
done

if [[ -z "$REPO" || -z "$KEY_NAME" ]]; then
  echo "usage: setkey_env.sh --repo DIR --env-file FILE --key-name NAME" >&2
  exit 1
fi

ENV_LOCAL="${REPO}/${ENV_FILE}"
umask 077
mkdir -p "$REPO"
cd "$REPO"

sanitize_key() {
  python3 -c '
import re, sys
raw = sys.stdin.buffer.read()
s = raw.decode("utf-8", "replace")
s = s.replace("\r", "").replace("\n", "")
s = re.sub(r"\x1b\[\??200~", "", s)
s = re.sub(r"\x1b\[\??201~", "", s)
s = re.sub(r"\x1b\[[0-9;]*[A-Za-z]", "", s)
s = re.sub(r"\s+", "", s)
s = re.sub(r"[^A-Za-z0-9_\-]", "", s)
sys.stdout.write(s)
'
}

reject() {
  echo "error: $*" >&2
  echo "note: ${ENV_LOCAL} UNCHANGED (previous value still on disk if any)." >&2
  exit 1
}

if [[ ! -t 0 ]]; then
  reject "no TTY — run in Terminal.app"
fi

echo "Paste secret for ${KEY_NAME} (hidden). Target: ${ENV_LOCAL}"
# shellcheck disable=SC2162
read -r -s -p "${KEY_NAME}: " KEY_RAW || true
echo
KEY="$(printf '%s' "${KEY_RAW:-}" | sanitize_key)"

if [[ -z "$KEY" ]]; then
  reject "empty key after sanitize"
fi

touch "$ENV_LOCAL"
chmod 600 "$ENV_LOCAL" 2>/dev/null || true
tmp="$(mktemp "${ENV_LOCAL}.XXXXXX")"
if [[ -s "$ENV_LOCAL" ]]; then
  grep -v -E "^[[:space:]]*${KEY_NAME}=" "$ENV_LOCAL" >"$tmp" || true
else
  : >"$tmp"
fi
if [[ -s "$tmp" ]] && [[ "$(tail -c1 "$tmp" | wc -l)" -eq 0 ]]; then
  printf '\n' >>"$tmp"
fi
printf '%s=%s\n' "$KEY_NAME" "$KEY" >>"$tmp"
mv "$tmp" "$ENV_LOCAL"
chmod 600 "$ENV_LOCAL"

python3 - "$ENV_LOCAL" "$KEY_NAME" <<'PY'
import sys
from pathlib import Path
p = Path(sys.argv[1])
name = sys.argv[2]
ok = False
n = 0
for ln in p.read_text(encoding="utf-8").splitlines():
    s = ln.strip()
    if not s or s.startswith("#") or "=" not in s:
        continue
    k, v = s.split("=", 1)
    if k.strip() == name:
        v = v.strip().strip('"').strip("'")
        ok = bool(v)
        n = len(v)
print(f"ok set={ok} nchars={n} path={p.resolve()} key={name}")
raise SystemExit(0 if ok else 1)
PY

echo "done. restart processes that read this env file."

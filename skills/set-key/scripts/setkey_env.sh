#!/usr/bin/env bash
# Generic paste-and-return env writer for /set-key.
# Usage:
#   setkey_env.sh --repo DIR --env-file .env.local --key-name NAME
#   setkey_env.sh --repo DIR --env-file .env.local --key-name NAME --from-env
# Never echoes the secret.

set -euo pipefail

REPO=""
ENV_FILE=".env.local"
KEY_NAME=""
FROM_ENV=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo) REPO="${2:-}"; shift 2 ;;
    --env-file) ENV_FILE="${2:-}"; shift 2 ;;
    --key-name) KEY_NAME="${2:-}"; shift 2 ;;
    --from-env) FROM_ENV=1; shift ;;
    *)
      echo "error: unknown arg: $1" >&2
      exit 1
      ;;
  esac
done

if [[ -z "$REPO" || -z "$KEY_NAME" ]]; then
  echo "usage: setkey_env.sh --repo DIR --env-file FILE --key-name NAME [--from-env]" >&2
  exit 1
fi

ENV_LOCAL="${REPO}/${ENV_FILE}"
umask 077
mkdir -p "$REPO"
cd "$REPO"

read_key() {
  if [[ "$FROM_ENV" -eq 1 ]]; then
    if [[ -z "${!KEY_NAME:-}" ]]; then
      echo "error: ${KEY_NAME} empty in environment" >&2
      exit 1
    fi
    printf '%s' "${!KEY_NAME}"
    return
  fi
  if [[ ! -t 0 ]]; then
    echo "error: no TTY — run in Terminal.app" >&2
    exit 1
  fi
  echo "Paste secret for ${KEY_NAME} (input hidden)."
  echo "Target: ${ENV_LOCAL}"
  # shellcheck disable=SC2162
  read -r -s -p "${KEY_NAME}: " KEY
  echo
  printf '%s' "$KEY"
}

KEY="$(read_key)"
KEY="$(printf '%s' "$KEY" | tr -d '\r\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')"
if [[ -z "$KEY" ]]; then
  echo "error: empty key" >&2
  exit 1
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

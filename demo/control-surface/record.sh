#!/usr/bin/env bash
set -euo pipefail
ROOT="/Users/gilraitses/wavves_build"
CAP="/Users/gilraitses/magatfairy/demo_data/exports/finder_walkthrough"
OUT_DIR="$ROOT/demo/control-surface/output"
DESKTOP="/Users/gilraitses/Desktop"
PORT="${PORT:-8767}"
STAMP="$(date +%Y%m%d_%H%M%S)"
FINAL="$DESKTOP/wavves_control_surface_${STAMP}.mp4"
ALIAS="$DESKTOP/wavves_control_surface.mp4"
ASSET="$ROOT/assets/wavves-control-surface.mp4"
URL="http://127.0.0.1:${PORT}/demo/control-surface/index.html"

mkdir -p "$OUT_DIR" "$ROOT/assets"
export PATH="/opt/homebrew/bin:$PATH"
export OUT_DIR URL FINAL_MP4="$FINAL" DESKTOP_ALIAS="$ALIAS"

if lsof -tiTCP:"$PORT" -sTCP:LISTEN >/dev/null 2>&1; then
  kill "$(lsof -tiTCP:"$PORT" -sTCP:LISTEN)" 2>/dev/null || true
  sleep 0.4
fi

python3 -m http.server "$PORT" --bind 127.0.0.1 --directory "$ROOT" >/tmp/wavves_finder_http.log 2>&1 &
HTTP_PID=$!
trap 'kill $HTTP_PID 2>/dev/null || true' EXIT
sleep 0.5

cd "$CAP"
echo "Capturing $URL"
node record.mjs
cp -f "$FINAL" "$ASSET"
ls -lh "$FINAL" "$ALIAS" "$ASSET"
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$FINAL"
echo "DONE $FINAL"

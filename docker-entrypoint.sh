#!/bin/sh
set -eu

MARIMO_HOST="${MARIMO_HOST:-0.0.0.0}"
MARIMO_DISPLAY_HOST="${MARIMO_DISPLAY_HOST:-localhost}"
if [ -z "${MARIMO_TOKEN_PASSWORD:-}" ]; then
  MARIMO_TOKEN_PASSWORD="$(openssl rand -hex 16)"
  export MARIMO_TOKEN_PASSWORD
fi

npx -y stdio-to-ws "npx -y opencode-ai acp" --port "${OPENCODE_PORT:-3023}" &
agent_pid=$!
cleanup() {
  kill "$agent_pid" 2>/dev/null || true
}
trap cleanup INT TERM EXIT

printf 'Open Marimo at http://%s:%s?access_token=%s\n' "$MARIMO_DISPLAY_HOST" "${MARIMO_PORT:-2718}" "${MARIMO_TOKEN_PASSWORD}"

marimo "$@" --host "$MARIMO_HOST" --token-password "$MARIMO_TOKEN_PASSWORD"


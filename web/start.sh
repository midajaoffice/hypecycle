#!/usr/bin/env bash
# HypeCycle Dashboard — lokaler Webserver
cd "$(dirname "$0")/.." || exit 1
PORT="${PORT:-8765}"
echo ""
echo "  HypeCycle Dashboard"
echo "  → http://localhost:${PORT}/web/"
echo ""
echo "  Stoppen: Ctrl+C"
echo ""
exec python3 -m http.server "$PORT"

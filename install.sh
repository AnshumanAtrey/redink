#!/usr/bin/env bash
# install.sh — register redink as a Claude Code plugin
#
# Usage:
#   ./install.sh             # symlink into ~/.claude/plugins (user scope)
#   ./install.sh --project   # use as a project-local plugin (no symlink)
#
# Requires: Claude Code 2.1+

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLUGIN_NAME="redink"
SCOPE="user"

for arg in "$@"; do
  case "$arg" in
    --project) SCOPE="project" ;;
    --user)    SCOPE="user" ;;
    -h|--help)
      grep -E '^# ' "$0" | sed 's/^# //'
      exit 0
      ;;
    *)
      echo "Unknown flag: $arg" >&2
      exit 1
      ;;
  esac
done

if [ "$SCOPE" = "project" ]; then
  echo "[install] Using project scope — no symlink needed."
  echo "[install] Open Claude Code from this directory; it will pick up .claude/ automatically."
  exit 0
fi

PLUGIN_DIR="$HOME/.claude/plugins/$PLUGIN_NAME"
mkdir -p "$HOME/.claude/plugins"

if [ -e "$PLUGIN_DIR" ] && [ ! -L "$PLUGIN_DIR" ]; then
  echo "[install] ERROR: $PLUGIN_DIR exists and is not a symlink. Refusing to overwrite." >&2
  echo "[install] Move or remove it first, then re-run." >&2
  exit 1
fi

if [ -L "$PLUGIN_DIR" ]; then
  echo "[install] Removing existing symlink: $PLUGIN_DIR"
  rm "$PLUGIN_DIR"
fi

ln -s "$REPO_DIR" "$PLUGIN_DIR"
echo "[install] Linked: $PLUGIN_DIR -> $REPO_DIR"
echo
echo "[install] Python deps (for assembler + recipe picker):"
echo "  pip install python-docx pyyaml"
echo
echo "[install] Done."
echo "  Claude Code users:   open Claude Code anywhere, then  /redink-recipe  and  /redink-build"
echo "  Codex / Cursor / Gemini / Aider / Kimi users:  see AGENTS.md, use python3 scripts/recipe.py + assemble_docx.py"
echo "  (To uninstall: rm $PLUGIN_DIR)"

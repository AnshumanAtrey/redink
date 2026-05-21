#!/usr/bin/env python3
"""
recipe.py — interactive section picker for redink (no LLM needed).

Walks every section under sections/, asks Y/N for each, writes report-recipe.yaml.
The standalone Python equivalent of Claude Code's /redink-recipe slash command,
for users running redink with Codex / Cursor / Gemini CLI / Aider / Kimi or just bare Python.

Reads:
  - framework.yaml              — active framework (sets defaults)
  - frameworks/<active>/manifest.yaml — section defaults + explicitly_excluded_sections
  - sections/<id>/section.md    — section title + description for the prompts

Writes:
  - report-recipe.yaml          — the user's section selection

Usage:
    python3 scripts/recipe.py
    python3 scripts/recipe.py --framework owasp-optrs
    python3 scripts/recipe.py --reset                # ignore any existing recipe
    python3 scripts/recipe.py --non-interactive      # accept all framework defaults, no prompts

Requires: pyyaml
    pip install pyyaml
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore
except ImportError:
    sys.exit("error: pyyaml not installed. Run: pip install pyyaml")


REPO_ROOT = Path(__file__).resolve().parent.parent
SECTIONS_DIR = REPO_ROOT / "sections"
FRAMEWORKS_DIR = REPO_ROOT / "frameworks"
FRAMEWORK_FILE = REPO_ROOT / "framework.yaml"
RECIPE_FILE = REPO_ROOT / "report-recipe.yaml"


def load_framework_name(override: str | None) -> str:
    if override:
        return override
    if not FRAMEWORK_FILE.exists():
        sys.exit(f"error: {FRAMEWORK_FILE} not found.")
    data = yaml.safe_load(FRAMEWORK_FILE.read_text())
    name = data.get("framework") if isinstance(data, dict) else None
    if not name:
        sys.exit("error: framework.yaml does not specify 'framework: <name>'.")
    return name


def load_framework_manifest(name: str) -> dict[str, Any]:
    fw_dir = FRAMEWORKS_DIR / name
    if not fw_dir.exists():
        avail = sorted(p.name for p in FRAMEWORKS_DIR.iterdir() if p.is_dir())
        sys.exit(f"error: framework '{name}' not found. Available: {', '.join(avail)}")
    manifest = fw_dir / "manifest.yaml"
    if not manifest.exists():
        sys.exit(f"error: {manifest} missing.")
    return yaml.safe_load(manifest.read_text())


def list_sections() -> list[str]:
    """Return section IDs in folder-name order (which is also numeric)."""
    return sorted(p.name for p in SECTIONS_DIR.iterdir() if p.is_dir())


def parse_section_frontmatter(section_id: str) -> dict[str, Any]:
    md = SECTIONS_DIR / section_id / "section.md"
    if not md.exists():
        return {}
    text = md.read_text()
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    return yaml.safe_load(m.group(1)) or {}


def parse_section_description(section_id: str) -> str:
    """Extract the first non-empty paragraph after the H1 heading from section.md."""
    md = SECTIONS_DIR / section_id / "section.md"
    if not md.exists():
        return ""
    text = md.read_text()
    # Drop frontmatter
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.DOTALL)
    # Find first H1 and capture text until next heading
    m = re.search(r"^# .+?\n+(.+?)(?:\n##|\n---|\Z)", text, re.DOTALL)
    if m:
        desc = m.group(1).strip()
        # First sentence or first 200 chars
        first_sentence = re.split(r"(?<=\.) ", desc)[0]
        return first_sentence[:200]
    return ""


def ask_yn(prompt: str, default: bool) -> bool:
    default_str = "[Y/n]" if default else "[y/N]"
    while True:
        try:
            ans = input(f"{prompt} {default_str} ").strip().lower()
        except EOFError:
            return default
        if ans == "":
            return default
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("  → please answer y or n (or press Enter to accept default)")


def build_recipe_interactive(framework: str, manifest: dict[str, Any]) -> dict[str, Any]:
    defaults = set(manifest.get("sections", []))
    excluded = set(manifest.get("explicitly_excluded_sections", []))
    sections = list_sections()

    print()
    print("=" * 70)
    print(f"  redink — section picker")
    print(f"  Active framework: {framework} ({manifest.get('name', '?')})")
    print(f"  This preset enables {len(defaults)} of {len(sections)} sections by default.")
    if excluded:
        print(f"  This framework explicitly EXCLUDES: {', '.join(sorted(excluded))}")
    print("=" * 70)
    print()
    print("  For each section, press Enter to accept the framework default,")
    print("  or type y / n to override.")
    print()

    selections: dict[str, bool] = {}
    for sid in sections:
        fm = parse_section_frontmatter(sid)
        title = fm.get("title", sid)
        desc = parse_section_description(sid)
        is_default = sid in defaults
        is_excluded = sid in excluded

        marker = "✓" if is_default else ("⊘" if is_excluded else "·")
        default_str = "ENABLED" if is_default else ("EXCLUDED by framework" if is_excluded else "disabled")

        print(f"  [{marker}] {sid} — {title}")
        if desc:
            print(f"      {desc}")
        print(f"      Default for {framework}: {default_str}")

        if is_excluded:
            print(f"      ⚠  This framework explicitly excludes this section.")
            answer = ask_yn("      Include anyway?", False)
        else:
            answer = ask_yn("      Include in this engagement?", is_default)

        selections[sid] = answer
        print()

    return {
        "framework_preset": framework,
        "generated_at": date.today().isoformat(),
        "total_sections_enabled": sum(1 for v in selections.values() if v),
        "sections": [
            {"id": sid, "enabled": selections[sid]}
            for sid in sections
        ],
    }


def build_recipe_non_interactive(framework: str, manifest: dict[str, Any]) -> dict[str, Any]:
    """Accept all framework defaults without asking."""
    defaults = set(manifest.get("sections", []))
    sections = list_sections()
    return {
        "framework_preset": framework,
        "generated_at": date.today().isoformat(),
        "total_sections_enabled": len(defaults & set(sections)),
        "sections": [
            {"id": sid, "enabled": sid in defaults}
            for sid in sections
        ],
    }


def write_recipe(recipe: dict[str, Any]) -> Path:
    # Custom dump for the inline {id: ..., enabled: ...} style
    lines = [
        f"# Generated by scripts/recipe.py on {recipe['generated_at']}",
        f"# Edit by hand or re-run scripts/recipe.py (or /redink-recipe in Claude Code).",
        "",
        f"framework_preset: {recipe['framework_preset']}",
        f"generated_at: {recipe['generated_at']}",
        f"total_sections_enabled: {recipe['total_sections_enabled']}",
        "",
        "sections:",
    ]
    for s in recipe["sections"]:
        lines.append(f"  - {{ id: {s['id']}, enabled: {str(s['enabled']).lower()} }}")
    lines.append("")
    RECIPE_FILE.write_text("\n".join(lines))
    return RECIPE_FILE


def main() -> None:
    parser = argparse.ArgumentParser(description="Interactive section picker for redink.")
    parser.add_argument("--framework", help="Override framework.yaml for this picker run.", default=None)
    parser.add_argument("--reset", action="store_true", help="Ignore any existing report-recipe.yaml.")
    parser.add_argument("--non-interactive", action="store_true", help="Accept all framework defaults; do not prompt.")
    args = parser.parse_args()

    framework = load_framework_name(args.framework)
    manifest = load_framework_manifest(framework)

    if args.non_interactive:
        recipe = build_recipe_non_interactive(framework, manifest)
    else:
        recipe = build_recipe_interactive(framework, manifest)

    print()
    print("=" * 70)
    print(f"  RECIPE SUMMARY ({recipe['total_sections_enabled']} sections enabled)")
    print("=" * 70)
    for s in recipe["sections"]:
        mark = "✓" if s["enabled"] else "✗"
        print(f"  {mark}  {s['id']}")
    print()

    if not args.non_interactive:
        confirm = ask_yn("Save to report-recipe.yaml?", True)
        if not confirm:
            print("Aborted. Existing report-recipe.yaml is unchanged.")
            return

    output = write_recipe(recipe)
    print(f"✓ Recipe saved to {output.relative_to(REPO_ROOT)}")
    print(f"  Run scripts/assemble_docx.py (or /redink-build in Claude Code) to assemble.")


if __name__ == "__main__":
    main()

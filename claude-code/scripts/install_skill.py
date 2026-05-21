#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import shutil
from pathlib import Path


SKILL_NAME = "pink-starfish-pet"


def claude_home() -> Path:
    override = os.environ.get("CLAUDE_HOME")
    if override:
        return Path(override).expanduser()
    return Path.home() / ".claude"


def ignore_for_install(_directory: str, names: list[str]) -> set[str]:
    ignored = {
        ".git",
        ".github",
        "__pycache__",
        ".pytest_cache",
        ".ruff_cache",
        ".DS_Store",
    }
    return {
        name
        for name in names
        if name in ignored or name.startswith(".") or name.endswith(".pyc")
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Install the Pink Starfish Claude Code skill.")
    parser.add_argument(
        "--claude-home",
        help="Override Claude home. Defaults to CLAUDE_HOME or ~/.claude.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the target directory without copying files.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing installed skill directory.",
    )
    args = parser.parse_args()

    source_dir = Path(__file__).resolve().parents[1]
    home = Path(args.claude_home).expanduser() if args.claude_home else claude_home()
    target_dir = home / "skills" / SKILL_NAME

    print(f"source_dir={source_dir}")
    print(f"target_dir={target_dir}")
    if args.dry_run:
        return

    if target_dir.exists():
        if not args.force:
            raise SystemExit(f"Target already exists: {target_dir} (use --force to replace)")
        shutil.rmtree(target_dir)

    target_dir.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source_dir, target_dir, ignore=ignore_for_install)
    print("installed=true")


if __name__ == "__main__":
    main()

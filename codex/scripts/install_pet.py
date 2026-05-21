#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import shutil
from pathlib import Path


PET_ID = "pink-starfish"


def codex_home() -> Path:
    override = os.environ.get("CODEX_HOME")
    if override:
        return Path(override).expanduser()
    return Path.home() / ".codex"


def main() -> None:
    parser = argparse.ArgumentParser(description="Install the Pink Starfish Codex pet.")
    parser.add_argument(
        "--codex-home",
        help="Override Codex home. Defaults to CODEX_HOME or ~/.codex.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the target files without copying.",
    )
    args = parser.parse_args()

    skill_dir = Path(__file__).resolve().parents[1]
    assets = skill_dir / "assets"
    source_pet = assets / "pet.json"
    source_sheet = assets / "spritesheet.webp"
    if not source_pet.is_file() or not source_sheet.is_file():
        raise SystemExit("Missing assets/pet.json or assets/spritesheet.webp")

    home = Path(args.codex_home).expanduser() if args.codex_home else codex_home()
    target_dir = home / "pets" / PET_ID
    target_pet = target_dir / "pet.json"
    target_sheet = target_dir / "spritesheet.webp"

    print(f"target_dir={target_dir}")
    print(f"pet_json={target_pet}")
    print(f"spritesheet={target_sheet}")
    if args.dry_run:
        return

    target_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_sheet, target_sheet)

    pet = json.loads(source_pet.read_text(encoding="utf-8"))
    pet["id"] = PET_ID
    pet["spritesheetPath"] = "spritesheet.webp"
    target_pet.write_text(json.dumps(pet, indent=2) + "\n", encoding="utf-8")
    print("installed=true")


if __name__ == "__main__":
    main()

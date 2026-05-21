---
name: pink-starfish-pet
description: Install or package a Codex-compatible Pink Starfish desktop pet from bundled pet assets. Use when the user wants to install, copy, verify, or prepare the pink-starfish pet for local Codex use or GitHub distribution.
---

# Pink Starfish Pet

This skill installs the bundled `pink-starfish` Codex pet. It is a generic sleepy pink starfish desktop pet with patterned green shorts. Do not describe it as an official character, branded asset, or copyrighted franchise resource.

## Install

Run the installer from this skill directory:

```bash
python scripts/install_pet.py
```

The installer copies:

- `assets/pet.json`
- `assets/spritesheet.webp`

to:

```text
${CODEX_HOME:-~/.codex}/pets/pink-starfish/
```

Use `--dry-run` to preview targets, or `--codex-home <path>` to install into a custom Codex home.

## Verify

After installation, check that both files exist:

```text
~/.codex/pets/pink-starfish/pet.json
~/.codex/pets/pink-starfish/spritesheet.webp
```

If Codex already had a pet loaded, switch pets or restart Codex to refresh cached sprites.

## Publishing Notes

For public distribution, keep the generic name `pink-starfish-pet`. Do not add official show names, character names, logos, screenshots, quotes, or trademarked branding to the repository metadata or prompts.

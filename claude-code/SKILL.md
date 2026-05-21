---
name: pink-starfish-pet
description: Install, inspect, or package a bundled Pink Starfish desktop pet asset set for Claude Code workflows. Use when the user wants a Claude Code skill that carries pet assets, installs this skill into ~/.claude/skills, or copies the bundled pet manifest and spritesheet into another compatible pet runtime.
---

# Pink Starfish Pet

This Claude Code skill bundles a generic sleepy pink starfish desktop pet asset set.
It includes a transparent spritesheet and a small manifest for compatible pet runtimes.

Do not describe this pet as an official character, branded asset, or franchise resource.
Keep public wording generic: "pink starfish", "desktop pet", or "pet asset set".

## Install This Skill

From the repository root:

```bash
python scripts/install_skill.py
```

This copies the full skill folder into:

```text
${CLAUDE_HOME:-~/.claude}/skills/pink-starfish-pet/
```

Use:

```bash
python scripts/install_skill.py --dry-run
python scripts/install_skill.py --force
python scripts/install_skill.py --claude-home /path/to/.claude
```

## Use The Bundled Assets

Pet files live in:

```text
assets/pet.json
assets/spritesheet.webp
```

When a user wants to install the pet into a compatible runtime, copy both files together
to that runtime's pet directory. Keep `spritesheetPath` in `pet.json` as `spritesheet.webp`.

For atlas details, read `references/pet-format.md`.

## Public Distribution

For GitHub releases, keep the repository name and metadata generic, such as
`pink-starfish-claude-skill`. Do not add official show names, character names, logos,
screenshots, quotes, or trademarked branding.

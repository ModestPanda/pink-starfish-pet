# Pet Asset Format

The bundled pet assets are stored under `assets/`.

- `pet.json`: generic manifest for tools that understand Codex-style desktop pets.
- `spritesheet.webp`: a transparent, lossless WebP animation atlas.

Atlas geometry:

- 8 columns
- 9 rows
- 192x208 cells
- 1536x1872 total size

Rows:

0. idle, 6 frames
1. running-right, 8 frames
2. running-left, 8 frames
3. waving, 4 frames
4. jumping, 5 frames
5. failed, 8 frames
6. waiting, 6 frames
7. running, 6 frames
8. review, 6 frames

Claude Code skills do not currently define a universal desktop-pet runtime contract.
Treat these files as bundled assets that can be copied into a compatible pet runtime,
viewer, or downstream customization workflow.

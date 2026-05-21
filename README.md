# Pink Starfish Pet

[English](#english) | [中文](#中文)

![Pink Starfish preview](codex/assets/spritesheet.webp)

## English

A cozy pink starfish desktop pet packaged for both Codex and Claude Code workflows.

This repository contains two installable variants:

- `codex/` - Codex pet skill and installer
- `claude-code/` - Claude Code skill that bundles the same pet assets

The pet is an original, generic pink starfish desktop companion with a transparent
animated spritesheet.

### Repository Layout

```text
pink-starfish-pet/
  README.md
  codex/
    SKILL.md
    agents/openai.yaml
    assets/pet.json
    assets/spritesheet.webp
    scripts/install_pet.py
  claude-code/
    SKILL.md
    assets/pet.json
    assets/spritesheet.webp
    references/pet-format.md
    scripts/install_skill.py
```

### Install For Codex

From the repository root:

```bash
cd codex
python scripts/install_pet.py
```

This installs the pet into:

```text
${CODEX_HOME:-~/.codex}/pets/pink-starfish/
```

If Codex already had a pet loaded, switch pets or restart Codex to refresh cached sprites.

### Install For Claude Code

From the repository root:

```bash
cd claude-code
python scripts/install_skill.py
```

This installs the Claude Code skill into:

```text
${CLAUDE_HOME:-~/.claude}/skills/pink-starfish-pet/
```

Claude Code skills do not currently define a universal desktop-pet runtime. The
Claude Code variant bundles the pet assets so Claude can inspect, copy, package,
or adapt them for compatible downstream tooling.

### Pet Details

- Pet id: `pink-starfish`
- Display name: `Pink Starfish`
- Atlas size: `1536x1872`
- Cell size: `192x208`
- Format: transparent lossless WebP

### Public Use Notes

This package uses generic pink starfish naming and does not include official logos,
screenshots, names, quotes, or other branded materials.

## 中文

这是一个粉色海星桌面宠物资源仓库，同时提供 Codex 和 Claude Code 两个版本。

仓库包含两个可安装目录：

- `codex/` - Codex pet skill 和安装脚本
- `claude-code/` - Claude Code skill，内置同一套 pet 资源

这个 pet 是原创的通用粉色海星桌面伙伴，使用带透明通道的动画 spritesheet。

### 仓库结构

```text
pink-starfish-pet/
  README.md
  codex/
    SKILL.md
    agents/openai.yaml
    assets/pet.json
    assets/spritesheet.webp
    scripts/install_pet.py
  claude-code/
    SKILL.md
    assets/pet.json
    assets/spritesheet.webp
    references/pet-format.md
    scripts/install_skill.py
```

### 安装到 Codex

在仓库根目录运行：

```bash
cd codex
python scripts/install_pet.py
```

默认安装到：

```text
${CODEX_HOME:-~/.codex}/pets/pink-starfish/
```

如果安装后没有立刻显示，可以在 Codex 里切换 pet，或者重启 Codex 刷新缓存。

### 安装到 Claude Code

在仓库根目录运行：

```bash
cd claude-code
python scripts/install_skill.py
```

默认安装到：

```text
${CLAUDE_HOME:-~/.claude}/skills/pink-starfish-pet/
```

Claude Code skill 目前没有统一的桌面宠物运行时规范。Claude Code 版本会把 pet
资源打包进 skill，方便 Claude 查看、复制、再打包，或适配到其他兼容工具。

### Pet 信息

- Pet id: `pink-starfish`
- 显示名称：`Pink Starfish`
- 图集尺寸：`1536x1872`
- 单元格尺寸：`192x208`
- 格式：带透明通道的 lossless WebP

### 公开使用说明

这个仓库使用通用粉色海星命名，不包含官方 logo、截图、角色名称、台词或其他品牌素材。

## License

Choose a license before publishing the repository publicly.

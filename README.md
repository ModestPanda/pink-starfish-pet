# Pink Starfish Pet

[English](#english) | [中文](#中文)

![Pink Starfish preview](assets/spritesheet.webp)

## English

A cozy Codex skill that installs a bundled sleepy pink starfish desktop pet.

This repository packages a ready-to-use Codex desktop pet with a soft cartoon
spritesheet, a small installer, and the skill metadata needed for Codex to
recognize it.

### What Is Included

- `SKILL.md` - Codex skill instructions
- `agents/openai.yaml` - Codex UI metadata
- `assets/pet.json` - Pet manifest
- `assets/spritesheet.webp` - Animated pet spritesheet
- `scripts/install_pet.py` - Local installer

### Install

Clone or download this repository, then run:

```bash
python scripts/install_pet.py
```

The installer copies the pet into:

```text
${CODEX_HOME:-~/.codex}/pets/pink-starfish/
```

After installing, switch pets or restart Codex if the new pet does not appear
immediately.

### Custom Codex Home

```bash
python scripts/install_pet.py --codex-home /path/to/.codex
```

Preview the target paths without copying files:

```bash
python scripts/install_pet.py --dry-run
```

### Pet Details

- Pet id: `pink-starfish`
- Display name: `Pink Starfish`
- Atlas size: `1536x1872`
- Cell size: `192x208`
- Format: lossless WebP with transparency

### Notes

This is an original, generic pink starfish desktop pet package for personal
Codex customization. It does not include official logos, screenshots, names,
quotes, or other branded assets.

## 中文

这是一个用于 Codex 的粉色海星桌面宠物 skill。它包含已经制作好的动画
spritesheet、安装脚本，以及让 Codex 识别这个 pet 所需的 skill 元数据。

### 包含内容

- `SKILL.md` - Codex skill 说明
- `agents/openai.yaml` - Codex UI 元数据
- `assets/pet.json` - pet 配置文件
- `assets/spritesheet.webp` - 动画 spritesheet
- `scripts/install_pet.py` - 本地安装脚本

### 安装

克隆或下载这个仓库后，在仓库根目录运行：

```bash
python scripts/install_pet.py
```

安装脚本会把 pet 复制到：

```text
${CODEX_HOME:-~/.codex}/pets/pink-starfish/
```

如果安装后没有立刻显示，可以在 Codex 里切换 pet，或者重启 Codex 来刷新缓存。

### 自定义 Codex Home

如果你想安装到指定的 Codex 目录：

```bash
python scripts/install_pet.py --codex-home /path/to/.codex
```

只预览安装路径、不复制文件：

```bash
python scripts/install_pet.py --dry-run
```

### Pet 信息

- Pet id: `pink-starfish`
- 显示名称：`Pink Starfish`
- 图集尺寸：`1536x1872`
- 单元格尺寸：`192x208`
- 格式：带透明通道的 lossless WebP

### 说明

这是一个原创的通用粉色海星桌面宠物包，用于个人 Codex 自定义。仓库不包含官方
logo、截图、角色名称、台词或其他品牌素材。

## License

Choose the license that fits how you want others to use the pet before making
the repository public.

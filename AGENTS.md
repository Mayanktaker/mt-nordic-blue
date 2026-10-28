# AGENTS.md — MT Nordic Blue

© Mayanktaker Computers & Web Development | https://mayanktaker.com

GNOME dark theme suite: Shell + GTK3 + GTK4 (best-effort) + Flatpak GTK3 extension + Companion Icon Pack + Cursor Pack + Procedural 4K Wallpapers + App Extras.
Display name **MT Nordic Blue**, technical/theme-dir name `MT-Nordic-Blue`.

## Stack & toolchain (verify before assuming; update when versions change)
- Targets: GNOME Shell 50.x and 51.x (Wayland/X11). Host: GNOME Shell 51.1.
- Build: `sassc` (libsass 3.6.6), Python 3 + `numpy` 2.5.4 + `Pillow` 13.0.0 + `pycairo` + `PyGObject` (Rsvg, Gio).
- Repo: git 2.56, `gh` authenticated as `Mayanktaker`, default branch `master`.
- **Installation policy:** ALWAYS install user themes into the user's `~/.themes` (e.g. `/home/<user>/.themes`) ONLY, and user icon/cursor packs into the user's `~/.icons` (e.g. `/home/<user>/.icons`) ONLY — never `~/.local/share/themes`, `~/.local/share/icons`, or system dirs. `tools/install.sh` implements and maintains this. Shell activation requires the **User Themes** extension (`user-theme@gnome-shell-extensions.gcampax.github.com`).
- **Installer behavior:** `tools/install.sh` detects distro (`/etc/os-release`) + GNOME Shell major (50/51), checks missing dependencies (python3, gi, sassc, numpy, Pillow, User Themes extension), prints distro install commands, and uses **sudo only for system package installs** via `--install-deps`; theme install itself is strictly unprivileged. Old installs under `~/.local/share/themes` are moved to `deleted_files_folders/`, never hard-deleted.

## Single source of truth
- `palette/tokens.json` — every color in CSS/wallpaper/builds comes from here. No magic values; add tokens instead.
- `palette/presets/` — curated starting configurations:
  - `nordic-polar-night.json` (Deep Polar Night #0E141D, default)
  - `nordic-classic.json` (Classic Nord Spec #2E3440)
  - `nordic-cyber-frost.json` (Arctic Cyber Frost #0A0E17 / #00D2FF)
- Shell theme is derived from upstream GNOME Shell CSS per major version, recolored via `src/shell/` maps (never hand-edit generated CSS).
- Icons & Cursors dynamically draw gradients and geometry fills from `palette/tokens.json`.

## Quick Scaffold / Initialization
- Rebrand or switch palette: `python3 init_theme.py [--preset <name>] [--name "Theme Name"] [--accent "#HEX"]`

## Build & Test Commands
- Unified master build: `python3 build_all.py` (runs contrast gate, GTK, Shell 50/51, icons, cursors, wallpapers in sequence).
- Contrast gate: `python3 tools/dev/check_contrast.py` (must pass before commits).
- GTK build: `python3 tools/gtk/build.py` → `build/theme/gtk-{3,4}.0/`.
- Shell build: `python3 tools/shell/build.py [--major N | --all]` (extracts host CSS or uses `src/shell/upstream-<major>/`).
- Icons build: `python3 tools/icons/generate_icons.py` → `src/icons/MT-Nordic-Blue-Icons/`.
- Cursors build: `python3 tools/icons/generate_cursors.py` → `src/cursors/MT-Nordic-Blue-Cursors/`.
- Wallpaper suite: `python3 tools/wallpaper/generate.py [--which 1|2|3|4|all]` (dark) and `python3 tools/wallpaper/process_light.py` (light).
- Install suite: `./install.sh` (interactive CLI wizard) or `tools/install.sh [--panel round-island|pill|bottom-round|flat] [--corners round|sharp] [--controls standard|macos] [--size standard|compact] [--base polar|classic|cyber|oled] [--accent frost|glacier|aurora|arctic|cyber|blaze] [--blur|--no-blur] [--icons] [--gtk4-libadwaita] [--wallpaper all]`.
- App ecosystem install: `tools/extras/install-all.sh`.
- Package release: `tools/release.sh <version>`.

## Layout
- `palette/` tokens (`tokens.json` single source of truth) + `presets/` library
- `src/` source layers (gtk-2.0, gtk-3.0, gtk-4.0, shell colormaps, tweaks, icons, cursors)
- `tools/` build engines (gtk, shell, icons, wallpapers, dev contrast gate, installer, packager)
- `extras/` application themes (terminals, shells, editors, KDE, GDM, SDDM, GRUB, Plymouth)
- `flatpak/` extension manifest + appdata (`org.gtk.Gtk3theme.MT-Nordic-Blue`)
- `docs/` documentation (`workflow.md`, `design.md`, `compatibility.md`, `flatpak.md`)
- `init_theme.py` rapid rebranding & setup script
- `build_all.py` master build runner

## Documentation pointers (do not duplicate content here)
- `docs/design.md` — design direction, token table, wallpaper rules
- `docs/compatibility.md` — GNOME version matrix + test checklist
- `docs/flatpak.md` — Flatpak GTK3 theme extension plan & status
- `docs/workflow.md` — build/release workflow

## Conventions
- Every file starts with the © header: `© Mayanktaker Computers & Web Development | https://mayanktaker.com`.
- Every function/block gets ≤1-line comment.
- License: GPL-3.0 (code/CSS) + CC BY-SA 4.0 (artwork). See `LICENSES/`.

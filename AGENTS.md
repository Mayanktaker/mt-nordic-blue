# AGENTS.md — MT Nordic Blue

© Mayanktaker Computers & Web Development | https://mayanktaker.com

GNOME dark theme suite: Shell + GTK3 + GTK4 (best-effort) + Flatpak GTK3 extension + Companion Icon Pack + Cursor Pack + Procedural 4K Wallpapers + App Extras.
Display name **MT Nordic Blue**, technical/theme-dir name `MT-Nordic-Blue`.

## Stack & toolchain (verify before assuming; update when versions change)
- Targets: GNOME Shell 50.x and 51.x (host dev machine: GNOME Shell 51.1, Wayland).
- Build: `sassc` (libsass 3.6.6), Python 3 + `numpy` 2.5.4 + `Pillow` 13.0.0 + `pycairo` + `PyGObject` (Rsvg, Gio).
- Repo: git 2.56, `gh` 2.102.1 authenticated as `Mayanktaker`, default branch `master`.
- **Installation policy:** ALWAYS install user themes into the user's `~/.themes` (e.g. `/home/<user>/.themes`) ONLY, and user icon/cursor packs into the user's `~/.icons` (e.g. `/home/<user>/.icons`) ONLY — never `~/.local/share/themes`, `~/.local/share/icons`, or system dirs. `tools/install.sh` implements and maintains this. Shell activation requires the **User Themes** extension (`user-theme@gnome-shell-extensions.gcampax.github.com`).
- **Installer behavior:** `tools/install.sh` detects distro (`/etc/os-release`) + GNOME Shell major (50/51), checks missing dependencies (python3, gi, sassc, numpy, Pillow, User Themes extension), prints distro install commands, and uses **sudo only for system package installs** via `--install-deps`; theme install itself is strictly unprivileged. Old installs under `~/.local/share/themes` are moved to `deleted_files_folders/`, never hard-deleted.

## Single source of truth
- `palette/tokens.json` — every color in CSS/wallpaper/builds comes from here. No magic values; add tokens instead.
- `palette/presets/` — curated starting configurations:
  - `nordic-polar-night.json` (Deep Polar Night #0E141D, default)
  - `nordic-classic.json` (Classic Nord Spec #2E3440)
  - `nordic-cyber-frost.json` (Arctic Cyber Frost #0A0E17 / #00D2FF)
  - `nordic-snow-storm.json` (Nordic Snow Storm Light #E5E9F0 / #ECEFF4)
- Shell theme is derived from upstream GNOME Shell CSS per major version, recolored via `src/shell/` maps into both **MT Nordic Blue** (`~/.themes/MT-Nordic-Blue/gnome-shell/`) and **MT Nordic Light** (`~/.themes/MT-Nordic-Light/gnome-shell/`) (never hand-edit generated CSS).
- Wallpapers: 4K 3D Glacial Silk Bloom suite generated procedurally via Cairo vectors (`tools/wallpaper/generate.py` for dark and `tools/wallpaper/process_light.py` for light) with inverted high-contrast adaptive pairing in GNOME Settings.
- Icons & Cursors dynamically draw gradients and geometry fills from `palette/tokens.json`. Companion icon pack inherits `Tela-circle,Adwaita,breeze-dark,breeze,hicolor` with full FreeDesktop & KDE standards metadata and standalone form-control symbolic glyphs (`object-select-symbolic`, `check-symbolic`, `checkbox-checked-symbolic`, `radio-checked-symbolic`).
- Icon coverage: ~480 app names (153 hand-drawn + 7 popular-app batches + aliases), 119 mimetypes via badge engine (`tools/icons/mime_assets.py`), 26 GNOME Settings symbolics, 16 misc FreeDesktop symbolics. Batch modules: `apps_popular_1..7.py`, `settings_symbolics.py`, `misc_symbolics.py`, `apps_extra.py`.

## Commands
- Contrast gate: `python3 tools/dev/check_contrast.py` (must pass before commits).
- Icon context gate: `python3 tools/dev/check_icon_contexts.py` (catches lookup-order shadowing + dangling aliases; run after icon builds).
- Wallpaper suite: `python3 tools/wallpaper/generate.py [--which 1|2|3|4|all]` (dark) and `python3 tools/wallpaper/process_light.py` (light) → generates 4K renders into `wallpaper/dist/` and `wallpaper/dist/light/` + preview JPGs in `wallpaper/preview/`.
- Icons & Cursors build: `python3 tools/icons/generate_icons.py && python3 tools/icons/generate_cursors.py` → builds `src/icons/MT-Nordic-Blue-Icons` and `src/cursors/MT-Nordic-Blue-Cursors`.
- Icons packaging: `tools/icons/package.sh [version]` → creates `dist/mt-nordic-blue-icons-v<version>.tar.xz`.
- Shell theme build: `python3 tools/shell/build.py [--major N | --all]` (host major extracts from gresource; others use vendored `src/shell/upstream-<major>/`).
- GTK build: `python3 tools/gtk/build.py` → `build/theme/gtk-{3,4}.0/`.
- Unified master build: `python3 build_all.py` (runs contrast gate, GTK, Shell 50/51, icons, cursors, wallpapers in sequence).
- Install: `./install.sh` (interactive CLI wizard) or `tools/install.sh [--panel round-island|pill|bottom-round|flat] [--corners round|sharp] [--controls standard|macos] [--size standard|compact] [--base polar|classic|cyber|oled] [--accent frost|glacier|aurora|arctic|cyber|blaze] [--blur|--no-blur] [--icons] [--gtk4-libadwaita] [--wallpaper [1-4|all|none]] [--install-deps]` → installs theme into `~/.themes/MT-Nordic-Blue` and companion packs into `~/.icons/`.
- Theme toggle: `mt-nordic-toggle` or shortcut `Super+Shift+T` (switches dark/light shell, GTK, libadwaita, and wallpaper).
- Flatpak overrides: `flatpak/apply-overrides.sh` (grants read-only access to `~/.config/gtk-4.0`, `~/.themes`, and `~/.icons`).
- App extras install: `tools/extras/install-all.sh` (scans & installs for all detected apps) or individual scripts under `extras/`.
- Package release: `tools/release.sh <version>` → creates complete tarball in `dist/` (automated via `.github/workflows/release.yml` on tag push).

## Layout
- `palette/` tokens (`tokens.json` single source of truth) + `presets/` library
- `src/` source layers (gtk-2.0, gtk-3.0, gtk-4.0, shell colormaps, tweaks, icons, cursors)
- `tools/` build engines (gtk, shell, icons, wallpapers, dev contrast gate, installer, packager)
- `extras/` application themes (terminals, shells, editors, KDE, GDM, SDDM, GRUB, Plymouth)
- `flatpak/` extension manifest + appdata (`org.gtk.Gtk3theme.MT-Nordic-Blue`)
- `docs/` documentation (`workflow.md`, `design.md`, `compatibility.md`, `flatpak.md`, `index.html`)
- `build/` generated output (gitignored)
- `dist/` release packages (gitignored)
- `wallpaper/preview/` committed previews

## Documentation pointers (do not duplicate content here)
- `docs/design.md` — Nordic design direction, token table, wallpaper rules
- `docs/compatibility.md` — GNOME version matrix + test checklist
- `docs/flatpak.md` — Flatpak GTK3 theme extension plan & status
- `docs/workflow.md` — build/release workflow
- `docs/index.html` — GitHub Pages interactive showcase site

## Conventions
- Every file starts with the © header: `© Mayanktaker Computers & Web Development | https://mayanktaker.com`.
- Every function/block gets ≤1-line comment.
- License: GPL-3.0 (code/CSS) + CC BY-SA 4.0 (artwork). See `LICENSES/`.
- Public repo `Mayanktaker/mt-nordic-blue`; commit at verified milestones, never force-push, secrets/license scan before push.

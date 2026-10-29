#!/bin/sh
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Install MT Nordic Blue GNOME Suite at user level into ~/.themes ONLY (project policy),
# and companion icon/cursor packs into ~/.icons ONLY.
# Supports interactive CLI wizard, human-friendly settings, modular tweaks, and 4K wallpapers.

set -eu

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
if [ -f "${REPO_ROOT}/palette/tokens.json" ]; then
  THEME_NAME="$(python3 -c "import json; print(json.load(open('${REPO_ROOT}/palette/tokens.json'))['meta']['tech_name'])" 2>/dev/null || echo "MT-Nordic-Blue")"
  DISPLAY_NAME="$(python3 -c "import json; print(json.load(open('${REPO_ROOT}/palette/tokens.json'))['meta']['name'])" 2>/dev/null || echo "MT Nordic Blue")"
else
  THEME_NAME="MT-Nordic-Blue"
  DISPLAY_NAME="MT Nordic Blue"
fi
THEME_DIR="${HOME}/.themes/${THEME_NAME}"
ICONS_NAME="${THEME_NAME}-Icons"
CURSORS_NAME="${THEME_NAME}-Cursors"
ICONS_DIR="${HOME}/.icons"

# Defaults
PANEL_STYLE="round-island"   # Choices: round-island, pill, bottom-round, flat
CORNERS="round"              # Choices: round (16px), sharp (0px non-rounded)
CONTROLS="standard"          # Choices: standard, macos
THEME_SIZE="standard"        # Choices: standard, compact
BASE_PALETTE="polar"         # Choices: polar (deep dark), classic (nord 2e3440), cyber (midnight neon), oled (black)
ACCENT="frost"               # Choices: frost (#88C0D0), glacier (#81A1C1), aurora (#8FBCBB), arctic (#5E81AC), cyber (#00D2FF), blaze (#D08770)
WANT_BLUR=1
WANT_ICONS=1
WANT_GTK4_OVERRIDE=1
WANT_WALLPAPER=1
WALLPAPER_CHOICE="1"
INSTALL_DEPS=0
INTERACTIVE=0
EXPLICIT_ARGS=0
TWEAKS_ARG=""

# Detect if stdin is an interactive terminal and no arguments were passed
if [ $# -eq 0 ] && [ -t 0 ]; then
  INTERACTIVE=1
fi

# ---------- argument parsing ----------
while [ $# -gt 0 ]; do
  EXPLICIT_ARGS=1
  case "$1" in
    --wizard)
      INTERACTIVE=1
      ;;
    --non-interactive|--no-interactive)
      INTERACTIVE=0
      ;;
    --panel|--tray)
      shift
      PANEL_STYLE="${1:-round-island}"
      ;;
    --panel=*|--tray=*)
      PANEL_STYLE="${1#*=}"
      ;;
    --corners)
      shift
      CORNERS="${1:-round}"
      ;;
    --corners=*)
      CORNERS="${1#*=}"
      ;;
    --controls)
      shift
      CONTROLS="${1:-standard}"
      ;;
    --controls=*)
      CONTROLS="${1#*=}"
      ;;
    --size)
      shift
      THEME_SIZE="${1:-standard}"
      ;;
    --size=*)
      THEME_SIZE="${1#*=}"
      ;;
    --base)
      shift
      BASE_PALETTE="${1:-polar}"
      ;;
    --base=*)
      BASE_PALETTE="${1#*=}"
      ;;
    --accent)
      shift
      ACCENT="${1:-frost}"
      ;;
    --accent=*)
      ACCENT="${1#*=}"
      ;;
    --blur)
      WANT_BLUR=1
      ;;
    --no-blur|--noblur)
      WANT_BLUR=0
      ;;
    --icons)
      WANT_ICONS=1
      ;;
    --no-icons)
      WANT_ICONS=0
      ;;
    --gtk4-libadwaita)
      WANT_GTK4_OVERRIDE=1
      ;;
    --no-gtk4-libadwaita)
      WANT_GTK4_OVERRIDE=0
      ;;
    --wallpaper)
      WANT_WALLPAPER=1
      if [ $# -gt 1 ] && [ "${2#-}" = "$2" ]; then
        shift
        WALLPAPER_CHOICE="$1"
      else
        WALLPAPER_CHOICE="1"
      fi
      ;;
    --wallpaper=*)
      WANT_WALLPAPER=1
      WALLPAPER_CHOICE="${1#*=}"
      ;;
    --no-wallpaper)
      WANT_WALLPAPER=0
      WALLPAPER_CHOICE="none"
      ;;
    --tweaks)
      shift
      TWEAKS_ARG="${1:-float,translucent,round}"
      ;;
    --tweaks=*)
      TWEAKS_ARG="${1#*=}"
      ;;
    --install-deps)
      INSTALL_DEPS=1
      ;;
    -h|--help)
      cat <<EOF
Usage: tools/install.sh [options]

Run without arguments in an interactive terminal to launch the setup wizard.

User-Friendly Options:
  --panel, --tray <style> Top bar / tray style:
                            round-island : 16px curved floating island (Default)
                            pill         : 999px full circular capsule ends
                            bottom-round : Connected to top edge with 16px bottom rounded corners
                            flat         : Classic full-width edge-to-edge square bar
  --corners <style>       Corner curvature:
                            round        : Modern 16px smooth rounded curves (Default)
                            sharp        : Non-rounded 0px sharp corners (Industrial/Tiling look)
  --controls <style>      Window controls style: standard (native Adwaita) or macos (Nordic traffic dots)
  --size <type>           Theme density sizing: standard (default) or compact (slim controls)
  --base <flavor>         Background base palette:
                            polar        : Deep Polar Night (#0E141D, Default)
                            classic      : Classic Nord Spec Slate (#2E3440)
                            cyber        : Arctic Cyber Frost Midnight Navy (#0A0E17)
                            oled         : True pitch-black OLED (#040609)
  --accent <flavor>       Accent color variant:
                            frost        : Nordic Frost Cyan (#88C0D0, Default)
                            glacier      : Glacier Ice Blue (#81A1C1)
                            aurora       : Nordic Aurora Teal (#8FBCBB)
                            arctic       : Deep Arctic Blue (#5E81AC)
                            cyber        : Electric Neon Cyan (#00D2FF)
                            blaze        : Nordic Amber Blaze (#D08770)
  --blur / --no-blur      Enable or disable frosted glassmorphism blur and translucency
  --icons / --no-icons    Install companion ${ICONS_NAME} and ${CURSORS_NAME} into ~/.icons
  --gtk4-libadwaita       Link GTK4 styles to ~/.config/gtk-4.0/gtk.css for libadwaita apps
  --wallpaper [choice]    Apply 4K wallpaper (1: Fjord Canopy, 2: Aurora, 3: Glacial Flow, 4: Topographic Frost, all, none)
  --wizard                Force interactive step-by-step setup wizard
  --non-interactive       Skip wizard and apply specified options or defaults directly
  --install-deps          Automatically install missing system dependencies with sudo
  -h, --help              Show this help message
EOF
      exit 0
      ;;
    *)
      echo "unknown option: $1" >&2
      exit 1
      ;;
  esac
  shift
done

# ---------- interactive wizard ----------
if [ "${INTERACTIVE}" -eq 1 ]; then
  cat <<EOF
========================================================================
  ✨ ${DISPLAY_NAME} — Theme Suite Installer & Configurator
========================================================================
Welcome! Press Enter at any prompt to accept the [Default] option.
EOF

  # 1. Top Bar / System Tray Style
  echo ""
  echo "1. System Tray & Top Bar Style:"
  echo "   [1] Rounded Modern Island (16px curved floating bar) [Default]"
  echo "   [2] Floating Pill Capsule (Full circular 999px capsule ends)"
  echo "   [3] Connected Bottom-Rounded (Attached to screen top, 16px bottom rounded corners)"
  echo "   [4] Classic Flat Bar (Full-width edge-to-edge square bar)"
  printf "   Select [1-4, default=1]: "
  read -r choice || choice=""
  case "${choice}" in
    2) PANEL_STYLE="pill" ;;
    3) PANEL_STYLE="bottom-round" ;;
    4) PANEL_STYLE="flat" ;;
    *) PANEL_STYLE="round-island" ;;
  esac

  # 2. Corner Curvature Style
  echo ""
  echo "2. Corner Curvature Style:"
  echo "   [1] Modern Rounded (16px smooth window corners & curved dialogs) [Default]"
  echo "   [2] Sharp / Non-Rounded (0px sharp corners for industrial/tiling aesthetic)"
  printf "   Select [1-2, default=1]: "
  read -r choice || choice=""
  case "${choice}" in
    2) CORNERS="sharp" ;;
    *) CORNERS="round" ;;
  esac

  # 3. Window Controls
  echo ""
  echo "3. Window Titlebar Buttons:"
  echo "   [1] Standard Native Adwaita (Clean system glyphs) [Default]"
  echo "   [2] macOS / Colloid Style (Nordic-tinted traffic dots: Aurora Red, Gold, Green)"
  printf "   Select [1-2, default=1]: "
  read -r choice || choice=""
  case "${choice}" in
    2) CONTROLS="macos" ;;
    *) CONTROLS="standard" ;;
  esac

  # 4. Theme Sizing / Density
  echo ""
  echo "4. Theme Sizing Density:"
  echo "   [1] Standard Sizing (Comfortable upstream GNOME proportions) [Default]"
  echo "   [2] Compact Sizing (Slim headerbars, compact padding, space-saving)"
  printf "   Select [1-2, default=1]: "
  read -r choice || choice=""
  case "${choice}" in
    2) THEME_SIZE="compact" ;;
    *) THEME_SIZE="standard" ;;
  esac

  # 5. Glassmorphism / Blur
  echo ""
  echo "5. Frosted Glassmorphism & Translucency:"
  echo "   [1] Frosted Blur & Translucent Glass (Modern depth) [Default]"
  echo "   [2] Solid Opaque Surfaces (Optimal for low-end GPUs or strict opaque look)"
  printf "   Select [1-2, default=1]: "
  read -r choice || choice=""
  case "${choice}" in
    2) WANT_BLUR=0 ;;
    *) WANT_BLUR=1 ;;
  esac

  # 6. Base Palette Flavor
  echo ""
  echo "6. Theme Base Background Flavor:"
  echo "   [1] Deep Polar Night (#0E141D - High contrast OLED-friendly dark) [Default]"
  echo "   [2] Classic Nord Spec (#2E3440 - Authentic muted Scandinavian slate)"
  echo "   [3] Arctic Cyber Frost (#0A0E17 - Midnight navy cyber aesthetic)"
  echo "   [4] Pitch OLED Black (#040609 - True pitch black for OLED screens)"
  printf "   Select [1-4, default=1]: "
  read -r choice || choice=""
  case "${choice}" in
    2) BASE_PALETTE="classic" ;;
    3) BASE_PALETTE="cyber" ;;
    4) BASE_PALETTE="oled" ;;
    *) BASE_PALETTE="polar" ;;
  esac

  # 7. Accent Color Flavor
  echo ""
  echo "7. Accent Color Variant:"
  echo "   [1] Nordic Frost Cyan (#88C0D0 - Crisp arctic cyan) [Default]"
  echo "   [2] Glacier Ice Blue (#81A1C1 - Cool glacial blue)"
  echo "   [3] Nordic Aurora Teal (#8FBCBB - Serene arctic sea green)"
  echo "   [4] Deep Arctic Blue (#5E81AC - Subdued Nordic navy blue)"
  echo "   [5] Electric Neon Cyan (#00D2FF - High-luminance cyber ice)"
  echo "   [6] Nordic Amber Blaze (#D08770 - Warm Scandinavian sunset)"
  printf "   Select [1-6, default=1]: "
  read -r choice || choice=""
  case "${choice}" in
    2) ACCENT="glacier" ;;
    3) ACCENT="aurora" ;;
    4) ACCENT="arctic" ;;
    5) ACCENT="cyber" ;;
    6) ACCENT="blaze" ;;
    *) ACCENT="frost" ;;
  esac

  # 8. Companion Icon & Cursor Suite
  echo ""
  echo "8. Install Companion Icon & Cursor Suite (${ICONS_NAME} & ${CURSORS_NAME})?"
  echo "   [1] Yes (Install and activate into ~/.icons) [Default]"
  echo "   [2] No"
  printf "   Select [1-2, default=1]: "
  read -r choice || choice=""
  case "${choice}" in
    2) WANT_ICONS=0 ;;
    *) WANT_ICONS=1 ;;
  esac

  # 9. GTK4 / Libadwaita Override
  echo ""
  echo "9. Apply GTK4 / Libadwaita Theme Override (~/.config/gtk-4.0)?"
  echo "   [1] Yes (Themed style for Settings, Nautilus, Console) [Default]"
  echo "   [2] No"
  printf "   Select [1-2, default=1]: "
  read -r choice || choice=""
  case "${choice}" in
    2) WANT_GTK4_OVERRIDE=0 ;;
    *) WANT_GTK4_OVERRIDE=1 ;;
  esac

  # 10. 4K Wallpaper
  echo ""
  echo "10. 4K Procedural Nordic Wallpaper:"
  echo "   [1] Fjord Canopy (Atmospheric mountain/glacier canopy) [Default]"
  echo "   [2] Radiant Aurora (Vibrant northern lights over snowy pine ridge)"
  echo "   [3] Glacial Flow (Minimal fluid glacier contours in Nordic cyan)"
  echo "   [4] Topographic Frost (Isoline elevations with glowing veins)"
  echo "   [5] All 4 Wallpapers (Copy to ~/Pictures/wallpapers-mt-nordic-blue)"
  echo "   [6] None (Keep current wallpaper)"
  printf "   Select [1-6, default=1]: "
  read -r choice || choice=""
  case "${choice}" in
    2) WANT_WALLPAPER=1; WALLPAPER_CHOICE="2" ;;
    3) WANT_WALLPAPER=1; WALLPAPER_CHOICE="3" ;;
    4) WANT_WALLPAPER=1; WALLPAPER_CHOICE="4" ;;
    5) WANT_WALLPAPER=1; WALLPAPER_CHOICE="all" ;;
    6|none) WANT_WALLPAPER=0; WALLPAPER_CHOICE="none" ;;
    *) WANT_WALLPAPER=1; WALLPAPER_CHOICE="1" ;;
  esac

  echo ""
  echo "Configuration summary:"
  echo "  - Top Bar Style:     ${PANEL_STYLE}"
  echo "  - Corner Curvature:  ${CORNERS}"
  echo "  - Window Controls:   ${CONTROLS}"
  echo "  - Theme Density:     ${THEME_SIZE}"
  echo "  - Surface Blur:      $([ "${WANT_BLUR}" -eq 1 ] && echo "Frosted Glass" || echo "Solid Opaque")"
  echo "  - Base Palette:      ${BASE_PALETTE}"
  echo "  - Accent Flavor:     ${ACCENT}"
  echo "  - Icons & Cursors:   $([ "${WANT_ICONS}" -eq 1 ] && echo "Install to ~/.icons" || echo "Skip")"
  echo "  - GTK4 / Libadwaita: $([ "${WANT_GTK4_OVERRIDE}" -eq 1 ] && echo "Linked" || echo "Skip")"
  echo "  - 4K Wallpaper:      ${WALLPAPER_CHOICE}"
  echo ""
fi

# ---------- legacy tweaks mapping (backwards compatibility) ----------
if [ -n "${TWEAKS_ARG}" ]; then
  echo "${TWEAKS_ARG}" | grep -q "macos" && CONTROLS="macos"
  echo "${TWEAKS_ARG}" | grep -q "compact" && THEME_SIZE="compact"
  echo "${TWEAKS_ARG}" | grep -q "sharp" && CORNERS="sharp"
  if echo "${TWEAKS_ARG}" | grep -q "float"; then
    PANEL_STYLE="pill"
  elif echo "${TWEAKS_ARG}" | grep -q "round"; then
    PANEL_STYLE="round-island"
  elif echo "${TWEAKS_ARG}" | grep -q "flat"; then
    PANEL_STYLE="flat"
  fi
  echo "${TWEAKS_ARG}" | grep -q "noblur" && WANT_BLUR=0
fi

# ---------- distro + package-manager detection ----------
. /etc/os-release 2>/dev/null || ID=unknown
case "${ID:-unknown}" in
  ubuntu|debian)
    DEP_INSTALL="sudo apt-get install -y gnome-shell python3 python3-gi sassc python3-numpy python3-pil gnome-shell-extension-user-theme" ;;
  fedora)
    DEP_INSTALL="sudo dnf install -y gnome-shell python3 python3-gobject sassc python3-numpy python3-pillow gnome-shell-extension-user-theme" ;;
  arch|cachyos)
    DEP_INSTALL="sudo pacman -S --needed gnome-shell python python-gobject sassc python-numpy python-pillow gnome-shell-extension-user-theme" ;;
  opensuse*)
    DEP_INSTALL="sudo zypper install gnome-shell python3 python3-gobject sassc python3-numpy python3-Pillow gnome-shell-extension-user-theme" ;;
  *)
    DEP_INSTALL="(unknown distro '${ID:-?}' — install: gnome-shell, python3 + gobject-introspection, sassc, numpy, Pillow, user-theme extension)" ;;
esac

# ---------- helpers ----------
have() { command -v "$1" >/dev/null 2>&1; }
py_has() { python3 -c "import $1" >/dev/null 2>&1; }
miss() { MISSING="${MISSING:-}${MISSING:+; }$1"; }

# ---------- shell version detection & build check ----------
have gnome-shell || { echo "gnome-shell not found on PATH" >&2; exit 1; }
SHELL_VERSION="$(gnome-shell --version)"
SHELL_MAJOR="$(echo "${SHELL_VERSION}" | sed -E 's/[^0-9]*([0-9]+).*/\1/')"

if [ "${SHELL_MAJOR}" -lt 50 ]; then
  echo "GNOME Shell ${SHELL_MAJOR} is unsupported; ${DISPLAY_NAME} targets GNOME Shell 50.x and 51.x." >&2
  exit 1
fi

[ -f "${REPO_ROOT}/src/shell/colormap-${SHELL_MAJOR}.json" ] || {
  echo "missing src/shell/colormap-${SHELL_MAJOR}.json — Shell ${SHELL_MAJOR} not yet mapped." >&2
  exit 1
}

echo "detected: ${ID:-unknown} · GNOME Shell ${SHELL_MAJOR}"

# Determine which build artifacts are missing
NEED_SHELL_BUILD=0
NEED_GTK_BUILD=0
NEED_WALLPAPER_GEN=0
NEED_ICONS_GEN=0

[ -f "${REPO_ROOT}/build/theme/gnome-shell-${SHELL_MAJOR}/gnome-shell.css" ] || NEED_SHELL_BUILD=1
[ -f "${REPO_ROOT}/build/theme/gtk-3.0/gtk.css" ] || NEED_GTK_BUILD=1
[ -f "${REPO_ROOT}/wallpaper/dist/mt-nordic-blue-3840x2160.png" ] || NEED_WALLPAPER_GEN=1
[ -d "${REPO_ROOT}/src/icons/${ICONS_NAME}" ] || NEED_ICONS_GEN=1

MISSING=""

# ---------- dependency checks ----------
have python3 || miss "python3"
if [ "${NEED_SHELL_BUILD}" -eq 1 ] || [ "${NEED_GTK_BUILD}" -eq 1 ]; then
  py_has gi || miss "python3 gobject-introspection (gi)"
fi
if [ "${NEED_GTK_BUILD}" -eq 1 ]; then
  have sassc || miss "sassc"
fi
if [ "${NEED_WALLPAPER_GEN}" -ne 0 ]; then
  py_has numpy || miss "python3-numpy"
  py_has PIL || miss "python3-pillow"
fi

if [ -n "${MISSING}" ]; then
  echo "missing requirements: ${MISSING}"
  echo "install them for this distro with:"
  echo "  ${DEP_INSTALL}"
  if [ "${INSTALL_DEPS}" -eq 1 ]; then
    echo "running (sudo used only here, for system packages):"
    sh -c "${DEP_INSTALL}"
  else
    echo "re-run with --install-deps to install them automatically, then retry."
    exit 1
  fi
fi

# ---------- builds (only missing outputs) ----------
[ "${NEED_SHELL_BUILD}" -eq 0 ] || python3 "${REPO_ROOT}/tools/shell/build.py" --major "${SHELL_MAJOR}"
[ "${NEED_GTK_BUILD}" -eq 0 ] || python3 "${REPO_ROOT}/tools/gtk/build.py" >/dev/null
if [ "${NEED_WALLPAPER_GEN}" -ne 0 ]; then
  python3 "${REPO_ROOT}/tools/wallpaper/generate.py" >/dev/null
  python3 "${REPO_ROOT}/tools/wallpaper/process_light.py" >/dev/null
fi
if [ "${NEED_ICONS_GEN}" -eq 1 ]; then
  python3 "${REPO_ROOT}/tools/icons/generate_icons.py" >/dev/null
  python3 "${REPO_ROOT}/tools/icons/generate_cursors.py" >/dev/null
fi

# ---------- install into ~/.themes (policy: user themes dir only) ----------
OLD_DIR="${HOME}/.local/share/themes/${THEME_NAME}"
if [ -d "${OLD_DIR}" ]; then
  PARK="${REPO_ROOT}/deleted_files_folders"
  mkdir -p "${PARK}"
  mv "${OLD_DIR}" "${PARK}/${THEME_NAME}-local-share"
  echo "moved previous install from ${OLD_DIR} to ${PARK}/${THEME_NAME}-local-share"
fi

mkdir -p "${THEME_DIR}/gtk-4.0"
mkdir -p "${THEME_DIR}/wallpapers"
mkdir -p "${THEME_DIR}/extras"
cp "${REPO_ROOT}/src/index.theme" "${THEME_DIR}/index.theme"
rm -rf "${THEME_DIR}/gnome-shell"
cp -r "${REPO_ROOT}/build/theme/gnome-shell-${SHELL_MAJOR}" "${THEME_DIR}/gnome-shell"
cp -r "${REPO_ROOT}/build/theme/gtk-3.0" "${THEME_DIR}/"
if [ -f "${REPO_ROOT}/src/gtk-4.0/overrides-light.css" ]; then
  cp "${REPO_ROOT}/src/gtk-4.0/overrides-light.css" "${THEME_DIR}/gtk-4.0/gtk.css"
else
  cp "${REPO_ROOT}/src/gtk-4.0/overrides.css" "${THEME_DIR}/gtk-4.0/gtk.css"
fi
cp "${REPO_ROOT}/src/gtk-4.0/overrides.css" "${THEME_DIR}/gtk-4.0/gtk-dark.css"

if [ -f "${REPO_ROOT}/src/gtk-2.0/gtkrc" ]; then
  mkdir -p "${THEME_DIR}/gtk-2.0"
  cp "${REPO_ROOT}/src/gtk-2.0/gtkrc" "${THEME_DIR}/gtk-2.0/gtkrc"
fi

# Copy wallpapers, instantiate dynamic XMLs, and register with GNOME Settings
if [ -d "${REPO_ROOT}/wallpaper/dist" ]; then
  cp -r "${REPO_ROOT}/wallpaper/dist/"* "${THEME_DIR}/wallpapers/" 2>/dev/null || true
  if [ -f "${THEME_DIR}/wallpapers/mt-nordic-blue-timed.xml.in" ]; then
    sed "s|@WALLPAPER_DIR@|${THEME_DIR}/wallpapers|g" "${THEME_DIR}/wallpapers/mt-nordic-blue-timed.xml.in" > "${THEME_DIR}/wallpapers/mt-nordic-blue-timed.xml"
  fi
  if [ -f "${THEME_DIR}/wallpapers/gnome-background-properties.xml.in" ]; then
    sed "s|@WALLPAPER_DIR@|${THEME_DIR}/wallpapers|g" "${THEME_DIR}/wallpapers/gnome-background-properties.xml.in" > "${THEME_DIR}/wallpapers/gnome-background-properties.xml"
  fi
  mkdir -p "${HOME}/.local/share/gnome-background-properties"
  cp "${THEME_DIR}/wallpapers/gnome-background-properties.xml" "${HOME}/.local/share/gnome-background-properties/mt-nordic-blue.xml" 2>/dev/null || true
fi
if [ -d "${REPO_ROOT}/extras" ]; then
  cp -r "${REPO_ROOT}/extras/"* "${THEME_DIR}/extras/" 2>/dev/null || true
fi

# ---------- apply base polish layer ----------
cat "${REPO_ROOT}/src/tweaks/shell/polish.css" >> "${THEME_DIR}/gnome-shell/gnome-shell.css"
if [ -f "${REPO_ROOT}/src/tweaks/gtk/polish-light.css" ]; then
  cat "${REPO_ROOT}/src/tweaks/gtk/polish-light.css" >> "${THEME_DIR}/gtk-3.0/gtk.css"
  cat "${REPO_ROOT}/src/tweaks/gtk/polish-light.css" >> "${THEME_DIR}/gtk-4.0/gtk.css"
else
  cat "${REPO_ROOT}/src/tweaks/gtk/polish.css" >> "${THEME_DIR}/gtk-3.0/gtk.css"
  cat "${REPO_ROOT}/src/tweaks/gtk/polish.css" >> "${THEME_DIR}/gtk-4.0/gtk.css"
fi
cat "${REPO_ROOT}/src/tweaks/gtk/polish.css" >> "${THEME_DIR}/gtk-3.0/gtk-dark.css"
cat "${REPO_ROOT}/src/tweaks/gtk/polish.css" >> "${THEME_DIR}/gtk-4.0/gtk-dark.css"

# ---------- apply base palette flavor (polar, classic, cyber, oled) ----------
case "${BASE_PALETTE}" in
  classic)
    [ -f "${REPO_ROOT}/src/tweaks/shell/base-classic.css" ] && cat "${REPO_ROOT}/src/tweaks/shell/base-classic.css" >> "${THEME_DIR}/gnome-shell/gnome-shell.css"
    if [ -f "${REPO_ROOT}/src/tweaks/gtk/base-classic.css" ]; then
      cat "${REPO_ROOT}/src/tweaks/gtk/base-classic.css" >> "${THEME_DIR}/gtk-3.0/gtk.css"
      cat "${REPO_ROOT}/src/tweaks/gtk/base-classic.css" >> "${THEME_DIR}/gtk-3.0/gtk-dark.css"
      cat "${REPO_ROOT}/src/tweaks/gtk/base-classic.css" >> "${THEME_DIR}/gtk-4.0/gtk.css"
      cat "${REPO_ROOT}/src/tweaks/gtk/base-classic.css" >> "${THEME_DIR}/gtk-4.0/gtk-dark.css"
    fi
    echo "  + base palette: Classic Nord Spec (#2E3440 slate)"
    ;;
  cyber)
    [ -f "${REPO_ROOT}/src/tweaks/shell/base-cyber.css" ] && cat "${REPO_ROOT}/src/tweaks/shell/base-cyber.css" >> "${THEME_DIR}/gnome-shell/gnome-shell.css"
    if [ -f "${REPO_ROOT}/src/tweaks/gtk/base-cyber.css" ]; then
      cat "${REPO_ROOT}/src/tweaks/gtk/base-cyber.css" >> "${THEME_DIR}/gtk-3.0/gtk.css"
      cat "${REPO_ROOT}/src/tweaks/gtk/base-cyber.css" >> "${THEME_DIR}/gtk-3.0/gtk-dark.css"
      cat "${REPO_ROOT}/src/tweaks/gtk/base-cyber.css" >> "${THEME_DIR}/gtk-4.0/gtk.css"
      cat "${REPO_ROOT}/src/tweaks/gtk/base-cyber.css" >> "${THEME_DIR}/gtk-4.0/gtk-dark.css"
    fi
    echo "  + base palette: Arctic Cyber Frost (#0A0E17 midnight navy)"
    ;;
  oled)
    [ -f "${REPO_ROOT}/src/tweaks/shell/black.css" ] && cat "${REPO_ROOT}/src/tweaks/shell/black.css" >> "${THEME_DIR}/gnome-shell/gnome-shell.css"
    if [ -f "${REPO_ROOT}/src/tweaks/gtk/black.css" ]; then
      cat "${REPO_ROOT}/src/tweaks/gtk/black.css" >> "${THEME_DIR}/gtk-3.0/gtk.css"
      cat "${REPO_ROOT}/src/tweaks/gtk/black.css" >> "${THEME_DIR}/gtk-3.0/gtk-dark.css"
      cat "${REPO_ROOT}/src/tweaks/gtk/black.css" >> "${THEME_DIR}/gtk-4.0/gtk.css"
      cat "${REPO_ROOT}/src/tweaks/gtk/black.css" >> "${THEME_DIR}/gtk-4.0/gtk-dark.css"
    fi
    echo "  + base palette: True pitch-black OLED"
    ;;
  *)
    echo "  + base palette: Deep Polar Night (#0E141D high-contrast)"
    ;;
esac

# ---------- apply top bar / system tray style ----------
case "${PANEL_STYLE}" in
  round-island)
    [ -f "${REPO_ROOT}/src/tweaks/shell/tray-round.css" ] && cat "${REPO_ROOT}/src/tweaks/shell/tray-round.css" >> "${THEME_DIR}/gnome-shell/gnome-shell.css"
    echo "  + top bar: rounded modern island (16px curved floating bar)"
    if have dconf && [ -d "${HOME}/.local/share/gnome-shell/extensions/blur-my-shell@aunetx" ]; then
      dconf write /org/gnome/shell/extensions/blur-my-shell/panel/blur true 2>/dev/null || true
      dconf write /org/gnome/shell/extensions/blur-my-shell/panel/corner-radius 16 2>/dev/null || true
      dconf write /org/gnome/shell/extensions/blur-my-shell/panel/override-background false 2>/dev/null || true
    fi
    ;;
  pill)
    [ -f "${REPO_ROOT}/src/tweaks/shell/tray-pill.css" ] && cat "${REPO_ROOT}/src/tweaks/shell/tray-pill.css" >> "${THEME_DIR}/gnome-shell/gnome-shell.css"
    echo "  + top bar: floating pill capsule (999px circular ends)"
    if have dconf && [ -d "${HOME}/.local/share/gnome-shell/extensions/blur-my-shell@aunetx" ]; then
      dconf write /org/gnome/shell/extensions/blur-my-shell/panel/blur true 2>/dev/null || true
      dconf write /org/gnome/shell/extensions/blur-my-shell/panel/corner-radius 30 2>/dev/null || true
      dconf write /org/gnome/shell/extensions/blur-my-shell/panel/override-background false 2>/dev/null || true
    fi
    ;;
  bottom-round)
    [ -f "${REPO_ROOT}/src/tweaks/shell/tray-bottom-round.css" ] && cat "${REPO_ROOT}/src/tweaks/shell/tray-bottom-round.css" >> "${THEME_DIR}/gnome-shell/gnome-shell.css"
    echo "  + top bar: bottom-rounded (connected to top edge)"
    if have dconf && [ -d "${HOME}/.local/share/gnome-shell/extensions/blur-my-shell@aunetx" ]; then
      dconf write /org/gnome/shell/extensions/blur-my-shell/panel/blur true 2>/dev/null || true
      dconf write /org/gnome/shell/extensions/blur-my-shell/panel/corner-radius 16 2>/dev/null || true
      dconf write /org/gnome/shell/extensions/blur-my-shell/panel/override-background false 2>/dev/null || true
    fi
    ;;
  flat)
    [ -f "${REPO_ROOT}/src/tweaks/shell/tray-flat.css" ] && cat "${REPO_ROOT}/src/tweaks/shell/tray-flat.css" >> "${THEME_DIR}/gnome-shell/gnome-shell.css"
    echo "  + top bar: classic edge-to-edge square bar"
    if have dconf && [ -d "${HOME}/.local/share/gnome-shell/extensions/blur-my-shell@aunetx" ]; then
      dconf write /org/gnome/shell/extensions/blur-my-shell/panel/blur true 2>/dev/null || true
      dconf write /org/gnome/shell/extensions/blur-my-shell/panel/corner-radius 0 2>/dev/null || true
    fi
    ;;
esac

# ---------- apply corner curvature (round vs sharp) ----------
if [ "${CORNERS}" = "sharp" ]; then
  [ -f "${REPO_ROOT}/src/tweaks/shell/sharp.css" ] && cat "${REPO_ROOT}/src/tweaks/shell/sharp.css" >> "${THEME_DIR}/gnome-shell/gnome-shell.css"
  if [ -f "${REPO_ROOT}/src/tweaks/gtk/sharp.css" ]; then
    cat "${REPO_ROOT}/src/tweaks/gtk/sharp.css" >> "${THEME_DIR}/gtk-3.0/gtk.css"
    cat "${REPO_ROOT}/src/tweaks/gtk/sharp.css" >> "${THEME_DIR}/gtk-3.0/gtk-dark.css"
    cat "${REPO_ROOT}/src/tweaks/gtk/sharp.css" >> "${THEME_DIR}/gtk-4.0/gtk.css"
    cat "${REPO_ROOT}/src/tweaks/gtk/sharp.css" >> "${THEME_DIR}/gtk-4.0/gtk-dark.css"
  fi
  echo "  + corner curvature: sharp 0px corners (non-rounded industrial aesthetic)"
else
  [ -f "${REPO_ROOT}/src/tweaks/shell/round.css" ] && cat "${REPO_ROOT}/src/tweaks/shell/round.css" >> "${THEME_DIR}/gnome-shell/gnome-shell.css"
  if [ -f "${REPO_ROOT}/src/tweaks/gtk/round.css" ]; then
    cat "${REPO_ROOT}/src/tweaks/gtk/round.css" >> "${THEME_DIR}/gtk-3.0/gtk.css"
    cat "${REPO_ROOT}/src/tweaks/gtk/round.css" >> "${THEME_DIR}/gtk-3.0/gtk-dark.css"
    cat "${REPO_ROOT}/src/tweaks/gtk/round.css" >> "${THEME_DIR}/gtk-4.0/gtk.css"
    cat "${REPO_ROOT}/src/tweaks/gtk/round.css" >> "${THEME_DIR}/gtk-4.0/gtk-dark.css"
  fi
  echo "  + corner curvature: modern 16px rounded curves"
fi

# ---------- apply surface blur & frosted glassmorphism ----------
if [ "${WANT_BLUR}" -eq 1 ]; then
  [ -f "${REPO_ROOT}/src/tweaks/shell/translucent.css" ] && cat "${REPO_ROOT}/src/tweaks/shell/translucent.css" >> "${THEME_DIR}/gnome-shell/gnome-shell.css"
  [ -f "${REPO_ROOT}/src/tweaks/shell/blur-my-shell.css" ] && cat "${REPO_ROOT}/src/tweaks/shell/blur-my-shell.css" >> "${THEME_DIR}/gnome-shell/gnome-shell.css"
  echo "  + surface: frosted glass translucency & blur enabled"
  if have dconf && [ -d "${HOME}/.local/share/gnome-shell/extensions/blur-my-shell@aunetx" ]; then
    dconf write /org/gnome/shell/extensions/blur-my-shell/dash-to-dock/blur true 2>/dev/null || true
    dconf write /org/gnome/shell/extensions/blur-my-shell/overview/blur true 2>/dev/null || true
    dconf write /org/gnome/shell/extensions/blur-my-shell/appfolder/blur true 2>/dev/null || true
  fi
  if have dconf && [ -d "${HOME}/.local/share/gnome-shell/extensions/dash-to-dock@micxgx.gmail.com" ]; then
    dconf write /org/gnome/shell/extensions/dash-to-dock/apply-custom-theme true 2>/dev/null || true
  fi
else
  [ -f "${REPO_ROOT}/src/tweaks/shell/noblur.css" ] && cat "${REPO_ROOT}/src/tweaks/shell/noblur.css" >> "${THEME_DIR}/gnome-shell/gnome-shell.css"
  if [ -f "${REPO_ROOT}/src/tweaks/gtk/noblur.css" ]; then
    cat "${REPO_ROOT}/src/tweaks/gtk/noblur.css" >> "${THEME_DIR}/gtk-3.0/gtk.css"
    cat "${REPO_ROOT}/src/tweaks/gtk/noblur.css" >> "${THEME_DIR}/gtk-3.0/gtk-dark.css"
    cat "${REPO_ROOT}/src/tweaks/gtk/noblur.css" >> "${THEME_DIR}/gtk-4.0/gtk.css"
    cat "${REPO_ROOT}/src/tweaks/gtk/noblur.css" >> "${THEME_DIR}/gtk-4.0/gtk-dark.css"
  fi
  echo "  + surface: solid opaque surfaces"
  if have dconf && [ -d "${HOME}/.local/share/gnome-shell/extensions/blur-my-shell@aunetx" ]; then
    dconf write /org/gnome/shell/extensions/blur-my-shell/panel/blur false 2>/dev/null || true
    dconf write /org/gnome/shell/extensions/blur-my-shell/dash-to-dock/blur false 2>/dev/null || true
  fi
fi

# ---------- apply window controls (buttons) ----------
if [ "${CONTROLS}" = "macos" ]; then
  if [ -f "${REPO_ROOT}/src/tweaks/gtk/macos.css" ]; then
    cat "${REPO_ROOT}/src/tweaks/gtk/macos.css" >> "${THEME_DIR}/gtk-3.0/gtk.css"
    cat "${REPO_ROOT}/src/tweaks/gtk/macos.css" >> "${THEME_DIR}/gtk-3.0/gtk-dark.css"
    cat "${REPO_ROOT}/src/tweaks/gtk/macos.css" >> "${THEME_DIR}/gtk-4.0/gtk.css"
    cat "${REPO_ROOT}/src/tweaks/gtk/macos.css" >> "${THEME_DIR}/gtk-4.0/gtk-dark.css"
  fi
  echo "  + window controls: macOS traffic dots (Aurora Red / Amber / Green)"
else
  echo "  + window controls: standard Adwaita clean buttons"
fi

# ---------- apply theme sizing / density ----------
if [ "${THEME_SIZE}" = "compact" ]; then
  [ -f "${REPO_ROOT}/src/tweaks/shell/compact.css" ] && cat "${REPO_ROOT}/src/tweaks/shell/compact.css" >> "${THEME_DIR}/gnome-shell/gnome-shell.css"
  if [ -f "${REPO_ROOT}/src/tweaks/gtk/compact.css" ]; then
    cat "${REPO_ROOT}/src/tweaks/gtk/compact.css" >> "${THEME_DIR}/gtk-3.0/gtk.css"
    cat "${REPO_ROOT}/src/tweaks/gtk/compact.css" >> "${THEME_DIR}/gtk-3.0/gtk-dark.css"
    cat "${REPO_ROOT}/src/tweaks/gtk/compact.css" >> "${THEME_DIR}/gtk-4.0/gtk.css"
    cat "${REPO_ROOT}/src/tweaks/gtk/compact.css" >> "${THEME_DIR}/gtk-4.0/gtk-dark.css"
  fi
  echo "  + theme density: compact (slim padding & headerbars)"
else
  echo "  + theme density: standard"
fi

# ---------- apply accent flavor ----------
if [ -f "${REPO_ROOT}/src/tweaks/gtk/accent-${ACCENT}.css" ]; then
  cat "${REPO_ROOT}/src/tweaks/gtk/accent-${ACCENT}.css" >> "${THEME_DIR}/gtk-3.0/gtk.css"
  cat "${REPO_ROOT}/src/tweaks/gtk/accent-${ACCENT}.css" >> "${THEME_DIR}/gtk-3.0/gtk-dark.css"
  cat "${REPO_ROOT}/src/tweaks/gtk/accent-${ACCENT}.css" >> "${THEME_DIR}/gtk-4.0/gtk.css"
  cat "${REPO_ROOT}/src/tweaks/gtk/accent-${ACCENT}.css" >> "${THEME_DIR}/gtk-4.0/gtk-dark.css"
  echo "  + accent color: ${ACCENT}"
else
  echo "  + accent color: frost (#88C0D0)"
fi

echo "installed theme files to ${THEME_DIR}"

# ---------- optional: icons & cursors (user ~/.icons only) ----------
if [ "${WANT_ICONS}" -eq 1 ]; then
  mkdir -p "${ICONS_DIR}"
  if [ -d "${REPO_ROOT}/src/icons/${ICONS_NAME}" ]; then
    rm -rf "${ICONS_DIR}/${ICONS_NAME}"
    cp -r "${REPO_ROOT}/src/icons/${ICONS_NAME}" "${ICONS_DIR}/"
    if command -v gtk-update-icon-cache >/dev/null 2>&1; then
      gtk-update-icon-cache -f -t "${ICONS_DIR}/${ICONS_NAME}" >/dev/null 2>&1 || true
    fi
    gsettings set org.gnome.desktop.interface icon-theme "${ICONS_NAME}" || true
    echo "installed and activated icon pack in ${ICONS_DIR}/${ICONS_NAME}"
  fi
  if [ -d "${REPO_ROOT}/src/cursors/${CURSORS_NAME}" ]; then
    rm -rf "${ICONS_DIR}/${CURSORS_NAME}"
    cp -r "${REPO_ROOT}/src/cursors/${CURSORS_NAME}" "${ICONS_DIR}/"
    gsettings set org.gnome.desktop.interface cursor-theme "${CURSORS_NAME}" || true
    echo "installed and activated cursor pack in ${ICONS_DIR}/${CURSORS_NAME}"
  fi
fi

# ---------- optional: wallpaper (explicit opt-in) ----------
if [ "${WANT_WALLPAPER}" -eq 1 ] && [ "${WALLPAPER_CHOICE}" != "none" ]; then
  WP_SRC=""
  case "${WALLPAPER_CHOICE}" in
    1|fjord|canopy)
      WP_SRC="${REPO_ROOT}/wallpaper/dist/mt-nordic-blue-art-1-3840x2160.png"
      WP_NAME="mt-nordic-blue-art-1.png"
      ;;
    2|aurora)
      WP_SRC="${REPO_ROOT}/wallpaper/dist/mt-nordic-blue-art-2-3840x2160.png"
      WP_NAME="mt-nordic-blue-art-2.png"
      ;;
    3|flow)
      WP_SRC="${REPO_ROOT}/wallpaper/dist/mt-nordic-blue-art-3-3840x2160.png"
      WP_NAME="mt-nordic-blue-art-3.png"
      ;;
    4|frost|topographic)
      WP_SRC="${REPO_ROOT}/wallpaper/dist/mt-nordic-blue-art-4-3840x2160.png"
      WP_NAME="mt-nordic-blue-art-4.png"
      ;;
    all)
      WP_SRC="${REPO_ROOT}/wallpaper/dist/mt-nordic-blue-art-1-3840x2160.png"
      WP_NAME="mt-nordic-blue-art-1.png"
      mkdir -p "${HOME}/Pictures/wallpapers-mt-nordic-blue"
      cp "${REPO_ROOT}/wallpaper/dist/"*.png "${HOME}/Pictures/wallpapers-mt-nordic-blue/" 2>/dev/null || true
      echo "all 4 wallpapers copied to ~/Pictures/wallpapers-mt-nordic-blue/"
      ;;
    *)
      WP_SRC="${REPO_ROOT}/wallpaper/dist/mt-nordic-blue-3840x2160.png"
      WP_NAME="mt-nordic-blue.png"
      ;;
  esac

  if [ -n "${WP_SRC}" ] && [ -f "${WP_SRC}" ]; then
    DEST="${HOME}/Pictures/${WP_NAME}"
    mkdir -p "${HOME}/Pictures"
    cp "${WP_SRC}" "${DEST}"
    cp "${WP_SRC}" "${HOME}/.config/background" 2>/dev/null || true
    gsettings set org.gnome.desktop.background picture-uri "file://${DEST}" 2>/dev/null || true
    gsettings set org.gnome.desktop.background picture-uri-dark "file://${DEST}" 2>/dev/null || true
    echo "wallpaper applied: ${DEST}"
  fi
fi

# ---------- optional: libadwaita best-effort override ----------
if [ "${WANT_GTK4_OVERRIDE}" -eq 1 ]; then
  CONF_DIR="${HOME}/.config/gtk-4.0"
  mkdir -p "${CONF_DIR}"
  [ -f "${CONF_DIR}/gtk.css" ] && [ ! -L "${CONF_DIR}/gtk.css" ] && cp "${CONF_DIR}/gtk.css" "${CONF_DIR}/gtk.css.pre-nordic"
  [ -f "${CONF_DIR}/gtk-dark.css" ] && [ ! -L "${CONF_DIR}/gtk-dark.css" ] && cp "${CONF_DIR}/gtk-dark.css" "${CONF_DIR}/gtk-dark.css.pre-nordic"
  ln -sf "${THEME_DIR}/gtk-4.0/gtk.css" "${CONF_DIR}/gtk.css"
  ln -sf "${THEME_DIR}/gtk-4.0/gtk-dark.css" "${CONF_DIR}/gtk-dark.css"
  cat <<'EOF_GTK4_INI' > "${CONF_DIR}/settings.ini"
[Settings]
gtk-application-prefer-dark-theme=1
EOF_GTK4_INI
  echo "libadwaita best-effort override linked at ${CONF_DIR}/gtk.css and gtk-dark.css"
fi

# ---------- GTK3 config sync & cleanup ----------
CONF3_DIR="${HOME}/.config/gtk-3.0"
mkdir -p "${CONF3_DIR}"
if [ -f "${CONF3_DIR}/gtk.css" ] && grep -q "colors.css" "${CONF3_DIR}/gtk.css" 2>/dev/null; then
  mv "${CONF3_DIR}/gtk.css" "${CONF3_DIR}/gtk.css.pre-nordic" 2>/dev/null || true
fi
cat <<EOF_GTK3_INI > "${CONF3_DIR}/settings.ini"
[Settings]
gtk-theme-name=${THEME_NAME}
gtk-icon-theme-name=${ICONS_NAME}
gtk-cursor-theme-name=${CURSORS_NAME}
gtk-cursor-theme-size=24
gtk-application-prefer-dark-theme=1
EOF_GTK3_INI

# ---------- default cursor fallback for all toolkits ----------
mkdir -p "${HOME}/.icons/default"
cat <<EOF_CUR_INI > "${HOME}/.icons/default/index.theme"
[Icon Theme]
Name=Default
Comment=Default Cursor Theme
Inherits=${CURSORS_NAME}
EOF_CUR_INI

# ---------- GNOME settings activation ----------
if have dconf; then
  # Toggle to blank then theme name to trigger immediate live reload in GNOME Shell
  dconf write /org/gnome/shell/extensions/user-theme/name "''" 2>/dev/null || true
  sleep 0.2
  dconf write /org/gnome/shell/extensions/user-theme/name "'${THEME_NAME}'" 2>/dev/null || true
fi
if have gsettings; then
  gsettings set org.gnome.desktop.interface gtk-theme "${THEME_NAME}" 2>/dev/null || true
  if [ "${WANT_ICONS}" -eq 1 ]; then
    gsettings set org.gnome.desktop.interface icon-theme "${ICONS_NAME}" 2>/dev/null || true
    gsettings set org.gnome.desktop.interface cursor-theme "${CURSORS_NAME}" 2>/dev/null || true
  fi
fi

# ---------- activation hint ----------
if have gnome-extensions && ! gnome-extensions list 2>/dev/null | grep -q '^user-theme@'; then
  echo "NOTE: User Themes extension not found/enabled — Shell styling needs it:"
  echo "  ${DEP_INSTALL%%gnome-shell-extension-user-theme*}gnome-shell-extension-user-theme"
  echo "  then: gnome-extensions enable user-theme@gnome-shell-extensions.gcampax.github.com (re-login if new)"
fi

cat <<EOF

========================================================================
  ✨ Theme Installation Complete!
========================================================================
Theme Name:       ${THEME_NAME}
Installed To:     ${THEME_DIR}
Top Bar Style:    ${PANEL_STYLE}
Corner Style:     ${CORNERS}
Window Controls:  ${CONTROLS}
Density:          ${THEME_SIZE}
Base Palette:     ${BASE_PALETTE}
Accent Color:     ${ACCENT}
Frosted Blur:     $([ "${WANT_BLUR}" -eq 1 ] && echo "Enabled" || echo "Disabled")

Settings Applied:
  Shell Theme:    ${THEME_NAME}
  GTK Theme:      ${THEME_NAME}
  Icon Theme:     ${ICONS_NAME}
  Cursor Theme:   ${CURSORS_NAME}

Restore Defaults (Adwaita):
  dconf write /org/gnome/shell/extensions/user-theme/name "''"
  gsettings set org.gnome.desktop.interface gtk-theme 'Adwaita'
  gsettings set org.gnome.desktop.interface icon-theme 'Adwaita'
  gsettings set org.gnome.desktop.interface cursor-theme 'Adwaita'
  rm -f ~/.config/gtk-4.0/gtk.css
EOF

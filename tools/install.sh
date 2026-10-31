#!/bin/sh
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Install MT Nordic Blue GNOME Suite at user level into ~/.themes ONLY (project policy),
# and companion icon/cursor packs into ~/.icons ONLY.
# Supports interactive CLI wizard, human-friendly settings, modular tweaks, and 4K wallpapers.

set -eu

if [ -f "$(dirname "$0")/index.theme" ]; then
  REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
elif [ -f "$(dirname "$0")/../tools/install.sh" ]; then
  REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
elif [ -f "$(dirname "$0")/tools/install.sh" ]; then
  REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
else
  REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
fi
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

# Source layout: repository checkout (builds on demand) or release bundle (prebuilt artifacts).
if [ -d "${REPO_ROOT}/build/theme" ]; then
  LAYOUT="repo"
  SRC_TWEAKS="${REPO_ROOT}/src/tweaks"
  SRC_GTK4="${REPO_ROOT}/src/gtk-4.0"
  SRC_GTK2="${REPO_ROOT}/src/gtk-2.0"
  SRC_ICONS="${REPO_ROOT}/src/icons"
  SRC_CURSORS="${REPO_ROOT}/src/cursors"
  SRC_INDEX="${REPO_ROOT}/src/index.theme"
  SRC_INDEX_LIGHT="${REPO_ROOT}/src/index-light.theme"
  BUILD_THEME="${REPO_ROOT}/build/theme"
  SRC_WALLPAPERS="${REPO_ROOT}/wallpaper/dist"
  SRC_EXTRAS="${REPO_ROOT}/extras"
  SRC_PALETTE="${REPO_ROOT}/palette"
  SRC_TOOLS="${REPO_ROOT}/tools"
else
  LAYOUT="bundle"
  SRC_TWEAKS="${REPO_ROOT}/tweaks"
  SRC_GTK4="${REPO_ROOT}/gtk-4.0-src"
  SRC_GTK2="${REPO_ROOT}/gtk-2.0"
  SRC_ICONS="${REPO_ROOT}/icons"
  SRC_CURSORS="${REPO_ROOT}/cursors"
  SRC_INDEX="${REPO_ROOT}/index.theme"
  SRC_INDEX_LIGHT="${REPO_ROOT}/index-light.theme"
  BUILD_THEME="${REPO_ROOT}"
  SRC_WALLPAPERS="${REPO_ROOT}/wallpapers"
  SRC_EXTRAS="${REPO_ROOT}/extras"
  SRC_PALETTE="${REPO_ROOT}"
  SRC_TOOLS="${REPO_ROOT}/tools"
fi

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

# Append a Shell tweak to the dark theme, and to the light theme when it is present.
append_shell_tweak() {
  [ -f "$1" ] || return 0
  cat "$1" >> "${THEME_DIR}/gnome-shell/gnome-shell.css"
  if [ -f "${LIGHT_THEME_DIR}/gnome-shell/gnome-shell.css" ]; then
    cat "$1" >> "${LIGHT_THEME_DIR}/gnome-shell/gnome-shell.css"
  fi
  return 0
}
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

SHELL_SRC="${BUILD_THEME}/gnome-shell-${SHELL_MAJOR}"
SHELL_LIGHT_SRC="${BUILD_THEME}/gnome-shell-${SHELL_MAJOR}-light"
if [ "${LAYOUT}" = "bundle" ]; then
  SHELL_LIGHT_SRC="${REPO_ROOT}/gnome-shell-light/gnome-shell-${SHELL_MAJOR}-light"
fi

if [ "${LAYOUT}" = "repo" ] && [ ! -f "${REPO_ROOT}/src/shell/colormap-${SHELL_MAJOR}.json" ]; then
  echo "missing src/shell/colormap-${SHELL_MAJOR}.json — Shell ${SHELL_MAJOR} not yet mapped." >&2
  exit 1
fi
if [ "${LAYOUT}" = "bundle" ] && [ ! -f "${SHELL_SRC}/gnome-shell.css" ]; then
  echo "bundle has no gnome-shell.css for Shell ${SHELL_MAJOR}." >&2
  exit 1
fi

echo "detected: ${ID:-unknown} · GNOME Shell ${SHELL_MAJOR}"

# Determine which build artifacts are missing
NEED_SHELL_BUILD=0
NEED_GTK_BUILD=0
NEED_WALLPAPER_GEN=0
NEED_ICONS_GEN=0

[ -f "${SHELL_SRC}/gnome-shell.css" ] || NEED_SHELL_BUILD=1
# Shell CSS is accent-dependent: rebuild when the recorded accent differs from the requested one.
SHELL_ACCENT_MARKER="${SHELL_SRC}/.accent"
[ "$(cat "${SHELL_ACCENT_MARKER}" 2>/dev/null)" = "${ACCENT}" ] || NEED_SHELL_BUILD=1
[ -f "${BUILD_THEME}/gtk-3.0/gtk.css" ] || NEED_GTK_BUILD=1
[ -f "${SRC_WALLPAPERS}/mt-nordic-blue-3840x2160.png" ] || NEED_WALLPAPER_GEN=1
[ -d "${SRC_ICONS}/${ICONS_NAME}" ] || NEED_ICONS_GEN=1

# Bundles ship prebuilt artifacts and no build tools: never attempt a rebuild.
if [ "${LAYOUT}" = "bundle" ]; then
  NEED_SHELL_BUILD=0
  NEED_GTK_BUILD=0
  NEED_WALLPAPER_GEN=0
  NEED_ICONS_GEN=0
  BUNDLED_ACCENT="$(cat "${SHELL_SRC}/.accent" 2>/dev/null || echo unknown)"
  if [ "${BUNDLED_ACCENT}" != "${ACCENT}" ] && [ ! -f "${SRC_TOOLS}/dev/recolor_accent.py" ]; then
    echo "notice: this bundle ships '${BUNDLED_ACCENT}' CSS without the recolor tool; rebuild from source for --accent ${ACCENT}." >&2
  fi
fi

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

# ---------- builds (only missing or stale outputs) ----------
[ "${NEED_SHELL_BUILD}" -eq 0 ] || python3 "${SRC_TOOLS}/shell/build.py" --major "${SHELL_MAJOR}" --accent "${ACCENT}"
[ "${NEED_GTK_BUILD}" -eq 0 ] || python3 "${SRC_TOOLS}/gtk/build.py" >/dev/null
if [ "${NEED_WALLPAPER_GEN}" -ne 0 ]; then
  python3 "${SRC_TOOLS}/wallpaper/generate.py" >/dev/null
  python3 "${SRC_TOOLS}/wallpaper/process_light.py" >/dev/null
fi
if [ "${NEED_ICONS_GEN}" -eq 1 ]; then
  python3 "${SRC_TOOLS}/icons/generate_icons.py" >/dev/null
  python3 "${SRC_TOOLS}/icons/generate_cursors.py" >/dev/null
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
cp "${SRC_INDEX}" "${THEME_DIR}/index.theme"
rm -rf "${THEME_DIR}/gnome-shell"
cp -r "${SHELL_SRC}" "${THEME_DIR}/gnome-shell"
cp -r "${BUILD_THEME}/gtk-3.0" "${THEME_DIR}/"
cp "${SRC_GTK4}/overrides.css" "${THEME_DIR}/gtk-4.0/gtk.css"
cp "${SRC_GTK4}/overrides.css" "${THEME_DIR}/gtk-4.0/gtk-dark.css"

if [ -f "${SRC_GTK2}/gtkrc" ]; then
  mkdir -p "${THEME_DIR}/gtk-2.0"
  cp "${SRC_GTK2}/gtkrc" "${THEME_DIR}/gtk-2.0/gtkrc"
fi

# Copy wallpapers, instantiate dynamic XMLs, and register with GNOME Settings
if [ -d "${SRC_WALLPAPERS}" ]; then
  cp -r "${SRC_WALLPAPERS}/"* "${THEME_DIR}/wallpapers/" 2>/dev/null || true
  if [ -f "${THEME_DIR}/wallpapers/mt-nordic-blue-timed.xml.in" ]; then
    sed "s|@WALLPAPER_DIR@|${THEME_DIR}/wallpapers|g" "${THEME_DIR}/wallpapers/mt-nordic-blue-timed.xml.in" > "${THEME_DIR}/wallpapers/mt-nordic-blue-timed.xml"
  fi
  if [ -f "${THEME_DIR}/wallpapers/gnome-background-properties.xml.in" ]; then
    sed "s|@WALLPAPER_DIR@|${THEME_DIR}/wallpapers|g" "${THEME_DIR}/wallpapers/gnome-background-properties.xml.in" > "${THEME_DIR}/wallpapers/gnome-background-properties.xml"
  fi
  mkdir -p "${HOME}/.local/share/gnome-background-properties"
  cp "${THEME_DIR}/wallpapers/gnome-background-properties.xml" "${HOME}/.local/share/gnome-background-properties/mt-nordic-blue.xml" 2>/dev/null || true
fi
if [ -d "${SRC_EXTRAS}" ]; then
  cp -r "${SRC_EXTRAS}/"* "${THEME_DIR}/extras/" 2>/dev/null || true
fi

# ---------- install dedicated MT-Nordic-Light into ~/.themes/MT-Nordic-Light ----------
LIGHT_THEME_DIR="${HOME}/.themes/MT-Nordic-Light"
mkdir -p "${LIGHT_THEME_DIR}/gnome-shell"
mkdir -p "${LIGHT_THEME_DIR}/gtk-4.0"
cp "${SRC_INDEX_LIGHT}" "${LIGHT_THEME_DIR}/index.theme"
if [ -d "${SHELL_LIGHT_SRC}" ]; then
  cp -r "${SHELL_LIGHT_SRC}/"* "${LIGHT_THEME_DIR}/gnome-shell/"
  if [ -f "${SRC_TWEAKS}/shell/polish-light.css" ]; then
    cat "${SRC_TWEAKS}/shell/polish-light.css" >> "${LIGHT_THEME_DIR}/gnome-shell/gnome-shell.css"
  fi
fi
cp -r "${BUILD_THEME}/gtk-3.0" "${LIGHT_THEME_DIR}/"
if [ -f "${SRC_GTK4}/overrides-light.css" ]; then
  cp "${SRC_GTK4}/overrides-light.css" "${LIGHT_THEME_DIR}/gtk-4.0/gtk.css"
  cp "${SRC_GTK4}/overrides-light.css" "${LIGHT_THEME_DIR}/gtk-4.0/gtk-dark.css"
else
  cp "${THEME_DIR}/gtk-4.0/gtk.css" "${LIGHT_THEME_DIR}/gtk-4.0/gtk.css"
  cp "${THEME_DIR}/gtk-4.0/gtk-dark.css" "${LIGHT_THEME_DIR}/gtk-4.0/gtk-dark.css"
fi
if [ -f "${SRC_TWEAKS}/gtk/polish-light.css" ]; then
  cat "${SRC_TWEAKS}/gtk/polish-light.css" >> "${LIGHT_THEME_DIR}/gtk-3.0/gtk.css"
  cat "${SRC_TWEAKS}/gtk/polish-light.css" >> "${LIGHT_THEME_DIR}/gtk-4.0/gtk.css"
fi

# ---------- apply base polish layer ----------
cat "${SRC_TWEAKS}/shell/polish.css" >> "${THEME_DIR}/gnome-shell/gnome-shell.css"
cat "${SRC_TWEAKS}/gtk/polish.css" >> "${THEME_DIR}/gtk-3.0/gtk.css"
cat "${SRC_TWEAKS}/gtk/polish.css" >> "${THEME_DIR}/gtk-4.0/gtk.css"
cat "${SRC_TWEAKS}/gtk/polish.css" >> "${THEME_DIR}/gtk-3.0/gtk-dark.css"
cat "${SRC_TWEAKS}/gtk/polish.css" >> "${THEME_DIR}/gtk-4.0/gtk-dark.css"

# ---------- apply base palette flavor (polar, classic, cyber, oled) ----------
case "${BASE_PALETTE}" in
  classic)
    [ -f "${SRC_TWEAKS}/shell/base-classic.css" ] && cat "${SRC_TWEAKS}/shell/base-classic.css" >> "${THEME_DIR}/gnome-shell/gnome-shell.css"
    if [ -f "${SRC_TWEAKS}/gtk/base-classic.css" ]; then
      cat "${SRC_TWEAKS}/gtk/base-classic.css" >> "${THEME_DIR}/gtk-3.0/gtk.css"
      cat "${SRC_TWEAKS}/gtk/base-classic.css" >> "${THEME_DIR}/gtk-3.0/gtk-dark.css"
      cat "${SRC_TWEAKS}/gtk/base-classic.css" >> "${THEME_DIR}/gtk-4.0/gtk.css"
      cat "${SRC_TWEAKS}/gtk/base-classic.css" >> "${THEME_DIR}/gtk-4.0/gtk-dark.css"
    fi
    echo "  + base palette: Classic Nord Spec (#2E3440 slate)"
    ;;
  cyber)
    [ -f "${SRC_TWEAKS}/shell/base-cyber.css" ] && cat "${SRC_TWEAKS}/shell/base-cyber.css" >> "${THEME_DIR}/gnome-shell/gnome-shell.css"
    if [ -f "${SRC_TWEAKS}/gtk/base-cyber.css" ]; then
      cat "${SRC_TWEAKS}/gtk/base-cyber.css" >> "${THEME_DIR}/gtk-3.0/gtk.css"
      cat "${SRC_TWEAKS}/gtk/base-cyber.css" >> "${THEME_DIR}/gtk-3.0/gtk-dark.css"
      cat "${SRC_TWEAKS}/gtk/base-cyber.css" >> "${THEME_DIR}/gtk-4.0/gtk.css"
      cat "${SRC_TWEAKS}/gtk/base-cyber.css" >> "${THEME_DIR}/gtk-4.0/gtk-dark.css"
    fi
    echo "  + base palette: Arctic Cyber Frost (#0A0E17 midnight navy)"
    ;;
  oled)
    [ -f "${SRC_TWEAKS}/shell/black.css" ] && cat "${SRC_TWEAKS}/shell/black.css" >> "${THEME_DIR}/gnome-shell/gnome-shell.css"
    if [ -f "${SRC_TWEAKS}/gtk/black.css" ]; then
      cat "${SRC_TWEAKS}/gtk/black.css" >> "${THEME_DIR}/gtk-3.0/gtk.css"
      cat "${SRC_TWEAKS}/gtk/black.css" >> "${THEME_DIR}/gtk-3.0/gtk-dark.css"
      cat "${SRC_TWEAKS}/gtk/black.css" >> "${THEME_DIR}/gtk-4.0/gtk.css"
      cat "${SRC_TWEAKS}/gtk/black.css" >> "${THEME_DIR}/gtk-4.0/gtk-dark.css"
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
    append_shell_tweak "${SRC_TWEAKS}/shell/tray-round.css"
    echo "  + top bar: rounded modern island (16px curved floating bar)"
    if have dconf && [ -d "${HOME}/.local/share/gnome-shell/extensions/blur-my-shell@aunetx" ]; then
      dconf write /org/gnome/shell/extensions/blur-my-shell/panel/blur true 2>/dev/null || true
      dconf write /org/gnome/shell/extensions/blur-my-shell/panel/corner-radius 16 2>/dev/null || true
      dconf write /org/gnome/shell/extensions/blur-my-shell/panel/override-background false 2>/dev/null || true
    fi
    ;;
  pill)
    append_shell_tweak "${SRC_TWEAKS}/shell/tray-pill.css"
    echo "  + top bar: floating pill capsule (999px circular ends)"
    if have dconf && [ -d "${HOME}/.local/share/gnome-shell/extensions/blur-my-shell@aunetx" ]; then
      dconf write /org/gnome/shell/extensions/blur-my-shell/panel/blur true 2>/dev/null || true
      dconf write /org/gnome/shell/extensions/blur-my-shell/panel/corner-radius 30 2>/dev/null || true
      dconf write /org/gnome/shell/extensions/blur-my-shell/panel/override-background false 2>/dev/null || true
    fi
    ;;
  bottom-round)
    append_shell_tweak "${SRC_TWEAKS}/shell/tray-bottom-round.css"
    echo "  + top bar: bottom-rounded (connected to top edge)"
    if have dconf && [ -d "${HOME}/.local/share/gnome-shell/extensions/blur-my-shell@aunetx" ]; then
      dconf write /org/gnome/shell/extensions/blur-my-shell/panel/blur true 2>/dev/null || true
      dconf write /org/gnome/shell/extensions/blur-my-shell/panel/corner-radius 16 2>/dev/null || true
      dconf write /org/gnome/shell/extensions/blur-my-shell/panel/override-background false 2>/dev/null || true
    fi
    ;;
  flat)
    append_shell_tweak "${SRC_TWEAKS}/shell/tray-flat.css"
    echo "  + top bar: classic edge-to-edge square bar"
    if have dconf && [ -d "${HOME}/.local/share/gnome-shell/extensions/blur-my-shell@aunetx" ]; then
      dconf write /org/gnome/shell/extensions/blur-my-shell/panel/blur true 2>/dev/null || true
      dconf write /org/gnome/shell/extensions/blur-my-shell/panel/corner-radius 0 2>/dev/null || true
    fi
    ;;
esac

# ---------- apply corner curvature (round vs sharp) ----------
if [ "${CORNERS}" = "sharp" ]; then
  append_shell_tweak "${SRC_TWEAKS}/shell/sharp.css"
  if [ -f "${SRC_TWEAKS}/gtk/sharp.css" ]; then
    cat "${SRC_TWEAKS}/gtk/sharp.css" >> "${THEME_DIR}/gtk-3.0/gtk.css"
    cat "${SRC_TWEAKS}/gtk/sharp.css" >> "${THEME_DIR}/gtk-3.0/gtk-dark.css"
    cat "${SRC_TWEAKS}/gtk/sharp.css" >> "${THEME_DIR}/gtk-4.0/gtk.css"
    cat "${SRC_TWEAKS}/gtk/sharp.css" >> "${THEME_DIR}/gtk-4.0/gtk-dark.css"
  fi
  echo "  + corner curvature: sharp 0px corners (non-rounded industrial aesthetic)"
else
  append_shell_tweak "${SRC_TWEAKS}/shell/round.css"
  if [ -f "${SRC_TWEAKS}/gtk/round.css" ]; then
    cat "${SRC_TWEAKS}/gtk/round.css" >> "${THEME_DIR}/gtk-3.0/gtk.css"
    cat "${SRC_TWEAKS}/gtk/round.css" >> "${THEME_DIR}/gtk-3.0/gtk-dark.css"
    cat "${SRC_TWEAKS}/gtk/round.css" >> "${THEME_DIR}/gtk-4.0/gtk.css"
    cat "${SRC_TWEAKS}/gtk/round.css" >> "${THEME_DIR}/gtk-4.0/gtk-dark.css"
  fi
  echo "  + corner curvature: modern 16px rounded curves"
fi

# ---------- apply surface blur & frosted glassmorphism ----------
if [ "${WANT_BLUR}" -eq 1 ]; then
  append_shell_tweak "${SRC_TWEAKS}/shell/blur-my-shell.css"
  [ -f "${SRC_TWEAKS}/shell/translucent.css" ] && cat "${SRC_TWEAKS}/shell/translucent.css" >> "${THEME_DIR}/gnome-shell/gnome-shell.css"
  # The light theme needs its own surfaces: translucent.css is written for dark glass.
  if [ -f "${LIGHT_THEME_DIR}/gnome-shell/gnome-shell.css" ]; then
    if [ -f "${SRC_TWEAKS}/shell/translucent-light.css" ]; then
      cat "${SRC_TWEAKS}/shell/translucent-light.css" >> "${LIGHT_THEME_DIR}/gnome-shell/gnome-shell.css"
    fi
  fi
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
  [ -f "${SRC_TWEAKS}/shell/noblur.css" ] && cat "${SRC_TWEAKS}/shell/noblur.css" >> "${THEME_DIR}/gnome-shell/gnome-shell.css"
  # The light theme needs its own opaque surfaces: noblur.css is written for dark.
  if [ -f "${LIGHT_THEME_DIR}/gnome-shell/gnome-shell.css" ] && [ -f "${SRC_TWEAKS}/shell/noblur-light.css" ]; then
    cat "${SRC_TWEAKS}/shell/noblur-light.css" >> "${LIGHT_THEME_DIR}/gnome-shell/gnome-shell.css"
  fi
  if [ -f "${SRC_TWEAKS}/gtk/noblur.css" ]; then
    cat "${SRC_TWEAKS}/gtk/noblur.css" >> "${THEME_DIR}/gtk-3.0/gtk.css"
    cat "${SRC_TWEAKS}/gtk/noblur.css" >> "${THEME_DIR}/gtk-3.0/gtk-dark.css"
    cat "${SRC_TWEAKS}/gtk/noblur.css" >> "${THEME_DIR}/gtk-4.0/gtk.css"
    cat "${SRC_TWEAKS}/gtk/noblur.css" >> "${THEME_DIR}/gtk-4.0/gtk-dark.css"
  fi
  echo "  + surface: solid opaque surfaces"
  if have dconf && [ -d "${HOME}/.local/share/gnome-shell/extensions/blur-my-shell@aunetx" ]; then
    dconf write /org/gnome/shell/extensions/blur-my-shell/panel/blur false 2>/dev/null || true
    dconf write /org/gnome/shell/extensions/blur-my-shell/dash-to-dock/blur false 2>/dev/null || true
  fi
fi

# ---------- apply window controls (buttons) ----------
if [ "${CONTROLS}" = "macos" ]; then
  if [ -f "${SRC_TWEAKS}/gtk/macos.css" ]; then
    cat "${SRC_TWEAKS}/gtk/macos.css" >> "${THEME_DIR}/gtk-3.0/gtk.css"
    cat "${SRC_TWEAKS}/gtk/macos.css" >> "${THEME_DIR}/gtk-3.0/gtk-dark.css"
    cat "${SRC_TWEAKS}/gtk/macos.css" >> "${THEME_DIR}/gtk-4.0/gtk.css"
    cat "${SRC_TWEAKS}/gtk/macos.css" >> "${THEME_DIR}/gtk-4.0/gtk-dark.css"
  fi
  echo "  + window controls: macOS traffic dots (Aurora Red / Amber / Green)"
else
  echo "  + window controls: standard Adwaita clean buttons"
fi

# ---------- apply theme sizing / density ----------
if [ "${THEME_SIZE}" = "compact" ]; then
  append_shell_tweak "${SRC_TWEAKS}/shell/compact.css"
  if [ -f "${SRC_TWEAKS}/gtk/compact.css" ]; then
    cat "${SRC_TWEAKS}/gtk/compact.css" >> "${THEME_DIR}/gtk-3.0/gtk.css"
    cat "${SRC_TWEAKS}/gtk/compact.css" >> "${THEME_DIR}/gtk-3.0/gtk-dark.css"
    cat "${SRC_TWEAKS}/gtk/compact.css" >> "${THEME_DIR}/gtk-4.0/gtk.css"
    cat "${SRC_TWEAKS}/gtk/compact.css" >> "${THEME_DIR}/gtk-4.0/gtk-dark.css"
  fi
  echo "  + theme density: compact (slim padding & headerbars)"
else
  echo "  + theme density: standard"
fi

# ---------- apply accent flavor ----------
# Accent base is baked by the Shell build; this only clears literals left in the tweak layers.
# The light theme also receives dark-written tweaks (tray borders), so its accent is normalised
# from the dark source even when the flavor is the default frost.
if have python3 && [ -f "${LIGHT_THEME_DIR}/gnome-shell/gnome-shell.css" ]; then
  python3 "${SRC_TOOLS}/dev/recolor_accent.py" --variant light --source-variant dark \
    --base-only --flavor "${ACCENT}" "${LIGHT_THEME_DIR}/gnome-shell/gnome-shell.css" 2>/dev/null || true
fi

if [ "${ACCENT}" != "frost" ] && have python3; then
  python3 "${SRC_TOOLS}/dev/recolor_accent.py" --variant dark --flavor "${ACCENT}" \
    "${THEME_DIR}/gnome-shell/gnome-shell.css" 2>/dev/null || true
  if [ -f "${LIGHT_THEME_DIR}/gnome-shell/gnome-shell.css" ]; then
    python3 "${SRC_TOOLS}/dev/recolor_accent.py" --variant light --base-only --flavor "${ACCENT}" \
      "${LIGHT_THEME_DIR}/gnome-shell/gnome-shell.css" 2>/dev/null || true
  fi
  # GTK: dark ships accent-<flavor>.css but still carries hardcoded accent literals, and light
  # ships no accent tweak at all, so recolor both trees and re-declare the accent colors.
  for gtk_spec in \
    "dark:${THEME_DIR}/gtk-4.0/gtk.css" "dark:${THEME_DIR}/gtk-4.0/gtk-dark.css" \
    "light:${LIGHT_THEME_DIR}/gtk-4.0/gtk.css" "light:${LIGHT_THEME_DIR}/gtk-4.0/gtk-dark.css"; do
    gtk_variant="${gtk_spec%%:*}"
    gtk_file="${gtk_spec#*:}"
    if [ -f "${gtk_file}" ]; then
      # GTK files are static frost-written source (never pre-baked), so base and strong both map safely.
      python3 "${SRC_TOOLS}/dev/recolor_accent.py" --variant "${gtk_variant}" \
        --flavor "${ACCENT}" --define-colors "${gtk_file}" 2>/dev/null || true
    fi
  done
fi

if [ -f "${SRC_TWEAKS}/gtk/accent-${ACCENT}.css" ]; then
  cat "${SRC_TWEAKS}/gtk/accent-${ACCENT}.css" >> "${THEME_DIR}/gtk-3.0/gtk.css"
  cat "${SRC_TWEAKS}/gtk/accent-${ACCENT}.css" >> "${THEME_DIR}/gtk-3.0/gtk-dark.css"
  cat "${SRC_TWEAKS}/gtk/accent-${ACCENT}.css" >> "${THEME_DIR}/gtk-4.0/gtk.css"
  cat "${SRC_TWEAKS}/gtk/accent-${ACCENT}.css" >> "${THEME_DIR}/gtk-4.0/gtk-dark.css"
  echo "  + accent color: ${ACCENT}"
else
  echo "  + accent color: frost (#88C0D0)"
fi

echo "installed theme files to ${THEME_DIR}"

# ---------- optional: icons & cursors (user ~/.icons only) ----------
if [ "${WANT_ICONS}" -eq 1 ]; then
  mkdir -p "${ICONS_DIR}"
  if [ -d "${SRC_ICONS}/${ICONS_NAME}" ]; then
    rm -rf "${ICONS_DIR}/${ICONS_NAME}"
    cp -r "${SRC_ICONS}/${ICONS_NAME}" "${ICONS_DIR}/"
    if command -v gtk-update-icon-cache >/dev/null 2>&1; then
      gtk-update-icon-cache -f -t "${ICONS_DIR}/${ICONS_NAME}" >/dev/null 2>&1 || true
    fi
    gsettings set org.gnome.desktop.interface icon-theme "${ICONS_NAME}" || true
    echo "installed and activated icon pack in ${ICONS_DIR}/${ICONS_NAME}"
  fi
  if [ -d "${SRC_CURSORS}/${CURSORS_NAME}" ]; then
    rm -rf "${ICONS_DIR}/${CURSORS_NAME}"
    cp -r "${SRC_CURSORS}/${CURSORS_NAME}" "${ICONS_DIR}/"
    gsettings set org.gnome.desktop.interface cursor-theme "${CURSORS_NAME}" || true
    echo "installed and activated cursor pack in ${ICONS_DIR}/${CURSORS_NAME}"
  fi
fi

# ---------- optional: wallpaper (explicit opt-in) ----------
if [ "${WANT_WALLPAPER}" -eq 1 ] && [ "${WALLPAPER_CHOICE}" != "none" ]; then
  WP_DARK_SRC=""
  WP_LIGHT_SRC=""
  case "${WALLPAPER_CHOICE}" in
    1|bloom|prime|canopy|fjord)
      WP_DARK_SRC="${THEME_DIR}/wallpapers/mt-nordic-blue-art-1-3840x2160.png"
      WP_LIGHT_SRC="${THEME_DIR}/wallpapers/light/mt-nordic-blue-canopy-dawn-3840x2160.png"
      ;;
    2|aurora|drift)
      WP_DARK_SRC="${THEME_DIR}/wallpapers/mt-nordic-blue-art-2-3840x2160.png"
      WP_LIGHT_SRC="${THEME_DIR}/wallpapers/light/mt-nordic-blue-celestial-rift-3840x2160.png"
      ;;
    3|sanctuary|macro|flow)
      WP_DARK_SRC="${THEME_DIR}/wallpapers/mt-nordic-blue-art-3-3840x2160.png"
      WP_LIGHT_SRC="${THEME_DIR}/wallpapers/light/mt-nordic-blue-cosmic-dawn-3840x2160.png"
      ;;
    4|crest|frost|topographic)
      WP_DARK_SRC="${THEME_DIR}/wallpapers/mt-nordic-blue-art-4-3840x2160.png"
      WP_LIGHT_SRC="${THEME_DIR}/wallpapers/light/mt-nordic-blue-botanical-horizon-3840x2160.png"
      ;;
    all)
      WP_DARK_SRC="${THEME_DIR}/wallpapers/mt-nordic-blue-art-1-3840x2160.png"
      WP_LIGHT_SRC="${THEME_DIR}/wallpapers/light/mt-nordic-blue-canopy-dawn-3840x2160.png"
      mkdir -p "${HOME}/Pictures/wallpapers-mt-nordic-blue/light"
      cp "${SRC_WALLPAPERS}/"*.png "${HOME}/Pictures/wallpapers-mt-nordic-blue/" 2>/dev/null || true
      cp "${SRC_WALLPAPERS}/light/"*.png "${HOME}/Pictures/wallpapers-mt-nordic-blue/light/" 2>/dev/null || true
      echo "all 4K wallpapers (dark & light) copied to ~/Pictures/wallpapers-mt-nordic-blue/"
      ;;
    *)
      WP_DARK_SRC="${THEME_DIR}/wallpapers/mt-nordic-blue-art-1-3840x2160.png"
      WP_LIGHT_SRC="${THEME_DIR}/wallpapers/light/mt-nordic-blue-canopy-dawn-3840x2160.png"
      ;;
  esac

  if [ -n "${WP_DARK_SRC}" ] && [ -f "${WP_DARK_SRC}" ]; then
    # Inverted High-Contrast pairing: Dark wallpaper on Light mode, Light wallpaper on Dark mode
    gsettings set org.gnome.desktop.background picture-uri "file://${WP_DARK_SRC}" 2>/dev/null || true
    if [ -n "${WP_LIGHT_SRC}" ] && [ -f "${WP_LIGHT_SRC}" ]; then
      gsettings set org.gnome.desktop.background picture-uri-dark "file://${WP_LIGHT_SRC}" 2>/dev/null || true
    fi
    echo "applied inverted high-contrast 4K Bloom wallpaper pairing: dark on light theme, light on dark theme"
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
else
  # libadwaita forces gtk-theme-name to Adwaita-empty, so this link is the only way in.
  echo "  ! libadwaita apps (Nautilus, Settings, Text Editor) stay stock Adwaita without this link; re-run with --gtk4-libadwaita"
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

# ---------- install toggle CLI, desktop entry, and Flatpak overrides ----------
mkdir -p "${HOME}/.local/bin" "${HOME}/.local/share/applications"
if [ -f "${SRC_TOOLS}/dev/mt-nordic-toggle" ]; then
  cp "${SRC_TOOLS}/dev/mt-nordic-toggle" "${HOME}/.local/bin/mt-nordic-toggle"
  chmod +x "${HOME}/.local/bin/mt-nordic-toggle"
  "${HOME}/.local/bin/mt-nordic-toggle" --bind-shortcut 2>/dev/null || true
fi
if [ -f "${SRC_EXTRAS}/desktop/mt-nordic-toggle.desktop" ]; then
  cp "${SRC_EXTRAS}/desktop/mt-nordic-toggle.desktop" "${HOME}/.local/share/applications/mt-nordic-toggle.desktop"
  if command -v update-desktop-database >/dev/null 2>&1; then
    update-desktop-database "${HOME}/.local/share/applications" 2>/dev/null || true
  fi
fi
if [ -f "${REPO_ROOT}/flatpak/apply-overrides.sh" ]; then
  bash "${REPO_ROOT}/flatpak/apply-overrides.sh" 2>/dev/null || true
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
  Theme Toggle:   Super+Shift+T or mt-nordic-toggle

Restore Defaults (Adwaita):
  dconf write /org/gnome/shell/extensions/user-theme/name "''"
  gsettings set org.gnome.desktop.interface gtk-theme 'Adwaita'
  gsettings set org.gnome.desktop.interface icon-theme 'Adwaita'
  gsettings set org.gnome.desktop.interface cursor-theme 'Adwaita'
  rm -f ~/.config/gtk-4.0/gtk.css
EOF

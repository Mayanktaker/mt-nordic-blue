#!/bin/sh
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Automated installer for MT Nordic Blue app ecosystem and terminal themes.
# Detects installed user tools and registers matching color schemes.

set -eu

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"

if [ -f "${REPO_ROOT}/palette/tokens.json" ]; then
  DISPLAY_NAME="$(python3 -c "import json; print(json.load(open('${REPO_ROOT}/palette/tokens.json'))['meta']['name'])" 2>/dev/null || echo "MT Nordic Blue")"
else
  DISPLAY_NAME="MT Nordic Blue"
fi

echo "=== ${DISPLAY_NAME}: Application Ecosystem Installer ==="

have() {
  command -v "$1" >/dev/null 2>&1
}

# 1. Terminals
# Ghostty
if have ghostty || [ -d "${HOME}/.config/ghostty" ]; then
  mkdir -p "${HOME}/.config/ghostty/themes"
  cp "${REPO_ROOT}/extras/terminals/ghostty/mt-nordic-blue" "${HOME}/.config/ghostty/themes/"
  echo "✓ Ghostty: theme installed to ~/.config/ghostty/themes/mt-nordic-blue"
fi

# Kitty
if have kitty || [ -d "${HOME}/.config/kitty" ]; then
  mkdir -p "${HOME}/.config/kitty/themes"
  cp "${REPO_ROOT}/extras/terminals/kitty/mt-nordic-blue.conf" "${HOME}/.config/kitty/themes/"
  echo "✓ Kitty: theme installed to ~/.config/kitty/themes/mt-nordic-blue.conf"
fi

# Alacritty
if have alacritty || [ -d "${HOME}/.config/alacritty" ]; then
  mkdir -p "${HOME}/.config/alacritty/themes"
  cp "${REPO_ROOT}/extras/terminals/alacritty/mt-nordic-blue.toml" "${HOME}/.config/alacritty/themes/"
  echo "✓ Alacritty: theme installed to ~/.config/alacritty/themes/mt-nordic-blue.toml"
fi

# Foot
if have foot || [ -d "${HOME}/.config/foot" ]; then
  mkdir -p "${HOME}/.config/foot/themes"
  cp "${REPO_ROOT}/extras/terminals/foot/mt-nordic-blue.ini" "${HOME}/.config/foot/themes/"
  echo "✓ Foot: theme installed to ~/.config/foot/themes/mt-nordic-blue.ini"
fi

# GNOME Terminal
if have gnome-terminal || have dconf; then
  if [ -f "${REPO_ROOT}/extras/terminals/gnome-terminal/install.sh" ]; then
    bash "${REPO_ROOT}/extras/terminals/gnome-terminal/install.sh" >/dev/null 2>&1 || true
    echo "✓ GNOME Terminal: profile registered via dconf"
  fi
fi

# 2. Shells
# Fish Shell
if have fish || [ -d "${HOME}/.config/fish" ]; then
  if [ -f "${REPO_ROOT}/extras/fish/install.sh" ]; then
    bash "${REPO_ROOT}/extras/fish/install.sh" >/dev/null 2>&1 || true
    echo "✓ Fish Shell: theme installed and activated"
  fi
fi

# 3. Text Editors & IDEs
# GNOME Text Editor / GtkSourceView
if [ -f "${REPO_ROOT}/extras/text-editors/gnome-text-editor/install.sh" ]; then
  bash "${REPO_ROOT}/extras/text-editors/gnome-text-editor/install.sh" >/dev/null 2>&1 || true
  echo "✓ GNOME Text Editor: GtkSourceView-5 style registered"
fi

# VS Code / VSCodium
for vsc_dir in "${HOME}/.vscode/extensions" "${HOME}/.vscode-oss/extensions" "${HOME}/.cursor/extensions"; do
  if [ -d "${vsc_dir}" ]; then
    target="${vsc_dir}/mt-nordic-blue-theme"
    mkdir -p "${target}"
    cp -r "${REPO_ROOT}/extras/vscode/"* "${target}/"
    echo "✓ VS Code/Cursor: extension installed to ${target}"
  fi
done

# Fastfetch
if have fastfetch || [ -d "${HOME}/.config/fastfetch" ]; then
  mkdir -p "${HOME}/.config/fastfetch"
  cp "${REPO_ROOT}/extras/fastfetch/mt-nordic-blue.txt" "${HOME}/.config/fastfetch/"
  echo "✓ Fastfetch: Nordic ASCII art installed to ~/.config/fastfetch/mt-nordic-blue.txt"
fi

# KDE / Qt color schemes
if [ -d "${HOME}/.local/share/color-schemes" ] || have kwriteconfig5 || have kwriteconfig6; then
  if [ -f "${REPO_ROOT}/extras/kde/color-schemes/install.sh" ]; then
    bash "${REPO_ROOT}/extras/kde/color-schemes/install.sh" >/dev/null 2>&1 || true
    echo "✓ KDE: color scheme registered in ~/.local/share/color-schemes"
  fi
fi

echo "=== All compatible application themes installed successfully! ==="

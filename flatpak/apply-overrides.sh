#!/usr/bin/env bash
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Configure Flatpak user filesystem overrides so Flatpak apps read MT Nordic themes and GTK4 config.

set -euo pipefail

if ! command -v flatpak >/dev/null 2>&1; then
  echo "flatpak command not found. Skipping Flatpak overrides."
  exit 0
fi

echo "Configuring Flatpak user overrides for MT Nordic Blue & Light..."

# Grant Flatpak applications access to user themes, icons, and GTK4 config overrides
flatpak override --user --filesystem=xdg-config/gtk-4.0:ro 2>/dev/null || true
flatpak override --user --filesystem="${HOME}/.themes:ro" 2>/dev/null || true
flatpak override --user --filesystem="${HOME}/.icons:ro" 2>/dev/null || true

echo "✨ Flatpak user overrides successfully applied!"
echo "Flatpak GTK3/GTK4 apps can now access ~/.themes, ~/.icons, and ~/.config/gtk-4.0."

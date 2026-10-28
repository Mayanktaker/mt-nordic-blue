#!/bin/sh
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Install MT Nordic Blue Plymouth boot splash (requires root)

set -eu

THEME_NAME="mt-nordic-blue"
THEME_DIR="/usr/share/plymouth/themes/${THEME_NAME}"
SRC_DIR="$(cd "$(dirname "$0")" && pwd)"

if [ "$(id -u)" -ne 0 ]; then
  echo "Error: Plymouth installation requires root privileges." >&2
  exit 1
fi

mkdir -p "${THEME_DIR}"
cp -r "${SRC_DIR}"/* "${THEME_DIR}/"

if command -v plymouth-set-default-theme >/dev/null 2>&1; then
  plymouth-set-default-theme -R "${THEME_NAME}"
  echo "✓ MT Nordic Blue Plymouth theme installed and active!"
elif command -v update-alternatives >/dev/null 2>&1; then
  update-alternatives --install /usr/share/plymouth/themes/default.plymouth default.plymouth "${THEME_DIR}/${THEME_NAME}.plymouth" 100
  update-alternatives --set default.plymouth "${THEME_DIR}/${THEME_NAME}.plymouth"
  update-initramfs -u
  echo "✓ MT Nordic Blue Plymouth theme configured via update-alternatives!"
fi

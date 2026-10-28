#!/bin/sh
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Install MT Nordic Blue GRUB theme (requires root)

set -eu

THEME_NAME="mt-nordic-blue"
THEME_DIR="/boot/grub/themes/${THEME_NAME}"
SRC_DIR="$(cd "$(dirname "$0")" && pwd)"

if [ "$(id -u)" -ne 0 ]; then
  echo "Error: GRUB installation requires root privileges." >&2
  exit 1
fi

mkdir -p "${THEME_DIR}"
cp -r "${SRC_DIR}"/* "${THEME_DIR}/"

if [ -f /etc/default/grub ]; then
  sed -i '/^GRUB_THEME=/d' /etc/default/grub
  echo "GRUB_THEME=\"${THEME_DIR}/theme.txt\"" >> /etc/default/grub
  if command -v update-grub >/dev/null 2>&1; then
    update-grub
  elif command -v grub-mkconfig >/dev/null 2>&1; then
    grub-mkconfig -o /boot/grub/grub.cfg
  fi
  echo "✓ MT Nordic Blue GRUB theme installed successfully!"
fi

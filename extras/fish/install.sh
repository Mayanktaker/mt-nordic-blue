#!/bin/sh
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Install MT Nordic Blue theme for Fish Shell

set -eu

THEME_NAME="mt_nordic_blue"
SRC="$(cd "$(dirname "$0")" && pwd)/${THEME_NAME}.theme"
DEST="${HOME}/.config/fish/themes/${THEME_NAME}.theme"

mkdir -p "${HOME}/.config/fish/themes"
cp "${SRC}" "${DEST}"
echo "Installed to ${DEST}"

if command -v fish >/dev/null 2>&1; then
  fish -c "fish_config theme choose ${THEME_NAME}"
  echo "Activated ${THEME_NAME} in fish"
fi

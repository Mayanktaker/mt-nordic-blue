#!/usr/bin/env bash
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Install MT Nordic Blue color scheme into KDE Plasma / Qt.

DEST_DIR="${HOME}/.local/share/color-schemes"
SRC_FILE="$(cd "$(dirname "$0")" && pwd)/MTNordicBlue.colors"

mkdir -p "${DEST_DIR}"
cp "${SRC_FILE}" "${DEST_DIR}/MTNordicBlue.colors"

echo "Installed to ${DEST_DIR}/MTNordicBlue.colors"
echo "Select 'MT Nordic Blue' in KDE System Settings -> Appearance -> Colors."

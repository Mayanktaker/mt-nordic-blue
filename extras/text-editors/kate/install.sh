#!/usr/bin/env bash
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Install MT-Nordic-Blue theme into KDE Kate / KWrite.

DEST_DIR="${HOME}/.local/share/org.kde.syntax-highlighting/themes"
SRC_FILE="$(cd "$(dirname "$0")" && pwd)/MT-Nordic-Blue.colors"

mkdir -p "${DEST_DIR}"
cp "${SRC_FILE}" "${DEST_DIR}/MT-Nordic-Blue.colors"

echo "Installed to ${DEST_DIR}/MT-Nordic-Blue.colors"
echo "Select 'MT-Nordic-Blue' in Kate Settings -> Configure Kate -> Color Themes."

#!/bin/sh
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Install MT Nordic Blue GtkSourceView style scheme for GNOME Text Editor, Builder, Gedit

set -eu

SRC_FILE="$(cd "$(dirname "$0")" && pwd)/mt-nordic-blue.xml"
DEST_DIR="${HOME}/.local/share/gtksourceview-5/styles"

mkdir -p "${DEST_DIR}"
cp "${SRC_FILE}" "${DEST_DIR}/"

echo "Installed to ${DEST_DIR}/mt-nordic-blue.xml"
echo "Select 'MT Nordic Blue' in GNOME Text Editor preferences."

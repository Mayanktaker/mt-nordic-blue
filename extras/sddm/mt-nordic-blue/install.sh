#!/bin/sh
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Install MT Nordic Blue SDDM theme (requires root)

set -eu

THEME_NAME="mt-nordic-blue"
THEME_DIR="/usr/share/sddm/themes/${THEME_NAME}"
SRC_DIR="$(cd "$(dirname "$0")" && pwd)"

if [ "$(id -u)" -ne 0 ]; then
  echo "Error: SDDM installation requires root privileges." >&2
  exit 1
fi

mkdir -p "${THEME_DIR}"
cp -r "${SRC_DIR}"/* "${THEME_DIR}/"

mkdir -p /etc/sddm.conf.d
cat <<EOF > /etc/sddm.conf.d/theme.conf
[Theme]
Current=${THEME_NAME}
EOF

echo "✓ MT Nordic Blue SDDM theme installed successfully!"

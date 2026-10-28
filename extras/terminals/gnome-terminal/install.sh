#!/bin/sh
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Configure GNOME Terminal profile for MT Nordic Blue

set -eu

PROFILE_NAME="MT Nordic Blue"
PROFILE_ID="$(uuidgen 2>/dev/null || python3 -c 'import uuid; print(uuid.uuid4())')"
DCONF_PATH="/org/gnome/terminal/legacy/profiles:/:${PROFILE_ID}/"

echo "Creating GNOME Terminal profile: ${PROFILE_NAME} (${PROFILE_ID})..."

dconf write "${DCONF_PATH}visible-name" "'${PROFILE_NAME}'"
dconf write "${DCONF_PATH}use-theme-colors" "false"
dconf write "${DCONF_PATH}background-color" "'#0E141D'"
dconf write "${DCONF_PATH}foreground-color" "'#ECEFF4'"
dconf write "${DCONF_PATH}cursor-colors-set" "true"
dconf write "${DCONF_PATH}cursor-background-color" "'#88C0D0'"
dconf write "${DCONF_PATH}cursor-foreground-color" "'#090D14'"
dconf write "${DCONF_PATH}highlight-colors-set" "true"
dconf write "${DCONF_PATH}highlight-background-color" "'#88C0D0'"
dconf write "${DCONF_PATH}highlight-foreground-color" "'#090D14'"

PALETTE="['#151D2A', '#BF616A', '#A3BE8C', '#EBCB8B', '#81A1C1', '#B48EAD', '#88C0D0', '#D8DEE9', '#25344A', '#D08770', '#8FBCBB', '#F0D7A3', '#5E81AC', '#C9A7C5', '#A3D4E2', '#ECEFF4']"
dconf write "${DCONF_PATH}palette" "${PALETTE}"

# Register profile in list
LIST="$(dconf read /org/gnome/terminal/legacy/profiles:/list || echo '[]')"
if [ "${LIST}" = "[]" ] || [ -z "${LIST}" ]; then
  dconf write /org/gnome/terminal/legacy/profiles:/list "['${PROFILE_ID}']"
else
  NEW_LIST="$(echo "${LIST}" | sed "s/]/, '${PROFILE_ID}']/")"
  dconf write /org/gnome/terminal/legacy/profiles:/list "${NEW_LIST}"
fi

echo "✓ GNOME Terminal profile installed: ${PROFILE_NAME}"

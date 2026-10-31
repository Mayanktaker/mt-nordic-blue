#!/bin/sh
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Build everything and assemble the vX.Y release tarball + wallpaper into dist/.
# Usage: tools/release.sh <version>   (e.g. tools/release.sh 0.1.0)

set -eu

VERSION="${1:?usage: tools/release.sh <version>}"
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

if [ -f "${REPO_ROOT}/palette/tokens.json" ]; then
  TECH_NAME="$(python3 -c "import json; print(json.load(open('${REPO_ROOT}/palette/tokens.json'))['meta']['tech_name'])" 2>/dev/null || echo "MT-Theme-Starter")"
  DISPLAY_NAME="$(python3 -c "import json; print(json.load(open('${REPO_ROOT}/palette/tokens.json'))['meta']['name'])" 2>/dev/null || echo "MT Theme Starter")"
  TECH_SLUG="$(python3 -c "import json; print(json.load(open('${REPO_ROOT}/palette/tokens.json'))['meta']['tech_name'].lower())" 2>/dev/null || echo "mt-theme-starter")"
else
  TECH_NAME="MT-Theme-Starter"
  DISPLAY_NAME="MT Theme Starter"
  TECH_SLUG="mt-theme-starter"
fi

DIST="${REPO_ROOT}/dist/${TECH_SLUG}-v${VERSION}"
TARBALL="${REPO_ROOT}/dist/${TECH_SLUG}-v${VERSION}.tar.xz"

# Rebuild all layers from tokens
python3 "${REPO_ROOT}/tools/dev/check_contrast.py" > /dev/null
python3 "${REPO_ROOT}/tools/wallpaper/generate.py" > /dev/null
python3 "${REPO_ROOT}/tools/wallpaper/process_light.py" > /dev/null
python3 "${REPO_ROOT}/tools/icons/generate_icons.py" > /dev/null
python3 "${REPO_ROOT}/tools/icons/generate_cursors.py" > /dev/null
python3 "${REPO_ROOT}/tools/shell/build.py" --all
python3 "${REPO_ROOT}/tools/gtk/build.py" > /dev/null

# Assemble the installable tree (installer layout) per supported shell major
rm -rf "${DIST}"
mkdir -p "${DIST}"
cp "${REPO_ROOT}/src/index.theme" "${DIST}/index.theme"
cp "${REPO_ROOT}/src/index-light.theme" "${DIST}/index-light.theme" 2>/dev/null || true
for major_dir in "${REPO_ROOT}"/build/theme/gnome-shell-*; do
  name="${major_dir##*/}"
  case "${name}" in
    gnome-shell-*-light)
      major="${name#gnome-shell-}"; major="${major%-light}"
      mkdir -p "${DIST}/gnome-shell-light"
      cp -r "${major_dir}" "${DIST}/gnome-shell-light/gnome-shell-${major}-light"
      ;;
    gnome-shell-*)
      major="${name#gnome-shell-}"
      cp -r "${major_dir}" "${DIST}/gnome-shell-${major}"
      ;;
  esac
done
cp -r "${REPO_ROOT}/build/theme/gtk-3.0" "${DIST}/gtk-3.0"
cp -r "${REPO_ROOT}/src/gtk-4.0" "${DIST}/gtk-4.0-src"
cp -r "${REPO_ROOT}/src/tweaks" "${DIST}/tweaks"
cp -r "${REPO_ROOT}/src/icons" "${DIST}/icons"
cp -r "${REPO_ROOT}/src/cursors" "${DIST}/cursors"
cp -r "${REPO_ROOT}/extras" "${DIST}/extras"
mkdir -p "${DIST}/tools/dev" "${DIST}/flatpak"
cp "${REPO_ROOT}/tools/dev/mt-nordic-toggle" "${DIST}/tools/dev/mt-nordic-toggle"
# Accent switching inside a bundle needs the recolor tool and the token source it reads.
cp "${REPO_ROOT}/tools/dev/recolor_accent.py" "${DIST}/tools/dev/recolor_accent.py"
cp -r "${REPO_ROOT}/palette" "${DIST}/palette"
cp "${REPO_ROOT}/flatpak/apply-overrides.sh" "${DIST}/flatpak/apply-overrides.sh"
cp "${REPO_ROOT}/tools/install.sh" "${DIST}/install.sh"

if [ -d "${REPO_ROOT}/wallpaper/dist" ] && [ "$(ls -A "${REPO_ROOT}/wallpaper/dist" 2>/dev/null)" ]; then
  mkdir -p "${DIST}/wallpapers"
  cp -r "${REPO_ROOT}/wallpaper/dist/"* "${DIST}/wallpapers/" 2>/dev/null || true
fi

cp "${REPO_ROOT}/README.md" "${REPO_ROOT}/LICENSES/GPL-3.0.txt" "${REPO_ROOT}/LICENSES/CC-BY-SA-4.0.txt" "${DIST}/" 2>/dev/null || true

mkdir -p "${REPO_ROOT}/dist"
tar -C "${REPO_ROOT}/dist" -cJf "${TARBALL}" "${TECH_SLUG}-v${VERSION}"
rm -rf "${DIST}"

# Assemble standalone icon pack tarball
if [ -f "${REPO_ROOT}/tools/icons/package.sh" ]; then
  bash "${REPO_ROOT}/tools/icons/package.sh" "${VERSION}"
fi

echo "Release ready:"
echo "  - Theme bundle: ${TARBALL}"
echo "  - Standalone icons: ${REPO_ROOT}/dist/${TECH_SLUG}-icons-v${VERSION}.tar.xz"
echo "Attach to GitHub release: git tag v${VERSION} && gh release create v${VERSION} ${TARBALL} ${REPO_ROOT}/dist/${TECH_SLUG}-icons-v${VERSION}.tar.xz"

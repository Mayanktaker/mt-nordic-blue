# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Generates GRUB bootloader theme assets for MT Nordic Blue.

from pathlib import Path
from PIL import Image, ImageDraw

REPO_ROOT = Path(__file__).resolve().parents[2]
GRUB_DIR = REPO_ROOT / "extras" / "grub" / "mt-nordic-blue"
GRUB_DIR.mkdir(parents=True, exist_ok=True)

def generate_selection():
    # Selection bar in frost cyan #88C0D0
    w, h = 420, 38
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=8, fill=(136, 192, 208, 45), outline=(136, 192, 208, 180), width=1)
    im.save(GRUB_DIR / "select_c.png")

def generate_theme_txt():
    bg_src = REPO_ROOT / "wallpaper" / "preview" / "mt-nordic-blue-art-1-1920x1080.jpg"
    if bg_src.exists():
        im = Image.open(bg_src)
        im.save(GRUB_DIR / "background.png")

    theme_txt = """# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# GRUB2 theme: MT Nordic Blue

title-text: "MT Nordic Blue"
title-font: "DejaVu Sans Regular 16"
title-color: "#88C0D0"

message-font: "DejaVu Sans Regular 12"
message-color: "#ECEFF4"
message-bg-color: "#0E141D"

desktop-image: "background.png"
desktop-color: "#0E141D"

+ boot_menu {
  left = 30%
  top = 35%
  width = 40%
  height = 45%
  item_font = "DejaVu Sans Regular 14"
  item_color = "#D8DEE9"
  selected_item_color = "#ECEFF4"
  icon_width = 24
  icon_height = 24
  item_height = 42
  item_padding = 10
  item_spacing = 6
  selected_item_pixmap_style = "select_*.png"
}

+ progress_bar {
  id = "__timeout__"
  left = 30%
  top = 85%
  width = 40%
  height = 14
  text_color = "#ECEFF4"
  font = "DejaVu Sans Regular 11"
  bar_style = "progress_bar_*.png"
  highlight_style = "progress_highlight_*.png"
}
"""
    (GRUB_DIR / "theme.txt").write_text(theme_txt)

    installer = """#!/bin/sh
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Install MT Nordic Blue GRUB theme (requires sudo)

set -eu
THEME_NAME="mt-nordic-blue"
DEST_DIR="/boot/grub/themes/${THEME_NAME}"
SRC_DIR="$(cd "$(dirname "$0")" && pwd)"

if [ "$(id -u)" -ne 0 ]; then
  echo "This script must be run as root (use sudo)." >&2
  exit 1
fi

echo "Installing MT Nordic Blue GRUB theme to ${DEST_DIR}..."
mkdir -p "${DEST_DIR}"
cp -r "${SRC_DIR}/"* "${DEST_DIR}/"

if [ -f /etc/default/grub ]; then
  if grep -q "^GRUB_THEME=" /etc/default/grub; then
    sed -i "s|^GRUB_THEME=.*|GRUB_THEME=\\"${DEST_DIR}/theme.txt\\"|" /etc/default/grub
  else
    echo "GRUB_THEME=\\"${DEST_DIR}/theme.txt\\"" >> /etc/default/grub
  fi
  echo "Updated /etc/default/grub. Run 'sudo grub-mkconfig -o /boot/grub/grub.cfg' or 'sudo update-grub' to activate."
fi
"""
    (GRUB_DIR / "install.sh").write_text(installer)
    (GRUB_DIR / "install.sh").chmod(0o755)

if __name__ == "__main__":
    generate_selection()
    generate_theme_txt()
    print(f"Generated GRUB assets in {GRUB_DIR}")

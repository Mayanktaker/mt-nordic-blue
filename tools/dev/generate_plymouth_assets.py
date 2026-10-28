# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Generates Plymouth boot splash theme assets for MT Nordic Blue.

import math
from pathlib import Path
from PIL import Image, ImageDraw

REPO_ROOT = Path(__file__).resolve().parents[2]
PLYMOUTH_DIR = REPO_ROOT / "extras" / "plymouth" / "mt-nordic-blue"
PLYMOUTH_DIR.mkdir(parents=True, exist_ok=True)

def generate_spinner():
    # 24-frame Nordic spinner (48x48) in frost cyan
    for frame in range(24):
        im = Image.new("RGBA", (48, 48), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        angle_step = 2 * math.pi / 8
        base_angle = frame * (2 * math.pi / 24)
        for i in range(8):
            a = base_angle + i * angle_step
            r = 16
            cx = 24 + r * math.cos(a)
            cy = 24 + r * math.sin(a)
            alpha = int(35 + (220 * (i + 1) / 8))
            dot_r = 2.5
            d.ellipse([cx - dot_r, cy - dot_r, cx + dot_r, cy + dot_r], fill=(136, 192, 208, alpha))
        im.save(PLYMOUTH_DIR / f"throbber-{frame:02d}.png")

def generate_lock_box():
    # Password entry prompt box
    w, h = 320, 42
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=10, fill=(21, 29, 42, 220), outline=(37, 52, 74, 255), width=1)
    im.save(PLYMOUTH_DIR / "entry.png")

    bullet = Image.new("RGBA", (10, 10), (0, 0, 0, 0))
    bd = ImageDraw.Draw(bullet)
    bd.ellipse([1, 1, 8, 8], fill=(136, 192, 208, 255))
    bullet.save(PLYMOUTH_DIR / "bullet.png")

def generate_config():
    bg_src = REPO_ROOT / "wallpaper" / "preview" / "mt-nordic-blue-art-1-1920x1080.jpg"
    if bg_src.exists():
        im = Image.open(bg_src)
        im.save(PLYMOUTH_DIR / "background.png")

    plymouth_cfg = """# © Mayanktaker Computers & Web Development | https://mayanktaker.com
[Plymouth Theme]
Name=MT Nordic Blue
Description=Nordic Frost & Arctic Blue Boot Splash Theme
ModuleName=script

[script]
ImageDir=/usr/share/plymouth/themes/mt-nordic-blue
ScriptFile=/usr/share/plymouth/themes/mt-nordic-blue/mt-nordic-blue.script
"""
    (PLYMOUTH_DIR / "mt-nordic-blue.plymouth").write_text(plymouth_cfg)

    script_content = """# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Plymouth boot script for MT Nordic Blue

screen_width = Window.GetWidth();
screen_height = Window.GetHeight();

# 1. Background
bg_image = Image("background.png");
if (bg_image) {
    resized_bg = bg_image.Scale(screen_width, screen_height);
    bg_sprite = Sprite(resized_bg);
    bg_sprite.SetZ(-100);
}

# 2. Animated Spinner
for (i = 0; i < 24; i++) {
    spinner_images[i] = Image("throbber-" + (i < 10 ? "0" : "") + i + ".png");
}

spinner_sprite = Sprite();
spinner_sprite.SetX(screen_width / 2 - 24);
spinner_sprite.SetY(screen_height / 2 + 120);
spinner_sprite.SetZ(10);

frame = 0;
fun refresh_callback () {
    frame = (frame + 1) % 24;
    spinner_sprite.SetImage(spinner_images[frame]);
}
Plymouth.SetRefreshFunction(refresh_callback);

# 3. Password Dialog
fun dialog_setup() {
    entry_image = Image("entry.png");
    entry_sprite = Sprite(entry_image);
    entry_sprite.SetX(screen_width / 2 - 160);
    entry_sprite.SetY(screen_height / 2 + 60);
    entry_sprite.SetZ(20);
}
Plymouth.SetDisplayPasswordFunction(dialog_setup);
"""
    (PLYMOUTH_DIR / "mt-nordic-blue.script").write_text(script_content)

    installer = """#!/bin/sh
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Install MT Nordic Blue Plymouth boot theme (requires sudo)

set -eu
THEME_NAME="mt-nordic-blue"
DEST_DIR="/usr/share/plymouth/themes/${THEME_NAME}"
SRC_DIR="$(cd "$(dirname "$0")" && pwd)"

if [ "$(id -u)" -ne 0 ]; then
  echo "This script must be run as root (use sudo)." >&2
  exit 1
fi

echo "Installing MT Nordic Blue Plymouth theme to ${DEST_DIR}..."
mkdir -p "${DEST_DIR}"
cp -r "${SRC_DIR}/"* "${DEST_DIR}/"

if command -v plymouth-set-default-theme >/dev/null 2>&1; then
  plymouth-set-default-theme -R "${THEME_NAME}" || true
  echo "Set default theme to ${THEME_NAME} and rebuilt initramfs."
fi
"""
    (PLYMOUTH_DIR / "install.sh").write_text(installer)
    (PLYMOUTH_DIR / "install.sh").chmod(0o755)

if __name__ == "__main__":
    generate_spinner()
    generate_lock_box()
    generate_config()
    print(f"Generated Plymouth assets in {PLYMOUTH_DIR}")

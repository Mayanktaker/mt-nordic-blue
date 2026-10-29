# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Generates companion Xcursor suite: authentic high-definition Nordic cursors in MT Nordic Blue.
# Multi-resolution (30x30, 45x45, 60x60) with Deep Polar Night body, Frost Cyan borders & Electric Cyan accents.

import json
import os
from pathlib import Path
import shutil
import struct
import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[2]
TOKENS = json.loads((REPO_ROOT / "palette" / "tokens.json").read_text())
TECH_NAME = TOKENS.get("meta", {}).get("tech_name", "MT-Nordic-Blue")
DISPLAY_NAME = TOKENS.get("meta", {}).get("name", "MT Nordic Blue")
OUT_DIR = REPO_ROOT / "src" / "cursors" / f"{TECH_NAME}-Cursors"
SYSTEM_NORDIC_CURSORS = Path.home() / ".icons" / "Nordic-cursors" / "cursors"

INDEX_THEME = f"""[Icon Theme]
Name={TECH_NAME}-Cursors
Comment=Authentic Nordic cursor suite for {DISPLAY_NAME}
Inherits=Adwaita
"""


def hex_to_rgb(hex_color: str) -> tuple:
    # Convert #RRGGBB into RGB tuple.
    return tuple(int(hex_color[i : i + 2], 16) for i in (1, 3, 5))


# Nordic palette color definitions from tokens.json
COLOR_BODY_BASE = hex_to_rgb(TOKENS["color"]["bg"]["base"])               # #0E141D
COLOR_BODY_SURFACE = hex_to_rgb(TOKENS["color"]["bg"]["surface"])         # #202D40
COLOR_BORDER_FROST = hex_to_rgb(TOKENS["color"]["accent"]["base"])        # #88C0D0
COLOR_BORDER_WHITE = hex_to_rgb(TOKENS["color"]["text"]["primary"])       # #ECEFF4
COLOR_ACCENT_CYAN = hex_to_rgb(TOKENS["color"]["accent_flavors"]["cyber"]) # #00D2FF
COLOR_STATUS_RED = hex_to_rgb(TOKENS["color"]["status"]["destructive"])    # #BF616A


def recolor_bgra_chunk(bgra_bytes: bytes, w: int, h: int) -> bytes:
    # Recolor an Xcursor BGRA image chunk into MT Nordic Blue tokens.
    arr = np.frombuffer(bgra_bytes, dtype=np.uint8).reshape((h, w, 4)).astype(np.float32)
    b, g, r, a = arr[..., 0], arr[..., 1], arr[..., 2], arr[..., 3]
    mask = a > 5

    # Safe un-premultiply alpha without divide-by-zero
    r_un = np.zeros_like(r)
    g_un = np.zeros_like(g)
    b_un = np.zeros_like(b)
    np.divide(r * 255.0, a, out=r_un, where=mask)
    np.divide(g * 255.0, a, out=g_un, where=mask)
    np.divide(b * 255.0, a, out=b_un, where=mask)

    max_c = np.maximum(np.maximum(r_un, g_un), b_un)
    min_c = np.minimum(np.minimum(r_un, g_un), b_un)
    lum = (max_c + min_c) / 2.0
    chroma = max_c - min_c

    # Detect color roles in source cursor
    is_red = (r_un > g_un + 25) & (r_un > b_un + 25) & (chroma > 20)
    is_cyan = (b_un > r_un + 15) & (chroma > 15)

    # 1. Dark body: #0E141D to #202D40
    t_dark = np.clip(lum / 110.0, 0, 1)
    body_r = COLOR_BODY_BASE[0] + t_dark * (COLOR_BODY_SURFACE[0] - COLOR_BODY_BASE[0])
    body_g = COLOR_BODY_BASE[1] + t_dark * (COLOR_BODY_SURFACE[1] - COLOR_BODY_BASE[1])
    body_b = COLOR_BODY_BASE[2] + t_dark * (COLOR_BODY_SURFACE[2] - COLOR_BODY_BASE[2])

    # 2. Bright perimeter border: Frost Cyan #88C0D0 to Snow White #ECEFF4
    t_light = np.clip((lum - 110.0) / 145.0, 0, 1)
    border_r = COLOR_BORDER_FROST[0] + t_light * (COLOR_BORDER_WHITE[0] - COLOR_BORDER_FROST[0])
    border_g = COLOR_BORDER_FROST[1] + t_light * (COLOR_BORDER_WHITE[1] - COLOR_BORDER_FROST[1])
    border_b = COLOR_BORDER_FROST[2] + t_light * (COLOR_BORDER_WHITE[2] - COLOR_BORDER_FROST[2])

    is_body = lum < 110.0
    out_r = np.where(is_body, body_r, border_r)
    out_g = np.where(is_body, body_g, border_g)
    out_b = np.where(is_body, body_b, border_b)

    # 3. Status Red accents
    out_r = np.where(is_red, COLOR_STATUS_RED[0], out_r)
    out_g = np.where(is_red, COLOR_STATUS_RED[1], out_g)
    out_b = np.where(is_red, COLOR_STATUS_RED[2], out_b)

    # 4. Electric Ice Cyan accents / spinners
    t_cyan = np.clip(lum / 255.0, 0, 1)
    out_r = np.where(is_cyan, COLOR_ACCENT_CYAN[0] + t_cyan * (COLOR_BORDER_FROST[0] - COLOR_ACCENT_CYAN[0]), out_r)
    out_g = np.where(is_cyan, COLOR_ACCENT_CYAN[1] + t_cyan * (COLOR_BORDER_FROST[1] - COLOR_ACCENT_CYAN[1]), out_g)
    out_b = np.where(is_cyan, COLOR_ACCENT_CYAN[2], out_b)

    # Re-premultiply alpha for Xcursor binary standard
    out_r = np.clip(out_r * (a / 255.0), 0, 255).astype(np.uint8)
    out_g = np.clip(out_g * (a / 255.0), 0, 255).astype(np.uint8)
    out_b = np.clip(out_b * (a / 255.0), 0, 255).astype(np.uint8)
    return np.stack([out_b, out_g, out_r, a.astype(np.uint8)], axis=-1).tobytes()


def process_xcursor_file(src_path: Path, dst_path: Path) -> None:
    # Parse an Xcursor file, recolor all image frames across all resolutions, and write to destination.
    data = src_path.read_bytes()
    magic, hdr_size, ver, ntoc = struct.unpack("<IIII", data[:16])
    if magic != 0x72756358:
        # Not a valid Xcursor, copy directly
        dst_path.write_bytes(data)
        return

    new_chunks = []
    toc_entries = []
    cur_offset = 16 + ntoc * 12

    for i in range(ntoc):
        type_, subtype, offset = struct.unpack("<III", data[16 + i * 12 : 28 + i * 12])
        img_hdr = struct.unpack("<IIIIIIIII", data[offset : offset + 36])
        w, h = img_hdr[4], img_hdr[5]
        pixel_bytes = data[offset + 36 : offset + 36 + w * h * 4]
        recolored_pixels = recolor_bgra_chunk(pixel_bytes, w, h)
        chunk = data[offset : offset + 36] + recolored_pixels
        new_chunks.append(chunk)
        toc_entries.append(struct.pack("<III", type_, subtype, cur_offset))
        cur_offset += len(chunk)

    new_data = struct.pack("<IIII", magic, hdr_size, ver, ntoc) + b"".join(toc_entries) + b"".join(new_chunks)
    dst_path.write_bytes(new_data)


def build_cursors() -> None:
    # Build complete authentic Nordic Xcursor suite.
    cursors_dir = OUT_DIR / "cursors"
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    cursors_dir.mkdir(parents=True, exist_ok=True)

    # 1. Write index.theme
    (OUT_DIR / "index.theme").write_text(INDEX_THEME)

    # 2. Check source cursors
    if not SYSTEM_NORDIC_CURSORS.exists():
        print(f"[ERROR] Source Nordic cursors not found at {SYSTEM_NORDIC_CURSORS}")
        return

    # 3. Process all real files
    real_files = [p for p in SYSTEM_NORDIC_CURSORS.iterdir() if p.is_file() and not p.is_symlink()]
    symlinks = [p for p in SYSTEM_NORDIC_CURSORS.iterdir() if p.is_symlink()]

    for p in real_files:
        process_xcursor_file(p, cursors_dir / p.name)

    # 4. Replicate all symlinks
    for p in symlinks:
        target = os.readlink(p)
        link_dest = cursors_dir / p.name
        if link_dest.exists():
            link_dest.unlink()
        link_dest.symlink_to(target)

    print(f"Generated {len(real_files)} authentic Nordic cursors + {len(symlinks)} symlinks in {OUT_DIR}")


if __name__ == "__main__":
    build_cursors()

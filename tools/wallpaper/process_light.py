# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Processes, enhances, and renders the 4K Light Suite wallpapers and 1080p previews.

import json
from pathlib import Path
from typing import Dict, List, Tuple
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

REPO_ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = REPO_ROOT / "wallpaper" / "raw_light"
DIST_LIGHT_DIR = REPO_ROOT / "wallpaper" / "dist" / "light"
PREVIEW_LIGHT_DIR = REPO_ROOT / "wallpaper" / "preview" / "light"
WIDTH, HEIGHT = 3840, 2160
PREVIEW_W, PREVIEW_H = 1920, 1080

TOKENS = json.loads((REPO_ROOT / "palette" / "tokens.json").read_text())
TECH_SLUG = TOKENS.get("meta", {}).get("tech_name", "mt-nordic-blue").lower()

WALLPAPERS = [
    {
        "id": "1",
        "raw": "1-canopy-dawn.jpg",
        "title": "Nordic Fjord Canopy Dawn (Morning Mist)",
        "file": f"{TECH_SLUG}-canopy-dawn-3840x2160.png",
        "preview": f"{TECH_SLUG}-canopy-dawn-1920x1080.jpg",
    },
    {
        "id": "2",
        "raw": "2-celestial-rift.jpg",
        "title": "Arctic Frost Celestial Rift Dawn",
        "file": f"{TECH_SLUG}-celestial-rift-3840x2160.png",
        "preview": f"{TECH_SLUG}-celestial-rift-1920x1080.jpg",
    },
    {
        "id": "3",
        "raw": "3-cosmic-dawn.jpg",
        "title": "Nordic Glacial Cosmic Dawn",
        "file": f"{TECH_SLUG}-cosmic-dawn-3840x2160.png",
        "preview": f"{TECH_SLUG}-cosmic-dawn-1920x1080.jpg",
    },
    {
        "id": "4",
        "raw": "4-botanical-horizon.jpg",
        "title": "Nordic Topographic Horizon Dawn",
        "file": f"{TECH_SLUG}-botanical-horizon-3840x2160.png",
        "preview": f"{TECH_SLUG}-botanical-horizon-1920x1080.jpg",
    },
]


def add_subtle_grain(image: Image.Image, seed: int = 20261028) -> Image.Image:
    # Adds subtle noise to prevent 4K gradient banding.
    rng = np.random.default_rng(seed)
    noise = rng.normal(0.0, 1.4, (HEIGHT, WIDTH, 1)).repeat(3, axis=2)
    data = np.clip(np.asarray(image, dtype=float) + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(data, "RGB")


def extract_dominant_colors(image: Image.Image, count: int = 8) -> List[str]:
    # Samples top dominant hex colors from resized image.
    thumb = image.resize((150, 150), Image.Resampling.BILINEAR)
    colors = thumb.getcolors(maxcolors=22500)
    if not colors:
        return []
    sorted_colors = sorted(colors, key=lambda x: x[0], reverse=True)
    hex_list = []
    for count_val, rgb in sorted_colors:
        if len(rgb) >= 3:
            r, g, b = rgb[:3]
            h = f"#{r:02x}{g:02x}{b:02x}"
            if h not in hex_list:
                hex_list.append(h)
        if len(hex_list) >= count:
            break
    return hex_list


def process_image(raw_path: Path, wp_info: Dict[str, str]) -> Dict:
    # Processes raw image: upscale to 4K, enhance, add grain, and save 4K + preview.
    print(f"Processing 4K: {wp_info['title']}...")
    img = Image.open(raw_path).convert("RGB")

    # Resize/crop to exactly 3840x2160
    if img.size != (WIDTH, HEIGHT):
        img = img.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)

    # Enhance clarity and color vibrance
    img = ImageEnhance.Color(img).enhance(1.08)
    img = ImageEnhance.Contrast(img).enhance(1.04)
    img = ImageEnhance.Sharpness(img).enhance(1.10)

    # Subtle film grain
    img = add_subtle_grain(img, seed=20261028 + int(wp_info["id"]))

    # Save 4K PNG
    out_4k_path = DIST_LIGHT_DIR / wp_info["file"]
    img.save(out_4k_path, format="PNG", optimize=True)

    # Save 1080p preview
    preview_img = img.resize((PREVIEW_W, PREVIEW_H), Image.Resampling.LANCZOS)
    out_preview_path = PREVIEW_LIGHT_DIR / wp_info["preview"]
    preview_img.save(out_preview_path, format="JPEG", quality=90, optimize=True)

    dominant = extract_dominant_colors(img)

    return {
        "id": wp_info["id"],
        "title": wp_info["title"],
        "file": wp_info["file"],
        "preview": wp_info["preview"],
        "resolution": f"{WIDTH}x{HEIGHT}",
        "dominant_colors": dominant,
    }


def main():
    # Orchestrates processing of all 4 light artworks and updates palette summary.
    DIST_LIGHT_DIR.mkdir(parents=True, exist_ok=True)
    PREVIEW_LIGHT_DIR.mkdir(parents=True, exist_ok=True)

    manifest = []
    for wp in WALLPAPERS:
        raw_path = RAW_DIR / wp["raw"]
        if not raw_path.exists():
            print(f"Warning: {raw_path} not found. Skipping.")
            continue
        meta = process_image(raw_path, wp)
        manifest.append(meta)

    summary_file = DIST_LIGHT_DIR / "palette-summary.json"
    summary_file.write_text(json.dumps(manifest, indent=2))

    # Also generate dynamic timed xml
    from generate_dynamic import main as gen_dyn
    gen_dyn()

    print(f"Done! Light suite generated at: {DIST_LIGHT_DIR}")


if __name__ == "__main__":
    main()

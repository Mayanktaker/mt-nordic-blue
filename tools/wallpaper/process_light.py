# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Procedural 4K Light Suite wallpaper generator for MT Nordic Blue.
# Generates 4 matching Scandinavian dawn / daylight 4K artworks and 1080p previews.

import json
import math
import random
import sys
from pathlib import Path
from typing import Dict, List

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

REPO_ROOT = Path(__file__).resolve().parents[2]
DIST_LIGHT_DIR = REPO_ROOT / "wallpaper" / "dist" / "light"
PREVIEW_LIGHT_DIR = REPO_ROOT / "wallpaper" / "preview" / "light"
WIDTH, HEIGHT = 3840, 2160
PREVIEW_W, PREVIEW_H = 1920, 1080

TOKENS = json.loads((REPO_ROOT / "palette" / "tokens.json").read_text())
COLOR = TOKENS["color"]
TECH_SLUG = TOKENS.get("meta", {}).get("tech_name", "mt-nordic-blue").lower()


def hex_to_rgb(hex_color: str, alpha: int = 255) -> tuple:
    # Convert #RRGGBB plus alpha into an RGBA tuple.
    r, g, b = (int(hex_color[i : i + 2], 16) for i in (1, 3, 5))
    return (r, g, b, alpha)


def radial_glow(size: tuple, center: tuple, radius: float, rgb: tuple, max_alpha: int) -> Image.Image:
    # Soft additive radial light as an RGBA layer.
    w, h = size
    yy, xx = np.mgrid[0:h, 0:w]
    dist = np.sqrt((xx - center[0]) ** 2 + (yy - center[1]) ** 2)
    falloff = np.clip(1.0 - dist / radius, 0.0, 1.0) ** 2.2
    alpha = (falloff * max_alpha).astype(np.uint8)
    layer = np.zeros((h, w, 4), dtype=np.uint8)
    layer[..., 0], layer[..., 1], layer[..., 2] = rgb
    layer[..., 3] = alpha
    return Image.fromarray(layer, "RGBA")


def vignette_light(intensity: int = 40) -> Image.Image:
    # Soft delicate edge darkening for light wallpapers.
    yy, xx = np.mgrid[0:HEIGHT, 0:WIDTH]
    dist = np.sqrt(((xx - WIDTH / 2) / (WIDTH / 2)) ** 2 + ((yy - HEIGHT / 2) / (HEIGHT / 2)) ** 2)
    alpha = (np.clip(dist - 0.60, 0.0, 1.0) * intensity).astype(np.uint8)
    layer = np.zeros((HEIGHT, WIDTH, 4), dtype=np.uint8)
    layer[..., 0], layer[..., 1], layer[..., 2] = (46, 52, 64)
    layer[..., 3] = alpha
    return Image.fromarray(layer, "RGBA")


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


# =========================================================================
# Light Wallpaper 1: Nordic Fjord & Glacial Peaks Dawn
# =========================================================================

def make_fractal_ridge_light(w: int, seed_val: int = 0, octaves: int = 7, lacunarity: float = 2.1, gain: float = 0.52) -> np.ndarray:
    # Continuous multi-octave fractional Brownian motion for daylight mountain relief
    r = np.random.default_rng(seed_val)
    x = np.linspace(0, 14, w)
    h = np.zeros(w, dtype=float)
    amp = 1.0
    freq = 1.0
    for _ in range(octaves):
        phase = r.uniform(0, 2 * math.pi)
        h += amp * (1.0 - np.abs(np.sin(freq * x + phase))) ** 2
        amp *= gain
        freq *= lacunarity
    return (h - h.min()) / (h.max() - h.min())


def generate_fjord_light(seed: int = 20261101) -> Image.Image:
    # Compose Light Wallpaper 1: Photorealistic Scandinavian Dawn Fjord & Alpine Glacial Ridges.
    rng = random.Random(seed)

    # 1. Sky gradient: Crisp Scandinavian dawn sky
    sky_top = np.array((216, 222, 233), dtype=float)  # #D8DEE9
    sky_bot = np.array((236, 239, 244), dtype=float)  # #ECEFF4
    t = np.linspace(0.0, 1.0, HEIGHT)[:, None, None]
    rows = sky_top * (1 - t) + sky_bot * t
    canvas = Image.fromarray(np.repeat(rows, WIDTH, axis=1).astype(np.uint8), "RGB").convert("RGBA")

    # 2. Morning sun / frost cyan glow
    cyan_rgb = hex_to_rgb(COLOR["accent"]["base"])[:3]
    canvas.alpha_composite(radial_glow((WIDTH, HEIGHT), (WIDTH * 0.74, HEIGHT * 0.24), WIDTH * 0.45, cyan_rgb, 36))

    # 3. Mountain Layer 1: Distant snow peaks
    r1 = make_fractal_ridge_light(WIDTH, seed_val=seed + 101, octaves=6)
    y1 = (HEIGHT * 0.62 - r1 * (HEIGHT * 0.22)).astype(int)
    m1 = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    d1 = ImageDraw.Draw(m1)
    pts1 = [(0, HEIGHT)] + [(x, int(y1[x])) for x in range(WIDTH)] + [(WIDTH, HEIGHT)]
    d1.polygon(pts1, fill=(216, 225, 238, 210))
    d1.line([(x, int(y1[x])) for x in range(WIDTH)], fill=hex_to_rgb(COLOR["accent"]["base"], 140), width=2)
    canvas.alpha_composite(m1)

    # Valley dawn mist
    mist = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    md = ImageDraw.Draw(mist)
    md.rectangle([(0, int(HEIGHT * 0.50)), (WIDTH, int(HEIGHT * 0.72))], fill=(240, 244, 250, 95))
    canvas.alpha_composite(mist.filter(ImageFilter.GaussianBlur(28)))

    # 4. Mountain Layer 2: Main alpine massif with snow slope shading
    r2 = make_fractal_ridge_light(WIDTH, seed_val=seed + 202, octaves=8)
    y2 = (HEIGHT * 0.72 - r2 * (HEIGHT * 0.36)).astype(int)
    dy2 = np.gradient(y2)
    slope_norm = np.clip((dy2 - dy2.min()) / (dy2.max() - dy2.min() + 1e-5), 0.0, 1.0)

    yy, xx = np.mgrid[0:HEIGHT, 0:WIDTH]
    mask2 = yy >= y2

    # Lit snow slopes (#FFFFFF), cool blue glacier shadows (#81A1C1 to #A3D4E2)
    col_r = 140.0 + slope_norm * 115.0
    col_g = 170.0 + slope_norm * 85.0
    col_b = 205.0 + slope_norm * 50.0

    # Pristine white summit caps
    depth = yy - y2
    summit_mask = mask2 & (depth < 30)
    col_r = np.where(summit_mask, 255.0 - depth * 1.5, col_r)
    col_g = np.where(summit_mask, 255.0 - depth * 1.5, col_g)
    col_b = np.where(summit_mask, 255.0 - depth * 1.0, col_b)

    m2_arr = np.zeros((HEIGHT, WIDTH, 4), dtype=np.uint8)
    m2_arr[..., 0] = np.where(mask2, np.clip(col_r, 0, 255), 0)
    m2_arr[..., 1] = np.where(mask2, np.clip(col_g, 0, 255), 0)
    m2_arr[..., 2] = np.where(mask2, np.clip(col_b, 0, 255), 0)
    m2_arr[..., 3] = np.where(mask2, 255, 0)
    canvas.alpha_composite(Image.fromarray(m2_arr, "RGBA"))

    # Frost Cyan ridge highlight
    crest_img = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    cd = ImageDraw.Draw(crest_img)
    cd.line([(x, int(y2[x])) for x in range(WIDTH)], fill=hex_to_rgb(COLOR["accent"]["base"], 220), width=3)
    canvas.alpha_composite(crest_img)

    # 5. Mountain Layer 3: Foreground coastal crags
    r3 = make_fractal_ridge_light(WIDTH, seed_val=seed + 303, octaves=7)
    y3 = (HEIGHT * 0.84 - r3 * (HEIGHT * 0.24)).astype(int)
    crag_mask = (xx < WIDTH * 0.36) | (xx > WIDTH * 0.64)
    mask3 = (yy >= y3) & crag_mask
    m3_arr = np.zeros((HEIGHT, WIDTH, 4), dtype=np.uint8)
    m3_arr[..., 0] = np.where(mask3, 59, 0)
    m3_arr[..., 1] = np.where(mask3, 66, 0)
    m3_arr[..., 2] = np.where(mask3, 82, 0)
    m3_arr[..., 3] = np.where(mask3, 245, 0)
    canvas.alpha_composite(Image.fromarray(m3_arr, "RGBA"))

    # 6. Fjord Glacial Meltwater
    water = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    water_y = int(HEIGHT * 0.78)
    h_water = HEIGHT - water_y
    water_top = np.array((163, 212, 226), dtype=float)  # #A3D4E2
    water_bot = np.array((216, 222, 233), dtype=float)  # #D8DEE9
    tw = np.linspace(0.0, 1.0, h_water)[:, None, None]
    w_rows = water_top * (1 - tw) + water_bot * tw
    water_surf = Image.fromarray(np.repeat(w_rows, WIDTH, axis=1).astype(np.uint8), "RGB").convert("RGBA")

    # Water ripples
    wd_surf = ImageDraw.Draw(water_surf)
    for idx in range(24):
        ry = int(h_water * (0.06 + (idx / 24.0) * 0.88))
        rw = rng.uniform(WIDTH * 0.25, WIDTH * 0.85)
        rx = rng.uniform(WIDTH * 0.08, WIDTH * 0.92 - rw)
        wd_surf.line([(rx, ry), (rx + rw, ry)], fill=(255, 255, 255, 140), width=max(1, int(2.5 * (1 - idx / 24.0))))

    water.paste(water_surf, (0, water_y))
    canvas.alpha_composite(water)
    canvas.alpha_composite(vignette_light(40))
    return add_subtle_grain(canvas.convert("RGB"), seed)


# =========================================================================
# Light Wallpaper 2: Radiant Aurora Daylight Rift
# =========================================================================

def generate_aurora_light(seed: int = 20261102) -> Image.Image:
    # Compose Light Wallpaper 2: Arctic Frost Celestial Rift Dawn.
    rng = random.Random(seed)

    sky_top = np.array((229, 233, 240), dtype=float)  # #E5E9F0
    sky_bot = np.array((240, 244, 248), dtype=float)
    t = np.linspace(0.0, 1.0, HEIGHT)[:, None, None]
    rows = sky_top * (1 - t) + sky_bot * t
    canvas = Image.fromarray(np.repeat(rows, WIDTH, axis=1).astype(np.uint8), "RGB").convert("RGBA")

    # Luminous auroral curtains in sky
    aurora = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    ad = ImageDraw.Draw(aurora)
    pts1 = []
    for x in range(0, WIDTH + 30, 20):
        y = HEIGHT * 0.38 + math.sin(x * 0.0015) * 150 + math.cos(x * 0.0028) * 90
        pts1.append((x, y))
    for p in pts1:
        ad.line([(p[0], p[1] - 200), (p[0], p[1] + 140)], fill=hex_to_rgb(COLOR["accent"]["base"], 65), width=36)
        ad.line([(p[0], p[1] - 100), (p[0], p[1] + 60)], fill=hex_to_rgb(COLOR["accent_flavors"]["glacier"], 90), width=20)

    canvas.alpha_composite(aurora.filter(ImageFilter.GaussianBlur(26)))

    # Arctic mountain range silhouette
    m_sil = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    md = ImageDraw.Draw(m_sil)
    base_m = HEIGHT * 0.88
    ridge_pts = [(0, HEIGHT), (0, base_m)]
    cur_x = 0
    while cur_x < WIDTH:
        step = rng.uniform(80, 220)
        h_offset = rng.uniform(120, 360)
        cur_x += step
        ridge_pts.append((cur_x, base_m - h_offset))
    ridge_pts.append((WIDTH, HEIGHT))
    md.polygon(ridge_pts, fill=(76, 86, 106, 240))
    edge_pts = [(pt[0], pt[1]) for pt in ridge_pts[1:-1]]
    md.line(edge_pts, fill=hex_to_rgb(COLOR["accent"]["base"], 220), width=3)
    canvas.alpha_composite(m_sil)

    canvas.alpha_composite(vignette_light(40))
    return add_subtle_grain(canvas.convert("RGB"), seed)


# =========================================================================
# Light Wallpaper 3: Glacial Flow & Topographic Contours Dawn
# =========================================================================

def generate_topographic_light(seed: int = 20261103) -> Image.Image:
    # Compose Light Wallpaper 3: Nordic Glacial Cosmic Dawn (Topographic).
    top = np.array((244, 246, 249), dtype=float)
    bottom = np.array((229, 233, 240), dtype=float)
    t = np.linspace(0.0, 1.0, HEIGHT)[:, None, None]
    rows = top * (1 - t) + bottom * t
    canvas = Image.fromarray(np.repeat(rows, WIDTH, axis=1).astype(np.uint8), "RGB").convert("RGBA")

    # Ambient halo
    canvas.alpha_composite(radial_glow((WIDTH, HEIGHT), (WIDTH * 0.55, HEIGHT * 0.50), WIDTH * 0.48, hex_to_rgb(COLOR["accent"]["base"])[:3], 32))

    contours = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    cd = ImageDraw.Draw(contours)

    num_isolines = 30
    glowing_rivers = {7, 15, 23}
    river_points = {}

    for idx in range(num_isolines):
        base_y = HEIGHT * 0.08 + (idx / float(num_isolines)) * (HEIGHT * 0.94)
        phase = idx * 0.28
        freq = 0.0011 + (idx % 4) * 0.0002
        amp = 95 + math.sin(idx * 0.45) * 55

        pts = []
        for x in range(0, WIDTH + 25, 20):
            y = base_y + math.sin(x * freq + phase) * amp + math.cos(x * 0.0006 - phase * 0.5) * 45
            pts.append((x, y))

        if idx in glowing_rivers:
            river_points[idx] = pts
        else:
            cd.line(pts, fill=(180, 190, 205, 110), width=2)

    glow_layer = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow_layer)
    for idx, pts in river_points.items():
        gd.line(pts, fill=hex_to_rgb(COLOR["accent"]["base"], 90), width=20)
    glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(14))
    canvas.alpha_composite(glow_layer)

    for idx, pts in river_points.items():
        cd.line(pts, fill=hex_to_rgb(COLOR["accent"]["dim"], 220), width=4)
        cd.line(pts, fill=hex_to_rgb(COLOR["accent"]["base"], 240), width=2)

    canvas.alpha_composite(contours)
    canvas.alpha_composite(vignette_light(40))
    return add_subtle_grain(canvas.convert("RGB"), seed)


# =========================================================================
# Light Wallpaper 4: Nordic Cyber Horizon Dawn
# =========================================================================

def generate_cyber_light(seed: int = 20261104) -> Image.Image:
    # Compose Light Wallpaper 4: Nordic Topographic Horizon Dawn (Cyber Grid).
    sky_top = np.array((236, 239, 244), dtype=float)
    sky_bot = np.array((245, 248, 252), dtype=float)
    t = np.linspace(0.0, 1.0, HEIGHT)[:, None, None]
    rows = sky_top * (1 - t) + sky_bot * t
    canvas = Image.fromarray(np.repeat(rows, WIDTH, axis=1).astype(np.uint8), "RGB").convert("RGBA")

    grid_layer = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grid_layer)
    horizon_y = HEIGHT * 0.62
    vp_x = WIDTH / 2

    num_rays = 36
    for i in range(num_rays + 1):
        bottom_x = (i / float(num_rays)) * (WIDTH * 1.6) - (WIDTH * 0.3)
        gd.line([(vp_x, horizon_y), (bottom_x, HEIGHT)], fill=(180, 195, 215, 90), width=2)

    num_horiz = 22
    for j in range(num_horiz):
        factor = (j / float(num_horiz)) ** 2.2
        y = horizon_y + factor * (HEIGHT - horizon_y)
        alpha = int(40 + factor * 120)
        gd.line([(0, y), (WIDTH, y)], fill=hex_to_rgb(COLOR["accent"]["dim"], alpha), width=max(1, int(factor * 3)))

    canvas.alpha_composite(grid_layer)

    beam = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    bd = ImageDraw.Draw(beam)
    bd.line([(0, horizon_y), (WIDTH, horizon_y)], fill=hex_to_rgb(COLOR["accent"]["base"], 180), width=5)
    beam_blur = beam.filter(ImageFilter.GaussianBlur(10))
    canvas.alpha_composite(beam_blur)
    canvas.alpha_composite(beam)

    monoliths = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    md = ImageDraw.Draw(monoliths)
    monolith_data = [
        (WIDTH * 0.22, horizon_y, 160, 420),
        (WIDTH * 0.38, horizon_y, 120, 310),
        (WIDTH * 0.50, horizon_y, 220, 560),
        (WIDTH * 0.64, horizon_y, 140, 380),
        (WIDTH * 0.80, horizon_y, 180, 460),
    ]
    for mx, my, mw, mh in monolith_data:
        tip = (mx, my - mh)
        left_bot = (mx - mw / 2, my)
        right_bot = (mx + mw / 2, my)
        mid_bot = (mx, my + mh * 0.08)
        md.polygon([tip, left_bot, mid_bot], fill=(255, 255, 255, 240))
        md.polygon([tip, mid_bot, right_bot], fill=(216, 222, 233, 240))
        md.line([left_bot, tip, right_bot], fill=hex_to_rgb(COLOR["accent"]["base"], 210), width=3)
        md.line([tip, mid_bot], fill=hex_to_rgb(COLOR["accent"]["dim"], 220), width=2)

    canvas.alpha_composite(monoliths)
    canvas.alpha_composite(vignette_light(40))
    return add_subtle_grain(canvas.convert("RGB"), seed)


# =========================================================================
# Light Suite Manifest & CLI
# =========================================================================

LIGHT_WALLPAPERS = [
    {
        "id": "1",
        "title": "Nordic Fjord Canopy Dawn (Morning Mist)",
        "file": f"{TECH_SLUG}-canopy-dawn-3840x2160.png",
        "preview": f"{TECH_SLUG}-canopy-dawn-1920x1080.jpg",
        "fn": generate_fjord_light,
    },
    {
        "id": "2",
        "title": "Arctic Frost Celestial Rift Dawn",
        "file": f"{TECH_SLUG}-celestial-rift-3840x2160.png",
        "preview": f"{TECH_SLUG}-celestial-rift-1920x1080.jpg",
        "fn": generate_aurora_light,
    },
    {
        "id": "3",
        "title": "Nordic Glacial Cosmic Dawn",
        "file": f"{TECH_SLUG}-cosmic-dawn-3840x2160.png",
        "preview": f"{TECH_SLUG}-cosmic-dawn-1920x1080.jpg",
        "fn": generate_topographic_light,
    },
    {
        "id": "4",
        "title": "Nordic Topographic Horizon Dawn",
        "file": f"{TECH_SLUG}-botanical-horizon-3840x2160.png",
        "preview": f"{TECH_SLUG}-botanical-horizon-1920x1080.jpg",
        "fn": generate_cyber_light,
    },
]


def main():
    # Orchestrate procedural rendering of the 4K Light Suite and dynamic XML generation.
    DIST_LIGHT_DIR.mkdir(parents=True, exist_ok=True)
    PREVIEW_LIGHT_DIR.mkdir(parents=True, exist_ok=True)

    manifest = []
    for wp in LIGHT_WALLPAPERS:
        print(f"Generating Light 4K Wallpaper {wp['id']}: {wp['title']}...")
        img = wp["fn"]()

        out_4k = DIST_LIGHT_DIR / wp["file"]
        img.save(out_4k, format="PNG", optimize=True)

        preview_img = img.resize((PREVIEW_W, PREVIEW_H), Image.Resampling.LANCZOS)
        out_prev = PREVIEW_LIGHT_DIR / wp["preview"]
        preview_img.save(out_prev, format="JPEG", quality=90, optimize=True)

        dominant = extract_dominant_colors(img)
        manifest.append({
            "id": wp["id"],
            "title": wp["title"],
            "file": wp["file"],
            "preview": wp["preview"],
            "resolution": f"{WIDTH}x{HEIGHT}",
            "dominant_colors": dominant,
        })
        print(f"  ✓ Saved 4K: {out_4k.name}")
        print(f"  ✓ Saved Preview: {out_prev.name}")

    summary_file = DIST_LIGHT_DIR / "palette-summary.json"
    summary_file.write_text(json.dumps(manifest, indent=2))

    # Trigger dynamic timed XML generation
    from generate_dynamic import main as gen_dyn
    gen_dyn()
    print(f"\nAll light wallpapers generated successfully at: {DIST_LIGHT_DIR}")


if __name__ == "__main__":
    main()

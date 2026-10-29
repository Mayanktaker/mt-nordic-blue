# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Procedural 4K wallpaper suite generator for MT Nordic Blue.
# Deterministic: pinned seeds, colors strictly derived from palette/tokens.json.
# Generates 4 distinct 4K artworks: Fjord Peaks, Radiant Aurora, Topographic Flow, Cyber Horizon.

import argparse
import json
import math
import random
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

REPO_ROOT = Path(__file__).resolve().parents[2]
TOKENS = json.loads((REPO_ROOT / "palette" / "tokens.json").read_text())
COLOR = TOKENS["color"]
WIDTH, HEIGHT = 3840, 2160


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


def vignette(intensity: int = 80) -> Image.Image:
    # Edge darkening to focus composition and lift panel legibility.
    yy, xx = np.mgrid[0:HEIGHT, 0:WIDTH]
    dist = np.sqrt(((xx - WIDTH / 2) / (WIDTH / 2)) ** 2 + ((yy - HEIGHT / 2) / (HEIGHT / 2)) ** 2)
    alpha = (np.clip(dist - 0.55, 0.0, 1.0) * intensity).astype(np.uint8)
    layer = np.zeros((HEIGHT, WIDTH, 4), dtype=np.uint8)
    layer[..., 3] = alpha
    return Image.fromarray(layer, "RGBA")


def add_grain(image: Image.Image, seed: int = 20261027) -> Image.Image:
    # Subtle film grain to prevent banding on 4K gradients.
    rng = np.random.default_rng(seed)
    noise = rng.normal(0.0, 2.0, (HEIGHT, WIDTH, 1)).repeat(3, axis=2)
    data = np.clip(np.asarray(image, dtype=float) + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(data, "RGB")


# =========================================================================
# Wallpaper 1: Nordic Fjord & Glacial Peaks (Art 1)
# =========================================================================

def draw_starfield(draw: ImageDraw.ImageDraw, rng: random.Random, count: int, max_y: float) -> None:
    # Draw deterministic crystal stars with varying magnitudes and glow.
    primary_text = hex_to_rgb(COLOR["text"]["primary"])[:3]
    frost = hex_to_rgb(COLOR["accent"]["base"])[:3]
    for _ in range(count):
        sx = rng.uniform(0, WIDTH)
        sy = rng.uniform(0, max_y)
        sr = rng.uniform(0.8, 2.6)
        alpha = int(rng.uniform(60, 240))
        col = primary_text if rng.random() > 0.3 else frost
        draw.ellipse([(sx - sr, sy - sr), (sx + sr, sy + sr)], fill=(col[0], col[1], col[2], alpha))
        if sr > 2.2 and rng.random() > 0.6:
            # Diamond diffraction spikes on bright navigational stars
            spike = sr * 3.5
            draw.line([(sx - spike, sy), (sx + spike, sy)], fill=(col[0], col[1], col[2], int(alpha * 0.7)), width=1)
            draw.line([(sx, sy - spike), (sx, sy + spike)], fill=(col[0], col[1], col[2], int(alpha * 0.7)), width=1)


def make_fractal_ridge(w: int, seed_val: int = 0, octaves: int = 7, lacunarity: float = 2.1, gain: float = 0.52) -> np.ndarray:
    # Continuous multi-octave fractional Brownian motion with harmonic ridge folding
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


def generate_fjord(seed: int = 20261027) -> Image.Image:
    # Compose Wallpaper 1: Photorealistic Cinematic Nordic Fjord & Alpine Glacial Ridges.
    rng = random.Random(seed)

    # 1. Sky gradient: Non-linear atmospheric polar twilight (OLED space navy to horizon cyan)
    sky_top = np.array(hex_to_rgb(COLOR["bg"]["oled"])[:3], dtype=float)       # #040609
    sky_bot = np.array(hex_to_rgb(COLOR["bg"]["tile"])[:3], dtype=float)       # #151D2A
    t = np.linspace(0.0, 1.0, HEIGHT)[:, None, None]
    rows = sky_top * (1 - t**1.3) + sky_bot * (t**1.3)
    canvas = Image.fromarray(np.repeat(rows, WIDTH, axis=1).astype(np.uint8), "RGB").convert("RGBA")

    # 2. Polar celestial moon glow & ambient atmospheric wash
    cyan_rgb = hex_to_rgb(COLOR["accent_flavors"]["cyber"])[:3]
    frost_rgb = hex_to_rgb(COLOR["accent"]["base"])[:3]
    canvas.alpha_composite(radial_glow((WIDTH, HEIGHT), (WIDTH * 0.76, HEIGHT * 0.22), WIDTH * 0.42, cyan_rgb, 36))
    canvas.alpha_composite(radial_glow((WIDTH, HEIGHT), (WIDTH * 0.28, HEIGHT * 0.35), WIDTH * 0.48, frost_rgb, 26))

    # 3. Crystal starfield
    stars = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw_starfield(ImageDraw.Draw(stars), rng, count=320, max_y=HEIGHT * 0.62)
    canvas.alpha_composite(stars)

    # 4. Ethereal aurora haze curtain behind distant peaks
    aurora_haze = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    ahd = ImageDraw.Draw(aurora_haze)
    for x in range(0, WIDTH + 40, 30):
        y_aurora = HEIGHT * 0.42 + math.sin(x * 0.0016) * 140 + math.cos(x * 0.0031) * 70
        ahd.line([(x, y_aurora - 240), (x, y_aurora + 100)], fill=hex_to_rgb(COLOR["accent_flavors"]["cyber"], 34), width=48)
        ahd.line([(x, y_aurora - 140), (x, y_aurora + 50)], fill=hex_to_rgb(COLOR["accent_flavors"]["aurora"], 50), width=30)
    canvas.alpha_composite(aurora_haze.filter(ImageFilter.GaussianBlur(32)))

    # 5. Mountain Layer 1: Distant misty glacial peaks (fractal fBm ridge)
    r1 = make_fractal_ridge(WIDTH, seed_val=seed + 101, octaves=6)
    y1 = (HEIGHT * 0.60 - r1 * (HEIGHT * 0.22)).astype(int)
    m1 = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    d1 = ImageDraw.Draw(m1)
    pts1 = [(0, HEIGHT)] + [(x, int(y1[x])) for x in range(WIDTH)] + [(WIDTH, HEIGHT)]
    d1.polygon(pts1, fill=hex_to_rgb(COLOR["bg"]["raised"], 210))
    d1.line([(x, int(y1[x])) for x in range(WIDTH)], fill=hex_to_rgb(COLOR["accent"]["dim"], 160), width=2)
    canvas.alpha_composite(m1)

    # Atmospheric valley mist between distant and midground ranges
    valley_mist = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    vmd = ImageDraw.Draw(valley_mist)
    vmd.rectangle([(0, int(HEIGHT * 0.50)), (WIDTH, int(HEIGHT * 0.72))], fill=hex_to_rgb(COLOR["bg"]["tile"], 85))
    canvas.alpha_composite(valley_mist.filter(ImageFilter.GaussianBlur(28)))

    # 6. Mountain Layer 2: Main alpine glacial massif with slope shading & snow crests
    r2 = make_fractal_ridge(WIDTH, seed_val=seed + 202, octaves=8)
    y2 = (HEIGHT * 0.72 - r2 * (HEIGHT * 0.36)).astype(int)
    dy2 = np.gradient(y2)
    slope_norm = np.clip((dy2 - dy2.min()) / (dy2.max() - dy2.min() + 1e-5), 0.0, 1.0)

    yy, xx = np.mgrid[0:HEIGHT, 0:WIDTH]
    mask2 = yy >= y2

    # Lit faces receive Nordic Glacier Slate (#2A3A52), shadow couloirs receive Deep Polar Night (#0E141D)
    col_r = 14.0 + slope_norm * 36.0
    col_g = 20.0 + slope_norm * 48.0
    col_b = 29.0 + slope_norm * 64.0

    # Snow caps along upper ridges
    depth = yy - y2
    snow_mask = mask2 & (depth < 30)
    col_r = np.where(snow_mask, 236.0 - depth * 2.8, col_r)
    col_g = np.where(snow_mask, 239.0 - depth * 2.6, col_g)
    col_b = np.where(snow_mask, 244.0 - depth * 2.4, col_b)

    m2_arr = np.zeros((HEIGHT, WIDTH, 4), dtype=np.uint8)
    m2_arr[..., 0] = np.where(mask2, np.clip(col_r, 0, 255), 0)
    m2_arr[..., 1] = np.where(mask2, np.clip(col_g, 0, 255), 0)
    m2_arr[..., 2] = np.where(mask2, np.clip(col_b, 0, 255), 0)
    m2_arr[..., 3] = np.where(mask2, 255, 0)
    canvas.alpha_composite(Image.fromarray(m2_arr, "RGBA"))

    # Sharp specular frost cyan highlight along crest
    crest_img = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    cd = ImageDraw.Draw(crest_img)
    cd.line([(x, int(y2[x])) for x in range(WIDTH)], fill=hex_to_rgb(COLOR["accent"]["base"], 220), width=3)
    canvas.alpha_composite(crest_img)

    # 7. Mountain Layer 3: Foreground coastal fjord crags framing the left & right
    r3 = make_fractal_ridge(WIDTH, seed_val=seed + 303, octaves=7)
    y3 = (HEIGHT * 0.84 - r3 * (HEIGHT * 0.24)).astype(int)
    crag_mask = (xx < WIDTH * 0.36) | (xx > WIDTH * 0.64)
    mask3 = (yy >= y3) & crag_mask
    m3_arr = np.zeros((HEIGHT, WIDTH, 4), dtype=np.uint8)
    m3_arr[..., 0] = np.where(mask3, 9, 0)
    m3_arr[..., 1] = np.where(mask3, 13, 0)
    m3_arr[..., 2] = np.where(mask3, 20, 0)
    m3_arr[..., 3] = np.where(mask3, 255, 0)
    canvas.alpha_composite(Image.fromarray(m3_arr, "RGBA"))

    # 8. Fjord Glacial Water: Lower 22% with calm reflection sheen & ice ripples
    water_y = int(HEIGHT * 0.78)
    water_h = HEIGHT - water_y
    water = Image.new("RGBA", (WIDTH, water_h), (9, 13, 20, 255))
    water.alpha_composite(radial_glow((WIDTH, water_h), (WIDTH * 0.50, water_h * 0.18), WIDTH * 0.42, frost_rgb, 35))

    # Crystalline horizontal ice ripples across fjord
    wd_surf = ImageDraw.Draw(water)
    for idx in range(36):
        ry = int(water_h * (0.06 + (idx / 36.0) * 0.88))
        rw = rng.uniform(WIDTH * 0.25, WIDTH * 0.85)
        rx = rng.uniform(WIDTH * 0.08, WIDTH * 0.92 - rw)
        alpha = int(22 + (36 - idx) * 3)
        wd_surf.line([(rx, ry), (rx + rw, ry)], fill=hex_to_rgb(COLOR["accent"]["base"], alpha), width=max(1, int(3.0 * (1 - idx / 36.0))))

    canvas.paste(water, (0, water_y))

    # Vignette and grain
    canvas.alpha_composite(vignette(75))
    return add_grain(canvas.convert("RGB"), seed)


# =========================================================================
# Wallpaper 2: Radiant Aurora Borealis (Art 2)
# =========================================================================

def generate_aurora(seed: int = 20261028) -> Image.Image:
    # Compose Wallpaper 2: Radiant Aurora Borealis.
    rng = random.Random(seed)

    # Sky gradient: OLED dark space into arctic night
    sky_top = np.array(hex_to_rgb(COLOR["bg"]["oled"])[:3], dtype=float)
    sky_bot = np.array(hex_to_rgb(COLOR["bg"]["base_darker"])[:3], dtype=float)
    t = np.linspace(0.0, 1.0, HEIGHT)[:, None, None]
    rows = sky_top * (1 - t) + sky_bot * t
    canvas = Image.fromarray(np.repeat(rows, WIDTH, axis=1).astype(np.uint8), "RGB").convert("RGBA")

    # Starfield
    stars = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw_starfield(ImageDraw.Draw(stars), rng, count=360, max_y=HEIGHT * 0.75)
    canvas.alpha_composite(stars)

    # Aurora Curtain 1: Flowing Electric Cyber Cyan wave
    aurora1 = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    ad1 = ImageDraw.Draw(aurora1)
    pts1 = []
    for x in range(0, WIDTH + 30, 20):
        y = HEIGHT * 0.36 + math.sin(x * 0.0015) * 150 + math.cos(x * 0.0028) * 90 + math.sin(x * 0.0007) * 80
        pts1.append((x, y))
    for p in pts1:
        # Vertical ray curtains creating true undulating folds
        ad1.line([(p[0], p[1] - 220), (p[0], p[1] + 160)], fill=hex_to_rgb(COLOR["accent_flavors"]["cyber"], 52), width=36)
        ad1.line([(p[0], p[1] - 120), (p[0], p[1] + 80)], fill=hex_to_rgb(COLOR["accent"]["base"], 75), width=22)
        ad1.line([(p[0], p[1] - 40), (p[0], p[1] + 20)], fill=hex_to_rgb(COLOR["text"]["primary"], 90), width=8)

    canvas.alpha_composite(aurora1.filter(ImageFilter.GaussianBlur(24)))

    # Aurora Curtain 2: Arctic Aurora Teal harmonic counter-wave
    aurora2 = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    ad2 = ImageDraw.Draw(aurora2)
    pts2 = []
    for x in range(0, WIDTH + 30, 20):
        y = HEIGHT * 0.28 + math.cos(x * 0.0018 + 1.4) * 130 + math.sin(x * 0.0032) * 70
        pts2.append((x, y))
    for p in pts2:
        ad2.line([(p[0], p[1] - 180), (p[0], p[1] + 110)], fill=hex_to_rgb(COLOR["accent_flavors"]["aurora"], 44), width=32)
        ad2.line([(p[0], p[1] - 70), (p[0], p[1] + 40)], fill=hex_to_rgb(COLOR["accent_flavors"]["glacier"], 62), width=18)

    canvas.alpha_composite(aurora2.filter(ImageFilter.GaussianBlur(20)))

    # Aurora Ribbon 3: Deep Glacial Blue atmospheric wash
    aurora3 = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    ad3 = ImageDraw.Draw(aurora3)
    pts3 = []
    for x in range(0, WIDTH + 40, 30):
        y = HEIGHT * 0.48 + math.sin(x * 0.0012 + 2.5) * 160 + math.cos(x * 0.0022) * 80
        pts3.append((x, y))
    for p in pts3:
        ad3.line([(p[0], p[1] - 160), (p[0], p[1] + 140)], fill=hex_to_rgb(COLOR["accent"]["dim"], 38), width=48)

    canvas.alpha_composite(aurora3.filter(ImageFilter.GaussianBlur(32)))

    # Arctic mountain range silhouette at horizon
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
    md.polygon(ridge_pts, fill=hex_to_rgb(COLOR["bg"]["base_darker"], 255))
    # Glowing edge backlight from aurora reflection
    edge_pts = [(pt[0], pt[1]) for pt in ridge_pts[1:-1]]
    md.line(edge_pts, fill=hex_to_rgb(COLOR["accent_flavors"]["cyber"], 120), width=3)
    canvas.alpha_composite(m_sil)

    canvas.alpha_composite(vignette(80))
    return add_grain(canvas.convert("RGB"), seed)


# =========================================================================
# Wallpaper 3: Glacial Flow & Topographic Contours (Art 3)
# =========================================================================

def generate_topographic(seed: int = 20261029) -> Image.Image:
    # Compose Wallpaper 3: Glacial Flow & Topographic Contours.
    rng = random.Random(seed)

    # Base gradient: Polar Night into rich Nordic tile
    top = np.array(hex_to_rgb(COLOR["bg"]["base_darker"])[:3], dtype=float)
    bottom = np.array(hex_to_rgb(COLOR["bg"]["tile"])[:3], dtype=float)
    t = np.linspace(0.0, 1.0, HEIGHT)[:, None, None]
    rows = top * (1 - t) + bottom * t
    canvas = Image.fromarray(np.repeat(rows, WIDTH, axis=1).astype(np.uint8), "RGB").convert("RGBA")

    # Radial ambient halo
    canvas.alpha_composite(radial_glow((WIDTH, HEIGHT), (WIDTH * 0.55, HEIGHT * 0.52), WIDTH * 0.48, hex_to_rgb(COLOR["accent"]["base"])[:3], 32))

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
            # Subtle elevation contour isolines
            color = hex_to_rgb(COLOR["border"]["default"], 75)
            cd.line(pts, fill=color, width=2)

    # Multi-pass glow for arterial glacial river veins
    glow_layer = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow_layer)
    for idx, pts in river_points.items():
        # Wide ethereal bloom
        gd.line(pts, fill=hex_to_rgb(COLOR["accent_flavors"]["cyber"], 60), width=24)
        # Medium glow
        gd.line(pts, fill=hex_to_rgb(COLOR["accent"]["base"], 140), width=10)
    glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(16))
    canvas.alpha_composite(glow_layer)

    # Crisp sharp core for river veins
    for idx, pts in river_points.items():
        cd.line(pts, fill=hex_to_rgb(COLOR["text"]["primary"], 230), width=3)
        cd.line(pts, fill=hex_to_rgb(COLOR["accent"]["strong"], 180), width=5)

    canvas.alpha_composite(contours)
    canvas.alpha_composite(vignette(85))
    return add_grain(canvas.convert("RGB"), seed)


# =========================================================================
# Wallpaper 4: Nordic Cyber Horizon & Crystal Monoliths (Art 4)
# =========================================================================

def generate_cyber_grid(seed: int = 20261030) -> Image.Image:
    # Compose Wallpaper 4: Nordic Cyber Horizon & Ice Monoliths.
    rng = random.Random(seed)

    # Deep space OLED zenith to dark polar horizon
    sky_top = np.array(hex_to_rgb(COLOR["bg"]["oled"])[:3], dtype=float)
    sky_bot = np.array(hex_to_rgb(COLOR["bg"]["base"])[:3], dtype=float)
    t = np.linspace(0.0, 1.0, HEIGHT)[:, None, None]
    rows = sky_top * (1 - t) + sky_bot * t
    canvas = Image.fromarray(np.repeat(rows, WIDTH, axis=1).astype(np.uint8), "RGB").convert("RGBA")

    # Starfield
    stars = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw_starfield(ImageDraw.Draw(stars), rng, count=240, max_y=HEIGHT * 0.60)
    canvas.alpha_composite(stars)

    # Perspective Ground Grid
    grid_layer = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grid_layer)
    horizon_y = HEIGHT * 0.62
    vp_x = WIDTH / 2

    # Longitudinal perspective rays
    num_rays = 36
    for i in range(num_rays + 1):
        bottom_x = (i / float(num_rays)) * (WIDTH * 1.6) - (WIDTH * 0.3)
        gd.line([(vp_x, horizon_y), (bottom_x, HEIGHT)], fill=hex_to_rgb(COLOR["bg"]["surface"], 90), width=2)

    # Transverse perspective grid lines with exponential foreshortening
    num_horiz = 22
    for j in range(num_horiz):
        factor = (j / float(num_horiz)) ** 2.2
        y = horizon_y + factor * (HEIGHT - horizon_y)
        alpha = int(40 + factor * 110)
        gd.line([(0, y), (WIDTH, y)], fill=hex_to_rgb(COLOR["accent"]["dim"], alpha), width=max(1, int(factor * 3)))

    canvas.alpha_composite(grid_layer)

    # Glowing Cyan Horizon Beam
    beam = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    bd = ImageDraw.Draw(beam)
    bd.line([(0, horizon_y), (WIDTH, horizon_y)], fill=hex_to_rgb(COLOR["accent_flavors"]["cyber"], 200), width=6)
    bd.line([(0, horizon_y), (WIDTH, horizon_y)], fill=hex_to_rgb(COLOR["text"]["primary"], 240), width=2)
    beam_blur = beam.filter(ImageFilter.GaussianBlur(12))
    canvas.alpha_composite(beam_blur)
    canvas.alpha_composite(beam)

    # Crystalline Ice Monoliths along the horizon
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
        # Left facet
        md.polygon([tip, left_bot, mid_bot], fill=hex_to_rgb(COLOR["bg"]["surface"], 235))
        # Right facet
        md.polygon([tip, mid_bot, right_bot], fill=hex_to_rgb(COLOR["bg"]["tile"], 245))
        # Wireframe cyber edge highlights
        md.line([left_bot, tip, right_bot], fill=hex_to_rgb(COLOR["accent_flavors"]["cyber"], 210), width=3)
        md.line([tip, mid_bot], fill=hex_to_rgb(COLOR["accent"]["base"], 240), width=2)

    canvas.alpha_composite(monoliths)
    canvas.alpha_composite(vignette(80))
    return add_grain(canvas.convert("RGB"), seed)


# =========================================================================
# CLI and Output Orchestration
# =========================================================================

TECH_SLUG = TOKENS.get("meta", {}).get("tech_name", "mt-nordic-blue").lower()

WALLPAPER_META = {
    "1": (f"{TECH_SLUG}-art-1", "Nordic Fjord & Glacial Peaks (Art 1)", generate_fjord),
    "2": (f"{TECH_SLUG}-art-2", "Radiant Aurora Borealis (Art 2)", generate_aurora),
    "3": (f"{TECH_SLUG}-art-3", "Glacial Flow & Topographic Contours (Art 3)", generate_topographic),
    "4": (f"{TECH_SLUG}-art-4", "Nordic Cyber Horizon (Art 4)", generate_cyber_grid),
}


def dominant_palette(image: Image.Image, count: int = 8) -> list:
    # Report dominant colors so docs and packaging can show sampled palette.
    small = image.convert("RGB").resize((160, 90))
    quantized = small.quantize(colors=count, method=Image.Quantize.MEDIANCUT).convert("RGB")
    counts = sorted(quantized.getcolors(160 * 90) or [], reverse=True)
    return [f"#{r:02x}{g:02x}{b:02x}" for _, (r, g, b) in counts]


def main() -> None:
    # Generate requested wallpapers (1-4 or all).
    parser = argparse.ArgumentParser(description="Generate 4K procedural wallpapers for MT Nordic Blue")
    parser.add_argument("--which", default="all", choices=["1", "2", "3", "4", "all"], help="Which wallpaper to generate")
    args = parser.parse_args()

    dist = REPO_ROOT / "wallpaper" / "dist"
    preview = REPO_ROOT / "wallpaper" / "preview"
    dist.mkdir(parents=True, exist_ok=True)
    preview.mkdir(parents=True, exist_ok=True)

    targets = list(WALLPAPER_META.keys()) if args.which == "all" else [args.which]
    summaries = {}

    for key in targets:
        name_prefix, title, generator_fn = WALLPAPER_META[key]
        print(f"Generating Wallpaper {key}: {title} (4K 3840x2160)...")
        img = generator_fn()

        png_path = dist / f"{name_prefix}-3840x2160.png"
        img.save(png_path, optimize=True)

        jpg_path = preview / f"{name_prefix}-1920x1080.jpg"
        img.resize((1920, 1080), Image.Resampling.LANCZOS).save(jpg_path, quality=88, optimize=True)

        if key == "1":
            compat_png = dist / f"{TECH_SLUG}-3840x2160.png"
            compat_jpg = preview / f"{TECH_SLUG}-1920x1080.jpg"
            img.save(compat_png, optimize=True)
            img.resize((1920, 1080), Image.Resampling.LANCZOS).save(compat_jpg, quality=88, optimize=True)

        summaries[key] = {
            "title": title,
            "file": f"{name_prefix}-3840x2160.png",
            "preview": f"{name_prefix}-1920x1080.jpg",
            "dominant": dominant_palette(img),
        }
        print(f"  ✓ Saved 4K: {png_path.name}")
        print(f"  ✓ Saved Preview: {jpg_path.name}")

    summary_file = dist / "palette-summary.json"
    summary_file.write_text(json.dumps(summaries, indent=2))
    print(f"\nAll dark wallpapers generated successfully. Summary at {summary_file}")


if __name__ == "__main__":
    main()

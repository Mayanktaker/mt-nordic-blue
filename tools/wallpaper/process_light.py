# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Procedural 4K Glacial Snow Storm Bloom wallpaper generator for MT Nordic Light.
# Generates matching Scandinavian dawn / daylight 4K Bloom artworks and 1080p previews.
# Deterministic: pinned seeds, colors derived from palette/presets/nordic-snow-storm.json.

import json
import math
import sys
from pathlib import Path

import cairo
import numpy as np
from PIL import Image

REPO_ROOT = Path(__file__).resolve().parents[2]
DIST_LIGHT_DIR = REPO_ROOT / "wallpaper" / "dist" / "light"
PREVIEW_LIGHT_DIR = REPO_ROOT / "wallpaper" / "preview" / "light"
WIDTH, HEIGHT = 3840, 2160

TOKENS = json.loads((REPO_ROOT / "palette" / "presets" / "nordic-snow-storm.json").read_text())
COLOR = TOKENS["color"]
TECH_SLUG = "mt-nordic-blue"


def hex_to_rgb(hex_color: str) -> tuple:
    # Convert #RRGGBB into a normalized float (r, g, b) tuple for Cairo.
    h = hex_color.lstrip("#")
    return tuple(int(h[i : i + 2], 16) / 255.0 for i in (0, 2, 4))


def add_subtle_grain(image: Image.Image, seed: int = 20261028) -> Image.Image:
    # Subtle film grain to prevent banding on light 4K gradients.
    rng = np.random.default_rng(seed)
    noise = rng.normal(0.0, 1.4, (HEIGHT, WIDTH, 1)).repeat(3, axis=2)
    data = np.clip(np.asarray(image, dtype=float) + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(data, "RGB")


def surface_to_image_light(surface: cairo.ImageSurface, seed: int = 20261028) -> Image.Image:
    # Convert Cairo surface into a grain-enhanced RGB PIL Image.
    buf = surface.get_data()
    img = Image.frombuffer("RGBA", (WIDTH, HEIGHT), buf, "raw", "BGRA", 0, 1).convert("RGB")
    return add_subtle_grain(img, seed)


def draw_folded_ribbon_light(
    ctx: cairo.Context,
    cx: float,
    cy: float,
    angle_deg: float,
    length: float,
    width: float,
    curl_deg: float,
    tip_twist: float,
    c_top: tuple,
    c_bot: tuple,
    c_rim: tuple,
    shadow_offset: tuple = (16, 32),
    shadow_alpha: float = 0.20,
) -> None:
    # Draw a 3D folded porcelain snow ribbon petal with daylight shadow and crisp rim.
    rad = math.radians(angle_deg)
    curl = math.radians(curl_deg)

    bx0 = cx + math.cos(rad - math.pi / 2) * (width * 0.18)
    by0 = cy + math.sin(rad - math.pi / 2) * (width * 0.18)
    bx1 = cx + math.cos(rad + math.pi / 2) * (width * 0.18)
    by1 = cy + math.sin(rad + math.pi / 2) * (width * 0.18)

    mid_rad = rad + curl * 0.5
    mx = cx + math.cos(mid_rad) * (length * 0.52)
    my = cy + math.sin(mid_rad) * (length * 0.52)

    cp_out1_x = bx0 + math.cos(rad - math.pi / 3) * (length * 0.3) + math.cos(mid_rad - math.pi / 2) * (width * 0.75)
    cp_out1_y = by0 + math.sin(rad - math.pi / 3) * (length * 0.3) + math.sin(mid_rad - math.pi / 2) * (width * 0.75)

    cp_out2_x = mx + math.cos(mid_rad - math.pi / 2) * (width * 0.88)
    cp_out2_y = my + math.sin(mid_rad - math.pi / 2) * (width * 0.88)

    tip_rad = rad + curl
    tx = cx + math.cos(tip_rad) * length
    ty = cy + math.sin(tip_rad) * length
    tip_cap_x = tx + math.cos(tip_rad + math.radians(tip_twist)) * (width * 0.28)
    tip_cap_y = ty + math.sin(tip_rad + math.radians(tip_twist)) * (width * 0.28)

    cp_in1_x = mx + math.cos(mid_rad + math.pi / 2) * (width * 0.25) + math.cos(tip_rad) * (length * 0.1)
    cp_in1_y = my + math.sin(mid_rad + math.pi / 2) * (width * 0.25) + math.sin(tip_rad) * (length * 0.1)

    cp_in2_x = bx1 + math.cos(rad + math.pi / 4) * (length * 0.25)
    cp_in2_y = by1 + math.sin(rad + math.pi / 4) * (length * 0.25)

    # 1. Soft daylight shadow
    sx, sy = shadow_offset
    ctx.save()
    ctx.move_to(bx0 + sx, by0 + sy)
    ctx.curve_to(cp_out1_x + sx, cp_out1_y + sy, cp_out2_x + sx, cp_out2_y + sy, tx + sx, ty + sy)
    ctx.curve_to(tip_cap_x + sx, tip_cap_y + sy, cp_in1_x + sx, cp_in1_y + sy, cp_in2_x + sx, cp_in2_y + sy)
    ctx.line_to(bx1 + sx, by1 + sy)
    ctx.close_path()
    c_shadow = hex_to_rgb(COLOR["text"]["primary"])
    ctx.set_source_rgba(c_shadow[0], c_shadow[1], c_shadow[2], shadow_alpha)
    ctx.fill()
    ctx.restore()

    # 2. Main petal ribbon body with subtle porcelain-to-slate daylight gradient
    grad = cairo.LinearGradient(cp_out2_x, cp_out2_y, cp_in1_x, cp_in1_y)
    grad.add_color_stop_rgba(0.0, c_top[0], c_top[1], c_top[2], 0.98)
    grad.add_color_stop_rgba(0.60, (c_top[0] + c_bot[0]) * 0.5, (c_top[1] + c_bot[1]) * 0.5, (c_top[2] + c_bot[2]) * 0.5, 0.96)
    grad.add_color_stop_rgba(1.0, c_bot[0], c_bot[1], c_bot[2], 0.98)

    ctx.save()
    ctx.move_to(bx0, by0)
    ctx.curve_to(cp_out1_x, cp_out1_y, cp_out2_x, cp_out2_y, tx, ty)
    ctx.curve_to(tip_cap_x, tip_cap_y, cp_in1_x, cp_in1_y, cp_in2_x, cp_in2_y)
    ctx.line_to(bx1, by1)
    ctx.close_path()
    ctx.set_source(grad)
    ctx.fill_preserve()

    ctx.set_source_rgba(c_bot[0] * 0.9, c_bot[1] * 0.9, c_bot[2] * 0.9, 0.25)
    ctx.set_line_width(2.0)
    ctx.stroke()
    ctx.restore()

    # 3. Specular white/cyan rim
    ctx.save()
    ctx.move_to(bx0, by0)
    ctx.curve_to(cp_out1_x, cp_out1_y, cp_out2_x, cp_out2_y, tx, ty)
    ctx.set_source_rgba(c_rim[0], c_rim[1], c_rim[2], 0.95)
    ctx.set_line_width(4.8)
    ctx.stroke()
    ctx.restore()


# =========================================================================
# Light Wallpaper 1: Glacial Snow Storm Bloom (Art 1 Light)
# =========================================================================

def generate_canopy_dawn() -> Image.Image:
    # Full centered 3D folded Silk Bloom rosette in Scandinavian daylight mist.
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)

    # Daylight mist background
    c_base = hex_to_rgb(COLOR["bg"]["base"])
    c_dark = hex_to_rgb(COLOR["bg"]["base_darker"])
    bg = cairo.LinearGradient(0, 0, 0, HEIGHT)
    bg.add_color_stop_rgb(0, c_base[0], c_base[1], c_base[2])
    bg.add_color_stop_rgb(1, c_dark[0], c_dark[1], c_dark[2])
    ctx.set_source(bg)
    ctx.paint()

    # Radial ambient daylight glow
    cx, cy = WIDTH * 0.5, HEIGHT * 0.54
    c_white = (1.0, 1.0, 1.0)
    c_cyan_frost = hex_to_rgb(COLOR["accent_flavors"]["arctic"])
    c_glacier = hex_to_rgb(COLOR["accent_flavors"]["glacier"])

    rg = cairo.RadialGradient(cx, cy - 120, 80, cx, cy, 1500)
    rg.add_color_stop_rgba(0.0, c_white[0], c_white[1], c_white[2], 0.45)
    rg.add_color_stop_rgba(0.35, c_cyan_frost[0], c_cyan_frost[1], c_cyan_frost[2], 0.18)
    rg.add_color_stop_rgba(0.70, c_glacier[0], c_glacier[1], c_glacier[2], 0.08)
    rg.add_color_stop_rgba(1.0, 0.0, 0.0, 0.0, 0.0)
    ctx.set_source(rg)
    ctx.paint()

    # Palette definitions from snow storm tokens
    c_porcelain = hex_to_rgb(COLOR["bg"]["surface"])
    c_mist = hex_to_rgb(COLOR["border"]["default"])
    c_slate = (0.65, 0.72, 0.82)
    c_ice_blue = hex_to_rgb(COLOR["accent"]["base"])
    c_arctic_blue = hex_to_rgb(COLOR["accent"]["strong"])
    c_rim_light = (1.0, 1.0, 1.0)
    c_rim_cyan = hex_to_rgb(COLOR["accent_flavors"]["arctic"])

    # Tier 1: Large outer sweeping ribbons
    outer_petals = [
        (150, 960, 480, -45, 20, c_porcelain, c_slate, c_rim_cyan),
        (30, 940, 460, 40, -20, c_porcelain, c_slate, c_rim_cyan),
        (170, 900, 440, -35, 15, c_white, c_slate, c_rim_light),
        (10, 880, 420, 30, -15, c_white, c_slate, c_rim_light),
        (125, 840, 400, -50, 25, c_white, c_mist, c_rim_light),
        (55, 820, 380, 45, -25, c_white, c_mist, c_rim_light),
        (95, 760, 420, 15, 0, c_porcelain, c_slate, c_rim_cyan),
        (85, 740, 400, -15, 0, c_porcelain, c_slate, c_rim_cyan),
    ]
    for p in outer_petals:
        draw_folded_ribbon_light(ctx, cx, cy + 80, p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], (16, 32), 0.20)

    # Tier 2: Middle unfolding petals
    mid_petals = [
        (-140, 720, 340, 45, -15, c_white, c_mist, c_rim_light),
        (-40, 700, 320, -40, 15, c_white, c_mist, c_rim_light),
        (-110, 760, 360, -35, 20, c_white, c_ice_blue, c_rim_light),
        (-70, 740, 350, 35, -20, c_white, c_ice_blue, c_rim_light),
        (-165, 640, 300, 30, -10, c_white, c_mist, c_rim_light),
        (-15, 620, 280, -30, 10, c_white, c_mist, c_rim_light),
        (140, 640, 320, -40, 15, c_white, c_mist, c_rim_cyan),
        (40, 620, 300, 35, -15, c_white, c_mist, c_rim_cyan),
        (110, 580, 280, -25, 10, c_porcelain, c_ice_blue, c_rim_light),
        (70, 560, 270, 25, -10, c_porcelain, c_ice_blue, c_rim_light),
    ]
    for p in mid_petals:
        draw_folded_ribbon_light(ctx, cx, cy + 30, p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], (12, 24), 0.18)

    # Tier 3: Inner rosebud spiral core
    core_petals = [
        (-90, 520, 260, 50, -25, c_white, c_arctic_blue, c_rim_light),
        (-30, 480, 240, -55, 30, c_white, c_ice_blue, c_rim_cyan),
        (-150, 460, 230, 60, -30, c_white, c_ice_blue, c_rim_cyan),
        (30, 420, 220, -45, 20, c_white, c_mist, c_rim_light),
        (150, 400, 210, 45, -20, c_white, c_mist, c_rim_light),
        (-75, 360, 190, -60, 35, c_white, c_arctic_blue, c_rim_cyan),
        (-105, 340, 180, 60, -35, c_white, c_arctic_blue, c_rim_cyan),
        (90, 320, 170, 20, 0, c_porcelain, c_slate, c_rim_light),
        (-90, 240, 140, 45, -20, c_white, c_ice_blue, c_rim_light),
        (0, 180, 110, -45, 20, c_white, c_ice_blue, c_rim_light),
    ]
    for p in core_petals:
        draw_folded_ribbon_light(ctx, cx, cy - 20, p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], (8, 16), 0.15)

    # Soft daylight core vortex
    cg = cairo.RadialGradient(cx, cy - 30, 10, cx, cy - 30, 110)
    cg.add_color_stop_rgba(0, 0.30, 0.38, 0.50, 0.40)
    cg.add_color_stop_rgba(0.7, 0.50, 0.60, 0.70, 0.15)
    cg.add_color_stop_rgba(1, 0, 0, 0, 0)
    ctx.set_source(cg)
    ctx.paint()

    return surface_to_image_light(surface, 20261028)


# =========================================================================
# Light Wallpaper 2: Daylight Aurora Ribbon Drift (Art 2 Light)
# =========================================================================

def generate_celestial_rift() -> Image.Image:
    # Sweeping porcelain ribbons drifting across daylight auroral mist.
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)

    # Mist background
    c_base = hex_to_rgb(COLOR["bg"]["base"])
    c_dark = hex_to_rgb(COLOR["bg"]["base_darker"])
    bg = cairo.LinearGradient(0, 0, WIDTH, HEIGHT)
    bg.add_color_stop_rgb(0, c_base[0], c_base[1], c_base[2])
    bg.add_color_stop_rgb(1, c_dark[0], c_dark[1], c_dark[2])
    ctx.set_source(bg)
    ctx.paint()

    c_aurora = hex_to_rgb(COLOR["accent_flavors"]["aurora"])
    c_frost = hex_to_rgb(COLOR["accent_flavors"]["arctic"])
    c_glacier = hex_to_rgb(COLOR["accent_flavors"]["glacier"])
    c_white = (1.0, 1.0, 1.0)
    c_porcelain = hex_to_rgb(COLOR["bg"]["surface"])
    c_mist = hex_to_rgb(COLOR["border"]["default"])

    for i in range(4):
        ag = cairo.LinearGradient(WIDTH * 0.1 * i, 0, WIDTH * (0.3 + 0.2 * i), HEIGHT)
        ag.add_color_stop_rgba(0.0, c_white[0], c_white[1], c_white[2], 0.0)
        ag.add_color_stop_rgba(0.45, c_frost[0], c_frost[1], c_frost[2], 0.12)
        ag.add_color_stop_rgba(0.75, c_aurora[0], c_aurora[1], c_aurora[2], 0.06)
        ag.add_color_stop_rgba(1.0, 0.0, 0.0, 0.0, 0.0)
        ctx.set_source(ag)
        ctx.paint()

    aurora_petals = [
        (WIDTH * 0.35, HEIGHT * 0.70, -35, 920, 360, 45, -20, c_white, c_mist, c_frost),
        (WIDTH * 0.45, HEIGHT * 0.65, -45, 880, 340, 50, -25, c_white, c_mist, c_white),
        (WIDTH * 0.55, HEIGHT * 0.55, -55, 950, 380, -45, 20, c_porcelain, c_glacier, c_frost),
        (WIDTH * 0.65, HEIGHT * 0.45, -65, 890, 350, -50, 25, c_white, c_mist, c_white),
        (WIDTH * 0.40, HEIGHT * 0.60, 145, 780, 320, -35, 15, c_porcelain, c_mist, c_aurora),
        (WIDTH * 0.50, HEIGHT * 0.50, -30, 720, 300, 40, -15, c_white, c_frost, c_white),
        (WIDTH * 0.60, HEIGHT * 0.40, 150, 750, 310, 35, -20, c_porcelain, c_mist, c_frost),
    ]
    for p in aurora_petals:
        draw_folded_ribbon_light(ctx, p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], (14, 28), 0.18)

    return surface_to_image_light(surface, 20261029)


# =========================================================================
# Light Wallpaper 3: Glacial Petal Core Light (Art 3 Light)
# =========================================================================

def generate_cosmic_dawn() -> Image.Image:
    # Macro view of overlapping porcelain snow folds in daylight.
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)

    c_base = hex_to_rgb(COLOR["bg"]["base"])
    c_dark = hex_to_rgb(COLOR["bg"]["base_darker"])
    bg = cairo.LinearGradient(0, 0, 0, HEIGHT)
    bg.add_color_stop_rgb(0, c_base[0], c_base[1], c_base[2])
    bg.add_color_stop_rgb(1, c_dark[0], c_dark[1], c_dark[2])
    ctx.set_source(bg)
    ctx.paint()

    cx, cy = WIDTH * 0.5, HEIGHT * 0.50
    c_white = (1.0, 1.0, 1.0)
    c_porcelain = hex_to_rgb(COLOR["bg"]["surface"])
    c_mist = hex_to_rgb(COLOR["border"]["default"])
    c_ice_blue = hex_to_rgb(COLOR["accent"]["base"])
    c_frost = hex_to_rgb(COLOR["accent_flavors"]["arctic"])

    macro_petals = [
        (135, 1200, 540, -40, 25, c_white, c_mist, c_frost),
        (45, 1180, 520, 35, -20, c_white, c_mist, c_frost),
        (-135, 1050, 480, 45, -20, c_white, c_ice_blue, c_white),
        (-45, 1020, 460, -40, 20, c_white, c_ice_blue, c_white),
        (-90, 880, 420, 50, -25, c_white, c_ice_blue, c_frost),
        (90, 850, 400, -35, 20, c_porcelain, c_mist, c_white),
        (-60, 750, 360, -55, 30, c_white, c_frost, c_white),
        (-120, 720, 350, 55, -30, c_white, c_frost, c_white),
        (0, 580, 290, -45, 20, c_white, c_mist, c_frost),
        (180, 540, 280, 45, -20, c_porcelain, c_mist, c_white),
    ]
    for p in macro_petals:
        draw_folded_ribbon_light(ctx, cx, cy, p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], (18, 36), 0.22)

    return surface_to_image_light(surface, 20261030)


# =========================================================================
# Light Wallpaper 4: Ascending Snow Storm Crest (Art 4 Light)
# =========================================================================

def generate_cyber_light() -> Image.Image:
    # Upward swirling helical ribbons in porcelain and frost blue.
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)

    c_base = hex_to_rgb(COLOR["bg"]["base"])
    c_dark = hex_to_rgb(COLOR["bg"]["base_darker"])
    bg = cairo.LinearGradient(0, 0, 0, HEIGHT)
    bg.add_color_stop_rgb(0, c_base[0], c_base[1], c_base[2])
    bg.add_color_stop_rgb(1, c_dark[0], c_dark[1], c_dark[2])
    ctx.set_source(bg)
    ctx.paint()

    cx, cy = WIDTH * 0.5, HEIGHT * 0.62
    c_white = (1.0, 1.0, 1.0)
    c_porcelain = hex_to_rgb(COLOR["bg"]["surface"])
    c_mist = hex_to_rgb(COLOR["border"]["default"])
    c_ice_blue = hex_to_rgb(COLOR["accent"]["base"])
    c_frost = hex_to_rgb(COLOR["accent_flavors"]["arctic"])

    crest_petals = [
        (160, 850, 420, -50, 25, c_porcelain, c_mist, c_frost),
        (20, 830, 400, 45, -20, c_porcelain, c_mist, c_frost),
        (-150, 780, 380, 40, -20, c_white, c_mist, c_white),
        (-30, 760, 360, -40, 20, c_white, c_mist, c_white),
        (-110, 820, 370, -45, 25, c_white, c_ice_blue, c_frost),
        (-70, 800, 360, 45, -25, c_white, c_ice_blue, c_frost),
        (-90, 700, 330, 30, -15, c_white, c_frost, c_white),
        (-90, 540, 260, -35, 20, c_white, c_mist, c_frost),
        (-90, 380, 190, 40, -20, c_white, c_mist, c_white),
    ]
    for p in crest_petals:
        draw_folded_ribbon_light(ctx, cx, cy, p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], (14, 28), 0.20)

    return surface_to_image_light(surface, 20261031)


# =========================================================================
# CLI and Output Orchestration
# =========================================================================

LIGHT_WALLPAPERS = [
    {
        "id": "1",
        "title": "Glacial Snow Storm Bloom (Art 1 Light)",
        "file": f"{TECH_SLUG}-canopy-dawn-3840x2160.png",
        "preview": f"{TECH_SLUG}-canopy-dawn-1920x1080.jpg",
        "fn": generate_canopy_dawn,
    },
    {
        "id": "2",
        "title": "Daylight Aurora Ribbon Drift (Art 2 Light)",
        "file": f"{TECH_SLUG}-celestial-rift-3840x2160.png",
        "preview": f"{TECH_SLUG}-celestial-rift-1920x1080.jpg",
        "fn": generate_celestial_rift,
    },
    {
        "id": "3",
        "title": "Glacial Petal Core Light (Art 3 Light)",
        "file": f"{TECH_SLUG}-cosmic-dawn-3840x2160.png",
        "preview": f"{TECH_SLUG}-cosmic-dawn-1920x1080.jpg",
        "fn": generate_cosmic_dawn,
    },
    {
        "id": "4",
        "title": "Ascending Snow Storm Crest (Art 4 Light)",
        "file": f"{TECH_SLUG}-botanical-horizon-3840x2160.png",
        "preview": f"{TECH_SLUG}-botanical-horizon-1920x1080.jpg",
        "fn": generate_cyber_light,
    },
]


def dominant_palette(image: Image.Image, count: int = 8) -> list:
    # Report dominant colors for metadata manifest.
    small = image.convert("RGB").resize((160, 90))
    quantized = small.quantize(colors=count, method=Image.Quantize.MEDIANCUT).convert("RGB")
    counts = sorted(quantized.getcolors(160 * 90) or [], reverse=True)
    return [f"#{r:02x}{g:02x}{b:02x}" for _, (r, g, b) in counts]


def main():
    # Orchestrate procedural rendering of the 4K Light Suite and dynamic XML generation.
    DIST_LIGHT_DIR.mkdir(parents=True, exist_ok=True)
    PREVIEW_LIGHT_DIR.mkdir(parents=True, exist_ok=True)

    manifest = []
    for wp in LIGHT_WALLPAPERS:
        print(f"Generating Light 4K Wallpaper {wp['id']}: {wp['title']}...")
        img = wp["fn"]()

        out_4k = DIST_LIGHT_DIR / wp["file"]
        img.save(out_4k, optimize=True)

        out_prev = PREVIEW_LIGHT_DIR / wp["preview"]
        img.resize((1920, 1080), Image.Resampling.LANCZOS).save(out_prev, quality=88, optimize=True)

        dominant = dominant_palette(img)
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
    print(f"\nAll light Bloom wallpapers generated successfully at: {DIST_LIGHT_DIR}")


if __name__ == "__main__":
    main()

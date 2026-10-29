# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Procedural 4K Glacial Silk Bloom wallpaper generator for MT Nordic Blue.
# Recreates the 3D folded Bloom ribbon sculpture in Nordic Polar Night aesthetics.
# Deterministic: pinned seeds, colors strictly derived from palette/tokens.json.

import argparse
import json
import math
import random
import sys
from pathlib import Path

import cairo
import numpy as np
from PIL import Image

REPO_ROOT = Path(__file__).resolve().parents[2]
TOKENS = json.loads((REPO_ROOT / "palette" / "tokens.json").read_text())
COLOR = TOKENS["color"]
WIDTH, HEIGHT = 3840, 2160
TECH_SLUG = TOKENS.get("meta", {}).get("tech_name", "mt-nordic-blue").lower()


def hex_to_rgb(hex_color: str) -> tuple:
    # Convert #RRGGBB into a normalized float (r, g, b) tuple for Cairo.
    h = hex_color.lstrip("#")
    return tuple(int(h[i : i + 2], 16) / 255.0 for i in (0, 2, 4))


def add_grain(image: Image.Image, seed: int = 20261029) -> Image.Image:
    # Subtle film grain to prevent banding on 4K gradients.
    rng = np.random.default_rng(seed)
    noise = rng.normal(0.0, 1.8, (HEIGHT, WIDTH, 1)).repeat(3, axis=2)
    data = np.clip(np.asarray(image, dtype=float) + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(data, "RGB")


def surface_to_image(surface: cairo.ImageSurface, seed: int = 20261029) -> Image.Image:
    # Convert Cairo ARGB32 surface buffer into a grain-enhanced RGB PIL Image.
    buf = surface.get_data()
    img = Image.frombuffer("RGBA", (WIDTH, HEIGHT), buf, "raw", "BGRA", 0, 1).convert("RGB")
    return add_grain(img, seed)


def draw_folded_ribbon(
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
    shadow_alpha: float = 0.42,
) -> None:
    # Draw a 3D folded organic silk ribbon petal with cast shadow and luminous rim.
    rad = math.radians(angle_deg)
    curl = math.radians(curl_deg)

    # Base anchor points
    bx0 = cx + math.cos(rad - math.pi / 2) * (width * 0.18)
    by0 = cy + math.sin(rad - math.pi / 2) * (width * 0.18)
    bx1 = cx + math.cos(rad + math.pi / 2) * (width * 0.18)
    by1 = cy + math.sin(rad + math.pi / 2) * (width * 0.18)

    # Mid control points
    mid_rad = rad + curl * 0.5
    mx = cx + math.cos(mid_rad) * (length * 0.52)
    my = cy + math.sin(mid_rad) * (length * 0.52)

    # Outer bulging control points
    cp_out1_x = bx0 + math.cos(rad - math.pi / 3) * (length * 0.3) + math.cos(mid_rad - math.pi / 2) * (width * 0.75)
    cp_out1_y = by0 + math.sin(rad - math.pi / 3) * (length * 0.3) + math.sin(mid_rad - math.pi / 2) * (width * 0.75)

    cp_out2_x = mx + math.cos(mid_rad - math.pi / 2) * (width * 0.88)
    cp_out2_y = my + math.sin(mid_rad - math.pi / 2) * (width * 0.88)

    # Tip point and cap twist
    tip_rad = rad + curl
    tx = cx + math.cos(tip_rad) * length
    ty = cy + math.sin(tip_rad) * length
    tip_cap_x = tx + math.cos(tip_rad + math.radians(tip_twist)) * (width * 0.28)
    tip_cap_y = ty + math.sin(tip_rad + math.radians(tip_twist)) * (width * 0.28)

    # Inner boundary control points
    cp_in1_x = mx + math.cos(mid_rad + math.pi / 2) * (width * 0.25) + math.cos(tip_rad) * (length * 0.1)
    cp_in1_y = my + math.sin(mid_rad + math.pi / 2) * (width * 0.25) + math.sin(tip_rad) * (length * 0.1)

    cp_in2_x = bx1 + math.cos(rad + math.pi / 4) * (length * 0.25)
    cp_in2_y = by1 + math.sin(rad + math.pi / 4) * (length * 0.25)

    # 1. Cast shadow layer
    sx, sy = shadow_offset
    ctx.save()
    ctx.move_to(bx0 + sx, by0 + sy)
    ctx.curve_to(cp_out1_x + sx, cp_out1_y + sy, cp_out2_x + sx, cp_out2_y + sy, tx + sx, ty + sy)
    ctx.curve_to(tip_cap_x + sx, tip_cap_y + sy, cp_in1_x + sx, cp_in1_y + sy, cp_in2_x + sx, cp_in2_y + sy)
    ctx.line_to(bx1 + sx, by1 + sy)
    ctx.close_path()
    c_shadow = hex_to_rgb(COLOR["bg"]["base_darker"])
    ctx.set_source_rgba(c_shadow[0], c_shadow[1], c_shadow[2], shadow_alpha)
    ctx.fill()
    ctx.restore()

    # 2. Main petal body with linear gradient from lit outer edge to shadowed fold
    grad = cairo.LinearGradient(cp_out2_x, cp_out2_y, cp_in1_x, cp_in1_y)
    grad.add_color_stop_rgba(0.0, c_top[0], c_top[1], c_top[2], 0.96)
    grad.add_color_stop_rgba(0.55, (c_top[0] + c_bot[0]) * 0.5, (c_top[1] + c_bot[1]) * 0.5, (c_top[2] + c_bot[2]) * 0.5, 0.94)
    grad.add_color_stop_rgba(1.0, c_bot[0], c_bot[1], c_bot[2], 0.98)

    ctx.save()
    ctx.move_to(bx0, by0)
    ctx.curve_to(cp_out1_x, cp_out1_y, cp_out2_x, cp_out2_y, tx, ty)
    ctx.curve_to(tip_cap_x, tip_cap_y, cp_in1_x, cp_in1_y, cp_in2_x, cp_in2_y)
    ctx.line_to(bx1, by1)
    ctx.close_path()
    ctx.set_source(grad)
    ctx.fill_preserve()

    # 3. Soft internal edge crease stroke
    ctx.set_source_rgba(c_bot[0] * 0.8, c_bot[1] * 0.8, c_bot[2] * 0.8, 0.35)
    ctx.set_line_width(2.0)
    ctx.stroke()
    ctx.restore()

    # 4. Specular glowing rim along the outer crest
    ctx.save()
    ctx.move_to(bx0, by0)
    ctx.curve_to(cp_out1_x, cp_out1_y, cp_out2_x, cp_out2_y, tx, ty)
    ctx.set_source_rgba(c_rim[0], c_rim[1], c_rim[2], 0.92)
    ctx.set_line_width(5.2)
    ctx.stroke()
    ctx.restore()


# =========================================================================
# Wallpaper 1: Glacial Silk Bloom Prime (Art 1)
# =========================================================================

def generate_bloom_prime() -> Image.Image:
    # Full centered 3D folded Silk Bloom rosette sculpture in Nordic Polar Night.
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)

    # Polar Night background gradient
    c_base = hex_to_rgb(COLOR["bg"]["base"])
    c_dark = hex_to_rgb(COLOR["bg"]["base_darker"])
    bg = cairo.LinearGradient(0, 0, 0, HEIGHT)
    bg.add_color_stop_rgb(0, c_base[0], c_base[1], c_base[2])
    bg.add_color_stop_rgb(1, c_dark[0], c_dark[1], c_dark[2])
    ctx.set_source(bg)
    ctx.paint()

    # Radial ambient cyan aura behind the bloom
    cx, cy = WIDTH * 0.5, HEIGHT * 0.54
    c_cyber = hex_to_rgb(COLOR["accent_flavors"]["cyber"])
    c_frost = hex_to_rgb(COLOR["accent"]["base"])
    c_glacier = hex_to_rgb(COLOR["accent_flavors"]["arctic"])

    rg = cairo.RadialGradient(cx, cy - 120, 80, cx, cy, 1500)
    rg.add_color_stop_rgba(0.0, c_cyber[0], c_cyber[1], c_cyber[2], 0.25)
    rg.add_color_stop_rgba(0.35, c_frost[0], c_frost[1], c_frost[2], 0.15)
    rg.add_color_stop_rgba(0.70, c_glacier[0], c_glacier[1], c_glacier[2], 0.05)
    rg.add_color_stop_rgba(1.0, 0.0, 0.0, 0.0, 0.0)
    ctx.set_source(rg)
    ctx.paint()

    # Palette definitions from tokens
    c_deep = hex_to_rgb(COLOR["bg"]["surface"])
    c_navy = hex_to_rgb(COLOR["bg"]["surface_active"])
    c_ice = hex_to_rgb(COLOR["accent_flavors"]["glacier"])
    c_rim_bright = hex_to_rgb(COLOR["text"]["primary"])
    c_rim_cyan = hex_to_rgb(COLOR["accent_flavors"]["cyber"])

    # Tier 1: Large outer sweeping ribbons
    outer_petals = [
        (150, 960, 480, -45, 20, c_navy, c_deep, c_glacier),
        (30, 940, 460, 40, -20, c_navy, c_deep, c_glacier),
        (170, 900, 440, -35, 15, c_glacier, c_deep, c_ice),
        (10, 880, 420, 30, -15, c_glacier, c_deep, c_ice),
        (125, 840, 400, -50, 25, c_glacier, c_navy, c_frost),
        (55, 820, 380, 45, -25, c_glacier, c_navy, c_frost),
        (95, 760, 420, 15, 0, c_navy, c_deep, c_ice),
        (85, 740, 400, -15, 0, c_navy, c_deep, c_ice),
    ]
    for p in outer_petals:
        draw_folded_ribbon(ctx, cx, cy + 80, p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], (20, 40), 0.46)

    # Tier 2: Middle unfolding petals
    mid_petals = [
        (-140, 720, 340, 45, -15, c_ice, c_navy, c_frost),
        (-40, 700, 320, -40, 15, c_ice, c_navy, c_frost),
        (-110, 760, 360, -35, 20, c_frost, c_glacier, c_rim_bright),
        (-70, 740, 350, 35, -20, c_frost, c_glacier, c_rim_bright),
        (-165, 640, 300, 30, -10, c_ice, c_navy, c_frost),
        (-15, 620, 280, -30, 10, c_ice, c_navy, c_frost),
        (140, 640, 320, -40, 15, c_ice, c_navy, c_frost),
        (40, 620, 300, 35, -15, c_ice, c_navy, c_frost),
        (110, 580, 280, -25, 10, c_glacier, c_navy, c_rim_cyan),
        (70, 560, 270, 25, -10, c_glacier, c_navy, c_rim_cyan),
    ]
    for p in mid_petals:
        draw_folded_ribbon(ctx, cx, cy + 30, p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], (16, 30), 0.40)

    # Tier 3: Inner rosebud spiral core
    core_petals = [
        (-90, 520, 260, 50, -25, c_rim_bright, c_glacier, c_rim_cyan),
        (-30, 480, 240, -55, 30, c_frost, c_glacier, c_rim_bright),
        (-150, 460, 230, 60, -30, c_frost, c_glacier, c_rim_bright),
        (30, 420, 220, -45, 20, c_frost, c_navy, c_rim_cyan),
        (150, 400, 210, 45, -20, c_ice, c_navy, c_rim_bright),
        (-75, 360, 190, -60, 35, c_rim_bright, c_glacier, c_rim_cyan),
        (-105, 340, 180, 60, -35, c_rim_bright, c_glacier, c_rim_cyan),
        (90, 320, 170, 20, 0, c_frost, c_navy, c_rim_bright),
        (-90, 240, 140, 45, -20, c_rim_bright, c_glacier, c_rim_cyan),
        (0, 180, 110, -45, 20, c_rim_bright, c_frost, c_rim_cyan),
    ]
    for p in core_petals:
        draw_folded_ribbon(ctx, cx, cy - 20, p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], (10, 20), 0.35)

    # Central vortex depth
    cg = cairo.RadialGradient(cx, cy - 30, 10, cx, cy - 30, 110)
    cg.add_color_stop_rgba(0, c_dark[0], c_dark[1], c_dark[2], 0.88)
    cg.add_color_stop_rgba(0.7, c_base[0], c_base[1], c_base[2], 0.40)
    cg.add_color_stop_rgba(1, 0, 0, 0, 0)
    ctx.set_source(cg)
    ctx.paint()

    return surface_to_image(surface, 20261029)


# =========================================================================
# Wallpaper 2: Aurora Ribbon Drift (Art 2)
# =========================================================================

def generate_bloom_aurora() -> Image.Image:
    # Undulating silk bloom ribbons drifting across a northern lights auroral veil.
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)

    # Polar Night background
    c_base = hex_to_rgb(COLOR["bg"]["base"])
    c_dark = hex_to_rgb(COLOR["bg"]["base_darker"])
    bg = cairo.LinearGradient(0, 0, WIDTH, HEIGHT)
    bg.add_color_stop_rgb(0, c_base[0], c_base[1], c_base[2])
    bg.add_color_stop_rgb(1, c_dark[0], c_dark[1], c_dark[2])
    ctx.set_source(bg)
    ctx.paint()

    # Auroral curtains in the background
    c_aurora = hex_to_rgb(COLOR["accent_flavors"]["aurora"])
    c_frost = hex_to_rgb(COLOR["accent"]["base"])
    c_glacier = hex_to_rgb(COLOR["accent_flavors"]["glacier"])
    c_cyber = hex_to_rgb(COLOR["accent_flavors"]["cyber"])

    for i in range(4):
        ag = cairo.LinearGradient(WIDTH * 0.1 * i, 0, WIDTH * (0.3 + 0.2 * i), HEIGHT)
        ag.add_color_stop_rgba(0.0, c_aurora[0], c_aurora[1], c_aurora[2], 0.0)
        ag.add_color_stop_rgba(0.45, c_frost[0], c_frost[1], c_frost[2], 0.14)
        ag.add_color_stop_rgba(0.75, c_glacier[0], c_glacier[1], c_glacier[2], 0.08)
        ag.add_color_stop_rgba(1.0, 0.0, 0.0, 0.0, 0.0)
        ctx.set_source(ag)
        ctx.paint()

    # Flowing S-curve ribbon paths
    c_navy = hex_to_rgb(COLOR["bg"]["surface_active"])
    c_deep = hex_to_rgb(COLOR["bg"]["surface"])
    c_ice = hex_to_rgb(COLOR["accent_flavors"]["glacier"])
    c_rim_bright = hex_to_rgb(COLOR["text"]["primary"])

    aurora_petals = [
        # (cx, cy, angle, length, width, curl, twist, c_top, c_bot, c_rim)
        (WIDTH * 0.35, HEIGHT * 0.70, -35, 920, 360, 45, -20, c_glacier, c_deep, c_frost),
        (WIDTH * 0.45, HEIGHT * 0.65, -45, 880, 340, 50, -25, c_frost, c_navy, c_rim_bright),
        (WIDTH * 0.55, HEIGHT * 0.55, -55, 950, 380, -45, 20, c_ice, c_deep, c_cyber),
        (WIDTH * 0.65, HEIGHT * 0.45, -65, 890, 350, -50, 25, c_frost, c_navy, c_rim_bright),
        (WIDTH * 0.40, HEIGHT * 0.60, 145, 780, 320, -35, 15, c_aurora, c_deep, c_frost),
        (WIDTH * 0.50, HEIGHT * 0.50, -30, 720, 300, 40, -15, c_cyber, c_glacier, c_rim_bright),
        (WIDTH * 0.60, HEIGHT * 0.40, 150, 750, 310, 35, -20, c_ice, c_navy, c_frost),
    ]
    for p in aurora_petals:
        draw_folded_ribbon(ctx, p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], (18, 32), 0.42)

    return surface_to_image(surface, 20261030)


# =========================================================================
# Wallpaper 3: Glacial Fold Sanctuary (Art 3)
# =========================================================================

def generate_bloom_sanctuary() -> Image.Image:
    # Macro close-up on the heart of the folded silk bloom sculpture.
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)

    # Base background
    c_base = hex_to_rgb(COLOR["bg"]["base"])
    c_dark = hex_to_rgb(COLOR["bg"]["base_darker"])
    bg = cairo.LinearGradient(0, 0, 0, HEIGHT)
    bg.add_color_stop_rgb(0, c_base[0], c_base[1], c_base[2])
    bg.add_color_stop_rgb(1, c_dark[0], c_dark[1], c_dark[2])
    ctx.set_source(bg)
    ctx.paint()

    cx, cy = WIDTH * 0.5, HEIGHT * 0.50
    c_frost = hex_to_rgb(COLOR["accent"]["base"])
    c_cyber = hex_to_rgb(COLOR["accent_flavors"]["cyber"])
    c_glacier = hex_to_rgb(COLOR["accent_flavors"]["arctic"])
    c_ice = hex_to_rgb(COLOR["accent_flavors"]["glacier"])
    c_navy = hex_to_rgb(COLOR["bg"]["surface_active"])
    c_deep = hex_to_rgb(COLOR["bg"]["surface"])
    c_rim_bright = hex_to_rgb(COLOR["text"]["primary"])

    # Macro scale (1.5x larger petals filling the viewport)
    macro_petals = [
        (135, 1200, 540, -40, 25, c_glacier, c_deep, c_ice),
        (45, 1180, 520, 35, -20, c_glacier, c_deep, c_ice),
        (-135, 1050, 480, 45, -20, c_frost, c_navy, c_rim_bright),
        (-45, 1020, 460, -40, 20, c_frost, c_navy, c_rim_bright),
        (-90, 880, 420, 50, -25, c_rim_bright, c_glacier, c_cyber),
        (90, 850, 400, -35, 20, c_ice, c_navy, c_frost),
        (-60, 750, 360, -55, 30, c_cyber, c_glacier, c_rim_bright),
        (-120, 720, 350, 55, -30, c_frost, c_glacier, c_rim_bright),
        (0, 580, 290, -45, 20, c_rim_bright, c_frost, c_cyber),
        (180, 540, 280, 45, -20, c_ice, c_navy, c_rim_bright),
    ]
    for p in macro_petals:
        draw_folded_ribbon(ctx, cx, cy, p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], (22, 44), 0.48)

    # Deep core cavern
    cg = cairo.RadialGradient(cx, cy - 20, 20, cx, cy - 20, 160)
    cg.add_color_stop_rgba(0, c_dark[0], c_dark[1], c_dark[2], 0.92)
    cg.add_color_stop_rgba(0.7, c_base[0], c_base[1], c_base[2], 0.45)
    cg.add_color_stop_rgba(1, 0, 0, 0, 0)
    ctx.set_source(cg)
    ctx.paint()

    return surface_to_image(surface, 20261031)


# =========================================================================
# Wallpaper 4: Ascending Frost Crest (Art 4)
# =========================================================================

def generate_bloom_crest() -> Image.Image:
    # Architectural ascending helical ribbons swirling upwards in Nordic cyan.
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)

    # Background
    c_base = hex_to_rgb(COLOR["bg"]["base"])
    c_dark = hex_to_rgb(COLOR["bg"]["base_darker"])
    bg = cairo.LinearGradient(0, 0, 0, HEIGHT)
    bg.add_color_stop_rgb(0, c_base[0], c_base[1], c_base[2])
    bg.add_color_stop_rgb(1, c_dark[0], c_dark[1], c_dark[2])
    ctx.set_source(bg)
    ctx.paint()

    cx, cy = WIDTH * 0.5, HEIGHT * 0.62
    c_frost = hex_to_rgb(COLOR["accent"]["base"])
    c_cyber = hex_to_rgb(COLOR["accent_flavors"]["cyber"])
    c_glacier = hex_to_rgb(COLOR["accent_flavors"]["arctic"])
    c_ice = hex_to_rgb(COLOR["accent_flavors"]["glacier"])
    c_navy = hex_to_rgb(COLOR["bg"]["surface_active"])
    c_deep = hex_to_rgb(COLOR["bg"]["surface"])
    c_rim_bright = hex_to_rgb(COLOR["text"]["primary"])

    # Helical ascending swirls
    crest_petals = [
        (160, 850, 420, -50, 25, c_navy, c_deep, c_ice),
        (20, 830, 400, 45, -20, c_navy, c_deep, c_ice),
        (-150, 780, 380, 40, -20, c_glacier, c_navy, c_frost),
        (-30, 760, 360, -40, 20, c_glacier, c_navy, c_frost),
        (-110, 820, 370, -45, 25, c_frost, c_glacier, c_rim_bright),
        (-70, 800, 360, 45, -25, c_frost, c_glacier, c_rim_bright),
        (-90, 700, 330, 30, -15, c_rim_bright, c_glacier, c_cyber),
        (-90, 540, 260, -35, 20, c_cyber, c_frost, c_rim_bright),
        (-90, 380, 190, 40, -20, c_rim_bright, c_frost, c_cyber),
    ]
    for p in crest_petals:
        draw_folded_ribbon(ctx, cx, cy, p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], (18, 36), 0.44)

    return surface_to_image(surface, 20261032)


# =========================================================================
# CLI and Output Orchestration
# =========================================================================

WALLPAPER_META = {
    "1": (f"{TECH_SLUG}-art-1", "Glacial Silk Bloom Prime (Art 1)", generate_bloom_prime),
    "2": (f"{TECH_SLUG}-art-2", "Aurora Ribbon Drift (Art 2)", generate_bloom_aurora),
    "3": (f"{TECH_SLUG}-art-3", "Glacial Fold Sanctuary (Art 3)", generate_bloom_sanctuary),
    "4": (f"{TECH_SLUG}-art-4", "Ascending Frost Crest (Art 4)", generate_bloom_crest),
}


def dominant_palette(image: Image.Image, count: int = 8) -> list:
    # Report dominant colors for metadata manifest.
    small = image.convert("RGB").resize((160, 90))
    quantized = small.quantize(colors=count, method=Image.Quantize.MEDIANCUT).convert("RGB")
    counts = sorted(quantized.getcolors(160 * 90) or [], reverse=True)
    return [f"#{r:02x}{g:02x}{b:02x}" for _, (r, g, b) in counts]


def main() -> None:
    # Orchestrate procedural 4K Dark Bloom wallpaper generation.
    parser = argparse.ArgumentParser(description="Generate 4K procedural Bloom wallpapers for MT Nordic Blue")
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
        print(f"Generating 4K Dark Wallpaper {key}: {title} (3840x2160)...")
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
    print(f"\nAll dark Bloom wallpapers generated successfully. Summary at {summary_file}")


if __name__ == "__main__":
    main()

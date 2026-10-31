# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Recolor accent base and strong literals left in Shell tweak layers (panel, popups, hovers).
# Accent foreground is baked by tools/shell/build.py from tokens, so it is never touched here.

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

# Dark and light Shell variants read their accent flavors from different token files.
TOKEN_FILES = {
    "dark": REPO_ROOT / "palette" / "tokens.json",
    "light": REPO_ROOT / "palette" / "presets" / "nordic-snow-storm.json",
}


def accent_family(variant: str) -> dict:
    # Return the color tree for the requested Shell variant.
    return json.loads(TOKEN_FILES[variant].read_text())["color"]


def hex_to_rgb(value: str) -> tuple:
    # Convert #rrggbb to an (r, g, b) integer tuple.
    h = value.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def build_mapping(target_tree: dict, source_tree: dict, flavor: str, base_only: bool = False) -> dict:
    # Map every frost accent literal from the source tree to the target flavor.
    # base_only skips strong: the Shell build already bakes strong, and a flavor whose base equals
    # frost's strong would otherwise be re-mapped onto itself.
    families = ("accent_flavors",) if base_only else ("accent_flavors", "accent_strong_flavors")
    mapping = {}
    for family in families:
        targets = target_tree[family]
        if flavor not in targets:
            print(f"unknown accent flavor '{flavor}'; expected one of {sorted(targets)}", file=sys.stderr)
            sys.exit(2)
        source, target = source_tree[family]["frost"].lower(), targets[flavor].lower()
        if source != target:
            mapping[source] = target
    return mapping


def recolor(css: str, mapping: dict) -> tuple:
    # Replace every mapped hex and rgb/rgba() form in a single pass so targets are never re-matched.
    hits = 0

    def hex_sub(match):
        nonlocal hits
        found = match.group(0).lower()
        if found in mapping:
            hits += 1
            return mapping[found].upper()
        return match.group(0)

    css = re.sub(r"#[0-9a-fA-F]{6}\b", hex_sub, css)

    def rgba_sub(match):
        nonlocal hits
        key = f"#{int(match.group(1)):02x}{int(match.group(2)):02x}{int(match.group(3)):02x}"
        if key not in mapping:
            return match.group(0)
        hits += 1
        tr, tg, tb = hex_to_rgb(mapping[key])
        alpha = match.group(4)
        channel = f"{tr}, {tg}, {tb}"
        return f"rgba({channel},{alpha})" if alpha else f"rgb({channel})"

    css = re.sub(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*([\d.]+))?\s*\)", rgba_sub, css)
    return css, hits


def accent_defines(color_tree: dict, flavor: str) -> str:
    # Build the GTK @define-color block that re-declares the accent for a flavor.
    base = color_tree["accent_flavors"][flavor]
    fg = color_tree["accent_fg_flavors"][flavor]
    pairs = (
        ("accent_color", base),
        ("accent_bg_color", base),
        ("accent_fg_color", fg),
        ("theme_selected_bg_color", base),
        ("theme_selected_fg_color", fg),
    )
    lines = "\n".join(f"@define-color {name} {value};" for name, value in pairs)
    return f"\n/* accent flavor {flavor}: appended so it wins the cascade */\n{lines}\n"


def main() -> int:
    # Parse arguments and rewrite the stylesheet in place.
    parser = argparse.ArgumentParser(description="Recolor accent base/strong literals in a Shell stylesheet.")
    parser.add_argument("--variant", choices=sorted(TOKEN_FILES), default="dark")
    parser.add_argument("--source-variant", choices=sorted(TOKEN_FILES), default=None,
                        help="read the source accent from this variant (defaults to --variant)")
    parser.add_argument("--flavor", required=True)
    parser.add_argument("--base-only", action="store_true",
                        help="skip accent strong (used when the Shell build already baked it)")
    parser.add_argument("--define-colors", action="store_true", help="append GTK @define-color overrides")
    parser.add_argument("css", type=Path)
    args = parser.parse_args()

    color_tree = accent_family(args.variant)
    source_tree = accent_family(args.source_variant or args.variant)
    mapping = build_mapping(color_tree, source_tree, args.flavor, args.base_only)
    if not args.css.is_file():
        print(f"missing stylesheet: {args.css}", file=sys.stderr)
        return 2

    css, hits = recolor(args.css.read_text(), mapping)
    if args.define_colors:
        css += accent_defines(color_tree, args.flavor)
    args.css.write_text(css)
    pairs = ", ".join(f"{k}->{v}" for k, v in sorted(mapping.items())) or "no literals"
    print(f"{args.css.name}: {args.flavor} ({pairs}) {hits} replacements")
    return 0


if __name__ == "__main__":
    sys.exit(main())

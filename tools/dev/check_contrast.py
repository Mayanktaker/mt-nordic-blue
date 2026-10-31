# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# WCAG contrast validation for MT Nordic Blue tokens (dark tokens.json + light preset).
# Checks declared token pairs and every accent flavor's foreground-on-accent pair.

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

# Both shipped variants must keep readable accents, not just the dark default.
VARIANTS = {
    "dark": REPO_ROOT / "palette" / "tokens.json",
    "light": REPO_ROOT / "palette" / "presets" / "nordic-snow-storm.json",
}


def resolve(color_tree: dict, token_path: str):
    # Look up a dotted token path inside a color token tree, or None when absent.
    node = color_tree
    for part in token_path.split("."):
        if not isinstance(node, dict) or part not in node:
            return None
        node = node[part]
    return node


def srgb_to_linear(channel: int) -> float:
    # Convert an 8-bit sRGB channel to linear light.
    c = channel / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def relative_luminance(hex_color: str) -> float:
    # WCAG relative luminance of a #RRGGBB color.
    r, g, b = (int(hex_color[i : i + 2], 16) for i in (1, 3, 5))
    return 0.2126 * srgb_to_linear(r) + 0.7152 * srgb_to_linear(g) + 0.0722 * srgb_to_linear(b)


def contrast_ratio(fg: str, bg: str) -> float:
    # WCAG contrast ratio between two #RRGGBB colors.
    l1, l2 = relative_luminance(fg), relative_luminance(bg)
    lighter, darker = max(l1, l2), min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def report(label: str, ratio: float, needed: float, preferred: float, failures: list) -> None:
    # Print one PASS/FAIL line and record failures.
    ok = ratio >= needed
    state = "PASS+" if ratio >= preferred else ("PASS" if ok else "FAIL")
    print(f"{state}  {label}: {ratio:.2f}:1 (min {needed})")
    if not ok:
        failures.append((label, round(ratio, 2)))


def check_pairs(variant: str, color_tree: dict, minimums: dict, failures: list) -> None:
    # Validate the declared token pairs that exist in this variant.
    for fg_token, bg_token in minimums["pairs"]:
        fg, bg = resolve(color_tree, fg_token), resolve(color_tree, bg_token)
        if not fg or not bg:
            continue
        report(f"[{variant}] {fg_token} on {bg_token}",
               contrast_ratio(fg, bg), minimums["body_text"], minimums["preferred_text"], failures)


def check_accent_flavors(variant: str, color_tree: dict, minimums: dict, failures: list) -> None:
    # Every flavor's accent foreground must stay readable on its own accent fill.
    flavors = color_tree.get("accent_flavors", {})
    foregrounds = color_tree.get("accent_fg_flavors", {})
    for flavor, bg in flavors.items():
        fg = foregrounds.get(flavor)
        if not fg:
            # A flavor without a foreground token cannot be validated; surface it instead of hiding it.
            print(f"WARN  [{variant}] accent_fg_flavors.{flavor} missing — flavor unvalidated")
            continue
        report(f"[{variant}] accent_fg_flavors.{flavor} on accent_flavors.{flavor}",
               contrast_ratio(fg, bg), minimums["body_text"], minimums["preferred_text"], failures)


def main() -> int:
    # Validate declared pairs for the dark policy and accent flavors for every variant.
    # The dark `pairs` list assumes accents/statuses read as text on a dark background, which does
    # not hold for the light preset, so those pairs are only checked against tokens.json.
    minimums = json.loads(VARIANTS["dark"].read_text())["wcag_minimums"]
    failures = []
    for variant, path in VARIANTS.items():
        color_tree = json.loads(path.read_text())["color"]
        if variant == "dark":
            check_pairs(variant, color_tree, minimums, failures)
        check_accent_flavors(variant, color_tree, minimums, failures)
    if failures:
        print("\nContrast failures:", failures, file=sys.stderr)
        return 1
    print("\nAll token pairs and accent flavors meet WCAG minimums.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

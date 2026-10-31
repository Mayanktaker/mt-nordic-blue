#!/usr/bin/env python3
# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Icon context gate: catches lookup-order shadowing and dangling aliases in the icon theme.
# Run after generate_icons.py; exits non-zero on errors.

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
THEME_DIR = REPO_ROOT / "src" / "icons" / "MT-Nordic-Blue-Icons"
COLOR_CONTEXTS = ("apps", "devices", "places", "mimetypes", "categories")
SYMBOLIC_ONLY_CONTEXTS = ("status", "actions", "ui")


def directory_order() -> list[str]:
    # Parse the resolution order declared in index.theme.
    for line in (THEME_DIR / "index.theme").read_text().splitlines():
        if line.startswith("Directories="):
            return [d.strip() for d in line.split("=", 1)[1].split(",") if d.strip()]
    return []


def icon_names(directory: Path) -> set[str]:
    # Collect icon stems (svg/png, files and symlinks) in one directory.
    return {p.stem for p in directory.iterdir() if p.suffix in (".svg", ".png")}


def check_shadowing(order: list[str]) -> list[str]:
    # A color-named icon (no -symbolic suffix) living in a symbolic scalable dir listed
    # before a color dir hides the color art for that name.
    problems = []
    per_dir = {}
    for ctx in COLOR_CONTEXTS + SYMBOLIC_ONLY_CONTEXTS:
        d = THEME_DIR / "scalable" / ctx
        per_dir[f"scalable/{ctx}"] = icon_names(d) if d.is_dir() else set()
    rank = {d: i for i, d in enumerate(order)}
    for sym_ctx in SYMBOLIC_ONLY_CONTEXTS:
        sym_dir = f"scalable/{sym_ctx}"
        for color_ctx in COLOR_CONTEXTS:
            color_dir = f"scalable/{color_ctx}"
            if sym_dir not in rank or color_dir not in rank or rank[sym_dir] > rank[color_dir]:
                continue
            shared = per_dir[sym_dir] & per_dir[color_dir]
            for name in sorted(shared):
                if name.endswith("-symbolic"):
                    continue  # symbolic names have no color art to shadow
                color_file = THEME_DIR / color_dir / f"{name}.svg"
                if color_file.is_file() and "currentColor" in color_file.read_text(errors="ignore"):
                    continue  # same symbolic glyph in both places, nothing hidden
                problems.append(f"shadowing: {name} resolves to {sym_dir} before {color_dir}")
    return problems


def check_aliases() -> list[str]:
    # Every symlink must resolve to a real file inside the theme.
    problems = []
    for link in THEME_DIR.rglob("*"):
        if link.is_symlink() and not link.exists():
            problems.append(f"dangling alias: {link.relative_to(THEME_DIR)} -> {link.readlink()}")
    return problems


def main() -> int:
    # Run both gates and report a compact summary.
    if not THEME_DIR.is_dir():
        print(f"FAIL: theme directory missing ({THEME_DIR}); run tools/icons/generate_icons.py")
        return 1
    order = directory_order()
    errors = check_shadowing(order)
    warnings = check_aliases()
    for line in errors:
        print(f"FAIL {line}")
    for line in warnings:
        print(f"WARN {line}")
    if errors:
        print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"Icon context gate passed ({len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())

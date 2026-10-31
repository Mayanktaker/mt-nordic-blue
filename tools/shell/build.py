# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Build MT Nordic Blue and MT Nordic Light GNOME Shell themes per major Shell version:
# host major extracts its upstream CSS from the gresource, other majors use
# vendored upstream CSS in src/shell/upstream-<major>/, then recolor via maps.

import copy
import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOKENS_DARK = json.loads((REPO_ROOT / "palette" / "tokens.json").read_text())
TOKENS_LIGHT = json.loads((REPO_ROOT / "palette" / "presets" / "nordic-snow-storm.json").read_text())


def host_shell_major() -> int:
    # Detect the running Shell major version.
    version = subprocess.run(["gnome-shell", "--version"], capture_output=True, text=True, check=True).stdout
    return int(re.search(r"(\d+)\.", version).group(1))


def resolve_token(token_path: str, color_tree: dict) -> str:
    # Resolve a dotted token path inside the provided color tree.
    node = color_tree
    for part in token_path.split("."):
        node = node[part]
    return node


def load_upstream_css(major: int, variant: str = "dark") -> str:
    # Host major: extract from the installed gresource; other majors: vendored CSS.
    res_file = f"gnome-shell-{variant}.css"
    if major == host_shell_major():
        from gi.repository import Gio
        res = Gio.Resource.load("/usr/share/gnome-shell/gnome-shell-theme.gresource")
        return res.lookup_data(f"/org/gnome/shell/theme/{res_file}", Gio.ResourceLookupFlags.NONE).get_data().decode()
    vendored = REPO_ROOT / "src" / f"shell/upstream-{major}/{res_file}"
    if not vendored.exists():
        print(f"No vendored upstream CSS for Shell {major} {variant} — check src/shell/upstream-{major}/.", file=sys.stderr)
        sys.exit(2)
    return vendored.read_text()


def load_high_contrast(major: int) -> str:
    # Fetch the matching upstream high-contrast stylesheet as a11y fallback.
    if major == host_shell_major():
        from gi.repository import Gio
        res = Gio.Resource.load("/usr/share/gnome-shell/gnome-shell-theme.gresource")
        return res.lookup_data("/org/gnome/shell/theme/gnome-shell-high-contrast.css", Gio.ResourceLookupFlags.NONE).get_data().decode()
    vendored = REPO_ROOT / "src" / f"shell/upstream-{major}/gnome-shell-high-contrast.css"
    return vendored.read_text()


def normalize_hex(match_text: str) -> str:
    # Normalize a hex literal to lowercase 6-digit form for map lookups.
    h = match_text.lower().lstrip("#")
    if len(h) == 3:
        h = "".join(ch * 2 for ch in h)
    return f"#{h}"


def recolor(css: str, color_map: dict, color_tree: dict) -> tuple:
    # Apply hex and rgba-base replacements first, then accent pseudo values last.
    # Pseudo values must run last: their resolved hex (e.g. #FFFFFF) would otherwise be
    # re-mapped by the hex table and the accent foreground would silently change.
    usage = {}

    hex_map = {k.lower(): resolve_token(v, color_tree) for k, v in color_map["hex"].items()}

    # 1. plain hex literals
    def hex_sub(match):
        key = normalize_hex(match.group(0))
        mapped = hex_map.get(key)
        if mapped is None:
            return match.group(0)
        usage[key] = usage.get(key, 0) + 1
        return mapped
    css = re.sub(r"#[0-9a-fA-F]{3}\b|#[0-9a-fA-F]{6}\b", hex_sub, css)

    # 2. rgba() bases: map base color through the same table, preserve alpha
    base_overrides = {k: resolve_token(v, color_tree) for k, v in color_map.get("rgba_base_overrides", {}).items()}

    def rgba_sub(match):
        r, g, b, alpha = match.group(1), match.group(2), match.group(3), match.group(4)
        base = f"#{int(r):02x}{int(g):02x}{int(b):02x}"
        target = base_overrides.get(f"{base}:a{alpha or 1}") or hex_map.get(base)
        if target is None:
            return match.group(0)
        key = f"rgba-base {base}"
        usage[key] = usage.get(key, 0) + 1
        tr, tg, tb = (int(target[i : i + 2], 16) for i in (1, 3, 5))
        return f"rgba({tr}, {tg}, {tb}, {alpha})" if alpha else f"rgb({tr}, {tg}, {tb})"
    css = re.sub(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([\d.]+)\s*)?\)", rgba_sub, css)

    # 3. accent pseudo values last (longest first: fg before plain)
    for pseudo in sorted(color_map["pseudo"], key=len, reverse=True):
        token_hex = resolve_token(color_map["pseudo"][pseudo], color_tree)
        usage[pseudo] = css.count(pseudo)
        css = css.replace(pseudo, token_hex)

    return css, usage


def apply_accent_flavor(tokens: dict, variant: str, flavor: str) -> dict:
    # Override accent base/strong/foreground in place with the requested flavor and return the color tree.
    color_tree = tokens["color"]
    families = (
        ("accent_flavors", "base"),
        ("accent_strong_flavors", "strong"),
        ("accent_fg_flavors", "text_on_accent"),
    )
    for family_key, accent_field in families:
        family = color_tree.get(family_key, {})
        if flavor not in family:
            print(f"unknown accent flavor '{flavor}' for {variant}; expected one of {sorted(family)}", file=sys.stderr)
            sys.exit(2)
        color_tree["accent"][accent_field] = family[flavor]
    return color_tree


def build_major_variant(major: int, variant: str = "dark", flavor: str = "frost") -> None:
    # Build one Shell major and variant; fail on map drift.
    suffix = f"-{variant}" if variant == "light" else ""
    map_path = REPO_ROOT / "src" / f"shell/colormap-{major}{suffix}.json"
    if not map_path.exists():
        print(f"No color map for GNOME Shell {major} {variant} at {map_path}.", file=sys.stderr)
        return

    # Deep-copy so repeated builds never mutate the module-level token trees.
    tokens = copy.deepcopy(TOKENS_LIGHT if variant == "light" else TOKENS_DARK)
    color_tree = apply_accent_flavor(tokens, variant, flavor)
    header = f"/* {tokens['meta'].get('name', 'MT Theme')} — © Mayanktaker Computers & Web Development | https://mayanktaker.com */\n"

    color_map = json.loads(map_path.read_text())
    css, usage = recolor(load_upstream_css(major, variant), color_map, color_tree)

    out_dir = REPO_ROOT / "build" / "theme" / f"gnome-shell-{major}{suffix}"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "gnome-shell.css").write_text(header + css)
    (out_dir / "gnome-shell-high-contrast.css").write_text(header + load_high_contrast(major))
    # Record the accent so install.sh can tell a stale build from a current one.
    (out_dir / ".accent").write_text(flavor + "\n")

    unused = [k for k in usage if usage[k] == 0 and not k.startswith("rgba-base")]
    print(f"Shell {major} ({variant}, {flavor}): wrote {out_dir / 'gnome-shell.css'} ({len(css)} bytes) | "
          f"accent pseudo={usage.get('-st-accent-color', 0)}, hex={sum(v for k, v in usage.items() if k.startswith('#'))}, "
          f"rgba={sum(v for k, v in usage.items() if k.startswith('rgba-base'))}")
    if unused:
        print(f"Shell {major} ({variant}) mapped colors not found upstream (map drift):", unused, file=sys.stderr)
        sys.exit(1)


def main() -> int:
    # Build requested majors and variants: --all or --major N or host default, plus --accent <flavor>.
    args = sys.argv[1:]
    flavor = "frost"
    if "--accent" in args:
        idx = args.index("--accent")
        if idx + 1 >= len(args):
            print("--accent needs a flavor", file=sys.stderr)
            return 2
        flavor = args[idx + 1]
        del args[idx : idx + 2]

    if args[:1] == ["--all"]:
        majors = sorted(set(int(p.stem.split("-")[1]) for p in (REPO_ROOT / "src" / "shell").glob("colormap-*.json")))
    elif len(args) >= 2 and args[0] == "--major":
        majors = [int(args[1])]
    elif not args:
        majors = [host_shell_major()]
    else:
        print("usage: build.py [--major N | --all] [--accent frost|glacier|aurora|arctic|cyber|blaze]", file=sys.stderr)
        return 2

    for major in majors:
        build_major_variant(major, "dark", flavor)
        build_major_variant(major, "light", flavor)
    return 0


if __name__ == "__main__":
    sys.exit(main())

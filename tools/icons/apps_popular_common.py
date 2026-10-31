# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Shared 64x64 Nordic tile builder for the popular-app icon batches.
# Colors are loaded from palette/tokens.json (single source of truth).

import json
from pathlib import Path

_TOKENS = json.loads((Path(__file__).resolve().parents[2] / "palette" / "tokens.json").read_text())["color"]

ACCENT = _TOKENS["accent_flavors"]["cyber"]        # Frost accent used by app tiles
ACCENT2 = _TOKENS["accent"]["base"]                # Glacier secondary
SNOW = _TOKENS["text"]["primary"]                  # Snow paper
GOLD = _TOKENS["status"]["warning"]
RED = _TOKENS["status"]["destructive"]
GREEN = _TOKENS["status"]["success"]
PURPLE = _TOKENS["status"]["petal_decorative"]
ORANGE = _TOKENS["accent_flavors"]["blaze"]
TILE_FILL = _TOKENS["bg"]["tile"]
BORDER = _TOKENS["border"]["default"]
BASE = _TOKENS["bg"]["base"]


def tile(key: str, body: str) -> str:
    # Wrap a glyph body in the standard Nordic rounded app tile.
    return f'''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs>
  <linearGradient id="bg-{key}" x1="32" y1="6" x2="32" y2="58" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="{BORDER}"/>
    <stop offset="100%" stop-color="{BASE}"/>
  </linearGradient>
</defs>
<rect x="6" y="6" width="52" height="52" rx="14" fill="url(#bg-{key})" stroke="{BORDER}" stroke-width="1.5"/>
<rect x="8.5" y="8.5" width="47" height="4" rx="2" fill="{ACCENT2}" fill-opacity="0.25"/>
{body}
</svg>'''

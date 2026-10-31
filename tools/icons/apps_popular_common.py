# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Shared 64x64 Nordic tile builder for the popular-app icon batches.
# Every glyph uses palette tokens: frost #00D2FF / #88C0D0, snow #ECEFF4.

ACCENT = "#00D2FF"        # Frost accent (bright)
ACCENT2 = "#88C0D0"       # Glacier secondary
SNOW = "#ECEFF4"          # Snow paper
GOLD = "#EBCB8B"
RED = "#E5737F"
GREEN = "#A3BE8C"
PURPLE = "#B48EAD"
ORANGE = "#D08770"
TILE_FILL = "#151D2A"
BORDER = "#25344A"


def tile(key: str, body: str) -> str:
    # Wrap a glyph body in the standard Nordic rounded app tile.
    return f'''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs>
  <linearGradient id="bg-{key}" x1="32" y1="6" x2="32" y2="58" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="{BORDER}"/>
    <stop offset="100%" stop-color="#0e141d"/>
  </linearGradient>
</defs>
<rect x="6" y="6" width="52" height="52" rx="14" fill="url(#bg-{key})" stroke="{BORDER}" stroke-width="1.5"/>
<rect x="8.5" y="8.5" width="47" height="4" rx="2" fill="{ACCENT2}" fill-opacity="0.25"/>
{body}
</svg>'''

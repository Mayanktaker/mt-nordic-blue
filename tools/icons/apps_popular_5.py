# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Popular app icons, batch 5: photo tools, music players and media viewers.

try:
    from apps_popular_common import tile, ACCENT, ACCENT2, SNOW, GOLD, RED, GREEN, PURPLE, ORANGE, TILE_FILL
except ImportError:
    from tools.icons.apps_popular_common import tile, ACCENT, ACCENT2, SNOW, GOLD, RED, GREEN, PURPLE, ORANGE, TILE_FILL

POPULAR_ICONS_5 = {
    # PhotoFlare — photo with sparkle
    "photoflare": tile("photoflare", f'''
<rect x="13" y="20" width="34" height="26" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<circle cx="22" cy="28" r="3" fill="{GOLD}"/>
<polygon points="16,42 25,31 32,38 37,33 45,42" fill="{ACCENT}"/>
<path d="M 47 16 L 49 21 L 54 23 L 49 25 L 47 30 L 45 25 L 40 23 L 45 21 Z" fill="{ACCENT2}"/>'''),

    # nomacs — image viewer frame
    "nomacs": tile("nomacs", f'''
<rect x="12" y="18" width="40" height="30" rx="3" fill="{TILE_FILL}" stroke="{ACCENT2}" stroke-width="2"/>
<circle cx="22" cy="27" r="3" fill="{GOLD}"/>
<polygon points="15,44 26,30 34,38 39,32 49,44" fill="{ACCENT2}"/>
<path d="M 40 46 L 46 40 L 50 44 L 44 50 Z" fill="{ACCENT}"/>'''),

    # Gwenview — framed landscape
    "gwenview": tile("gwenview", f'''
<rect x="12" y="18" width="40" height="30" rx="3" fill="none" stroke="{ACCENT}" stroke-width="2.2"/>
<circle cx="23" cy="27" r="3" fill="{ACCENT2}"/>
<polygon points="15,44 27,30 35,38 40,32 49,44" fill="{ACCENT}" fill-opacity="0.7"/>
<rect x="20" y="46" width="24" height="3" rx="1.5" fill="{ACCENT2}"/>'''),

    # digiKam — camera with lens
    "digikam": tile("digikam", f'''
<rect x="12" y="22" width="40" height="24" rx="4" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<circle cx="32" cy="34" r="8" fill="none" stroke="{ACCENT2}" stroke-width="2.2"/>
<circle cx="32" cy="34" r="3" fill="{ACCENT2}"/>
<rect x="24" y="17" width="12" height="5" rx="2" fill="{ACCENT}"/>'''),

    # Converseen — convert arrows
    "converseen": tile("converseen", f'''
<rect x="12" y="16" width="18" height="16" rx="2.5" fill="none" stroke="{ACCENT2}" stroke-width="2"/>
<rect x="34" y="32" width="18" height="16" rx="2.5" fill="none" stroke="{ACCENT}" stroke-width="2"/>
<path d="M 30 24 C 38 24 40 26 44 28" stroke="{GOLD}" stroke-width="2.2" fill="none" stroke-linecap="round"/>
<path d="M 41 25 L 45 28 L 41 31" stroke="{GOLD}" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'''),

    # SVG Cleaner — broom on vector curve
    "svgcleaner": tile("svgcleaner", f'''
<path d="M 14 46 C 22 26 36 22 50 20" stroke="{ACCENT}" stroke-width="2.2" fill="none" stroke-linecap="round"/>
<circle cx="14" cy="46" r="3" fill="{ACCENT2}"/>
<circle cx="50" cy="20" r="3" fill="{ACCENT2}"/>
<path d="M 40 28 L 48 36 M 44 24 L 52 32" stroke="{GOLD}" stroke-width="2.4" stroke-linecap="round"/>'''),

    # Curtail — crop frame with arrows
    "curtail": tile("curtail", f'''
<path d="M 20 12 L 20 44 L 52 44" stroke="{ACCENT}" stroke-width="2.4" fill="none" stroke-linecap="round"/>
<path d="M 12 20 L 44 20 L 44 52" stroke="{ACCENT2}" stroke-width="2.4" fill="none" stroke-linecap="round"/>
<rect x="26" y="26" width="12" height="12" fill="{ACCENT}" fill-opacity="0.3" stroke="{ACCENT}" stroke-width="1.6"/>'''),

    # Metadata Cleaner — tag with eraser
    "MetadataCleaner": tile("metadataCleaner", f'''
<path d="M 14 22 L 32 14 L 50 22 L 50 42 L 32 50 L 14 42 Z" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2" stroke-linejoin="round"/>
<circle cx="24" cy="28" r="2.4" fill="{ACCENT2}"/>
<path d="M 26 38 L 40 24" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>'''),

    # Totem — video player
    "totem": tile("totem", f'''
<rect x="12" y="18" width="40" height="28" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2"/>
<polygon points="27,24 27,40 41,32" fill="{ACCENT}"/>
<rect x="24" y="48" width="16" height="3" rx="1.5" fill="{ACCENT2}"/>'''),

    # Rhythmbox — music note in ring
    "rhythmbox": tile("rhythmbox", f'''
<circle cx="32" cy="32" r="16" fill="none" stroke="{ACCENT}" stroke-width="2.2"/>
<rect x="36" y="22" width="2.2" height="14" rx="1.1" fill="{ACCENT2}"/>
<ellipse cx="34" cy="36" rx="3.8" ry="3" fill="{ACCENT2}"/>
<path d="M 38 22 C 41 22.6 43 24.6 43 27 L 41 26.6 C 41 25.2 40 24.2 38 23.8 Z" fill="{ACCENT}"/>'''),

    # Audacious — headphones with note
    "audacious": tile("audacious", f'''
<path d="M 16 38 L 16 30 C 16 22 23 16 32 16 C 41 16 48 22 48 30 L 48 38" fill="none" stroke="{ACCENT}" stroke-width="2.6" stroke-linecap="round"/>
<rect x="12" y="34" width="8" height="15" rx="3" fill="{ACCENT2}"/>
<rect x="44" y="34" width="8" height="15" rx="3" fill="{ACCENT2}"/>
<circle cx="32" cy="31" r="4" fill="{ACCENT}"/>'''),

    # Elisa — wave bars in circle
    "elisa": tile("elisa", f'''
<circle cx="32" cy="32" r="16" fill="none" stroke="{ACCENT}" stroke-width="2"/>
<g fill="{ACCENT2}">
<rect x="21" y="28" width="3" height="8" rx="1.5"/>
<rect x="27" y="24" width="3" height="16" rx="1.5"/>
<rect x="33" y="27" width="3" height="10" rx="1.5"/>
<rect x="39" y="25" width="3" height="14" rx="1.5"/>
</g>'''),

    # Clementine — orange with leaf
    "clementine": tile("clementine", f'''
<circle cx="32" cy="34" r="13" fill="{ORANGE}"/>
<path d="M 32 21 C 33 16 37 14 42 14 C 42 19 38 22 32 21 Z" fill="{GREEN}"/>'''),

    # Strawberry — berry with notes
    "strawberry": tile("strawberry", f'''
<path d="M 32 20 C 42 20 46 28 42 38 C 39 45 35 48 32 48 C 29 48 25 45 22 38 C 18 28 22 20 32 20 Z" fill="{RED}"/>
<path d="M 26 18 L 32 14 L 38 18 L 32 22 Z" fill="{GREEN}"/>
<g fill="{SNOW}"><circle cx="27" cy="30" r="1.2"/><circle cx="33" cy="28" r="1.2"/><circle cx="37" cy="33" r="1.2"/><circle cx="29" cy="37" r="1.2"/><circle cx="35" cy="40" r="1.2"/></g>'''),

    # Lollypop — lollipop swirl
    "lollypop": tile("lollypop", f'''
<circle cx="32" cy="26" r="12" fill="none" stroke="{ACCENT}" stroke-width="2.4"/>
<path d="M 32 14 A 12 12 0 0 1 32 38 A 6 6 0 0 1 32 26 A 6 6 0 0 0 32 14" fill="{ACCENT2}" fill-opacity="0.5"/>
<path d="M 32 38 L 32 52" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>'''),

    # Amberol — play ring
    "amberol": tile("amberol", f'''
<circle cx="32" cy="32" r="15" fill="{GOLD}" fill-opacity="0.18" stroke="{GOLD}" stroke-width="2.4"/>
<polygon points="28,24 28,40 40,32" fill="{GOLD}"/>'''),

    # Quod Libet — layered music list
    "quodlibet": tile("quodlibet", f'''
<rect x="13" y="16" width="38" height="9" rx="2.5" fill="{ACCENT}" fill-opacity="0.8"/>
<rect x="13" y="28" width="38" height="9" rx="2.5" fill="{ACCENT2}" fill-opacity="0.8"/>
<rect x="13" y="40" width="26" height="9" rx="2.5" fill="{ACCENT}" fill-opacity="0.5"/>
<circle cx="46" cy="46" r="2.4" fill="{GOLD}"/>'''),

    # Cantata — MPD client with notes
    "cantata": tile("cantata", f'''
<circle cx="32" cy="32" r="15" fill="none" stroke="{ACCENT2}" stroke-width="2"/>
<path d="M 25 40 L 25 26 L 39 22 L 39 36" stroke="{ACCENT}" stroke-width="2.2" fill="none" stroke-linecap="round"/>
<circle cx="22.5" cy="40" r="3" fill="{ACCENT}"/>
<circle cx="36.5" cy="36" r="3" fill="{ACCENT}"/>'''),

    # MuseScore — treble clef-ish note
    "musescore": tile("musescore", f'''
<path d="M 34 16 C 28 22 28 30 32 36 C 35 41 34 46 30 46 C 27 46 25 43 26 40" stroke="{ACCENT}" stroke-width="2.4" fill="none" stroke-linecap="round"/>
<ellipse cx="35" cy="46" rx="6" ry="4.4" fill="{ACCENT2}" transform="rotate(-20 35 46)"/>'''),

    # LMMS — waveform steps
    "lmms": tile("lmms", f'''
<g fill="{ACCENT2}">
<rect x="12" y="34" width="5" height="14" rx="1.5"/>
<rect x="20" y="28" width="5" height="20" rx="1.5"/>
<rect x="28" y="18" width="5" height="30" rx="1.5"/>
<rect x="36" y="26" width="5" height="22" rx="1.5"/>
<rect x="44" y="32" width="5" height="16" rx="1.5"/>
</g>
<circle cx="30.5" cy="14" r="2.4" fill="{GOLD}"/>'''),

    # K3b — optical disc with flame
    "k3b": tile("k3b", f'''
<circle cx="30" cy="32" r="14" fill="none" stroke="{ACCENT}" stroke-width="2.2"/>
<circle cx="30" cy="32" r="4" fill="{ACCENT2}"/>
<path d="M 44 40 C 48 36 50 31 49 26 C 45 29 43 31 42 35 C 40 32 40 29 41 27 C 37 30 36 35 38 39 C 40 43 42 43 44 40 Z" fill="{ORANGE}"/>'''),

    # Brasero — disc with spark
    "brasero": tile("brasero", f'''
<circle cx="32" cy="32" r="15" fill="{TILE_FILL}" stroke="{ACCENT2}" stroke-width="2.2"/>
<circle cx="32" cy="32" r="4.4" fill="{ACCENT}"/>
<path d="M 22 24 A 14 14 0 0 1 42 24" stroke="{ACCENT}" stroke-width="2" fill="none" stroke-linecap="round"/>
<path d="M 44 40 L 47 45 L 52 46 L 48 50 L 49 55 L 44 52 L 39 55 L 40 50 L 36 46 L 41 45 Z" fill="{GOLD}"/>'''),

    # EasyTAG — tag with note
    "easytag": tile("easytag", f'''
<path d="M 14 22 L 32 14 L 50 22 L 50 42 L 32 50 L 14 42 Z" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2" stroke-linejoin="round"/>
<circle cx="24" cy="28" r="2.2" fill="{ACCENT2}"/>
<path d="M 32 26 L 32 38" stroke="{ACCENT2}" stroke-width="2"/>
<ellipse cx="29.5" cy="38" rx="3" ry="2.4" fill="{ACCENT2}"/>'''),

    # Kid3 — ID3 tag
    "kid3": tile("kid3", f'''
<path d="M 14 22 L 32 14 L 50 22 L 50 42 L 32 50 L 14 42 Z" fill="{TILE_FILL}" stroke="{GOLD}" stroke-width="2.2" stroke-linejoin="round"/>
<text x="32" y="40" font-size="14" font-weight="bold" fill="{GOLD}" text-anchor="middle" font-family="sans-serif">ID3</text>'''),

    # Puddletag — tag with pencil
    "puddletag": tile("puddletag", f'''
<path d="M 14 22 L 32 14 L 50 22 L 50 42 L 32 50 L 14 42 Z" fill="{TILE_FILL}" stroke="{ACCENT2}" stroke-width="2.2" stroke-linejoin="round"/>
<path d="M 24 34 L 38 20 L 42 24 L 28 38 L 23 39 Z" fill="{ACCENT}"/>'''),

    # SMPlayer — video with equalizer
    "smplayer": tile("smplayer", f'''
<rect x="12" y="18" width="26" height="22" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<polygon points="21,23 21,35 30,29" fill="{ACCENT}"/>
<g fill="{ACCENT2}"><rect x="42" y="26" width="3" height="12" rx="1.5"/><rect x="47" y="20" width="3" height="18" rx="1.5"/></g>'''),

    # Kodi — play in rounded K
    "kodi": tile("kodi", f'''
<circle cx="32" cy="32" r="16" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.4"/>
<path d="M 24 20 L 30 26 L 36 20 L 40 24 L 34 30 L 40 36 L 36 40 L 30 34 L 24 40 L 20 36 L 26 30 L 20 24 Z" fill="{ACCENT}" fill-opacity="0.85"/>
<polygon points="32,27 32,37 40,32" fill="{GOLD}"/>'''),

    # Plex — play in rounded triangle
    "plex": tile("plex", f'''
<path d="M 20 16 L 44 16 L 56 32 L 44 48 L 20 48 L 32 32 Z" fill="{TILE_FILL}" stroke="{GOLD}" stroke-width="2.2" stroke-linejoin="round"/>
<polygon points="34,25 34,39 44,32" fill="{GOLD}"/>'''),

    # Foliate — open ebook
    "foliate": tile("foliate", f'''
<path d="M 12 20 C 20 17 26 19 32 23 C 38 19 44 17 52 20 L 52 46 C 44 43 38 45 32 49 C 26 45 20 43 12 46 Z" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2"/>
<line x1="32" y1="23" x2="32" y2="49" stroke="{ACCENT2}" stroke-width="1.6"/>
<path d="M 36 30 L 46 30 M 36 36 L 44 36 M 36 42 L 46 42" stroke="{ACCENT2}" stroke-width="1.6" stroke-linecap="round"/>'''),

    # Calibre — book with glasses
    "calibre-gui": tile("calibre-gui", f'''
<path d="M 16 16 L 40 16 L 48 24 L 48 50 L 16 50 Z" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2"/>
<path d="M 40 16 L 40 24 L 48 24" fill="none" stroke="{ACCENT}" stroke-width="2"/>
<circle cx="26" cy="34" r="5" fill="none" stroke="{ACCENT2}" stroke-width="2"/>
<circle cx="40" cy="34" r="5" fill="none" stroke="{ACCENT2}" stroke-width="2"/>
<line x1="31" y1="34" x2="35" y2="34" stroke="{ACCENT2}" stroke-width="2"/>'''),

    # Calibre Viewer — page with eye
    "calibre-viewer": tile("calibre-viewer", f'''
<rect x="14" y="14" width="36" height="36" rx="3" fill="{TILE_FILL}" stroke="{ACCENT2}" stroke-width="2.2"/>
<path d="M 20 30 C 24 24 40 24 44 30 C 40 36 24 36 20 30 Z" fill="none" stroke="{ACCENT}" stroke-width="2"/>
<circle cx="32" cy="30" r="3" fill="{ACCENT}"/>
<line x1="20" y1="42" x2="44" y2="42" stroke="{ACCENT2}" stroke-width="2" stroke-linecap="round"/>'''),

    # qpdfview — PDF page with magnifier
    "qpdfview": tile("qpdfview", f'''
<rect x="14" y="12" width="30" height="36" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<rect x="20" y="20" width="18" height="6" rx="2" fill="{RED}" fill-opacity="0.8"/>
<line x1="20" y1="32" x2="38" y2="32" stroke="{ACCENT2}" stroke-width="1.8"/>
<line x1="20" y1="38" x2="34" y2="38" stroke="{ACCENT2}" stroke-width="1.8"/>
<circle cx="42" cy="40" r="5" fill="none" stroke="{ACCENT2}" stroke-width="2.2"/>
<line x1="46" y1="44" x2="51" y2="49" stroke="{ACCENT2}" stroke-width="2.4" stroke-linecap="round"/>'''),
}

POPULAR_ALIASES_5 = {
    "photoflare-app": "photoflare",
    "nomacs-app": "nomacs",
    "gwenview-app": "gwenview",
    "digikam-app": "digikam",
    "converseen-app": "converseen",
    "svgcleaner-app": "svgcleaner",
    "fr.romainvigier.MetadataCleaner": "MetadataCleaner",
    "totem-video": "totem",
    "rhythmbox-app": "rhythmbox",
    "audacious-app": "audacious",
    "elisa-app": "elisa",
    "clementine-app": "clementine",
    "strawberry-app": "strawberry",
    "lollypop-app": "lollypop",
    "io.bassi.Amberol": "amberol",
    "quodlibet-app": "quodlibet",
    "cantata-app": "cantata",
    "musescore-app": "musescore",
    "lmms-app": "lmms",
    "k3b-app": "k3b",
    "brasero-app": "brasero",
    "easytag-app": "easytag",
    "kid3-app": "kid3",
    "puddletag-app": "puddletag",
    "smplayer-app": "smplayer",
    "kodi-app": "kodi",
    "tv.plex.PlexDesktop": "plex",
    "foliate-app": "foliate",
    "calibre": "calibre-gui",
    "calibre-ebook-viewer": "calibre-viewer",
    "qpdfview-app": "qpdfview",
}

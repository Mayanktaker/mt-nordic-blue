# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Popular app icons, batch 1: web browsers and internet tools.

try:
    from apps_popular_common import tile, ACCENT, ACCENT2, SNOW, GOLD, RED, GREEN, PURPLE, ORANGE, TILE_FILL
except ImportError:
    from tools.icons.apps_popular_common import tile, ACCENT, ACCENT2, SNOW, GOLD, RED, GREEN, PURPLE, ORANGE, TILE_FILL

POPULAR_ICONS_1 = {
    # Brave — shield with inner chevron
    "brave": tile("brave", f'''
<path d="M 32 13 L 46 18 L 46 32 C 46 41 39 48 32 51 C 25 48 18 41 18 32 L 18 18 Z" fill="none" stroke="{ORANGE}" stroke-width="2.5" stroke-linejoin="round"/>
<path d="M 26 29 L 32 42 L 38 29 L 32 25 Z" fill="{ORANGE}"/>'''),

    # Opera — brand ring
    "opera": tile("opera", f'''
<circle cx="32" cy="32" r="15" fill="none" stroke="{RED}" stroke-width="4"/>
<circle cx="32" cy="32" r="6" fill="{RED}"/>'''),

    # Vivaldi — V inside ring
    "vivaldi": tile("vivaldi", f'''
<circle cx="32" cy="32" r="16" fill="none" stroke="{ACCENT2}" stroke-width="2"/>
<path d="M 21 20 L 32 46 L 43 20" fill="none" stroke="{RED}" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>'''),

    # qutebrowser — window frame with magnifier handle
    "qutebrowser": tile("qutebrowser", f'''
<rect x="15" y="18" width="34" height="30" rx="4" fill="none" stroke="{ACCENT}" stroke-width="2.5"/>
<circle cx="28" cy="30" r="5" fill="none" stroke="{ACCENT2}" stroke-width="2.5"/>
<line x1="32" y1="34" x2="39" y2="41" stroke="{ACCENT2}" stroke-width="2.5" stroke-linecap="round"/>'''),

    # LibreWolf — wolf head with ears
    "librewolf": tile("librewolf", f'''
<path d="M 19 19 L 26 28 L 38 28 L 45 19 L 45 37 C 45 45 39 50 32 50 C 25 50 19 45 19 37 Z" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2" stroke-linejoin="round"/>
<circle cx="27" cy="35" r="2.2" fill="{SNOW}"/>
<circle cx="37" cy="35" r="2.2" fill="{SNOW}"/>
<path d="M 29 42 L 32 45 L 35 42" stroke="{ACCENT2}" stroke-width="2" fill="none" stroke-linecap="round"/>'''),

    # Floorp — flame
    "floorp": tile("floorp", f'''
<path d="M 32 12 C 36 21 45 24 45 34 C 45 42 39 49 32 49 C 25 49 19 42 19 34 C 19 27 25 24 27 16 C 28.5 21 31 23 33 24 C 33 20 32 16 32 12 Z" fill="{ORANGE}"/>
<path d="M 32 30 C 34 34 37 35 37 39 C 37 42 35 44 32 44 C 29 44 27 42 27 39 C 27 35 30 34 32 30 Z" fill="{GOLD}"/>'''),

    # Waterfox — ring with wave
    "waterfox": tile("waterfox", f'''
<circle cx="32" cy="32" r="15" fill="none" stroke="{ACCENT}" stroke-width="2.5"/>
<path d="M 19 32 C 23 27 27 37 31 32 C 35 27 39 37 45 32" stroke="{ACCENT2}" stroke-width="2.8" fill="none" stroke-linecap="round"/>'''),

    # Yandex browser — Y letterform
    "yandex-browser": tile("yandex-browser", f'''
<circle cx="32" cy="32" r="16" fill="none" stroke="{ACCENT2}" stroke-width="2"/>
<path d="M 27 17 L 37 33 L 37 48 M 43 17 L 26 34" stroke="{RED}" stroke-width="3.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'''),

    # Firefox Developer — flame with code brackets
    "firefox-developer-icon": tile("firefox-developer-icon", f'''
<circle cx="32" cy="32" r="15" fill="{ORANGE}" fill-opacity="0.22" stroke="{ORANGE}" stroke-width="2.2"/>
<path d="M 25 27 L 20 32 L 25 37 M 39 27 L 44 32 L 39 37" stroke="{SNOW}" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'''),

    # FreeTube — play screen with signal
    "freetube": tile("freetube", f'''
<rect x="13" y="19" width="30" height="25" rx="5" fill="{TILE_FILL}" stroke="{RED}" stroke-width="2.2"/>
<polygon points="26,26 26,38 35,32" fill="{RED}"/>
<path d="M 47 26 C 50 29 50 36 47 39" stroke="{ACCENT2}" stroke-width="2.2" fill="none" stroke-linecap="round"/>'''),

    # Stremio — play in ring
    "stremio": tile("stremio", f'''
<circle cx="32" cy="32" r="15" fill="none" stroke="{PURPLE}" stroke-width="2.5"/>
<polygon points="28,25 28,39 39,32" fill="{PURPLE}"/>'''),

    # Jellyfin — diamond stack
    "jellyfin": tile("jellyfin", f'''
<path d="M 32 13 L 45 33 L 32 47 L 19 33 Z" fill="none" stroke="{PURPLE}" stroke-width="2.5" stroke-linejoin="round"/>
<path d="M 32 22 L 39 33 L 32 41 L 25 33 Z" fill="{PURPLE}" fill-opacity="0.55"/>'''),

    # Popcorn Time — popcorn bucket
    "popcorntime": tile("popcorntime", f'''
<circle cx="25" cy="23" r="4" fill="{GOLD}"/>
<circle cx="32" cy="20" r="4.6" fill="{SNOW}"/>
<circle cx="39" cy="23" r="4" fill="{GOLD}"/>
<path d="M 22 26 L 42 26 L 39 48 L 25 48 Z" fill="{TILE_FILL}" stroke="{GOLD}" stroke-width="2" stroke-linejoin="round"/>'''),

    # Tixati — magnet
    "tixati": tile("tixati", f'''
<path d="M 22 18 L 22 33 C 22 41 26 47 32 47 C 38 47 42 41 42 33 L 42 18 L 36 18 L 36 33 C 36 38 34 41 32 41 C 30 41 28 38 28 33 L 28 18 Z" fill="{ACCENT2}"/>'''),

    # Motrix — rocket
    "motrix": tile("motrix", f'''
<path d="M 32 12 C 39 18 42 26 42 34 L 37 44 L 27 44 L 22 34 C 22 26 25 18 32 12 Z" fill="none" stroke="{ACCENT}" stroke-width="2.5" stroke-linejoin="round"/>
<circle cx="32" cy="27" r="3.5" fill="{ACCENT}"/>
<path d="M 27 44 L 25 50 M 37 44 L 39 50" stroke="{ORANGE}" stroke-width="2.5" stroke-linecap="round"/>'''),

    # XDM — framed download arrow
    "xdman": tile("xdman", f'''
<rect x="14" y="16" width="36" height="32" rx="4" fill="none" stroke="{ACCENT}" stroke-width="2"/>
<path d="M 32 23 L 32 36" stroke="{ACCENT2}" stroke-width="2.5" stroke-linecap="round"/>
<path d="M 26 31 L 32 37 L 38 31" stroke="{ACCENT2}" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<line x1="24" y1="42" x2="40" y2="42" stroke="{ACCENT}" stroke-width="2.5" stroke-linecap="round"/>'''),

    # Free Download Manager — arrow into tray
    "freedownloadmanager": tile("freedownloadmanager", f'''
<path d="M 32 13 L 32 34" stroke="{ACCENT}" stroke-width="3.5" stroke-linecap="round"/>
<path d="M 24 27 L 32 36 L 40 27" stroke="{ACCENT}" stroke-width="3.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M 18 37 L 18 47 L 46 47 L 46 37" stroke="{ACCENT2}" stroke-width="2.5" fill="none" stroke-linecap="round"/>'''),

    # Persepolis — shield with download arrow
    "persepolis": tile("persepolis", f'''
<path d="M 32 13 L 45 17 L 45 30 C 45 40 39 46 32 50 C 25 46 19 40 19 30 L 19 17 Z" fill="none" stroke="{ACCENT}" stroke-width="2.5" stroke-linejoin="round"/>
<path d="M 32 23 L 32 36 M 27 31 L 32 37 L 37 31" stroke="{ACCENT2}" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'''),

    # JDownloader — arrow into golden tray
    "jdownloader": tile("jdownloader", f'''
<path d="M 32 13 L 32 34" stroke="{ACCENT2}" stroke-width="3.5" stroke-linecap="round"/>
<path d="M 24 27 L 32 36 L 40 27" stroke="{ACCENT2}" stroke-width="3.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M 18 38 L 18 47 L 46 47 L 46 38" stroke="{GOLD}" stroke-width="3" fill="none" stroke-linecap="round"/>'''),

    # Remmina — overlapping screens
    "remmina": tile("remmina", f'''
<rect x="12" y="19" width="23" height="16" rx="3" fill="none" stroke="{ACCENT2}" stroke-width="2"/>
<rect x="29" y="29" width="23" height="16" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<line x1="18" y1="41" x2="24" y2="41" stroke="{ACCENT2}" stroke-width="2" stroke-linecap="round"/>'''),

    # RustDesk — monitor with cursor
    "rustdesk": tile("rustdesk", f'''
<rect x="14" y="17" width="36" height="25" rx="3" fill="none" stroke="{ACCENT}" stroke-width="2.5"/>
<path d="M 26 42 L 26 48 L 38 48" stroke="{ACCENT}" stroke-width="2.5" fill="none" stroke-linecap="round"/>
<path d="M 30 23 L 30 38 L 34 34 L 38 41 L 41 39 L 37 33 L 42 33 Z" fill="{SNOW}"/>'''),

    # TeamViewer — dual arrows in ring
    "teamviewer": tile("teamviewer", f'''
<circle cx="32" cy="32" r="15" fill="none" stroke="{ACCENT}" stroke-width="2.5"/>
<path d="M 22 27 C 26 22 38 22 42 27 M 42 37 C 38 42 26 42 22 37" stroke="{ACCENT2}" stroke-width="2.5" fill="none" stroke-linecap="round"/>'''),

    # LocalSend — device pair with transfer arrow
    "localsend": tile("localsend", f'''
<rect x="13" y="19" width="12" height="21" rx="2.5" fill="none" stroke="{ACCENT2}" stroke-width="2"/>
<rect x="31" y="26" width="19" height="13" rx="2" fill="none" stroke="{ACCENT}" stroke-width="2"/>
<path d="M 25 31 L 30 31 M 27 28 L 30 31 L 27 34" stroke="{GOLD}" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'''),

    # Warpinator — swap arrows
    "warpinator": tile("warpinator", f'''
<path d="M 19 27 L 41 27 M 37 22 L 42 27 L 37 32" stroke="{ACCENT}" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M 45 38 L 23 38 M 27 33 L 22 38 L 27 43" stroke="{ACCENT2}" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'''),

    # Syncthing — circular sync arrows
    "syncthing-gtk": tile("syncthing-gtk", f'''
<path d="M 32 17 A 15 15 0 0 1 47 32" stroke="{ACCENT}" stroke-width="2.8" fill="none" stroke-linecap="round"/>
<path d="M 32 47 A 15 15 0 0 1 17 32" stroke="{ACCENT}" stroke-width="2.8" fill="none" stroke-linecap="round"/>
<polygon points="41,15 47,20 40,23" fill="{ACCENT}"/>
<polygon points="23,49 17,44 24,41" fill="{ACCENT}"/>'''),

    # SimpleX Chat — locked bubble
    "simplex-chat": tile("simplex-chat", f'''
<path d="M 16 20 L 48 20 L 48 40 L 28 40 L 20 48 L 20 40 L 16 40 Z" fill="none" stroke="{ACCENT}" stroke-width="2.4" stroke-linejoin="round"/>
<rect x="26" y="26" width="12" height="9" rx="2" fill="{GOLD}"/>
<path d="M 29 26 L 29 24 C 29 22 31 20.6 32.5 20.6 C 34 20.6 35 22 35 24 L 35 26" stroke="{GOLD}" stroke-width="2" fill="none"/>'''),

    # Element — bubble with asterisk core
    "element-desktop": tile("element-desktop", f'''
<path d="M 16 20 L 48 20 L 48 40 L 28 40 L 20 48 L 20 40 L 16 40 Z" fill="none" stroke="{GREEN}" stroke-width="2.4" stroke-linejoin="round"/>
<circle cx="32" cy="30" r="5" fill="{GREEN}"/>
<circle cx="32" cy="30" r="1.8" fill="{TILE_FILL}"/>'''),

    # Fractal — message with text lines
    "fractal": tile("fractal", f'''
<path d="M 16 20 L 48 20 L 48 40 L 28 40 L 20 48 L 20 40 L 16 40 Z" fill="none" stroke="{ACCENT2}" stroke-width="2.4" stroke-linejoin="round"/>
<line x1="22" y1="27" x2="42" y2="27" stroke="{ACCENT2}" stroke-width="2" stroke-linecap="round"/>
<line x1="22" y1="33" x2="34" y2="33" stroke="{ACCENT2}" stroke-width="2" stroke-linecap="round"/>'''),

    # WeeChat — terminal with prompt
    "weechat": tile("weechat", f'''
<rect x="13" y="18" width="38" height="28" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2"/>
<path d="M 19 26 L 23 30 L 19 34" stroke="{ACCENT2}" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<line x1="26" y1="34" x2="33" y2="34" stroke="{ACCENT2}" stroke-width="2.2" stroke-linecap="round"/>
<path d="M 44 46 L 48 51" stroke="{ACCENT}" stroke-width="2.2" stroke-linecap="round"/>'''),

    # HexChat — bubble with hash
    "hexchat": tile("hexchat", f'''
<path d="M 16 20 L 48 20 L 48 40 L 28 40 L 20 48 L 20 40 L 16 40 Z" fill="none" stroke="{ACCENT2}" stroke-width="2.4" stroke-linejoin="round"/>
<text x="32" y="35" font-size="15" font-weight="bold" fill="{ACCENT}" text-anchor="middle" font-family="sans-serif">#</text>'''),

    # Pidgin — bubble with person
    "pidgin": tile("pidgin", f'''
<path d="M 16 19 L 48 19 L 48 39 L 28 39 L 20 47 L 20 39 L 16 39 Z" fill="none" stroke="{PURPLE}" stroke-width="2.4" stroke-linejoin="round"/>
<circle cx="32" cy="26" r="3.6" fill="{PURPLE}"/>
<path d="M 25 36 C 25 31.5 28 30 32 30 C 36 30 39 31.5 39 36 Z" fill="{PURPLE}"/>'''),

    # Polari — bubble with globe
    "polari": tile("polari", f'''
<path d="M 16 20 L 48 20 L 48 40 L 28 40 L 20 48 L 20 40 L 16 40 Z" fill="none" stroke="{ACCENT}" stroke-width="2.4" stroke-linejoin="round"/>
<circle cx="32" cy="30" r="6" fill="none" stroke="{ACCENT2}" stroke-width="1.8"/>
<ellipse cx="32" cy="30" rx="2.6" ry="6" fill="none" stroke="{ACCENT2}" stroke-width="1.2"/>
<line x1="26" y1="30" x2="38" y2="30" stroke="{ACCENT2}" stroke-width="1.2"/>'''),
}

# Aliases for batch 1 (alternate desktop entry names).
POPULAR_ALIASES_1 = {
    "brave-browser": "brave",
    "brave-beta": "brave",
    "brave-dev": "brave",
    "brave-nightly": "brave",
    "opera-beta": "opera",
    "opera-stable": "opera",
    "vivaldi-stable": "vivaldi",
    "browser-tor": "tor-browser",
    "firefox-developer-edition": "firefox-developer-icon",
    "freetube-desktop": "freetube",
    "stremio-desktop": "stremio",
    "io.stremio.Stremio": "stremio",
    "jellyfin-desktop": "jellyfin",
    "popcorn-time": "popcorntime",
    "xdm": "xdman",
    "freedownloadmanager-app": "freedownloadmanager",
    "jd2": "jdownloader",
    "rustdesk-desktop": "rustdesk",
    "teamviewer-desktop": "teamviewer",
    "localsend-app": "localsend",
    "warpinator-app": "warpinator",
    "syncthing": "syncthing-gtk",
    "simplex": "simplex-chat",
    "element": "element-desktop",
    "fractal-client": "fractal",
    "weechat-client": "weechat",
    "hexchat-client": "hexchat",
    "pidgin-im": "pidgin",
    "polari-client": "polari",
}

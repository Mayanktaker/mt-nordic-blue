# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Popular app icons, batch 6: office suites, games and system utilities.

try:
    from apps_popular_common import tile, ACCENT, ACCENT2, SNOW, GOLD, RED, GREEN, PURPLE, ORANGE, TILE_FILL
except ImportError:
    from tools.icons.apps_popular_common import tile, ACCENT, ACCENT2, SNOW, GOLD, RED, GREEN, PURPLE, ORANGE, TILE_FILL

POPULAR_ICONS_6 = {
    # Okular — document with check
    "okular": tile("okular", f'''
<path d="M 16 12 L 40 12 L 48 20 L 48 52 L 16 52 Z" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2"/>
<path d="M 40 12 L 40 20 L 48 20" fill="none" stroke="{ACCENT}" stroke-width="2"/>
<path d="M 23 36 L 29 42 L 41 28" stroke="{GREEN}" stroke-width="2.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'''),

    # Master PDF Editor — PDF page with pen
    "masterpdfeditor": tile("masterpdfeditor", f'''
<rect x="14" y="12" width="30" height="38" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<rect x="20" y="20" width="18" height="7" rx="2" fill="{RED}" fill-opacity="0.85"/>
<line x1="20" y1="33" x2="38" y2="33" stroke="{ACCENT2}" stroke-width="1.8"/>
<path d="M 34 50 L 48 36 L 52 40 L 38 54 L 33 55 Z" fill="{GOLD}"/>'''),

    # Xournal — handwriting on page
    "xournal": tile("xournal", f'''
<rect x="13" y="13" width="38" height="38" rx="3" fill="{TILE_FILL}" stroke="{ACCENT2}" stroke-width="2.2"/>
<path d="M 20 40 C 24 28 28 44 33 32 C 36 24 40 34 44 28" stroke="{ACCENT}" stroke-width="2.4" fill="none" stroke-linecap="round"/>
<line x1="19" y1="46" x2="45" y2="46" stroke="{ACCENT2}" stroke-width="1.8" stroke-linecap="round"/>'''),

    # TeXstudio — T with braces
    "texstudio": tile("texstudio", f'''
<rect x="12" y="14" width="40" height="36" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2"/>
<path d="M 20 22 L 28 22 M 24 22 L 24 42" stroke="{ACCENT2}" stroke-width="2.4" stroke-linecap="round"/>
<path d="M 36 22 L 33 26 L 33 38 L 36 42 M 44 22 L 47 26 L 47 38 L 44 42" stroke="{GOLD}" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'''),

    # Zotero — book with citation quote
    "zotero": tile("zotero", f'''
<rect x="14" y="14" width="36" height="36" rx="4" fill="{TILE_FILL}" stroke="{RED}" stroke-width="2.4"/>
<text x="32" y="42" font-size="22" font-weight="bold" fill="{RED}" text-anchor="middle" font-family="serif">Z</text>'''),

    # GnuCash — coin stack with leaf
    "gnucash-icon": tile("gnucash-icon", f'''
<ellipse cx="32" cy="20" rx="11" ry="4" fill="{GOLD}"/>
<path d="M 21 20 L 21 28 C 21 30.4 26 32 32 32 C 38 32 43 30.4 43 28 L 43 20" fill="{TILE_FILL}" stroke="{GOLD}" stroke-width="1.8"/>
<path d="M 21 30 L 21 38 C 21 40.4 26 42 32 42 C 38 42 43 40.4 43 38 L 43 30" fill="{TILE_FILL}" stroke="{GOLD}" stroke-width="1.8"/>
<circle cx="32" cy="20" r="2" fill="{TILE_FILL}"/>'''),

    # HomeBank — house with coin
    "homebank": tile("homebank", f'''
<path d="M 32 14 L 50 30 L 46 30 L 46 48 L 18 48 L 18 30 L 14 30 Z" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2" stroke-linejoin="round"/>
<circle cx="32" cy="38" r="6" fill="{GOLD}"/>
<text x="32" y="41.5" font-size="9" font-weight="bold" fill="{TILE_FILL}" text-anchor="middle" font-family="sans-serif">$</text>'''),

    # WPS Office — document with W
    "wps-office": tile("wps-office", f'''
<rect x="14" y="12" width="36" height="40" rx="4" fill="{TILE_FILL}" stroke="{RED}" stroke-width="2.4"/>
<path d="M 21 24 L 25 40 L 29 30 L 33 40 L 37 24" stroke="{RED}" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<line x1="22" y1="46" x2="42" y2="46" stroke="{ACCENT2}" stroke-width="1.8" stroke-linecap="round"/>'''),

    # FreeOffice TextMaker — T document
    "freeoffice-textmaker": tile("freeoffice-textmaker", f'''
<rect x="14" y="12" width="36" height="40" rx="4" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2"/>
<path d="M 22 22 L 42 22 M 32 22 L 32 42" stroke="{ACCENT2}" stroke-width="2.8" stroke-linecap="round"/>'''),

    # FreeOffice PlanMaker — spreadsheet grid
    "freeoffice-planmaker": tile("freeoffice-planmaker", f'''
<rect x="12" y="14" width="40" height="36" rx="3" fill="{TILE_FILL}" stroke="{GREEN}" stroke-width="2.2"/>
<line x1="12" y1="24" x2="52" y2="24" stroke="{GREEN}" stroke-width="2"/>
<line x1="25" y1="14" x2="25" y2="50" stroke="{GREEN}" stroke-width="1.4"/>
<line x1="39" y1="14" x2="39" y2="50" stroke="{GREEN}" stroke-width="1.4"/>
<line x1="12" y1="37" x2="52" y2="37" stroke="{GREEN}" stroke-width="1.4"/>'''),

    # FreeOffice Presentations — slide with chart
    "freeoffice-presentations": tile("freeoffice-presentations", f'''
<rect x="12" y="16" width="40" height="26" rx="3" fill="{TILE_FILL}" stroke="{ORANGE}" stroke-width="2.2"/>
<rect x="18" y="32" width="5" height="6" fill="{ORANGE}"/>
<rect x="26" y="27" width="5" height="11" fill="{ORANGE}" fill-opacity="0.7"/>
<rect x="34" y="23" width="5" height="15" fill="{ORANGE}"/>
<rect x="26" y="46" width="12" height="3" rx="1.5" fill="{ACCENT2}"/>'''),

    # 0 A.D. — laurel shield
    "0ad": tile("0ad", f'''
<path d="M 32 12 L 47 18 L 47 34 C 47 43 40 49 32 52 C 24 49 17 43 17 34 L 17 18 Z" fill="{TILE_FILL}" stroke="{GOLD}" stroke-width="2.4"/>
<path d="M 26 30 L 32 38 L 38 30" stroke="{GOLD}" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="32" cy="24" r="2.6" fill="{GOLD}"/>'''),

    # Minetest — voxel blocks
    "minetest": tile("minetest", f'''
<path d="M 20 24 L 32 18 L 44 24 L 44 40 L 32 46 L 20 40 Z" fill="none" stroke="{GREEN}" stroke-width="2.2" stroke-linejoin="round"/>
<path d="M 20 24 L 32 30 L 44 24 M 32 30 L 32 46" stroke="{GREEN}" stroke-width="1.6" fill="none"/>
<rect x="24" y="34" width="6" height="6" fill="{GOLD}" fill-opacity="0.7"/>'''),

    # SuperTuxKart — kart wheel
    "supertuxkart": tile("supertuxkart", f'''
<circle cx="32" cy="34" r="13" fill="none" stroke="{ACCENT}" stroke-width="3"/>
<circle cx="32" cy="34" r="4" fill="{ACCENT2}"/>
<path d="M 32 21 L 32 30 M 21 34 L 28 34 M 43 34 L 36 34 M 32 47 L 32 38" stroke="{ACCENT2}" stroke-width="1.6"/>
<path d="M 20 16 L 44 16" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>'''),

    # SuperTux — penguin
    "supertux": tile("supertux", f'''
<ellipse cx="32" cy="34" rx="13" ry="15" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2"/>
<circle cx="26" cy="28" r="2.6" fill="{SNOW}"/>
<circle cx="38" cy="28" r="2.6" fill="{SNOW}"/>
<circle cx="26" cy="28" r="1.1" fill="{TILE_FILL}"/>
<circle cx="38" cy="28" r="1.1" fill="{TILE_FILL}"/>
<path d="M 29 35 L 35 35 L 32 39 Z" fill="{ORANGE}"/>
<ellipse cx="32" cy="44" rx="7" ry="4" fill="{SNOW}" fill-opacity="0.85"/>'''),

    # Minecraft — grass block
    "minecraft": tile("minecraft", f'''
<rect x="16" y="18" width="32" height="30" rx="2" fill="#5A7A54"/>
<rect x="16" y="18" width="32" height="10" rx="2" fill="{GREEN}"/>
<g fill="#3E5A3A"><rect x="20" y="31" width="6" height="6"/><rect x="30" y="35" width="6" height="6"/><rect x="39" y="30" width="6" height="6"/></g>'''),

    # Factorio — gear with arrow
    "factorio": tile("factorio", f'''
<circle cx="30" cy="32" r="11" fill="none" stroke="{ORANGE}" stroke-width="3"/>
<circle cx="30" cy="32" r="3.6" fill="{ORANGE}"/>
<path d="M 30 19 L 30 14 M 30 45 L 30 50 M 17 32 L 12 32 M 43 32 L 48 32" stroke="{ORANGE}" stroke-width="2.6" stroke-linecap="round"/>
<path d="M 40 44 L 50 34 L 54 38 L 44 48 Z" fill="{ACCENT2}"/>'''),

    # PPSSPP — handheld console
    "ppsspp": tile("ppsspp", f'''
<rect x="10" y="22" width="44" height="24" rx="10" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2"/>
<rect x="22" y="26" width="20" height="16" rx="2" fill="#0A1018" stroke="{ACCENT2}" stroke-width="1.6"/>
<circle cx="17" cy="34" r="3" fill="{ACCENT2}"/>
<circle cx="47" cy="30" r="2.2" fill="{GOLD}"/>
<circle cx="47" cy="38" r="2.2" fill="{RED}"/>'''),

    # Dolphin Emulator — dolphin arc
    "dolphin-emu": tile("dolphin-emu", f'''
<path d="M 16 40 C 16 26 26 16 42 16 C 46 16 50 18 52 21 C 48 22 45 24 43 28 C 41 32 40 36 36 40 C 32 44 26 46 20 46 C 18 46 16 44 16 40 Z" fill="none" stroke="{ACCENT}" stroke-width="2.4"/>
<circle cx="38" cy="24" r="1.8" fill="{ACCENT2}"/>
<path d="M 20 46 C 24 42 28 40 32 40" stroke="{ACCENT2}" stroke-width="2" fill="none"/>'''),

    # DOSBox — terminal with floppy
    "dosbox": tile("dosbox", f'''
<rect x="12" y="16" width="40" height="30" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<path d="M 18 24 L 22 28 L 18 32" stroke="{ACCENT2}" stroke-width="2" fill="none" stroke-linecap="round"/>
<line x1="25" y1="32" x2="32" y2="32" stroke="{ACCENT2}" stroke-width="2" stroke-linecap="round"/>
<rect x="36" y="24" width="10" height="10" rx="1.5" fill="{GOLD}" fill-opacity="0.8"/>'''),

    # GNOME Tweaks — sliders
    "gnome-tweak-tool": tile("gnome-tweak-tool", f'''
<line x1="16" y1="22" x2="48" y2="22" stroke="{ACCENT2}" stroke-width="2.4" stroke-linecap="round"/>
<line x1="16" y1="32" x2="48" y2="32" stroke="{ACCENT2}" stroke-width="2.4" stroke-linecap="round"/>
<line x1="16" y1="42" x2="48" y2="42" stroke="{ACCENT2}" stroke-width="2.4" stroke-linecap="round"/>
<circle cx="38" cy="22" r="4" fill="{ACCENT}"/>
<circle cx="24" cy="32" r="4" fill="{ACCENT}"/>
<circle cx="42" cy="42" r="4" fill="{ACCENT}"/>'''),

    # GNOME Usage — gauge
    "gnome-usage": tile("gnome-usage", f'''
<path d="M 16 40 A 16 16 0 0 1 48 40" fill="none" stroke="{ACCENT2}" stroke-width="3" stroke-linecap="round"/>
<path d="M 32 40 L 42 26" stroke="{ACCENT}" stroke-width="3" stroke-linecap="round"/>
<circle cx="32" cy="40" r="3" fill="{ACCENT}"/>'''),

    # Mission Center — gauge with dial
    "io.missioncenter.MissionCenter": tile("missioncenter", f'''
<circle cx="32" cy="34" r="15" fill="none" stroke="{ACCENT}" stroke-width="2.4"/>
<path d="M 32 34 L 40 24" stroke="{ACCENT}" stroke-width="2.6" stroke-linecap="round"/>
<circle cx="32" cy="34" r="3" fill="{ACCENT}"/>
<path d="M 22 44 L 42 44" stroke="{ACCENT2}" stroke-width="2" stroke-linecap="round"/>'''),

    # Stacer — system sweep brush
    "stacer": tile("stacer", f'''
<path d="M 18 46 L 34 30" stroke="{ACCENT}" stroke-width="3" stroke-linecap="round"/>
<path d="M 32 28 L 44 16 L 50 22 L 38 34 Z" fill="{ACCENT2}"/>
<path d="M 16 40 L 22 46" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>'''),

    # BleachBit — broom with sparkles
    "bleachbit": tile("bleachbit", f'''
<path d="M 42 14 L 20 36 L 16 48 L 28 44 L 50 22 Z" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2" stroke-linejoin="round"/>
<path d="M 16 48 L 22 42 M 20 50 L 26 44" stroke="{ACCENT2}" stroke-width="2" stroke-linecap="round"/>
<path d="M 44 38 L 46 42 L 50 44 L 46 46 L 44 50 L 42 46 L 38 44 L 42 42 Z" fill="{GOLD}"/>'''),

    # Partition Manager — disk with divider
    "partitionmanager": tile("partitionmanager", f'''
<rect x="12" y="20" width="40" height="24" rx="4" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2"/>
<line x1="30" y1="20" x2="30" y2="44" stroke="{ACCENT2}" stroke-width="2.2"/>
<line x1="20" y1="32" x2="26" y2="32" stroke="{ACCENT2}" stroke-width="1.8" stroke-linecap="round"/>
<circle cx="40" cy="32" r="4" fill="{ACCENT}"/>'''),

    # USB Creator — stick with arrow
    "usb-creator": tile("usb-creator", f'''
<rect x="22" y="16" width="14" height="10" rx="2" fill="{ACCENT2}"/>
<path d="M 24 26 L 24 46 C 24 48 26 50 29 50 C 32 50 34 48 34 46 L 34 26 Z" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<path d="M 44 22 L 44 42 M 39 37 L 44 43 L 49 37" stroke="{GOLD}" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'''),

    # Ventoy — disk with arrow
    "ventoy": tile("ventoy", f'''
<circle cx="30" cy="34" r="13" fill="none" stroke="{ACCENT}" stroke-width="2.4"/>
<circle cx="30" cy="34" r="3.4" fill="{ACCENT2}"/>
<path d="M 44 22 L 44 40 M 39 35 L 44 41 L 49 35" stroke="{GOLD}" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'''),

    # Etcher — SD card with flash
    "etcher": tile("etcher", f'''
<path d="M 20 14 L 38 14 L 44 20 L 44 50 L 20 50 Z" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2"/>
<path d="M 38 14 L 38 20 L 44 20" fill="none" stroke="{ACCENT}" stroke-width="2"/>
<path d="M 36 26 L 27 38 L 33 38 L 29 46 L 39 34 L 33 34 Z" fill="{GOLD}"/>'''),

    # GDebi — package with check
    "gdebi": tile("gdebi", f'''
<path d="M 32 14 L 46 21 L 46 38 L 32 45 L 18 38 L 18 21 Z" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2" stroke-linejoin="round"/>
<path d="M 18 21 L 32 28 L 46 21 M 32 28 L 32 45" stroke="{ACCENT2}" stroke-width="1.6" fill="none"/>
<path d="M 25 40 L 30 45 L 41 34" stroke="{GREEN}" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'''),

    # Flatseal — sandbox lock
    "flatseal": tile("flatseal", f'''
<rect x="16" y="20" width="32" height="28" rx="5" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2"/>
<rect x="26" y="30" width="12" height="10" rx="2" fill="{ACCENT2}"/>
<path d="M 29 30 L 29 26 C 29 22 35 22 35 26 L 35 30" stroke="{ACCENT2}" stroke-width="2.2" fill="none"/>
<line x1="20" y1="44" x2="44" y2="44" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round"/>'''),

    # Warehouse — app box shelves
    "io.github.flattool.Warehouse": tile("warehouse", f'''
<rect x="13" y="16" width="16" height="16" rx="3" fill="{ACCENT}" fill-opacity="0.85"/>
<rect x="35" y="16" width="16" height="16" rx="3" fill="{ACCENT2}" fill-opacity="0.85"/>
<rect x="13" y="36" width="16" height="16" rx="3" fill="{ACCENT2}" fill-opacity="0.85"/>
<rect x="35" y="36" width="16" height="16" rx="3" fill="{GOLD}" fill-opacity="0.85"/>'''),
}

POPULAR_ALIASES_6 = {
    "okular-app": "okular",
    "master-pdf-editor": "masterpdfeditor",
    "xournal-app": "xournal",
    "texstudio-app": "texstudio",
    "zotero-app": "zotero",
    "gnucash": "gnucash-icon",
    "homebank-app": "homebank",
    "wps-office2019-wpsmain": "wps-office",
    "wps-office2023-wpsmain": "wps-office",
    "freeoffice-textmaker-app": "freeoffice-textmaker",
    "freeoffice-planmaker-app": "freeoffice-planmaker",
    "freeoffice-presentations-app": "freeoffice-presentations",
    "0ad-app": "0ad",
    "minetest-app": "minetest",
    "supertuxkart-app": "supertuxkart",
    "supertux-app": "supertux",
    "minecraft-launcher": "minecraft",
    "factorio-app": "factorio",
    "ppsspp-qt": "ppsspp",
    "dolphin-emu-app": "dolphin-emu",
    "dosbox-x": "dosbox",
    "gnome-tweaks": "gnome-tweak-tool",
    "gnome-usage-app": "gnome-usage",
    "missioncenter": "io.missioncenter.MissionCenter",
    "stacer-app": "stacer",
    "bleachbit-app": "bleachbit",
    "partitionmanager-app": "partitionmanager",
    "usb-creator-gtk": "usb-creator",
    "ventoy-app": "ventoy",
    "etcher-app": "etcher",
    "gdebi-app": "gdebi",
    "flatseal-app": "flatseal",
    "warehouse": "io.github.flattool.Warehouse",
}

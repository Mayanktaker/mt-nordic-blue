# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Popular app icons, batch 3: developer IDEs, editors and engineering tools.

try:
    from apps_popular_common import tile, ACCENT, ACCENT2, SNOW, GOLD, RED, GREEN, PURPLE, ORANGE, TILE_FILL
except ImportError:
    from tools.icons.apps_popular_common import tile, ACCENT, ACCENT2, SNOW, GOLD, RED, GREEN, PURPLE, ORANGE, TILE_FILL


def letter_tile(key: str, letter: str, color: str, extra: str = "") -> str:
    # JetBrains-style lettered product tile.
    return tile(key, f'''
<rect x="14" y="14" width="36" height="36" rx="9" fill="{color}" fill-opacity="0.18" stroke="{color}" stroke-width="2"/>
<text x="32" y="41" font-size="19" font-weight="bold" fill="{color}" text-anchor="middle" font-family="sans-serif">{letter}</text>{extra}''')


POPULAR_ICONS_3 = {
    # Kate — editor with pencil
    "kate": tile("kate", f'''
<rect x="15" y="16" width="34" height="32" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<line x1="21" y1="24" x2="43" y2="24" stroke="{ACCENT2}" stroke-width="2" stroke-linecap="round"/>
<line x1="21" y1="30" x2="38" y2="30" stroke="{ACCENT2}" stroke-width="2" stroke-linecap="round"/>
<line x1="21" y1="36" x2="33" y2="36" stroke="{ACCENT2}" stroke-width="2" stroke-linecap="round"/>
<path d="M 36 46 L 48 34 L 52 38 L 40 50 L 35 51 Z" fill="{GOLD}"/>'''),

    # KWrite — pencil on paper
    "kwrite": tile("kwrite", f'''
<rect x="14" y="15" width="32" height="34" rx="3" fill="{TILE_FILL}" stroke="{ACCENT2}" stroke-width="2"/>
<line x1="20" y1="23" x2="40" y2="23" stroke="{ACCENT2}" stroke-width="2" stroke-linecap="round"/>
<line x1="20" y1="29" x2="36" y2="29" stroke="{ACCENT2}" stroke-width="2" stroke-linecap="round"/>
<path d="M 34 49 L 48 35 L 52 39 L 38 53 L 33 54 Z" fill="{ACCENT}"/>'''),

    # Geany — desk lamp
    "geany": tile("geany", f'''
<path d="M 22 20 L 40 20 L 46 34 L 16 34 Z" fill="{GOLD}"/>
<rect x="29" y="34" width="6" height="14" fill="{ACCENT2}"/>
<rect x="20" y="48" width="24" height="5" rx="2.5" fill="{ACCENT}"/>'''),

    # GNOME Builder — wrench over code
    "gnome-builder": tile("gnome-builder", f'''
<path d="M 25 27 L 20 32 L 25 37 M 39 27 L 44 32 L 39 37" stroke="{ACCENT}" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M 32 22 L 32 44" stroke="{ACCENT2}" stroke-width="2.2" stroke-linecap="round"/>
<circle cx="32" cy="50" r="3" fill="{ACCENT2}"/>'''),

    # Emacs — gnu-inspired editor
    "emacs": tile("emacs", f'''
<path d="M 18 40 C 18 27 26 21 36 22 C 44 23 47 28 47 32 C 47 36 43 38 39 38 C 35 38 33 40 33 44 L 33 48 L 27 48 L 27 44 C 27 39 30 36 34 35" fill="none" stroke="{PURPLE}" stroke-width="2.4" stroke-linecap="round"/>
<circle cx="41" cy="26" r="2" fill="{PURPLE}"/>
<path d="M 24 30 C 27 29 30 30 31 32" stroke="{PURPLE}" stroke-width="1.8" fill="none" stroke-linecap="round"/>'''),

    # Helix — double helix
    "helix": tile("helix", f'''
<path d="M 22 16 C 42 24 22 40 42 48" stroke="{ACCENT}" stroke-width="2.8" fill="none" stroke-linecap="round"/>
<path d="M 42 16 C 22 24 42 40 22 48" stroke="{ACCENT2}" stroke-width="2.8" fill="none" stroke-linecap="round"/>
<line x1="24" y1="24" x2="40" y2="24" stroke="{ACCENT2}" stroke-width="1.6"/>
<line x1="24" y1="32" x2="40" y2="32" stroke="{ACCENT}" stroke-width="1.6"/>
<line x1="24" y1="40" x2="40" y2="40" stroke="{ACCENT2}" stroke-width="1.6"/>'''),

    # Code::Blocks — puzzle piece with brackets
    "codeblocks": tile("codeblocks", f'''
<path d="M 22 18 L 42 18 L 42 28 C 46 28 46 34 42 34 L 42 46 L 22 46 L 22 34 C 18 34 18 28 22 28 Z" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2"/>
<path d="M 27 28 L 24 32 L 27 36 M 37 28 L 40 32 L 37 36" stroke="{ACCENT2}" stroke-width="2" fill="none" stroke-linecap="round"/>'''),

    # JetBrains family — lettered product tiles
    "clion": letter_tile("clion", "C", GREEN),
    "datagrip": letter_tile("datagrip", "D", GREEN),
    "goland": letter_tile("goland", "GO", ACCENT),
    "phpstorm": letter_tile("phpstorm", "P", PURPLE),
    "rider": letter_tile("rider", "R", RED),
    "rubymine": letter_tile("rubymine", "R", RED),
    "webstorm": letter_tile("webstorm", "W", ACCENT),
    "rustrover": letter_tile("rustrover", "R", ORANGE),

    # Fleet — layered workspace windows
    "fleet": tile("fleet", f'''
<rect x="14" y="17" width="26" height="16" rx="3" fill="none" stroke="{ACCENT2}" stroke-width="2"/>
<rect x="24" y="25" width="26" height="16" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<line x1="29" y1="32" x2="45" y2="32" stroke="{ACCENT}" stroke-width="1.8" stroke-linecap="round"/>
<line x1="29" y1="37" x2="39" y2="37" stroke="{ACCENT2}" stroke-width="1.6" stroke-linecap="round"/>'''),

    # Sublime Merge — merging branches
    "sublime-merge": tile("sublime-merge", f'''
<path d="M 20 18 L 20 34 C 20 41 26 44 32 44" stroke="{ORANGE}" stroke-width="2.6" fill="none" stroke-linecap="round"/>
<path d="M 44 18 L 44 34 C 44 41 38 44 32 44" stroke="{ORANGE}" stroke-width="2.6" fill="none" stroke-linecap="round"/>
<circle cx="20" cy="16" r="3" fill="{ORANGE}"/>
<circle cx="44" cy="16" r="3" fill="{ORANGE}"/>
<circle cx="32" cy="46" r="3.4" fill="{ORANGE}"/>'''),

    # SmartGit — branch graph
    "smartgit": tile("smartgit", f'''
<circle cx="20" cy="20" r="3.4" fill="{ACCENT}"/>
<circle cx="20" cy="44" r="3.4" fill="{ACCENT}"/>
<circle cx="44" cy="32" r="3.4" fill="{ACCENT2}"/>
<path d="M 20 23 L 20 41" stroke="{ACCENT}" stroke-width="2.4"/>
<path d="M 22 24 C 34 26 38 28 41 31" stroke="{ACCENT2}" stroke-width="2.4" fill="none"/>
<path d="M 22 40 C 34 38 38 36 41 33" stroke="{ACCENT2}" stroke-width="2.4" fill="none"/>'''),

    # MySQL Workbench — database with wrench
    "mysql-workbench": tile("mysql-workbench", f'''
<ellipse cx="28" cy="24" rx="10" ry="3.6" fill="{ACCENT}"/>
<path d="M 18 24 L 18 42 C 18 44 22.5 46 28 46 C 33.5 46 38 44 38 42 L 38 24" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<path d="M 40 22 L 48 30 M 44 18 L 52 26" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>
<circle cx="42" cy="24" r="3" fill="{GOLD}"/>'''),

    # SQLiteBrowser — database with magnifier
    "sqlitebrowser": tile("sqlitebrowser", f'''
<ellipse cx="28" cy="24" rx="10" ry="3.6" fill="{ACCENT2}"/>
<path d="M 18 24 L 18 42 C 18 44 22.5 46 28 46 C 33.5 46 38 44 38 42 L 38 24" fill="{TILE_FILL}" stroke="{ACCENT2}" stroke-width="2"/>
<circle cx="44" cy="38" r="5.5" fill="none" stroke="{ACCENT}" stroke-width="2.2"/>
<line x1="48" y1="42" x2="52" y2="46" stroke="{ACCENT}" stroke-width="2.4" stroke-linecap="round"/>'''),

    # MongoDB Compass — leaf over database
    "mongodb-compass": tile("mongodb-compass", f'''
<path d="M 32 12 C 40 20 42 30 36 44 L 32 50 L 28 44 C 22 30 24 20 32 12 Z" fill="{GREEN}" fill-opacity="0.85"/>
<line x1="32" y1="16" x2="32" y2="50" stroke="{TILE_FILL}" stroke-width="1.6"/>'''),

    # Robo3T — database with robot eye
    "robo3t": tile("robo3t", f'''
<rect x="15" y="20" width="34" height="24" rx="5" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<circle cx="25" cy="32" r="3" fill="{ACCENT2}"/>
<circle cx="39" cy="32" r="3" fill="{ACCENT2}"/>
<path d="M 32 16 L 32 20" stroke="{ACCENT}" stroke-width="2"/>
<circle cx="32" cy="14" r="2" fill="{ACCENT}"/>'''),

    # Sequeler — database table grid
    "sequeler": tile("sequeler", f'''
<ellipse cx="32" cy="22" rx="14" ry="4" fill="{ACCENT2}"/>
<path d="M 18 22 L 18 44 C 18 46 24 48 32 48 C 40 48 46 46 46 44 L 46 22" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<line x1="18" y1="32" x2="46" y2="32" stroke="{ACCENT2}" stroke-width="1.6"/>
<line x1="32" y1="26" x2="32" y2="46" stroke="{ACCENT2}" stroke-width="1.4"/>'''),

    # Beekeeper Studio — hexagon with database
    "beekeeper-studio": tile("beekeeper-studio", f'''
<path d="M 32 12 L 45 20 L 45 36 L 32 44 L 19 36 L 19 20 Z" fill="none" stroke="{GOLD}" stroke-width="2.4" stroke-linejoin="round"/>
<ellipse cx="32" cy="24" rx="8" ry="3" fill="{GOLD}"/>
<path d="M 24 24 L 24 34 C 24 36 28 37 32 37 C 36 37 40 36 40 34 L 40 24" fill="none" stroke="{GOLD}" stroke-width="1.8"/>'''),

    # Bruno — API request loop
    "bruno": tile("bruno", f'''
<circle cx="32" cy="32" r="14" fill="none" stroke="{ORANGE}" stroke-width="2.6"/>
<path d="M 26 32 L 38 32 M 34 28 L 38 32 L 34 36" stroke="{ORANGE}" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="32" cy="32" r="3" fill="{ORANGE}" fill-opacity="0.4"/>'''),

    # Arduino — infinity board
    "arduino": tile("arduino", f'''
<path d="M 14 32 C 14 25 21 25 25 29 L 32 36 C 36 40 42 40 42 33 C 42 26 35 26 31 30 L 24 37 C 20 41 14 41 14 34 Z" fill="none" stroke="{ACCENT}" stroke-width="2.6" stroke-linecap="round"/>
<path d="M 22 30 L 22 36 M 19 33 L 25 33" stroke="{ACCENT2}" stroke-width="1.8" stroke-linecap="round"/>
<path d="M 39 30 L 45 30 M 42 27 L 42 33" stroke="{ACCENT2}" stroke-width="1.8" stroke-linecap="round"/>'''),

    # KiCad — circuit traces
    "kicad": tile("kicad", f'''
<rect x="16" y="16" width="14" height="14" rx="2" fill="none" stroke="{ACCENT}" stroke-width="2"/>
<rect x="34" y="34" width="14" height="14" rx="2" fill="none" stroke="{ACCENT2}" stroke-width="2"/>
<path d="M 30 23 L 40 23 L 40 34" stroke="{ACCENT}" stroke-width="2.2" fill="none"/>
<circle cx="23" cy="41" r="4" fill="{GOLD}"/>
<path d="M 27 41 L 34 41" stroke="{GOLD}" stroke-width="2"/>'''),

    # FreeCAD — cube with caliper
    "freecad": tile("freecad", f'''
<path d="M 32 14 L 46 21 L 46 37 L 32 44 L 18 37 L 18 21 Z" fill="none" stroke="{ACCENT}" stroke-width="2.4" stroke-linejoin="round"/>
<path d="M 18 21 L 32 28 L 46 21 M 32 28 L 32 44" stroke="{ACCENT2}" stroke-width="1.8" fill="none"/>
<path d="M 36 46 L 50 32" stroke="{GOLD}" stroke-width="2.4" stroke-linecap="round"/>'''),

    # OpenSCAD — cube with code
    "openscad": tile("openscad", f'''
<path d="M 26 16 L 40 23 L 40 39 L 26 46 L 12 39 L 12 23 Z" fill="none" stroke="{ACCENT2}" stroke-width="2.2" stroke-linejoin="round"/>
<path d="M 12 23 L 26 30 L 40 23" stroke="{ACCENT2}" stroke-width="1.6" fill="none"/>
<path d="M 38 34 L 44 38 L 38 42 M 50 34 L 44 38 L 50 42" stroke="{ACCENT}" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'''),

    # Godot — robot head
    "godot": tile("godot", f'''
<rect x="15" y="22" width="34" height="26" rx="8" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2"/>
<circle cx="25" cy="32" r="3" fill="{ACCENT}"/>
<circle cx="39" cy="32" r="3" fill="{ACCENT}"/>
<path d="M 26 41 C 29 44 35 44 38 41" stroke="{ACCENT2}" stroke-width="2" fill="none" stroke-linecap="round"/>
<path d="M 22 18 L 26 22 M 42 18 L 38 22" stroke="{ACCENT2}" stroke-width="2" stroke-linecap="round"/>'''),

    # Blockbench — voxel grid cube
    "blockbench": tile("blockbench", f'''
<rect x="18" y="18" width="12" height="12" rx="2" fill="{ACCENT}"/>
<rect x="34" y="18" width="12" height="12" rx="2" fill="{ACCENT2}"/>
<rect x="18" y="34" width="12" height="12" rx="2" fill="{ACCENT2}"/>
<rect x="34" y="34" width="12" height="12" rx="2" fill="{ACCENT}"/>'''),

    # RStudio — R with bar chart
    "rstudio": tile("rstudio", f'''
<circle cx="32" cy="32" r="16" fill="none" stroke="{ACCENT}" stroke-width="2.4"/>
<text x="27" y="40" font-size="18" font-weight="bold" fill="{ACCENT}" text-anchor="middle" font-family="sans-serif">R</text>
<rect x="38" y="32" width="3" height="8" fill="{ACCENT2}"/>
<rect x="43" y="27" width="3" height="13" fill="{ACCENT2}"/>'''),
}

POPULAR_ALIASES_3 = {
    "kate-editor": "kate",
    "org.kde.kate": "kate",
    "kwrite-editor": "kwrite",
    "org.kde.kwrite": "kwrite",
    "gnome-builder-app": "gnome-builder",
    "emacs-gtk": "emacs",
    "emacsclient": "emacs",
    "hx": "helix",
    "codeblocks-ide": "codeblocks",
    "clion-2024": "clion",
    "datagrip-2024": "datagrip",
    "goland-2024": "goland",
    "phpstorm-2024": "phpstorm",
    "rider-2024": "rider",
    "rubymine-2024": "rubymine",
    "webstorm-2024": "webstorm",
    "sublime-merge-app": "sublime-merge",
    "smartgit-app": "smartgit",
    "mysql-workbench-community": "mysql-workbench",
    "mongodb-compass-app": "mongodb-compass",
    "beekeeperstudio": "beekeeper-studio",
    "bruno-app": "bruno",
    "arduino-ide": "arduino",
    "kicad-app": "kicad",
    "freecad-app": "freecad",
    "openscad-app": "openscad",
    "godot-engine": "godot",
    "blockbench-app": "blockbench",
    "rstudio-desktop": "rstudio",
}

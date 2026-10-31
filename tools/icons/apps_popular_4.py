# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Popular app icons, batch 4: notes, diagrams, graphics and capture tools.

try:
    from apps_popular_common import tile, ACCENT, ACCENT2, SNOW, GOLD, RED, GREEN, PURPLE, ORANGE, TILE_FILL
except ImportError:
    from tools.icons.apps_popular_common import tile, ACCENT, ACCENT2, SNOW, GOLD, RED, GREEN, PURPLE, ORANGE, TILE_FILL

POPULAR_ICONS_4 = {
    # Jupyter — orbit with moon dots
    "jupyter": tile("jupyter", f'''
<circle cx="32" cy="32" r="13" fill="none" stroke="{ORANGE}" stroke-width="2.2"/>
<circle cx="45" cy="32" r="2.6" fill="{ORANGE}"/>
<circle cx="24" cy="20" r="2" fill="{ORANGE}"/>
<circle cx="24" cy="44" r="2" fill="{ORANGE}"/>
<circle cx="32" cy="32" r="4" fill="{ORANGE}" fill-opacity="0.5"/>'''),

    # Zeal — open documentation book
    "zeal": tile("zeal", f'''
<path d="M 12 20 C 20 17 26 19 32 23 C 38 19 44 17 52 20 L 52 44 C 44 41 38 43 32 47 C 26 43 20 41 12 44 Z" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2"/>
<line x1="32" y1="23" x2="32" y2="47" stroke="{ACCENT2}" stroke-width="1.6"/>
<line x1="17" y1="26" x2="27" y2="28" stroke="{ACCENT2}" stroke-width="1.6"/>
<line x1="37" y1="28" x2="47" y2="26" stroke="{ACCENT2}" stroke-width="1.6"/>'''),

    # XMind — mind map nodes
    "xmind": tile("xmind", f'''
<circle cx="18" cy="32" r="4" fill="{ACCENT}"/>
<circle cx="44" cy="20" r="3.4" fill="{ACCENT2}"/>
<circle cx="44" cy="32" r="3.4" fill="{ACCENT2}"/>
<circle cx="44" cy="44" r="3.4" fill="{ACCENT2}"/>
<path d="M 22 32 L 40 20 M 22 32 L 40 32 M 22 32 L 40 44" stroke="{ACCENT2}" stroke-width="1.8" fill="none"/>'''),

    # draw.io — flowchart
    "draw-io": tile("draw-io", f'''
<rect x="14" y="16" width="18" height="12" rx="2" fill="none" stroke="{ACCENT}" stroke-width="2"/>
<rect x="32" y="36" width="18" height="12" rx="2" fill="none" stroke="{ACCENT2}" stroke-width="2"/>
<path d="M 23 28 L 23 42 L 32 42" stroke="{ACCENT2}" stroke-width="2" fill="none"/>
<path d="M 32 36 L 40 30" stroke="{GOLD}" stroke-width="2" stroke-linecap="round"/>'''),

    # Figma — overlapping brand circles
    "figma": tile("figma", f'''
<circle cx="24" cy="22" r="7" fill="{RED}"/>
<circle cx="40" cy="22" r="7" fill="{ORANGE}"/>
<circle cx="24" cy="36" r="7" fill="{PURPLE}"/>
<circle cx="40" cy="36" r="7" fill="{ACCENT}"/>
<circle cx="24" cy="49" r="6" fill="{GREEN}"/>'''),

    # Typora — markdown editor
    "typora": tile("typora", f'''
<rect x="14" y="16" width="36" height="32" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<path d="M 21 24 L 27 24 M 24 24 L 24 40" stroke="{ACCENT2}" stroke-width="2.2" stroke-linecap="round"/>
<path d="M 33 40 L 33 26 L 37 33 L 41 26 L 41 40" stroke="{ACCENT2}" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'''),

    # Joplin — note with pin
    "joplin": tile("joplin", f'''
<rect x="16" y="14" width="32" height="36" rx="3" fill="{TILE_FILL}" stroke="{ACCENT2}" stroke-width="2"/>
<line x1="22" y1="22" x2="42" y2="22" stroke="{ACCENT2}" stroke-width="2" stroke-linecap="round"/>
<line x1="22" y1="28" x2="38" y2="28" stroke="{ACCENT2}" stroke-width="2" stroke-linecap="round"/>
<line x1="22" y1="34" x2="34" y2="34" stroke="{ACCENT2}" stroke-width="2" stroke-linecap="round"/>
<circle cx="42" cy="42" r="4" fill="{GOLD}"/>'''),

    # Logseq — outline graph
    "logseq": tile("logseq", f'''
<circle cx="20" cy="22" r="3" fill="{ACCENT}"/>
<circle cx="20" cy="34" r="3" fill="{ACCENT}"/>
<circle cx="20" cy="46" r="3" fill="{ACCENT}"/>
<line x1="26" y1="22" x2="44" y2="22" stroke="{ACCENT2}" stroke-width="2.2" stroke-linecap="round"/>
<line x1="26" y1="34" x2="38" y2="34" stroke="{ACCENT2}" stroke-width="2.2" stroke-linecap="round"/>
<line x1="26" y1="46" x2="42" y2="46" stroke="{ACCENT2}" stroke-width="2.2" stroke-linecap="round"/>'''),

    # Notesnook — notebook with lock
    "notesnook": tile("notesnook", f'''
<rect x="15" y="14" width="30" height="36" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<rect x="45" y="14" width="4" height="36" rx="2" fill="{ACCENT}" fill-opacity="0.5"/>
<rect x="24" y="27" width="14" height="10" rx="2" fill="{GOLD}"/>
<path d="M 27 27 L 27 24 C 27 21 35 21 35 24 L 35 27" stroke="{GOLD}" stroke-width="2" fill="none"/>'''),

    # Anytype — connected cube
    "anytype": tile("anytype", f'''
<path d="M 32 14 L 46 22 L 46 38 L 32 46 L 18 38 L 18 22 Z" fill="none" stroke="{ACCENT}" stroke-width="2.4" stroke-linejoin="round"/>
<circle cx="32" cy="14" r="2.4" fill="{ACCENT2}"/>
<circle cx="46" cy="22" r="2.4" fill="{ACCENT2}"/>
<circle cx="18" cy="22" r="2.4" fill="{ACCENT2}"/>
<circle cx="32" cy="46" r="2.4" fill="{ACCENT2}"/>'''),

    # CherryTree — hierarchical tree
    "cherrytree": tile("cherrytree", f'''
<circle cx="32" cy="16" r="4" fill="{RED}"/>
<circle cx="20" cy="34" r="4" fill="{RED}"/>
<circle cx="44" cy="34" r="4" fill="{RED}"/>
<circle cx="32" cy="48" r="3" fill="{RED}" fill-opacity="0.7"/>
<path d="M 32 20 L 32 44 M 32 28 L 20 32 M 32 28 L 44 32" stroke="{GREEN}" stroke-width="2.2" fill="none"/>'''),

    # ReText — markdown preview
    "retext": tile("retext", f'''
<rect x="14" y="16" width="20" height="30" rx="2.5" fill="{TILE_FILL}" stroke="{ACCENT2}" stroke-width="2"/>
<rect x="38" y="20" width="14" height="26" rx="2.5" fill="none" stroke="{ACCENT}" stroke-width="2"/>
<line x1="19" y1="24" x2="29" y2="24" stroke="{ACCENT2}" stroke-width="1.8"/>
<line x1="19" y1="30" x2="29" y2="30" stroke="{ACCENT2}" stroke-width="1.8"/>
<line x1="19" y1="36" x2="26" y2="36" stroke="{ACCENT2}" stroke-width="1.8"/>'''),

    # Ghostwriter — quill
    "ghostwriter": tile("ghostwriter", f'''
<path d="M 48 14 C 38 18 28 26 22 38 L 18 50 L 30 46 C 42 40 48 28 48 14 Z" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2"/>
<path d="M 22 38 L 34 26" stroke="{ACCENT2}" stroke-width="1.8"/>'''),

    # Marker — markdown file
    "marker": tile("marker", f'''
<path d="M 18 14 L 38 14 L 46 22 L 46 50 L 18 50 Z" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2"/>
<path d="M 38 14 L 38 22 L 46 22" fill="none" stroke="{ACCENT}" stroke-width="2"/>
<path d="M 24 32 L 26 38 L 32 32 L 38 38 L 40 32" stroke="{ACCENT2}" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'''),

    # GtkHash — fingerprint check
    "gtkhash": tile("gtkhash", f'''
<path d="M 22 42 C 22 30 26 22 32 22 C 38 22 42 30 42 42" fill="none" stroke="{ACCENT2}" stroke-width="2"/>
<path d="M 27 44 C 27 34 29 27 32 27 C 35 27 37 34 37 44" fill="none" stroke="{ACCENT2}" stroke-width="1.8"/>
<path d="M 30 46 C 30 38 31 32 32 32 C 33 32 34 38 34 46" fill="none" stroke="{ACCENT2}" stroke-width="1.6"/>
<path d="M 36 18 L 40 22 L 47 14" stroke="{GREEN}" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'''),

    # Nmap — radar sweep
    "nmap_icon": tile("nmap_icon", f'''
<circle cx="32" cy="32" r="15" fill="none" stroke="{ACCENT}" stroke-width="2"/>
<circle cx="32" cy="32" r="9" fill="none" stroke="{ACCENT2}" stroke-width="1.4"/>
<circle cx="32" cy="32" r="3" fill="{ACCENT}"/>
<path d="M 32 32 L 43 21" stroke="{GREEN}" stroke-width="2.4" stroke-linecap="round"/>
<circle cx="39" cy="38" r="2" fill="{GOLD}"/>'''),

    # PuTTY — terminal with key
    "putty": tile("putty", f'''
<rect x="12" y="16" width="30" height="26" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<path d="M 18 24 L 22 28 L 18 32" stroke="{ACCENT2}" stroke-width="2" fill="none" stroke-linecap="round"/>
<line x1="25" y1="32" x2="33" y2="32" stroke="{ACCENT2}" stroke-width="2" stroke-linecap="round"/>
<circle cx="42" cy="40" r="5" fill="none" stroke="{GOLD}" stroke-width="2.2"/>
<path d="M 46 44 L 52 50" stroke="{GOLD}" stroke-width="2.4" stroke-linecap="round"/>'''),

    # GNS3 — network topology
    "gns3": tile("gns3", f'''
<circle cx="32" cy="18" r="4.5" fill="{ACCENT}"/>
<circle cx="18" cy="42" r="4.5" fill="{ACCENT2}"/>
<circle cx="46" cy="42" r="4.5" fill="{ACCENT2}"/>
<path d="M 32 22 L 18 38 M 32 22 L 46 38 M 22 42 L 42 42" stroke="{ACCENT2}" stroke-width="1.8" fill="none"/>'''),

    # Scribus — page layout columns
    "scribus": tile("scribus", f'''
<rect x="14" y="14" width="36" height="36" rx="2.5" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<rect x="19" y="19" width="12" height="16" fill="{ACCENT2}" fill-opacity="0.6"/>
<rect x="34" y="19" width="12" height="8" fill="{ACCENT}" fill-opacity="0.7"/>
<line x1="19" y1="40" x2="45" y2="40" stroke="{ACCENT2}" stroke-width="2"/>
<line x1="19" y1="45" x2="38" y2="45" stroke="{ACCENT2}" stroke-width="2"/>'''),

    # Karbon — vector pen nib
    "karbon": tile("karbon", f'''
<path d="M 32 12 L 42 26 L 36 46 L 32 50 L 28 46 L 22 26 Z" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2" stroke-linejoin="round"/>
<circle cx="32" cy="30" r="3.4" fill="{ACCENT2}"/>
<path d="M 32 50 L 32 56" stroke="{ACCENT}" stroke-width="2"/>'''),

    # Synfig — bezier node curve
    "synfig": tile("synfig", f'''
<path d="M 16 44 C 24 22 40 22 48 44" stroke="{ACCENT}" stroke-width="2.4" fill="none" stroke-linecap="round"/>
<circle cx="16" cy="44" r="3.4" fill="{ACCENT2}"/>
<circle cx="48" cy="44" r="3.4" fill="{ACCENT2}"/>
<circle cx="32" cy="26" r="3" fill="{GOLD}"/>
<path d="M 16 44 L 32 26 L 48 44" stroke="{ACCENT2}" stroke-width="1.2" stroke-dasharray="3 3" fill="none"/>'''),

    # Olive Editor — timeline clips
    "olive-editor": tile("olive-editor", f'''
<rect x="12" y="18" width="40" height="8" rx="2" fill="{ACCENT}" fill-opacity="0.85"/>
<rect x="18" y="30" width="30" height="8" rx="2" fill="{ACCENT2}" fill-opacity="0.85"/>
<rect x="12" y="42" width="24" height="8" rx="2" fill="{GOLD}" fill-opacity="0.85"/>'''),

    # Shotcut — scissors and film
    "shotcut": tile("shotcut", f'''
<rect x="12" y="20" width="26" height="24" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<g fill="{ACCENT2}"><rect x="15" y="23" width="3" height="3"/><rect x="15" y="28" width="3" height="3"/><rect x="15" y="33" width="3" height="3"/><rect x="32" y="23" width="3" height="3"/><rect x="32" y="28" width="3" height="3"/><rect x="32" y="33" width="3" height="3"/></g>
<circle cx="44" cy="26" r="4" fill="none" stroke="{GOLD}" stroke-width="2"/>
<circle cx="44" cy="38" r="4" fill="none" stroke="{GOLD}" stroke-width="2"/>
<path d="M 41 29 L 33 36 M 41 35 L 33 28" stroke="{GOLD}" stroke-width="2" stroke-linecap="round"/>'''),

    # OpenShot — film strip with play
    "openshot": tile("openshot", f'''
<rect x="12" y="18" width="40" height="26" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<g fill="{ACCENT2}"><rect x="15" y="21" width="3" height="3"/><rect x="15" y="26" width="3" height="3"/><rect x="15" y="31" width="3" height="3"/><rect x="46" y="21" width="3" height="3"/><rect x="46" y="26" width="3" height="3"/><rect x="46" y="31" width="3" height="3"/></g>
<polygon points="28,24 28,38 39,31" fill="{ACCENT}"/>'''),

    # LosslessCut — scissors on video frame
    "losslesscut": tile("losslesscut", f'''
<rect x="12" y="16" width="30" height="22" rx="3" fill="{TILE_FILL}" stroke="{ACCENT2}" stroke-width="2"/>
<polygon points="22,21 22,33 31,27" fill="{ACCENT2}"/>
<circle cx="42" cy="34" r="4.4" fill="none" stroke="{RED}" stroke-width="2.2"/>
<circle cx="42" cy="46" r="4.4" fill="none" stroke="{RED}" stroke-width="2.2"/>
<path d="M 39 37 L 33 44 M 39 43 L 33 36" stroke="{RED}" stroke-width="2" stroke-linecap="round"/>'''),

    # MKVToolNix — film with merge arrows
    "mkvmerge": tile("mkvmerge", f'''
<rect x="10" y="22" width="24" height="20" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<g fill="{ACCENT2}"><rect x="13" y="25" width="2.6" height="2.6"/><rect x="13" y="30" width="2.6" height="2.6"/><rect x="13" y="35" width="2.6" height="2.6"/></g>
<path d="M 38 26 L 46 32 L 38 38" stroke="{GOLD}" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M 48 26 L 56 32 L 48 38" stroke="{GOLD}" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'''),

    # SimpleScreenRecorder — screen with record dot
    "simplescreenrecorder": tile("simplescreenrecorder", f'''
<rect x="12" y="16" width="40" height="26" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<circle cx="32" cy="29" r="6" fill="{RED}"/>
<circle cx="32" cy="29" r="2.2" fill="{SNOW}"/>
<rect x="26" y="44" width="12" height="3" rx="1.5" fill="{ACCENT2}"/>'''),

    # Peek — magnifier over record dot
    "peek": tile("peek", f'''
<circle cx="28" cy="28" r="11" fill="none" stroke="{ACCENT}" stroke-width="2.4"/>
<line x1="36" y1="36" x2="48" y2="48" stroke="{ACCENT}" stroke-width="3" stroke-linecap="round"/>
<circle cx="28" cy="28" r="4" fill="{RED}"/>'''),

    # Flameshot — camera with flame
    "flameshot": tile("flameshot", f'''
<rect x="12" y="24" width="34" height="20" rx="4" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<circle cx="29" cy="34" r="6" fill="none" stroke="{ACCENT2}" stroke-width="2"/>
<rect x="20" y="19" width="12" height="5" rx="2" fill="{ACCENT2}"/>
<path d="M 47 38 C 51 34 53 29 52 24 C 48 27 45 29 44 33 C 42 30 42 27 43 25 C 39 28 38 33 40 37 C 42 41 45 41 47 38 Z" fill="{ORANGE}"/>'''),

    # Shutter — camera shutter blades
    "shutter": tile("shutter", f'''
<circle cx="32" cy="32" r="15" fill="none" stroke="{ACCENT}" stroke-width="2.2"/>
<path d="M 32 17 L 40 31 L 24 31 Z" fill="{ACCENT2}" fill-opacity="0.8"/>
<path d="M 45 25 L 36 40 L 28 26 Z" fill="{ACCENT}" fill-opacity="0.5"/>
<circle cx="32" cy="32" r="4" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="1.8"/>'''),

    # ColorGrab — eyedropper
    "colorgrab": tile("colorgrab", f'''
<path d="M 40 14 L 50 24 L 44 30 L 34 20 Z" fill="{ACCENT2}"/>
<path d="M 36 24 L 18 42 L 16 50 L 24 48 L 42 30 Z" fill="none" stroke="{ACCENT}" stroke-width="2.2" stroke-linejoin="round"/>
<circle cx="20" cy="46" r="2.4" fill="{GOLD}"/>'''),

    # Pinta — brush and palette
    "pinta": tile("pinta", f'''
<path d="M 16 44 C 16 30 26 18 44 16 C 46 34 36 46 22 46 Z" fill="none" stroke="{ACCENT}" stroke-width="2.2"/>
<circle cx="24" cy="30" r="2.6" fill="{RED}"/>
<circle cx="32" cy="26" r="2.6" fill="{GOLD}"/>
<circle cx="30" cy="36" r="2.6" fill="{GREEN}"/>
<path d="M 44 46 L 52 54" stroke="{GOLD}" stroke-width="2.6" stroke-linecap="round"/>'''),
}

POPULAR_ALIASES_4 = {
    "jupyter-notebook": "jupyter",
    "jupyter-lab": "jupyter",
    "zeal-docs": "zeal",
    "xmind-app": "xmind",
    "drawio": "draw-io",
    "com.jgraph.drawio.desktop": "draw-io",
    "figma-linux": "figma",
    "typora-app": "typora",
    "joplin-desktop": "joplin",
    "logseq-app": "logseq",
    "notesnook-app": "notesnook",
    "anytype-app": "anytype",
    "cherrytree-app": "cherrytree",
    "retext-app": "retext",
    "ghostwriter-app": "ghostwriter",
    "marker-editor": "marker",
    "gtkhash-app": "gtkhash",
    "nmap": "nmap_icon",
    "putty-ssh": "putty",
    "gns3-app": "gns3",
    "scribus-app": "scribus",
    "karbon-app": "karbon",
    "synfig-studio": "synfig",
    "olive-video-editor": "olive-editor",
    "shotcut-app": "shotcut",
    "openshot-qt": "openshot",
    "losslesscut-app": "losslesscut",
    "mkvmerge-gui": "mkvmerge",
    "ssr": "simplescreenrecorder",
    "peek-recorder": "peek",
    "flameshot-app": "flameshot",
    "shutter-app": "shutter",
    "colorgrab-app": "colorgrab",
    "pinta-app": "pinta",
}

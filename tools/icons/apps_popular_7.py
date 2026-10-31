# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Popular app icons, batch 7: administration, security and tuning tools.

try:
    from apps_popular_common import tile, ACCENT, ACCENT2, SNOW, GOLD, RED, GREEN, PURPLE, ORANGE, TILE_FILL
except ImportError:
    from tools.icons.apps_popular_common import tile, ACCENT, ACCENT2, SNOW, GOLD, RED, GREEN, PURPLE, ORANGE, TILE_FILL

POPULAR_ICONS_7 = {
    # Flatsweep — broom over flatpak box
    "flatsweep": tile("flatsweep", f'''
<path d="M 32 14 L 44 20 L 44 34 L 32 40 L 20 34 L 20 20 Z" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2" stroke-linejoin="round"/>
<path d="M 20 20 L 32 26 L 44 20 M 32 26 L 32 40" stroke="{ACCENT2}" stroke-width="1.4" fill="none"/>
<path d="M 40 48 L 28 36 L 24 44 L 36 54 Z" fill="{GOLD}"/>'''),

    # Bauh — package with tag
    "bauh": tile("bauh", f'''
<path d="M 30 14 L 44 21 L 44 37 L 30 44 L 16 37 L 16 21 Z" fill="none" stroke="{ACCENT}" stroke-width="2.2" stroke-linejoin="round"/>
<path d="M 30 44 L 30 52" stroke="{ACCENT2}" stroke-width="2.2"/>
<path d="M 30 48 L 40 44 L 40 52 L 30 56 Z" fill="{GOLD}"/>'''),

    # Gearlever — appimage lever
    "it.mijorus.gearlever": tile("gearlever", f'''
<circle cx="24" cy="40" r="9" fill="none" stroke="{ACCENT}" stroke-width="2.4"/>
<circle cx="24" cy="40" r="3" fill="{ACCENT}"/>
<path d="M 31 33 L 48 16" stroke="{ACCENT2}" stroke-width="3" stroke-linecap="round"/>
<path d="M 44 14 L 52 22" stroke="{GOLD}" stroke-width="2.6" stroke-linecap="round"/>'''),

    # AppImageLauncher — appimage box with arrow
    "AppImageLauncher": tile("appimagelauncher", f'''
<rect x="16" y="16" width="20" height="20" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<path d="M 21 26 L 26 21 L 31 26" stroke="{ACCENT2}" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M 40 28 L 40 44 M 35 39 L 40 45 L 45 39" stroke="{GOLD}" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'''),

    # Déjà Dup — backup arrows with clock
    "deja-dup": tile("deja-dup", f'''
<path d="M 20 26 A 12 12 0 0 1 44 26" stroke="{ACCENT}" stroke-width="2.6" fill="none" stroke-linecap="round"/>
<path d="M 44 38 A 12 12 0 0 1 20 38" stroke="{ACCENT}" stroke-width="2.6" fill="none" stroke-linecap="round"/>
<polygon points="40,20 46,26 38,28" fill="{ACCENT}"/>
<polygon points="24,44 18,38 26,36" fill="{ACCENT}"/>
<circle cx="32" cy="32" r="3" fill="{GOLD}"/>'''),

    # VeraCrypt — vault with lock
    "veracrypt": tile("veracrypt", f'''
<circle cx="32" cy="32" r="15" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.4"/>
<circle cx="32" cy="32" r="10" fill="none" stroke="{ACCENT2}" stroke-width="1.6"/>
<rect x="27" y="28" width="10" height="9" rx="2" fill="{ACCENT2}"/>
<path d="M 29.5 28 L 29.5 25 C 29.5 21.5 34.5 21.5 34.5 25 L 34.5 28" stroke="{ACCENT2}" stroke-width="2" fill="none"/>'''),

    # KeePassXC — key with shield
    "keepassxc": tile("keepassxc", f'''
<path d="M 32 12 L 46 17 L 46 32 C 46 42 39 48 32 52 C 25 48 18 42 18 32 L 18 17 Z" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.4"/>
<circle cx="32" cy="28" r="4.4" fill="none" stroke="{ACCENT2}" stroke-width="2.2"/>
<path d="M 32 32 L 32 42 M 32 38 L 37 38" stroke="{ACCENT2}" stroke-width="2.2" stroke-linecap="round"/>'''),

    # Solaar — wireless mouse signal
    "solaar": tile("solaar", f'''
<rect x="24" y="24" width="16" height="22" rx="8" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2"/>
<line x1="32" y1="28" x2="32" y2="33" stroke="{ACCENT2}" stroke-width="2" stroke-linecap="round"/>
<path d="M 46 20 C 50 25 50 33 46 38" stroke="{GOLD}" stroke-width="2.2" fill="none" stroke-linecap="round"/>
<path d="M 18 20 C 14 25 14 33 18 38" stroke="{GOLD}" stroke-width="2.2" fill="none" stroke-linecap="round"/>'''),

    # OpenRGB — rainbow LED fan
    "openrgb": tile("openrgb", f'''
<circle cx="32" cy="32" r="14" fill="none" stroke="{ACCENT}" stroke-width="2.2"/>
<path d="M 32 18 A 14 14 0 0 1 46 32" stroke="{RED}" stroke-width="3" fill="none"/>
<path d="M 46 32 A 14 14 0 0 1 32 46" stroke="{GOLD}" stroke-width="3" fill="none"/>
<path d="M 32 46 A 14 14 0 0 1 18 32" stroke="{GREEN}" stroke-width="3" fill="none"/>
<circle cx="32" cy="32" r="4" fill="{PURPLE}"/>'''),

    # Piper — mouse with settings
    "piper": tile("piper", f'''
<rect x="20" y="14" width="24" height="36" rx="11" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2"/>
<line x1="32" y1="20" x2="32" y2="28" stroke="{ACCENT2}" stroke-width="2.2" stroke-linecap="round"/>
<circle cx="32" cy="38" r="5" fill="none" stroke="{GOLD}" stroke-width="2"/>
<circle cx="32" cy="38" r="1.8" fill="{GOLD}"/>'''),

    # CPU-X — processor die
    "cpu-x": tile("cpu-x", f'''
<rect x="18" y="18" width="28" height="28" rx="4" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.4"/>
<rect x="26" y="26" width="12" height="12" rx="2" fill="{ACCENT}" fill-opacity="0.5"/>
<g stroke="{ACCENT2}" stroke-width="2" stroke-linecap="round">
<line x1="24" y1="12" x2="24" y2="18"/><line x1="32" y1="12" x2="32" y2="18"/><line x1="40" y1="12" x2="40" y2="18"/>
<line x1="24" y1="46" x2="24" y2="52"/><line x1="32" y1="46" x2="32" y2="52"/><line x1="40" y1="46" x2="40" y2="52"/>
</g>'''),

    # HWiNFO — chip with graph
    "hwinfo": tile("hwinfo", f'''
<rect x="14" y="18" width="36" height="28" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2"/>
<path d="M 19 40 L 25 32 L 30 37 L 37 27 L 45 34" stroke="{GREEN}" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="22" cy="24" r="2" fill="{ACCENT2}"/>'''),

    # Psensor — thermometer gauge
    "psensor": tile("psensor", f'''
<path d="M 30 16 C 30 14 34 14 34 16 L 34 36 C 38 38 38 44 34 47 C 30 50 24 47 24 42 C 24 39 26 37 30 36 Z" fill="{TILE_FILL}" stroke="{RED}" stroke-width="2.2"/>
<circle cx="32" cy="42" r="3.4" fill="{RED}"/>
<line x1="40" y1="24" x2="46" y2="24" stroke="{ACCENT2}" stroke-width="2" stroke-linecap="round"/>
<line x1="40" y1="32" x2="48" y2="32" stroke="{ACCENT2}" stroke-width="2" stroke-linecap="round"/>'''),

    # Gufw — firewall wall with flame
    "gufw": tile("gufw", f'''
<rect x="14" y="18" width="26" height="28" rx="2" fill="none" stroke="{ACCENT}" stroke-width="2.2"/>
<line x1="14" y1="27" x2="40" y2="27" stroke="{ACCENT}" stroke-width="1.8"/>
<line x1="14" y1="36" x2="40" y2="36" stroke="{ACCENT}" stroke-width="1.8"/>
<line x1="23" y1="18" x2="23" y2="27" stroke="{ACCENT}" stroke-width="1.4"/>
<line x1="31" y1="27" x2="31" y2="36" stroke="{ACCENT}" stroke-width="1.4"/>
<path d="M 46 40 C 50 36 51 31 50 26 C 46 29 44 31 43 35 C 41 32 41 29 42 27 C 38 30 37 35 39 39 C 41 43 44 43 46 40 Z" fill="{ORANGE}"/>'''),

    # OpenSnitch — network guard
    "opensnitch-ui": tile("opensnitch-ui", f'''
<circle cx="32" cy="32" r="14" fill="none" stroke="{ACCENT}" stroke-width="2.2"/>
<circle cx="32" cy="32" r="3" fill="{ACCENT}"/>
<path d="M 32 18 L 32 29 M 32 35 L 32 46 M 18 32 L 29 32 M 35 32 L 46 32" stroke="{ACCENT2}" stroke-width="1.6"/>
<path d="M 40 20 L 46 26 L 40 32" stroke="{GOLD}" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'''),

    # Virt-Manager — virtual machines
    "virt-manager": tile("virt-manager", f'''
<rect x="12" y="16" width="40" height="26" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2"/>
<rect x="18" y="22" width="12" height="14" rx="2" fill="none" stroke="{ACCENT2}" stroke-width="1.8"/>
<rect x="34" y="22" width="12" height="14" rx="2" fill="none" stroke="{ACCENT2}" stroke-width="1.8"/>
<rect x="26" y="44" width="12" height="3" rx="1.5" fill="{ACCENT2}"/>'''),

    # GNOME Boxes — VM cube
    "gnome-boxes": tile("gnome-boxes", f'''
<path d="M 32 13 L 47 21 L 47 41 L 32 49 L 17 41 L 17 21 Z" fill="none" stroke="{ACCENT}" stroke-width="2.4" stroke-linejoin="round"/>
<path d="M 17 21 L 32 29 L 47 21 M 32 29 L 32 49" stroke="{ACCENT2}" stroke-width="1.8" fill="none"/>
<circle cx="32" cy="39" r="3" fill="{GOLD}"/>'''),

    # VMware Workstation — hexagon VM
    "vmware-workstation": tile("vmware-workstation", f'''
<path d="M 32 12 L 46 20 L 46 36 L 32 44 L 18 36 L 18 20 Z" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.4" stroke-linejoin="round"/>
<path d="M 23 28 L 27 34 L 32 26 L 37 34 L 41 28" stroke="{ACCENT2}" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'''),

    # Genymotion — android robot
    "genymotion": tile("genymotion", f'''
<rect x="18" y="22" width="28" height="22" rx="8" fill="none" stroke="{GREEN}" stroke-width="2.2"/>
<circle cx="26" cy="31" r="2.4" fill="{GREEN}"/>
<circle cx="38" cy="31" r="2.4" fill="{GREEN}"/>
<line x1="24" y1="16" x2="28" y2="21" stroke="{GREEN}" stroke-width="2" stroke-linecap="round"/>
<line x1="40" y1="16" x2="36" y2="21" stroke="{GREEN}" stroke-width="2" stroke-linecap="round"/>'''),

    # Redshift — sun to moon
    "redshift": tile("redshift", f'''
<circle cx="24" cy="28" r="7" fill="{GOLD}"/>
<path d="M 24 16 L 24 20 M 24 36 L 24 40 M 12 28 L 16 28 M 32 28 L 36 28" stroke="{GOLD}" stroke-width="2" stroke-linecap="round"/>
<path d="M 44 26 C 50 27 52 34 47 38 C 43 41 37 39 35 34 C 40 36 44 32 44 26 Z" fill="{ACCENT2}"/>
<path d="M 42 18 L 43 21 L 46 22 L 43 23 L 42 26 L 41 23 L 38 22 L 41 21 Z" fill="{ACCENT}"/>'''),

    # Safe Eyes — eye with pause
    "safeeyes": tile("safeeyes", f'''
<path d="M 12 32 C 20 22 44 22 52 32 C 44 42 20 42 12 32 Z" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2"/>
<circle cx="32" cy="32" r="6" fill="{ACCENT}"/>
<rect x="29.5" y="28.5" width="2" height="7" rx="1" fill="{TILE_FILL}"/>
<rect x="33" y="28.5" width="2" height="7" rx="1" fill="{TILE_FILL}"/>'''),

    # Caffeine — coffee cup with pulse
    "caffeine": tile("caffeine", f'''
<path d="M 18 24 L 40 24 L 38 44 L 20 44 Z" fill="{TILE_FILL}" stroke="{ACCENT2}" stroke-width="2.2"/>
<path d="M 40 28 L 46 28 C 48 28 48 34 46 34 L 39 34" fill="none" stroke="{ACCENT2}" stroke-width="2"/>
<path d="M 24 18 C 24 15 27 15 27 12 M 31 18 C 31 15 34 15 34 12" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round"/>'''),

    # Pomotroid — tomato timer
    "pomotroid": tile("pomotroid", f'''
<circle cx="32" cy="36" r="13" fill="{RED}"/>
<path d="M 32 20 C 32 16 36 14 40 16" stroke="{GREEN}" stroke-width="2.4" fill="none" stroke-linecap="round"/>
<path d="M 26 21 L 38 21 L 32 15 Z" fill="{GREEN}"/>
<path d="M 32 30 L 32 36 L 37 39" stroke="{TILE_FILL}" stroke-width="2.2" fill="none" stroke-linecap="round"/>'''),

    # Variety — wallpaper frame with globe
    "variety": tile("variety", f'''
<rect x="12" y="18" width="40" height="26" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2"/>
<circle cx="32" cy="31" r="8" fill="none" stroke="{ACCENT2}" stroke-width="1.8"/>
<ellipse cx="32" cy="31" rx="3.4" ry="8" fill="none" stroke="{ACCENT2}" stroke-width="1.2"/>
<line x1="24" y1="31" x2="40" y2="31" stroke="{ACCENT2}" stroke-width="1.2"/>
<rect x="26" y="46" width="12" height="3" rx="1.5" fill="{ACCENT2}"/>'''),

    # Gradience — gradient swatch
    "com.github.GradienceTeam.Gradience": tile("gradience", f'''
<defs>
  <linearGradient id="grad-sw" x1="16" y1="16" x2="48" y2="48" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="{ACCENT}"/>
    <stop offset="100%" stop-color="{PURPLE}"/>
  </linearGradient>
</defs>
<rect x="14" y="14" width="36" height="36" rx="8" fill="url(#grad-sw)"/>
<circle cx="32" cy="32" r="6" fill="{TILE_FILL}" fill-opacity="0.55"/>'''),

    # Flatpak Discover — box with magnifier
    "flatpak-discover": tile("flatpak-discover", f'''
<path d="M 30 12 L 44 19 L 44 35 L 30 42 L 16 35 L 16 19 Z" fill="none" stroke="{ACCENT}" stroke-width="2.2" stroke-linejoin="round"/>
<path d="M 16 19 L 30 26 L 44 19 M 30 26 L 30 42" stroke="{ACCENT2}" stroke-width="1.6" fill="none"/>
<circle cx="43" cy="43" r="5" fill="none" stroke="{GOLD}" stroke-width="2.2"/>
<line x1="47" y1="47" x2="51" y2="51" stroke="{GOLD}" stroke-width="2.4" stroke-linecap="round"/>'''),

    # htop — process bars
    "htop": tile("htop", f'''
<rect x="12" y="16" width="40" height="30" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<g fill="{ACCENT2}">
<rect x="17" y="22" width="18" height="3" rx="1.5"/>
<rect x="17" y="28" width="26" height="3" rx="1.5"/>
<rect x="17" y="34" width="12" height="3" rx="1.5"/>
<rect x="17" y="40" width="22" height="3" rx="1.5"/>
</g>
<rect x="38" y="22" width="8" height="3" rx="1.5" fill="{GREEN}"/>'''),

    # Onboard — on-screen keyboard
    "onboard": tile("onboard", f'''
<rect x="12" y="20" width="40" height="24" rx="4" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2"/>
<g fill="{ACCENT2}">
<rect x="17" y="25" width="4" height="4" rx="1"/><rect x="24" y="25" width="4" height="4" rx="1"/>
<rect x="31" y="25" width="4" height="4" rx="1"/><rect x="38" y="25" width="4" height="4" rx="1"/>
<rect x="45" y="25" width="3" height="4" rx="1"/>
<rect x="20" y="33" width="24" height="5" rx="2"/>
</g>'''),
}

POPULAR_ALIASES_7 = {
    "flatsweep-app": "flatsweep",
    "bauh-app": "bauh",
    "gearlever": "it.mijorus.gearlever",
    "appimagelauncher": "AppImageLauncher",
    "deja-dup-app": "deja-dup",
    "veracrypt-app": "veracrypt",
    "keepassxc-app": "keepassxc",
    "solaar-app": "solaar",
    "openrgb-app": "openrgb",
    "piper-app": "piper",
    "cpu-x-app": "cpu-x",
    "hwinfo-app": "hwinfo",
    "psensor-app": "psensor",
    "gufw-app": "gufw",
    "opensnitch": "opensnitch-ui",
    "virt-manager-app": "virt-manager",
    "boxes": "gnome-boxes",
    "vmware-player": "vmware-workstation",
    "genymotion-app": "genymotion",
    "redshift-app": "redshift",
    "safeeyes-app": "safeeyes",
    "caffeine-app": "caffeine",
    "pomotroid-app": "pomotroid",
    "variety-app": "variety",
    "gradience": "com.github.GradienceTeam.Gradience",
    "flatpak-discover-app": "flatpak-discover",
    "onboard-app": "onboard",
}

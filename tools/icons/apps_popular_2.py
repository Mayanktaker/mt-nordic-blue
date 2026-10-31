# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Popular app icons, batch 2: messaging, calls and cloud storage clients.

try:
    from apps_popular_common import tile, ACCENT, ACCENT2, SNOW, GOLD, RED, GREEN, PURPLE, ORANGE, TILE_FILL
except ImportError:
    from tools.icons.apps_popular_common import tile, ACCENT, ACCENT2, SNOW, GOLD, RED, GREEN, PURPLE, ORANGE, TILE_FILL

POPULAR_ICONS_2 = {
    # Franz — stacked chat bubbles
    "franz": tile("franz", f'''
<rect x="15" y="17" width="30" height="20" rx="4" fill="none" stroke="{ACCENT2}" stroke-width="2"/>
<path d="M 21 31 L 21 41 L 30 41" fill="none" stroke="{ACCENT}" stroke-width="2.4" stroke-linejoin="round"/>
<path d="M 27 29 L 47 29 L 47 43 L 36 43 L 30 49 L 30 43 L 27 43 Z" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2" stroke-linejoin="round"/>'''),

    # Rambox — stacked bubbles with ring
    "rambox": tile("rambox", f'''
<circle cx="32" cy="32" r="16" fill="none" stroke="{ACCENT2}" stroke-width="2"/>
<rect x="19" y="21" width="20" height="14" rx="3" fill="none" stroke="{ACCENT}" stroke-width="2"/>
<rect x="26" y="30" width="20" height="14" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>'''),

    # Teams for Linux — people + chat bubble
    "teams-for-linux": tile("teams-for-linux", f'''
<circle cx="24" cy="24" r="5" fill="{PURPLE}"/>
<circle cx="40" cy="26" r="4" fill="{ACCENT2}"/>
<path d="M 14 39 C 14 32 19 30 24 30 C 29 30 34 32 34 39 Z" fill="{PURPLE}"/>
<path d="M 33 34 C 39 34 44 36 44 42 L 33 42 Z" fill="{ACCENT2}" fill-opacity="0.6"/>
<rect x="30" y="40" width="18" height="12" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="1.8"/>
<path d="M 34 46 L 44 46" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round"/>'''),

    # Skype — cloud with phone
    "skype": tile("skype", f'''
<path d="M 22 24 C 22 18 30 16 34 20 C 40 18 46 23 43 29 C 47 34 43 41 37 40 C 34 45 25 45 23 39 C 17 38 16 29 22 24 Z" fill="none" stroke="{ACCENT}" stroke-width="2.2"/>
<path d="M 27 30 C 27 26 37 26 37 30 L 37 37 C 37 41 27 41 27 37 Z" fill="{ACCENT2}"/>'''),

    # Viber — phone with chat bubble
    "viber": tile("viber", f'''
<path d="M 20 18 L 32 18 L 32 30 L 26 36 L 26 30 L 20 30 Z" fill="none" stroke="{PURPLE}" stroke-width="2.2" stroke-linejoin="round"/>
<path d="M 36 22 C 42 22 46 27 46 33 C 46 40 41 45 34 45 C 28 45 25 41 25 37" fill="none" stroke="{ACCENT2}" stroke-width="2.2"/>
<path d="M 36 28 C 39 28 41 30 41 33" stroke="{ACCENT2}" stroke-width="1.8" fill="none" stroke-linecap="round"/>'''),

    # WeChat — dual bubbles
    "wechat": tile("wechat", f'''
<ellipse cx="26" cy="27" rx="11" ry="9" fill="none" stroke="{GREEN}" stroke-width="2.2"/>
<path d="M 19 35 L 17 41 L 24 36" fill="none" stroke="{GREEN}" stroke-width="2.2" stroke-linejoin="round"/>
<ellipse cx="38" cy="37" rx="9" ry="7.5" fill="{TILE_FILL}" stroke="{ACCENT2}" stroke-width="2"/>
<circle cx="22" cy="26" r="1.5" fill="{GREEN}"/><circle cx="30" cy="26" r="1.5" fill="{GREEN}"/>
<circle cx="35" cy="36" r="1.2" fill="{ACCENT2}"/><circle cx="41" cy="36" r="1.2" fill="{ACCENT2}"/>'''),

    # QQ — penguin face
    "qq": tile("qq", f'''
<ellipse cx="32" cy="34" rx="14" ry="15" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2"/>
<circle cx="26" cy="30" r="3" fill="{SNOW}"/>
<circle cx="38" cy="30" r="3" fill="{SNOW}"/>
<circle cx="26" cy="30" r="1.3" fill="{TILE_FILL}"/>
<circle cx="38" cy="30" r="1.3" fill="{TILE_FILL}"/>
<path d="M 29 38 L 32 41 L 35 38 Z" fill="{GOLD}"/>'''),

    # DingTalk — bubble with check
    "dingtalk": tile("dingtalk", f'''
<path d="M 16 20 L 48 20 L 48 40 L 28 40 L 20 48 L 20 40 L 16 40 Z" fill="none" stroke="{ACCENT}" stroke-width="2.4" stroke-linejoin="round"/>
<path d="M 26 30 L 30 34 L 38 26" stroke="{ACCENT2}" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'''),

    # WebCord — bubble with globe
    "webcord": tile("webcord", f'''
<path d="M 16 20 L 48 20 L 48 40 L 28 40 L 20 48 L 20 40 L 16 40 Z" fill="none" stroke="{ACCENT2}" stroke-width="2.4" stroke-linejoin="round"/>
<circle cx="32" cy="30" r="6" fill="none" stroke="{ACCENT}" stroke-width="1.8"/>
<line x1="26" y1="30" x2="38" y2="30" stroke="{ACCENT}" stroke-width="1.4"/>
<ellipse cx="32" cy="30" rx="2.4" ry="6" fill="none" stroke="{ACCENT}" stroke-width="1.2"/>'''),

    # WhatsApp — phone inside bubble
    "whatsapp": tile("whatsapp", f'''
<path d="M 32 14 C 22 14 14 22 14 32 C 14 36 15 39 17 42 L 14 50 L 22 47 C 25 49 28 50 32 50 C 42 50 50 42 50 32 C 50 22 42 14 32 14 Z" fill="none" stroke="{GREEN}" stroke-width="2.4"/>
<path d="M 25 26 C 25 22 39 22 39 26 L 39 36 C 39 40 25 40 25 36 Z" fill="none" stroke="{GREEN}" stroke-width="2.2"/>
<path d="M 28 33 C 30 36 34 36 36 33" stroke="{GREEN}" stroke-width="2" fill="none" stroke-linecap="round"/>'''),

    # Zoom — video camera
    "zoom": tile("zoom", f'''
<rect x="13" y="21" width="26" height="20" rx="4" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2"/>
<path d="M 39 28 L 51 22 L 51 42 L 39 36 Z" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2" stroke-linejoin="round"/>
<circle cx="26" cy="31" r="4" fill="{ACCENT2}"/>'''),

    # Tutanota — envelope with lock
    "tutanota-desktop": tile("tutanota-desktop", f'''
<rect x="13" y="20" width="38" height="24" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2"/>
<path d="M 13 22 L 32 34 L 51 22" fill="none" stroke="{ACCENT2}" stroke-width="2.2"/>
<rect x="26" y="30" width="12" height="9" rx="2" fill="{GOLD}"/>
<path d="M 29 30 L 29 27 C 29 24.5 35 24.5 35 27 L 35 30" stroke="{GOLD}" stroke-width="2" fill="none"/>'''),

    # Proton — envelope with atom core
    "protonplus": tile("protonplus", f'''
<rect x="13" y="20" width="38" height="24" rx="3" fill="{TILE_FILL}" stroke="{PURPLE}" stroke-width="2.2"/>
<path d="M 13 22 L 32 34 L 51 22" fill="none" stroke="{PURPLE}" stroke-width="2.2"/>
<circle cx="32" cy="31" r="2.4" fill="{PURPLE}"/>'''),

    # NordVPN — shield with N
    "nordvpn": tile("nordvpn", f'''
<path d="M 32 13 L 45 17 L 45 30 C 45 40 39 46 32 50 C 25 46 19 40 19 30 L 19 17 Z" fill="none" stroke="{ACCENT}" stroke-width="2.5" stroke-linejoin="round"/>
<path d="M 26 40 L 26 25 L 38 40 L 38 25" stroke="{ACCENT2}" stroke-width="2.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'''),

    # Nextcloud — cloud with sync arcs
    "nextcloud": tile("nextcloud", f'''
<path d="M 21 38 C 15 38 13 31 18 28 C 19 21 28 18 33 23 C 38 18 47 22 47 28 C 52 30 51 38 45 38 Z" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2"/>
<path d="M 25 43 A 8 8 0 0 1 39 43" stroke="{ACCENT2}" stroke-width="2" fill="none" stroke-linecap="round"/>
<path d="M 39 48 A 8 8 0 0 1 25 48" stroke="{ACCENT2}" stroke-width="2" fill="none" stroke-linecap="round"/>'''),

    # pCloud — cloud with P
    "pcloud": tile("pcloud", f'''
<path d="M 21 40 C 15 40 13 33 18 30 C 19 23 28 20 33 25 C 38 20 47 24 47 30 C 52 32 51 40 45 40 Z" fill="none" stroke="{ACCENT}" stroke-width="2.2"/>
<path d="M 29 46 L 29 36 L 34 36 C 37 36 37 41 34 41 L 29 41" stroke="{ACCENT2}" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'''),

    # MEGA — cloud with M monogram
    "mega": tile("mega", f'''
<path d="M 21 40 C 15 40 13 33 18 30 C 19 23 28 20 33 25 C 38 20 47 24 47 30 C 52 32 51 40 45 40 Z" fill="{TILE_FILL}" stroke="{RED}" stroke-width="2.2"/>
<path d="M 24 35 L 24 28 L 28 32 L 32 28 L 36 32 L 40 28 L 40 35" stroke="{RED}" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'''),

    # Dropbox — open box diamonds
    "dropbox": tile("dropbox", f'''
<path d="M 21 20 L 32 27 L 21 34 L 11 27 Z" fill="{ACCENT}"/>
<path d="M 43 20 L 53 27 L 43 34 L 32 27 Z" fill="{ACCENT}"/>
<path d="M 21 34 L 32 41 L 21 48 L 11 41 Z" fill="{ACCENT2}"/>
<path d="M 43 34 L 53 41 L 43 48 L 32 41 Z" fill="{ACCENT2}"/>'''),

    # Google Drive — triangle trio
    "google-drive": tile("google-drive", f'''
<path d="M 24 16 L 40 16 L 52 38 L 36 38 Z" fill="{ACCENT}" fill-opacity="0.9"/>
<path d="M 24 16 L 12 38 L 28 38 L 40 16 Z" fill="{GOLD}" fill-opacity="0.9"/>
<path d="M 12 38 L 20 50 L 44 50 L 52 38 Z" fill="{GREEN}" fill-opacity="0.9"/>'''),

    # ownCloud — simple cloud
    "owncloud": tile("owncloud", f'''
<path d="M 20 39 C 14 39 12 32 17 29 C 18 22 27 19 32 24 C 37 19 46 23 46 29 C 51 31 50 39 44 39 Z" fill="none" stroke="{ACCENT2}" stroke-width="2.4"/>'''),

    # Deezer — equalizer bars
    "deezer": tile("deezer", f'''
<g fill="{PURPLE}">
<rect x="15" y="38" width="5" height="10" rx="1"/>
<rect x="23" y="32" width="5" height="16" rx="1"/>
<rect x="31" y="26" width="5" height="22" rx="1"/>
<rect x="39" y="32" width="5" height="16" rx="1"/>
<rect x="47" y="38" width="5" height="10" rx="1"/>
</g>'''),

    # Spotube — play with note
    "spotube": tile("spotube", f'''
<circle cx="32" cy="32" r="16" fill="none" stroke="{GREEN}" stroke-width="2.4"/>
<polygon points="28,24 28,40 41,32" fill="{GREEN}"/>
<circle cx="22" cy="20" r="2" fill="{ACCENT}"/>'''),

    # Ripcord — chat with lightning
    "Ripcord_Icon": tile("ripcord", f'''
<path d="M 16 20 L 48 20 L 48 40 L 28 40 L 20 48 L 20 40 L 16 40 Z" fill="none" stroke="{ACCENT2}" stroke-width="2.4" stroke-linejoin="round"/>
<path d="M 34 24 L 27 33 L 32 33 L 29 40 L 38 30 L 33 30 Z" fill="{GOLD}"/>'''),

    # Betterbird — bird with forward arrow
    "betterbird": tile("betterbird", f'''
<path d="M 18 42 C 18 30 26 24 38 24 L 38 18 L 48 26 L 38 34 L 38 28 C 29 28 24 32 24 42 Z" fill="{ACCENT}"/>
<circle cx="33" cy="27" r="1.6" fill="{TILE_FILL}"/>'''),

    # NewsFlash — newspaper with RSS
    "newsflash": tile("newsflash", f'''
<rect x="13" y="18" width="38" height="28" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2.2"/>
<rect x="17" y="22" width="14" height="10" rx="1.5" fill="{ACCENT2}"/>
<line x1="17" y1="36" x2="47" y2="36" stroke="{ACCENT2}" stroke-width="2" stroke-linecap="round"/>
<line x1="17" y1="41" x2="40" y2="41" stroke="{ACCENT2}" stroke-width="2" stroke-linecap="round"/>
<path d="M 37 24 C 42 25 45 28 46 33" stroke="{ACCENT}" stroke-width="2" fill="none" stroke-linecap="round"/>'''),

    # gPodder — headphones
    "gpodder": tile("gpodder", f'''
<path d="M 18 36 L 18 30 C 18 22 24 16 32 16 C 40 16 46 22 46 30 L 46 36" fill="none" stroke="{ACCENT}" stroke-width="2.8" stroke-linecap="round"/>
<rect x="14" y="34" width="8" height="14" rx="3" fill="{ACCENT2}"/>
<rect x="42" y="34" width="8" height="14" rx="3" fill="{ACCENT2}"/>'''),

    # Cawbird — bird in bubble
    "cawbird": tile("cawbird", f'''
<path d="M 14 22 L 50 22 L 50 42 L 30 42 L 22 50 L 22 42 L 14 42 Z" fill="none" stroke="{ACCENT2}" stroke-width="2.4" stroke-linejoin="round"/>
<path d="M 22 36 C 22 27 30 24 36 26 C 42 28 42 34 38 36 C 34 38 26 38 22 36 Z" fill="{ACCENT}"/>
<circle cx="34" cy="28" r="1.4" fill="{TILE_FILL}"/>'''),

    # Tuner — radio waves with dial
    "com.github.louis77.tuner": tile("tuner", f'''
<circle cx="32" cy="32" r="15" fill="none" stroke="{ACCENT}" stroke-width="2.4"/>
<circle cx="32" cy="32" r="3" fill="{ACCENT2}"/>
<path d="M 32 20 L 36 32" stroke="{ACCENT2}" stroke-width="2.2" stroke-linecap="round"/>
<circle cx="40" cy="24" r="1.6" fill="{ACCENT}"/>
<circle cx="24" cy="24" r="1.6" fill="{ACCENT}"/>'''),
}

POPULAR_ALIASES_2 = {
    "franz-app": "franz",
    "rambox-app": "rambox",
    "teams": "teams-for-linux",
    "microsoft-teams": "teams-for-linux",
    "skypeforlinux": "skype",
    "viber-app": "viber",
    "wechat-app": "wechat",
    "linuxqq": "qq",
    "dingtalk-app": "dingtalk",
    "webcord-app": "webcord",
    "whatsapp-desktop": "whatsapp",
    "zoom-client": "zoom",
    "tutanota": "tutanota-desktop",
    "protonvpn": "protonplus",
    "nextcloud-client": "nextcloud",
    "dropbox-app": "dropbox",
    "google-drive-app": "google-drive",
    "owncloud-client": "owncloud",
    "deezer-app": "deezer",
    "spotube-app": "spotube",
    "ripcord": "Ripcord_Icon",
    "betterbird-app": "betterbird",
    "gpodder-app": "gpodder",
    "cawbird-app": "cawbird",
    "tuner": "com.github.louis77.tuner",
}

# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# FreeDesktop MIME badge library: badge SVG fragments + name→badge map.
# Badges are composited over MIME_DOC_BASE in tools/icons/generate_icons.py.

# Shared 64x64 badge fragments drawn inside the document body area.
BADGES = {
    # Generic text lines
    "text": '''
<line x1="21" y1="28" x2="43" y2="28" stroke="{COLOR_ACCENT}" stroke-width="2" stroke-linecap="round"/>
<line x1="21" y1="34" x2="43" y2="34" stroke="{COLOR_ACCENT}" stroke-width="2" stroke-linecap="round"/>
<line x1="21" y1="40" x2="35" y2="40" stroke="{COLOR_ACCENT}" stroke-width="2" stroke-linecap="round"/>
''',
    # Paragraph document
    "doc": '''
<line x1="21" y1="28" x2="43" y2="28" stroke="{COLOR_ACCENT_STRONG}" stroke-width="2.4" stroke-linecap="round"/>
<line x1="21" y1="33" x2="43" y2="33" stroke="{COLOR_ACCENT}" stroke-width="1.8" stroke-linecap="round"/>
<line x1="21" y1="37.5" x2="43" y2="37.5" stroke="{COLOR_ACCENT}" stroke-width="1.8" stroke-linecap="round"/>
<line x1="21" y1="42" x2="35" y2="42" stroke="{COLOR_ACCENT}" stroke-width="1.8" stroke-linecap="round"/>
''',
    # Image with sun and mountains
    "image": '''
<rect x="20" y="26" width="24" height="18" rx="2.5" fill="#151D2A" stroke="{COLOR_ACCENT}" stroke-width="1.5"/>
<circle cx="26" cy="31.5" r="2" fill="#EBCB8B"/>
<polygon points="22,42 28,35 33,40 37,36 42,42" fill="{COLOR_ACCENT}"/>
''',
    # Video frame with play glyph
    "video": '''
<rect x="19" y="26" width="26" height="18" rx="3" fill="#151D2A" stroke="{COLOR_ACCENT}" stroke-width="1.5"/>
<polygon points="28,30 28,40 37,35" fill="{COLOR_ACCENT_STRONG}"/>
''',
    # Music note
    "audio": '''
<rect x="36" y="26" width="2" height="13" rx="1" fill="{COLOR_ACCENT}"/>
<ellipse cx="34.4" cy="39.4" rx="3.6" ry="2.8" fill="{COLOR_ACCENT}"/>
<path d="M 38 26 C 40.5 26.4 42.5 28 42.5 30.5 L 40.8 30.2 C 40.8 28.8 39.8 27.8 38 27.4 Z" fill="{COLOR_ACCENT_STRONG}"/>
''',
    # Archive zipper
    "archive": '''
<rect x="26" y="26" width="12" height="3" rx="1.5" fill="{COLOR_ACCENT_STRONG}"/>
<g fill="{COLOR_ACCENT}">
  <rect x="30" y="30" width="4" height="3" rx="1"/>
  <rect x="30" y="34.5" width="4" height="3" rx="1"/>
  <rect x="30" y="39" width="4" height="3" rx="1"/>
</g>
<rect x="30" y="43" width="4" height="4" rx="1" fill="#EBCB8B"/>
''',
    # Code brackets with slash
    "code": '''
<path d="M 26 30 L 20.5 36 L 26 42" stroke="{COLOR_ACCENT}" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M 38 30 L 43.5 36 L 38 42" stroke="{COLOR_ACCENT}" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<line x1="34.5" y1="29" x2="29.5" y2="43" stroke="{COLOR_ACCENT_STRONG}" stroke-width="2" stroke-linecap="round"/>
''',
    # Spreadsheet grid
    "sheet": '''
<rect x="20" y="26" width="24" height="18" rx="2" fill="#151D2A" stroke="{COLOR_ACCENT}" stroke-width="1.4"/>
<line x1="20" y1="31" x2="44" y2="31" stroke="{COLOR_ACCENT_STRONG}" stroke-width="1.6"/>
<line x1="28" y1="26" x2="28" y2="44" stroke="{COLOR_BORDER}" stroke-width="1.2"/>
<line x1="36" y1="26" x2="36" y2="44" stroke="{COLOR_BORDER}" stroke-width="1.2"/>
<line x1="20" y1="37" x2="44" y2="37" stroke="{COLOR_BORDER}" stroke-width="1.2"/>
''',
    # Presentation with bar chart
    "slides": '''
<rect x="20" y="25" width="24" height="15" rx="2" fill="#151D2A" stroke="{COLOR_ACCENT}" stroke-width="1.4"/>
<rect x="23" y="34" width="3" height="4" fill="{COLOR_ACCENT}"/>
<rect x="28" y="31" width="3" height="7" fill="{COLOR_ACCENT_STRONG}"/>
<rect x="33" y="29" width="3" height="9" fill="{COLOR_ACCENT}"/>
<rect x="30" y="40" width="4" height="3" fill="{COLOR_BORDER}"/>
<rect x="24" y="44" width="16" height="2" rx="1" fill="{COLOR_BORDER}"/>
''',
    # Font specimen letter
    "font": '''
<text x="32" y="43" font-size="19" font-weight="bold" fill="{COLOR_ACCENT}" text-anchor="middle" font-family="sans-serif">A</text>
''',
    # Executable terminal window
    "exe": '''
<rect x="20" y="26" width="24" height="18" rx="2.5" fill="#151D2A" stroke="{COLOR_ACCENT}" stroke-width="1.5"/>
<path d="M 25 33 L 29 37 L 25 41" stroke="{COLOR_ACCENT_STRONG}" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<line x1="31" y1="41" x2="38" y2="41" stroke="{COLOR_ACCENT}" stroke-width="2" stroke-linecap="round"/>
''',
    # Optical disc
    "disc": '''
<circle cx="32" cy="36" r="9" fill="#151D2A" stroke="{COLOR_ACCENT}" stroke-width="1.6"/>
<circle cx="32" cy="36" r="3" fill="{COLOR_ACCENT_STRONG}"/>
<path d="M 26 31 A 8 8 0 0 1 36 29" stroke="{COLOR_BORDER}" stroke-width="1.6" fill="none" stroke-linecap="round"/>
''',
    # Calendar grid
    "calendar": '''
<rect x="21" y="26" width="22" height="18" rx="2.5" fill="#151D2A" stroke="{COLOR_ACCENT}" stroke-width="1.4"/>
<rect x="21" y="26" width="22" height="5" rx="2.5" fill="{COLOR_ACCENT_STRONG}"/>
<circle cx="27" cy="37" r="1.4" fill="{COLOR_ACCENT}"/>
<circle cx="32" cy="37" r="1.4" fill="{COLOR_ACCENT}"/>
<circle cx="37" cy="37" r="1.4" fill="{COLOR_ACCENT}"/>
<circle cx="27" cy="41.5" r="1.4" fill="{COLOR_ACCENT}"/>
<circle cx="32" cy="41.5" r="1.4" fill="{COLOR_ACCENT}"/>
''',
    # Contact person
    "contact": '''
<circle cx="32" cy="32" r="4.4" fill="{COLOR_ACCENT}"/>
<path d="M 23 44 C 23 39 26.5 37.4 32 37.4 C 37.5 37.4 41 39 41 44 Z" fill="{COLOR_ACCENT_STRONG}"/>
''',
    # Web globe
    "web": '''
<circle cx="32" cy="36" r="9" fill="none" stroke="{COLOR_ACCENT}" stroke-width="1.8"/>
<ellipse cx="32" cy="36" rx="4" ry="9" fill="none" stroke="{COLOR_ACCENT}" stroke-width="1.2"/>
<line x1="23" y1="36" x2="41" y2="36" stroke="{COLOR_ACCENT}" stroke-width="1.2"/>
''',
    # 3D model cube
    "model": '''
<path d="M 32 26 L 41 31 L 41 41 L 32 46 L 23 41 L 23 31 Z" fill="#151D2A" stroke="{COLOR_ACCENT}" stroke-width="1.6" stroke-linejoin="round"/>
<path d="M 23 31 L 32 36 L 41 31 M 32 36 L 32 46" stroke="{COLOR_ACCENT_STRONG}" stroke-width="1.4" fill="none"/>
''',
    # Ebook open pages
    "book": '''
<path d="M 22 27 C 22 26 23 25.5 24 25.5 L 31 25.5 L 31 45 L 24 45 C 23 45 22 44.5 22 43.5 Z" fill="{COLOR_ACCENT}" fill-opacity="0.85"/>
<path d="M 42 27 C 42 26 41 25.5 40 25.5 L 33 25.5 L 33 45 L 40 45 C 41 45 42 44.5 42 43.5 Z" fill="{COLOR_ACCENT_STRONG}" fill-opacity="0.85"/>
''',
    # Torrent download arrow
    "torrent": '''
<path d="M 32 26 L 32 38" stroke="{COLOR_ACCENT}" stroke-width="2.4" stroke-linecap="round"/>
<path d="M 26 34 L 32 41 L 38 34" stroke="{COLOR_ACCENT_STRONG}" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M 24 45 L 40 45" stroke="{COLOR_BORDER}" stroke-width="2" stroke-linecap="round"/>
''',
    # Software package box
    "package": '''
<path d="M 32 25 L 41 29.5 L 41 40.5 L 32 45 L 23 40.5 L 23 29.5 Z" fill="#151D2A" stroke="{COLOR_ACCENT}" stroke-width="1.6"/>
<path d="M 23 29.5 L 32 34 L 41 29.5" stroke="{COLOR_ACCENT_STRONG}" stroke-width="1.6" fill="none"/>
<line x1="32" y1="34" x2="32" y2="45" stroke="{COLOR_ACCENT}" stroke-width="1.4"/>
''',
    # RAW camera
    "camera": '''
<rect x="22" y="29" width="20" height="14" rx="2.5" fill="#151D2A" stroke="{COLOR_ACCENT}" stroke-width="1.6"/>
<circle cx="32" cy="36" r="4" fill="none" stroke="{COLOR_ACCENT_STRONG}" stroke-width="1.8"/>
<rect x="26" y="26" width="8" height="4" rx="1.5" fill="{COLOR_ACCENT}"/>
''',
    # Database cylinders
    "db": '''
<ellipse cx="32" cy="28" rx="9" ry="3.2" fill="{COLOR_ACCENT_STRONG}"/>
<path d="M 23 28 L 23 43 C 23 44.8 27 46.2 32 46.2 C 37 46.2 41 44.8 41 43 L 41 28" fill="{COLOR_ACCENT}" fill-opacity="0.35" stroke="{COLOR_ACCENT}" stroke-width="1.4"/>
<path d="M 23 35.5 C 23 37.3 27 38.7 32 38.7 C 37 38.7 41 37.3 41 35.5" fill="none" stroke="{COLOR_ACCENT}" stroke-width="1.2"/>
''',
    # Configuration gear
    "config": '''
<circle cx="32" cy="36" r="6" fill="none" stroke="{COLOR_ACCENT}" stroke-width="2"/>
<circle cx="32" cy="36" r="2" fill="{COLOR_ACCENT}"/>
<g stroke="{COLOR_ACCENT}" stroke-width="2" stroke-linecap="round">
  <line x1="32" y1="26" x2="32" y2="29"/><line x1="32" y1="43" x2="32" y2="46"/>
  <line x1="22" y1="36" x2="25" y2="36"/><line x1="39" y1="36" x2="42" y2="36"/>
  <line x1="25" y1="29" x2="27" y2="31"/><line x1="37" y1="41" x2="39" y2="43"/>
  <line x1="39" y1="29" x2="37" y2="31"/><line x1="27" y1="41" x2="25" y2="43"/>
</g>
''',
    # Vector curve with nodes
    "vector": '''
<path d="M 23 42 C 25 32 33 30 41 28" stroke="{COLOR_ACCENT}" stroke-width="2" fill="none" stroke-linecap="round"/>
<circle cx="23" cy="42" r="2" fill="{COLOR_ACCENT_STRONG}"/>
<circle cx="41" cy="28" r="2" fill="{COLOR_ACCENT_STRONG}"/>
<rect x="29" y="32" width="6" height="6" rx="1" fill="none" stroke="{COLOR_BORDER}" stroke-width="1.2"/>
''',
    # Shell terminal prompt
    "shell": '''
<rect x="20" y="26" width="24" height="18" rx="2.5" fill="#151D2A" stroke="{COLOR_ACCENT}" stroke-width="1.5"/>
<path d="M 24.5 32 L 28 35.5 L 24.5 39" stroke="{COLOR_ACCENT_STRONG}" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<line x1="30" y1="39.5" x2="37" y2="39.5" stroke="{COLOR_ACCENT}" stroke-width="2" stroke-linecap="round"/>
''',
}

# FreeDesktop MIME type → badge kind (merged into MIME_ICONS at build time).
MIME_BADGE_MAP = {
    # Documents & office
    "application/msword": "doc",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "doc",
    "application/vnd.oasis.opendocument.text": "doc",
    "application/vnd.oasis.opendocument.text-template": "doc",
    "application/rtf": "doc",
    "text/x-markdown": "doc",
    "application/vnd.oasis.opendocument.graphics": "vector",
    "application/vnd.ms-excel": "sheet",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": "sheet",
    "application/vnd.oasis.opendocument.spreadsheet": "sheet",
    "text/csv": "sheet",
    "application/vnd.ms-powerpoint": "slides",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation": "slides",
    "application/vnd.oasis.opendocument.presentation": "slides",
    # Web & code
    "text/html": "web",
    "text/xml": "code",
    "application/xml": "code",
    "text/javascript": "code",
    "application/javascript": "code",
    "application/json": "code",
    "text/css": "code",
    "text/x-csrc": "code",
    "text/x-c++src": "code",
    "text/x-java": "code",
    "text/x-perl": "code",
    "text/x-ruby": "code",
    "text/x-php": "code",
    "text/x-lua": "code",
    "text/x-go": "code",
    "text/x-rust": "code",
    "text/x-shellscript": "shell",
    "application/x-shellscript": "shell",
    # Archives
    "application/zip": "archive",
    "application/x-7z-compressed": "archive",
    "application/x-rar": "archive",
    "application/x-tar": "archive",
    "application/gzip": "archive",
    "application/x-compressed-tar": "archive",
    "application/x-bzip2": "archive",
    "application/x-xz": "archive",
    "application/x-lzma": "archive",
    "application/x-zstd": "archive",
    "application/x-lz4": "archive",
    # Packages & installers
    "application/x-deb": "package",
    "application/x-rpm": "package",
    "application/x-appimage": "package",
    "application/vnd.flatpak": "package",
    "application/x-msi": "package",
    "application/x-java-archive": "package",
    "application/vnd.android.package-archive": "package",
    # Disc images
    "application/x-cd-image": "disc",
    "application/x-iso9660-image": "disc",
    "application/x-raw-disk-image": "disc",
    # Fonts
    "application/x-font-ttf": "font",
    "application/x-font-otf": "font",
    "application/font-woff": "font",
    "application/vnd.ms-fontobject": "font",
    "application/x-font-bdf": "font",
    # Ebooks
    "application/epub+zip": "book",
    "application/x-mobipocket-ebook": "book",
    # Torrents
    "application/x-bittorrent": "torrent",
    # 3D models
    "model/stl": "model",
    "model/obj": "model",
    "model/gltf-binary": "model",
    "application/x-blender": "model",
    # Databases
    "application/x-sqlite3": "db",
    "application/x-database": "db",
    # Config
    "application/x-desktop": "config",
    "application/x-wine-extension-ini": "config",
    # Images
    "image/png": "image",
    "image/jpeg": "image",
    "image/gif": "image",
    "image/webp": "image",
    "image/bmp": "image",
    "image/tiff": "image",
    "image/x-icon": "image",
    "image/heic": "image",
    "image/avif": "image",
    "image/vnd.adobe.photoshop": "image",
    "image/x-xcf": "image",
    "image/svg+xml": "vector",
    # Video
    "video/mp4": "video",
    "video/x-matroska": "video",
    "video/webm": "video",
    "video/x-msvideo": "video",
    "video/quicktime": "video",
    "video/mpeg": "video",
    "video/x-flv": "video",
    "video/ogg": "video",
    "video/3gpp": "video",
    # Audio
    "audio/mpeg": "audio",
    "audio/ogg": "audio",
    "audio/flac": "audio",
    "audio/x-wav": "audio",
    "audio/wav": "audio",
    "audio/mp4": "audio",
    "audio/x-m4a": "audio",
    "audio/opus": "audio",
    "audio/x-aac": "audio",
    "audio/x-midi": "audio",
    # Generic fallbacks
    "image-x-generic": "image",
    "video-x-generic": "video",
    "audio-x-generic": "audio",
    "text-x-generic": "text",
    "application-x-generic": "doc",
    "package-x-generic": "package",
    "font-x-generic": "font",
    "x-office-document": "doc",
    "x-office-spreadsheet": "sheet",
    "x-office-presentation": "slides",
    "x-office-calendar": "calendar",
    "x-office-address-book": "contact",
}

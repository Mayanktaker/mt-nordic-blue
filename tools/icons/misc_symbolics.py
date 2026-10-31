# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Miscellaneous legacy/FreeDesktop symbolic glyphs missing from the MT-Nordic-Blue suite.
# Filled 16x16 paths using currentColor, safe for GTK4 symbolic shaders.

MISC_SYMBOLIC_ICONS = {
    # 1. Application exit — door with outward arrow
    "application-exit": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 2 2 C 1.45 2 1 2.45 1 3 L 1 13 C 1 13.55 1.45 14 2 14 L 6 14 C 6.55 14 7 13.55 7 13 L 7 11.5 L 5.5 11.5 L 5.5 12.5 L 2.5 12.5 L 2.5 3.5 L 5.5 3.5 L 5.5 4.5 L 7 4.5 L 7 3 C 7 2.45 6.55 2 6 2 Z"/>
  <path fill="currentColor" d="M 9.5 5 L 14.5 8 L 9.5 11 L 9.5 8.8 L 5.5 8.8 L 5.5 7.2 L 9.5 7.2 Z"/>
</svg>''',

    # 2. Applications system — category gear alias
    "applications-system-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 8 0.9 C 8.62 0.9 9.12 1.4 9.12 2.02 L 9.12 3.2 C 9.5 3.32 9.86 3.5 10.18 3.72 L 11.02 2.88 C 11.46 2.44 12.16 2.44 12.6 2.88 C 13.04 3.32 13.04 4.02 12.6 4.46 L 11.76 5.3 C 11.98 5.62 12.16 5.98 12.28 6.36 L 13.46 6.36 C 14.08 6.36 14.58 6.86 14.58 7.48 L 14.58 8.52 C 14.58 9.14 14.08 9.64 13.46 9.64 L 12.28 9.64 C 12.16 10.02 11.98 10.38 11.76 10.7 L 12.6 11.54 C 13.04 11.98 13.04 12.68 12.6 13.12 C 12.16 13.56 11.46 13.56 11.02 13.12 L 10.18 12.28 C 9.86 12.5 9.5 12.68 9.12 12.8 L 9.12 13.98 C 9.12 14.6 8.62 15.1 8 15.1 C 7.38 15.1 6.88 14.6 6.88 13.98 L 6.88 12.8 C 6.5 12.68 6.14 12.5 5.82 12.28 L 4.98 13.12 C 4.54 13.56 3.84 13.56 3.4 13.12 C 2.96 12.68 2.96 11.98 3.4 11.54 L 4.24 10.7 C 4.02 10.38 3.84 10.02 3.72 9.64 L 2.54 9.64 C 1.92 9.64 1.42 9.14 1.42 8.52 L 1.42 7.48 C 1.42 6.86 1.92 6.36 2.54 6.36 L 3.72 6.36 C 3.84 5.98 4.02 5.62 4.24 5.3 L 3.4 4.46 C 2.96 4.02 2.96 3.32 3.4 2.88 C 3.84 2.44 4.54 2.44 4.98 2.88 L 5.82 3.72 C 6.14 3.5 6.5 3.32 6.88 3.2 L 6.88 2.02 C 6.88 1.4 7.38 0.9 8 0.9 Z M 8 5.9 C 6.84 5.9 5.9 6.84 5.9 8 C 5.9 9.16 6.84 10.1 8 10.1 C 9.16 10.1 10.1 9.16 10.1 8 C 10.1 6.84 9.16 5.9 8 5.9 Z"/>
</svg>''',

    # 3. Appointment soon — calendar with imminent dot
    "appointment-soon": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 3 2 C 2.17 2 1.5 2.67 1.5 3.5 L 1.5 13 C 1.5 13.83 2.17 14.5 3 14.5 L 13 14.5 C 13.83 14.5 14.5 13.83 14.5 13 L 14.5 3.5 C 14.5 2.67 13.83 2 13 2 Z M 3 4 L 13 4 L 13 13 L 3 13 Z M 4.5 2.8 L 5.5 2.8 L 5.5 5 L 4.5 5 Z M 10.5 2.8 L 11.5 2.8 L 11.5 5 L 10.5 5 Z"/>
  <circle cx="8" cy="8.6" r="1.6" fill="currentColor"/>
</svg>''',

    # 4. Dialog password — key
    "dialog-password": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 10 1.5 C 7.5 1.5 5.5 3.5 5.5 6 C 5.5 6.6 5.6 7.2 5.8 7.7 L 1.6 11.9 C 1.2 12.3 1.2 12.9 1.6 13.3 L 2.7 14.4 C 3.1 14.8 3.7 14.8 4.1 14.4 L 4.8 13.7 L 6 13.7 L 6 12.5 L 7.2 12.5 L 7.2 11.3 L 8.3 11.3 L 8.3 10.2 C 8.8 10.4 9.4 10.5 10 10.5 C 12.5 10.5 14.5 8.5 14.5 6 C 14.5 3.5 12.5 1.5 10 1.5 Z M 10 3 C 11.7 3 13 4.3 13 6 C 13 7.7 11.7 9 10 9 C 8.3 9 7 7.7 7 6 C 7 4.3 8.3 3 10 3 Z"/>
</svg>''',

    # 5. Document new — page with plus badge
    "document-new": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 4 1.5 C 3.17 1.5 2.5 2.17 2.5 3 L 2.5 13 C 2.5 13.83 3.17 14.5 4 14.5 L 12 14.5 C 12.83 14.5 13.5 13.83 13.5 13 L 13.5 6 L 9 1.5 Z M 4 3 L 8.5 3 L 8.5 6.5 L 12 6.5 L 12 13 L 4 13 Z"/>
  <path fill="currentColor" d="M 7.2 8 L 8.8 8 L 8.8 9.6 L 10.4 9.6 L 10.4 11.2 L 8.8 11.2 L 8.8 12.8 L 7.2 12.8 L 7.2 11.2 L 5.6 11.2 L 5.6 9.6 L 7.2 9.6 Z"/>
</svg>''',

    # 6. Document print preview — page with text preview lines
    "document-print-preview": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 4 1.5 C 3.17 1.5 2.5 2.17 2.5 3 L 2.5 13 C 2.5 13.83 3.17 14.5 4 14.5 L 12 14.5 C 12.83 14.5 13.5 13.83 13.5 13 L 13.5 6 L 9 1.5 Z M 4 3 L 8.5 3 L 8.5 6.5 L 12 6.5 L 12 13 L 4 13 Z"/>
  <path fill="currentColor" d="M 5.5 8 L 10.5 8 L 10.5 9.2 L 5.5 9.2 Z M 5.5 10.4 L 9 10.4 L 9 11.6 L 5.5 11.6 Z"/>
</svg>''',

    # 7. Drive removable media — USB stick
    "drive-removable-media": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 6 1.5 C 5.45 1.5 5 1.95 5 2.5 L 5 5 L 3 7 L 3 13.5 C 3 14.05 3.45 14.5 4 14.5 L 12 14.5 C 12.55 14.5 13 14.05 13 13.5 L 13 7 L 11 5 L 11 2.5 C 11 1.95 10.55 1.5 10 1.5 Z M 6.5 3 L 7.5 3 L 7.5 4.5 L 6.5 4.5 Z M 8.5 3 L 9.5 3 L 9.5 4.5 L 8.5 4.5 Z M 4.5 8 L 11.5 8 L 11.5 13 L 4.5 13 Z"/>
</svg>''',

    # 8. Flatpak — sandbox package box
    "flatpak-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 8 1.2 L 14 4.6 L 14 11.4 L 8 14.8 L 2 11.4 L 2 4.6 Z M 8 3 L 3.5 5.6 L 8 8.2 L 12.5 5.6 Z M 3.5 7 L 7.2 9.1 L 7.2 13 L 3.5 10.9 Z M 12.5 7 L 8.8 9.1 L 8.8 13 L 12.5 10.9 Z"/>
</svg>''',

    # 9. Folder remote — folder with cloud badge
    "folder-remote": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 1.5 3.5 C 1.5 2.67 2.17 2 3 2 L 6.2 2 L 7.7 3.8 L 13 3.8 C 13.83 3.8 14.5 4.47 14.5 5.3 L 14.5 12.2 C 14.5 13.03 13.83 13.7 13 13.7 L 3 13.7 C 2.17 13.7 1.5 13.03 1.5 12.2 Z M 3 4 L 3 12 L 13 12 L 13 5.3 L 7.2 5.3 L 5.7 3.5 Z"/>
  <path fill="currentColor" d="M 6.5 8.2 C 6.5 7.4 7.1 6.8 7.9 6.8 C 8.4 6.8 8.9 7.1 9.1 7.5 C 9.2 7.5 9.4 7.4 9.6 7.4 C 10.4 7.4 11 8 11 8.8 C 11 9.6 10.4 10.2 9.6 10.2 L 7 10.2 C 6.3 10.2 5.8 9.7 5.8 9.1 C 5.8 8.6 6.1 8.3 6.5 8.2 Z"/>
</svg>''',

    # 10. Map globe — equator globe glyph
    "map-globe": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 8 1 C 4.134 1 1 4.134 1 8 C 1 11.866 4.134 15 8 15 C 11.866 15 15 11.866 15 8 C 15 4.134 11.866 1 8 1 Z M 8 2.5 C 11.038 2.5 13.5 4.962 13.5 8 C 13.5 11.038 11.038 13.5 8 13.5 C 4.962 13.5 2.5 11.038 2.5 8 C 2.5 4.962 4.962 2.5 8 2.5 Z"/>
  <path fill="currentColor" d="M 7.4 2.6 C 6.4 4 5.9 5.9 5.9 8 C 5.9 10.1 6.4 12 7.4 13.4 L 8.6 13.4 C 7.6 12 7.1 10.1 7.1 8 C 7.1 5.9 7.6 4 8.6 2.6 Z"/>
  <rect x="2.7" y="7.3" width="10.6" height="1.4" fill="currentColor"/>
</svg>''',

    # 11. Mark location — map pin
    "mark-location-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" d="M 8 1.2 C 5.5 1.2 3.5 3.2 3.5 5.7 C 3.5 8.9 8 14.8 8 14.8 C 8 14.8 12.5 8.9 12.5 5.7 C 12.5 3.2 10.5 1.2 8 1.2 Z M 8 3.9 C 9 3.9 9.8 4.7 9.8 5.7 C 9.8 6.7 9 7.5 8 7.5 C 7 7.5 6.2 6.7 6.2 5.7 C 6.2 4.7 7 3.9 8 3.9 Z"/>
</svg>''',

    # 12. Network wireless — three wifi arcs with dot
    "network-wireless-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" d="M 8 11.5 C 8.8 11.5 9.5 12.2 9.5 13 C 9.5 13.8 8.8 14.5 8 14.5 C 7.2 14.5 6.5 13.8 6.5 13 C 6.5 12.2 7.2 11.5 8 11.5 Z"/>
  <path fill="currentColor" d="M 4.4 8.4 C 5.4 7.5 6.6 7 8 7 C 9.4 7 10.6 7.5 11.6 8.4 L 10.4 9.7 C 9.7 9.1 8.9 8.8 8 8.8 C 7.1 8.8 6.3 9.1 5.6 9.7 Z"/>
  <path fill="currentColor" d="M 1.8 5.6 C 3.5 4.1 5.6 3.2 8 3.2 C 10.4 3.2 12.5 4.1 14.2 5.6 L 13 6.9 C 11.6 5.7 9.9 5 8 5 C 6.1 5 4.4 5.7 3 6.9 Z"/>
</svg>''',

    # 13. Preferences desktop keyboard — full keyboard glyph
    "preferences-desktop-keyboard": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 2.2 3 C 1.26 3 0.5 3.76 0.5 4.7 L 0.5 11.3 C 0.5 12.24 1.26 13 2.2 13 L 13.8 13 C 14.74 13 15.5 12.24 15.5 11.3 L 15.5 4.7 C 15.5 3.76 14.74 3 13.8 3 Z M 2.2 4.5 L 3.3 4.5 L 3.3 5.6 L 2.2 5.6 Z M 4.4 4.5 L 5.5 4.5 L 5.5 5.6 L 4.4 5.6 Z M 6.6 4.5 L 7.7 4.5 L 7.7 5.6 L 6.6 5.6 Z M 8.8 4.5 L 9.9 4.5 L 9.9 5.6 L 8.8 5.6 Z M 11 4.5 L 12.2 4.5 L 12.2 5.6 L 11 5.6 Z M 2.2 6.8 L 3.3 6.8 L 3.3 7.9 L 2.2 7.9 Z M 4.4 6.8 L 5.5 6.8 L 5.5 7.9 L 4.4 7.9 Z M 6.6 6.8 L 7.7 6.8 L 7.7 7.9 L 6.6 7.9 Z M 8.8 6.8 L 9.9 6.8 L 9.9 7.9 L 8.8 7.9 Z M 11 6.8 L 12.2 6.8 L 12.2 7.9 L 11 7.9 Z M 4.4 9.1 L 11.2 9.1 L 11.2 10.4 L 4.4 10.4 Z"/>
</svg>''',

    # 14. Security medium — half-filled shield
    "security-medium": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 8 1 L 2 3.2 L 2 7.6 C 2 11.4 4.6 14.1 8 15 C 11.4 14.1 14 11.4 14 7.6 L 14 3.2 Z M 8 2.8 L 12.5 4.4 L 12.5 7.6 C 12.5 10.4 10.7 12.4 8 13.2 Z"/>
</svg>''',

    # 15. Tab new — browser tab with plus badge
    "tab-new": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 2 3 C 1.17 3 0.5 3.67 0.5 4.5 L 0.5 12 C 0.5 12.83 1.17 13.5 2 13.5 L 12.5 13.5 C 13.33 13.5 14 12.83 14 12 L 14 9 L 12.5 9 L 12.5 12 L 2 12 L 2 4.5 L 8 4.5 L 8 3 Z"/>
  <path fill="currentColor" d="M 12 1 L 13.2 1 L 13.2 3.3 L 15.5 3.3 L 15.5 4.5 L 13.2 4.5 L 13.2 6.8 L 12 6.8 L 12 4.5 L 9.7 4.5 L 9.7 3.3 L 12 3.3 Z"/>
</svg>''',

    # 16. Window new — window frame with plus badge
    "window-new": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 2 2 C 1.17 2 0.5 2.67 0.5 3.5 L 0.5 12.5 C 0.5 13.33 1.17 14 2 14 L 12 14 C 12.83 14 13.5 13.33 13.5 12.5 L 13.5 8 L 12 8 L 12 12.5 L 2 12.5 L 2 3.5 L 8 3.5 L 8 2 Z"/>
  <path fill="currentColor" d="M 12 0.5 L 13.2 0.5 L 13.2 2.8 L 15.5 2.8 L 15.5 4 L 13.2 4 L 13.2 6.3 L 12 6.3 L 12 4 L 9.7 4 L 9.7 2.8 L 12 2.8 Z"/>
</svg>''',
}

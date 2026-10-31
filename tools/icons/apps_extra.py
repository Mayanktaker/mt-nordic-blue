# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# System utility application icons (KDE wallet, QEMU, IBus, Orca, Rygel, etc.)
# 64x64 Nordic vector tiles matching palette/tokens.json accents.

EXTRA_APP_ICONS = {
    # 1. KWalletManager — leather wallet with card slot
    "kwalletmanager": '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs>
  <linearGradient id="kwBg" x1="32" y1="6" x2="32" y2="58" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#25344A"/>
    <stop offset="100%" stop-color="#0e141d"/>
  </linearGradient>
  <linearGradient id="kwCard" x1="14" y1="30" x2="50" y2="30" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#88C0D0"/>
    <stop offset="100%" stop-color="#00D2FF"/>
  </linearGradient>
</defs>
<rect x="6" y="6" width="52" height="52" rx="14" fill="url(#kwBg)" stroke="#25344A" stroke-width="1.5"/>
<rect x="8.5" y="8.5" width="47" height="4" rx="2" fill="#88C0D0" fill-opacity="0.25"/>
<rect x="13" y="20" width="38" height="26" rx="5" fill="#1A2434" stroke="#405878" stroke-width="1.5"/>
<rect x="13" y="20" width="38" height="7" rx="3.5" fill="#2E415A"/>
<rect x="17" y="33" width="22" height="9" rx="2.5" fill="url(#kwCard)" fill-opacity="0.85"/>
<circle cx="45" cy="37.5" r="3.5" fill="#ECEFF4"/>
<circle cx="45" cy="37.5" r="1.5" fill="#0e141d"/>
</svg>''',

    # 2. QEMU — virtual machine processor chip
    "qemu": '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs>
  <linearGradient id="qemuBg" x1="32" y1="6" x2="32" y2="58" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#25344A"/>
    <stop offset="100%" stop-color="#0e141d"/>
  </linearGradient>
</defs>
<rect x="6" y="6" width="52" height="52" rx="14" fill="url(#qemuBg)" stroke="#25344A" stroke-width="1.5"/>
<rect x="8.5" y="8.5" width="47" height="4" rx="2" fill="#88C0D0" fill-opacity="0.25"/>
<rect x="20" y="20" width="24" height="24" rx="4" fill="#1A2434" stroke="#00D2FF" stroke-width="2"/>
<rect x="27" y="27" width="10" height="10" rx="2" fill="#00D2FF"/>
<g stroke="#88C0D0" stroke-width="2" stroke-linecap="round">
  <line x1="26" y1="14" x2="26" y2="20"/><line x1="32" y1="14" x2="32" y2="20"/><line x1="38" y1="14" x2="38" y2="20"/>
  <line x1="26" y1="44" x2="26" y2="50"/><line x1="32" y1="44" x2="32" y2="50"/><line x1="38" y1="44" x2="38" y2="50"/>
  <line x1="14" y1="26" x2="20" y2="26"/><line x1="14" y1="32" x2="20" y2="32"/><line x1="14" y1="38" x2="20" y2="38"/>
  <line x1="44" y1="26" x2="50" y2="26"/><line x1="44" y1="32" x2="50" y2="32"/><line x1="44" y1="38" x2="50" y2="38"/>
</g>
</svg>''',

    # 3. IBus — input keyboard with globe badge
    "ibus": '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs>
  <linearGradient id="ibusBg" x1="32" y1="6" x2="32" y2="58" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#25344A"/>
    <stop offset="100%" stop-color="#0e141d"/>
  </linearGradient>
</defs>
<rect x="6" y="6" width="52" height="52" rx="14" fill="url(#ibusBg)" stroke="#25344A" stroke-width="1.5"/>
<rect x="8.5" y="8.5" width="47" height="4" rx="2" fill="#88C0D0" fill-opacity="0.25"/>
<rect x="12" y="22" width="34" height="20" rx="4" fill="#1A2434" stroke="#405878" stroke-width="1.5"/>
<g fill="#88C0D0">
  <rect x="16" y="26" width="4" height="4" rx="1"/><rect x="22" y="26" width="4" height="4" rx="1"/>
  <rect x="28" y="26" width="4" height="4" rx="1"/><rect x="34" y="26" width="4" height="4" rx="1"/>
  <rect x="16" y="32" width="4" height="4" rx="1"/><rect x="22" y="32" width="4" height="4" rx="1"/>
  <rect x="28" y="32" width="4" height="4" rx="1"/><rect x="34" y="32" width="4" height="4" rx="1"/>
  <rect x="20" y="38" width="18" height="3" rx="1.5"/>
</g>
<circle cx="46" cy="40" r="10" fill="#0e141d" stroke="#00D2FF" stroke-width="2"/>
<ellipse cx="46" cy="40" rx="4" ry="10" fill="none" stroke="#00D2FF" stroke-width="1.2"/>
<line x1="36" y1="40" x2="56" y2="40" stroke="#00D2FF" stroke-width="1.2"/>
</svg>''',

    # 4. IBus Setup — keyboard with settings gear
    "ibus-setup": '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs>
  <linearGradient id="ibusSBg" x1="32" y1="6" x2="32" y2="58" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#25344A"/>
    <stop offset="100%" stop-color="#0e141d"/>
  </linearGradient>
</defs>
<rect x="6" y="6" width="52" height="52" rx="14" fill="url(#ibusSBg)" stroke="#25344A" stroke-width="1.5"/>
<rect x="8.5" y="8.5" width="47" height="4" rx="2" fill="#88C0D0" fill-opacity="0.25"/>
<rect x="10" y="20" width="30" height="18" rx="4" fill="#1A2434" stroke="#405878" stroke-width="1.5"/>
<g fill="#88C0D0">
  <rect x="14" y="24" width="3.5" height="3.5" rx="1"/><rect x="20" y="24" width="3.5" height="3.5" rx="1"/>
  <rect x="26" y="24" width="3.5" height="3.5" rx="1"/><rect x="32" y="24" width="3.5" height="3.5" rx="1"/>
  <rect x="14" y="30" width="3.5" height="3.5" rx="1"/><rect x="20" y="30" width="3.5" height="3.5" rx="1"/>
  <rect x="26" y="30" width="3.5" height="3.5" rx="1"/><rect x="32" y="30" width="3.5" height="3.5" rx="1"/>
</g>
<circle cx="44" cy="42" r="9" fill="#0e141d" stroke="#00D2FF" stroke-width="2"/>
<circle cx="44" cy="42" r="3.2" fill="#00D2FF"/>
<g stroke="#00D2FF" stroke-width="2" stroke-linecap="round">
  <line x1="44" y1="30" x2="44" y2="33"/><line x1="44" y1="51" x2="44" y2="54"/>
  <line x1="32" y1="42" x2="35" y2="42"/><line x1="53" y1="42" x2="56" y2="42"/>
</g>
</svg>''',

    # 5. Orca — eye with sound waves (screen reader)
    "orca": '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs>
  <linearGradient id="orcaBg" x1="32" y1="6" x2="32" y2="58" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#25344A"/>
    <stop offset="100%" stop-color="#0e141d"/>
  </linearGradient>
</defs>
<rect x="6" y="6" width="52" height="52" rx="14" fill="url(#orcaBg)" stroke="#25344A" stroke-width="1.5"/>
<rect x="8.5" y="8.5" width="47" height="4" rx="2" fill="#88C0D0" fill-opacity="0.25"/>
<path d="M 12 30 C 18 21 46 21 52 30 C 46 39 18 39 12 30 Z" fill="none" stroke="#88C0D0" stroke-width="2.5"/>
<circle cx="32" cy="30" r="6.5" fill="#00D2FF"/>
<circle cx="32" cy="30" r="2.6" fill="#0e141d"/>
<g stroke="#88C0D0" stroke-width="2" stroke-linecap="round" fill="none">
  <path d="M 46 41 C 49 44 49 49 46 52"/>
  <path d="M 50 38 C 55 43 55 50 50 55"/>
</g>
</svg>''',

    # 6. Pinentry — PIN pad lock
    "pinentry": '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs>
  <linearGradient id="pinBg" x1="32" y1="6" x2="32" y2="58" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#25344A"/>
    <stop offset="100%" stop-color="#0e141d"/>
  </linearGradient>
</defs>
<rect x="6" y="6" width="52" height="52" rx="14" fill="url(#pinBg)" stroke="#25344A" stroke-width="1.5"/>
<rect x="8.5" y="8.5" width="47" height="4" rx="2" fill="#88C0D0" fill-opacity="0.25"/>
<rect x="16" y="24" width="32" height="26" rx="5" fill="#1A2434" stroke="#405878" stroke-width="1.5"/>
<path d="M 24 24 L 24 19 C 24 14.6 27.6 11 32 11 C 36.4 11 40 14.6 40 19 L 40 24" fill="none" stroke="#00D2FF" stroke-width="3" stroke-linecap="round"/>
<g fill="#88C0D0">
  <circle cx="24" cy="32" r="2.6"/><circle cx="32" cy="32" r="2.6"/><circle cx="40" cy="32" r="2.6"/>
  <circle cx="24" cy="39" r="2.6"/><circle cx="32" cy="39" r="2.6"/><circle cx="40" cy="39" r="2.6"/>
  <rect x="24" y="44" width="16" height="3" rx="1.5"/>
</g>
</svg>''',

    # 7. QV4L2 — webcam test tool
    "qv4l2": '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs>
  <linearGradient id="qv4Bg" x1="32" y1="6" x2="32" y2="58" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#25344A"/>
    <stop offset="100%" stop-color="#0e141d"/>
  </linearGradient>
</defs>
<rect x="6" y="6" width="52" height="52" rx="14" fill="url(#qv4Bg)" stroke="#25344A" stroke-width="1.5"/>
<rect x="8.5" y="8.5" width="47" height="4" rx="2" fill="#88C0D0" fill-opacity="0.25"/>
<rect x="10" y="22" width="28" height="20" rx="4" fill="#1A2434" stroke="#405878" stroke-width="1.5"/>
<path d="M 38 28 L 52 21 L 52 43 L 38 36 Z" fill="#2E415A" stroke="#88C0D0" stroke-width="1.5" stroke-linejoin="round"/>
<circle cx="24" cy="32" r="6.5" fill="none" stroke="#00D2FF" stroke-width="2.5"/>
<circle cx="24" cy="32" r="2.4" fill="#00D2FF"/>
</svg>''',

    # 8. Qvidcap — capture camera with record dot
    "qvidcap": '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs>
  <linearGradient id="qvcBg" x1="32" y1="6" x2="32" y2="58" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#25344A"/>
    <stop offset="100%" stop-color="#0e141d"/>
  </linearGradient>
</defs>
<rect x="6" y="6" width="52" height="52" rx="14" fill="url(#qvcBg)" stroke="#25344A" stroke-width="1.5"/>
<rect x="8.5" y="8.5" width="47" height="4" rx="2" fill="#88C0D0" fill-opacity="0.25"/>
<rect x="10" y="22" width="28" height="20" rx="4" fill="#1A2434" stroke="#405878" stroke-width="1.5"/>
<path d="M 38 28 L 52 21 L 52 43 L 38 36 Z" fill="#2E415A" stroke="#88C0D0" stroke-width="1.5" stroke-linejoin="round"/>
<circle cx="24" cy="32" r="6" fill="#E5737F"/>
<circle cx="24" cy="32" r="2.2" fill="#ECEFF4"/>
</svg>''',

    # 9. Rygel — media server house with stream waves
    "rygel": '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs>
  <linearGradient id="rygBg" x1="32" y1="6" x2="32" y2="58" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#25344A"/>
    <stop offset="100%" stop-color="#0e141d"/>
  </linearGradient>
</defs>
<rect x="6" y="6" width="52" height="52" rx="14" fill="url(#rygBg)" stroke="#25344A" stroke-width="1.5"/>
<rect x="8.5" y="8.5" width="47" height="4" rx="2" fill="#88C0D0" fill-opacity="0.25"/>
<path d="M 32 16 L 46 28 L 43 28 L 43 44 L 21 44 L 21 28 L 18 28 Z" fill="#1A2434" stroke="#88C0D0" stroke-width="2" stroke-linejoin="round"/>
<g stroke="#00D2FF" stroke-width="2.4" stroke-linecap="round" fill="none">
  <path d="M 29 34 C 31.5 36.5 31.5 39.5 29 42"/>
  <path d="M 35 31 C 39 35 39 41 35 45"/>
</g>
</svg>''',

    # 10. Tecla — keyboard layout tester
    "org.gnome.Tecla": '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs>
  <linearGradient id="tclBg" x1="32" y1="6" x2="32" y2="58" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#25344A"/>
    <stop offset="100%" stop-color="#0e141d"/>
  </linearGradient>
</defs>
<rect x="6" y="6" width="52" height="52" rx="14" fill="url(#tclBg)" stroke="#25344A" stroke-width="1.5"/>
<rect x="8.5" y="8.5" width="47" height="4" rx="2" fill="#88C0D0" fill-opacity="0.25"/>
<rect x="11" y="20" width="42" height="25" rx="5" fill="#1A2434" stroke="#405878" stroke-width="1.5"/>
<g fill="#88C0D0">
  <rect x="15" y="24" width="4" height="4" rx="1"/><rect x="21" y="24" width="4" height="4" rx="1"/>
  <rect x="27" y="24" width="4" height="4" rx="1"/><rect x="33" y="24" width="4" height="4" rx="1"/>
  <rect x="39" y="24" width="4" height="4" rx="1"/><rect x="45" y="24" width="4" height="4" rx="1"/>
  <rect x="15" y="30" width="4" height="4" rx="1"/><rect x="21" y="30" width="4" height="4" rx="1"/>
  <rect x="39" y="30" width="4" height="4" rx="1"/><rect x="45" y="30" width="4" height="4" rx="1"/>
  <rect x="19" y="36" width="26" height="4" rx="2"/>
</g>
<rect x="27" y="30" width="4" height="4" rx="1" fill="#00D2FF"/>
<rect x="33" y="30" width="4" height="4" rx="1" fill="#00D2FF"/>
</svg>''',

    # 11. Captive Portal — wifi with login window
    "org.gnome.Shell.CaptivePortal": '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs>
  <linearGradient id="cptBg" x1="32" y1="6" x2="32" y2="58" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#25344A"/>
    <stop offset="100%" stop-color="#0e141d"/>
  </linearGradient>
</defs>
<rect x="6" y="6" width="52" height="52" rx="14" fill="url(#cptBg)" stroke="#25344A" stroke-width="1.5"/>
<rect x="8.5" y="8.5" width="47" height="4" rx="2" fill="#88C0D0" fill-opacity="0.25"/>
<g fill="none" stroke="#00D2FF" stroke-width="3" stroke-linecap="round">
  <path d="M 15 27 C 24 18 40 18 49 27"/>
  <path d="M 21 33 C 27 27 37 27 43 33"/>
</g>
<circle cx="32" cy="40" r="3.5" fill="#00D2FF"/>
<rect x="22" y="44" width="20" height="12" rx="2.5" fill="#1A2434" stroke="#88C0D0" stroke-width="1.5"/>
<line x1="22" y1="48" x2="42" y2="48" stroke="#88C0D0" stroke-width="1.2"/>
</svg>''',

    # 12. Mutter MDK — window with gear (window manager)
    "org.gnome.Mutter.Mdk": '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs>
  <linearGradient id="mdkBg" x1="32" y1="6" x2="32" y2="58" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#25344A"/>
    <stop offset="100%" stop-color="#0e141d"/>
  </linearGradient>
</defs>
<rect x="6" y="6" width="52" height="52" rx="14" fill="url(#mdkBg)" stroke="#25344A" stroke-width="1.5"/>
<rect x="8.5" y="8.5" width="47" height="4" rx="2" fill="#88C0D0" fill-opacity="0.25"/>
<rect x="11" y="17" width="42" height="30" rx="4" fill="#1A2434" stroke="#405878" stroke-width="1.5"/>
<rect x="11" y="17" width="42" height="7" rx="3.5" fill="#2E415A"/>
<circle cx="16" cy="20.5" r="1.6" fill="#E5737F"/>
<circle cx="21" cy="20.5" r="1.6" fill="#EBCB8B"/>
<circle cx="26" cy="20.5" r="1.6" fill="#A3BE8C"/>
<circle cx="44" cy="40" r="8" fill="#0e141d" stroke="#00D2FF" stroke-width="2"/>
<circle cx="44" cy="40" r="2.8" fill="#00D2FF"/>
</svg>''',

    # 13. Nautilus Previewer — image preview with magnifier
    "org.gnome.NautilusPreviewer": '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs>
  <linearGradient id="npvBg" x1="32" y1="6" x2="32" y2="58" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#25344A"/>
    <stop offset="100%" stop-color="#0e141d"/>
  </linearGradient>
</defs>
<rect x="6" y="6" width="52" height="52" rx="14" fill="url(#npvBg)" stroke="#25344A" stroke-width="1.5"/>
<rect x="8.5" y="8.5" width="47" height="4" rx="2" fill="#88C0D0" fill-opacity="0.25"/>
<rect x="12" y="18" width="32" height="24" rx="3" fill="#1A2434" stroke="#405878" stroke-width="1.5"/>
<circle cx="20" cy="25" r="2.6" fill="#EBCB8B"/>
<polygon points="14,40 23,29 30,35 35,31 42,40" fill="#88C0D0"/>
<circle cx="43" cy="41" r="7.5" fill="#0e141d" fill-opacity="0.9" stroke="#00D2FF" stroke-width="2.5"/>
<line x1="48.5" y1="46.5" x2="54" y2="52" stroke="#00D2FF" stroke-width="3" stroke-linecap="round"/>
</svg>''',

    # 14. Evolution Alarm — ringing alarm clock
    "org.gnome.Evolution-alarm-notify": '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs>
  <linearGradient id="evtBg" x1="32" y1="6" x2="32" y2="58" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#25344A"/>
    <stop offset="100%" stop-color="#0e141d"/>
  </linearGradient>
</defs>
<rect x="6" y="6" width="52" height="52" rx="14" fill="url(#evtBg)" stroke="#25344A" stroke-width="1.5"/>
<rect x="8.5" y="8.5" width="47" height="4" rx="2" fill="#88C0D0" fill-opacity="0.25"/>
<circle cx="32" cy="33" r="14" fill="#1A2434" stroke="#00D2FF" stroke-width="2.5"/>
<path d="M 32 25 L 32 33 L 38 37" stroke="#ECEFF4" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
<path d="M 20 14 L 26 20" stroke="#88C0D0" stroke-width="3" stroke-linecap="round"/>
<path d="M 44 14 L 38 20" stroke="#88C0D0" stroke-width="3" stroke-linecap="round"/>
<g stroke="#88C0D0" stroke-width="2" stroke-linecap="round">
  <line x1="14" y1="28" x2="10" y2="26"/><line x1="50" y1="28" x2="54" y2="26"/>
</g>
</svg>''',

    # 15. Malcontent Control — tablet with restriction shield
    "org.freedesktop.MalcontentControl": '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs>
  <linearGradient id="mlcBg" x1="32" y1="6" x2="32" y2="58" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#25344A"/>
    <stop offset="100%" stop-color="#0e141d"/>
  </linearGradient>
</defs>
<rect x="6" y="6" width="52" height="52" rx="14" fill="url(#mlcBg)" stroke="#25344A" stroke-width="1.5"/>
<rect x="8.5" y="8.5" width="47" height="4" rx="2" fill="#88C0D0" fill-opacity="0.25"/>
<rect x="15" y="12" width="24" height="38" rx="4" fill="#1A2434" stroke="#405878" stroke-width="1.5"/>
<rect x="19" y="17" width="16" height="26" rx="2" fill="#25344A"/>
<circle cx="27" cy="46" r="1.6" fill="#88C0D0"/>
<path d="M 45 24 L 52 26.6 L 52 34 C 52 39 49 42.4 45 43.8 C 41 42.4 38 39 38 34 L 38 26.6 Z" fill="#00D2FF" fill-opacity="0.2" stroke="#00D2FF" stroke-width="2" stroke-linejoin="round"/>
<path d="M 42 33 L 44.5 35.5 L 48.5 30.5" stroke="#00D2FF" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
</svg>''',

    # 16. Bluetooth — rune on tile
    "bluetooth": '''<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs>
  <linearGradient id="btBg" x1="32" y1="6" x2="32" y2="58" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#25344A"/>
    <stop offset="100%" stop-color="#0e141d"/>
  </linearGradient>
  <linearGradient id="btRune" x1="30" y1="12" x2="30" y2="52" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#88C0D0"/>
    <stop offset="100%" stop-color="#00D2FF"/>
  </linearGradient>
</defs>
<rect x="6" y="6" width="52" height="52" rx="14" fill="url(#btBg)" stroke="#25344A" stroke-width="1.5"/>
<rect x="8.5" y="8.5" width="47" height="4" rx="2" fill="#88C0D0" fill-opacity="0.25"/>
<path d="M 30 13 L 42 23 L 34 30 L 42 37 L 30 47 L 30 35 L 22 42 L 19 38.5 L 28 30 L 19 21.5 L 22 18 L 30 25 Z" fill="url(#btRune)"/>
</svg>''',
}

# Alias map: alternate desktop entry names pointing at the new icons.
EXTRA_APP_ALIASES = {
    "org.kde.kwalletmanager5": "kwalletmanager",
    "org.kde.kwalletmanager": "kwalletmanager",
    "kwalletmanager5": "kwalletmanager",
    "qemu-system": "qemu",
    "ibus-engine": "ibus",
    "org.freedesktop.IBus": "ibus",
    "orca-screen-reader": "orca",
    "org.gnome.Orca": "orca",
    "pinentry-gtk": "pinentry",
    "pinentry-qt": "pinentry",
    "qv4l2-capture": "qv4l2",
    "rygel-media-server": "rygel",
    "org.gnome.Shell.CaptivePortalNetwork": "org.gnome.Shell.CaptivePortal",
    "org.gnome.NautilusPreview": "org.gnome.NautilusPreviewer",
    "org.gnome.EvolutionAlarmNotify": "org.gnome.Evolution-alarm-notify",
    "malcontent-control": "org.freedesktop.MalcontentControl",
    "bluetooth-active": "bluetooth",
    "bluetooth-inactive": "bluetooth",
}

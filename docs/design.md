# Design System Guide — MT Nordic Blue

© Mayanktaker Computers & Web Development | https://mayanktaker.com

Single source of truth for colors: `palette/tokens.json` (do not hardcode hex values elsewhere).

## Principles
- **Polar Night & Arctic Glow:** balanced ultra-deep dark bases (#0E141D, #161F2E) refined for visual comfort, crisp contrast, and OLED depth.
- **Accented Focus:** Nordic Frost cyan (#88C0D0) and Glacier blue (#81A1C1) for primary actions, focus rings, and active selections.
- **Frosted Glassmorphism:** translucent surfaces with backdrop blur (28px blur), delicate glass specular highlights, and soft ambient drop shadows.
- **Familiar GNOME Shape:** upstream layout, geometry, and spacing are respected while elevating palette harmony.
- **Contrast is a gate:** `tools/dev/check_contrast.py` must pass (WCAG ≥4.5 body text, ≥7 preferred) before any milestone commit.
- **System fonts**, no intrusive custom typography in the theme itself.

## Tokens (MT Nordic Blue Baseline)
| Token | Starter Value | Use |
|---|---|---|
| `bg.base` | #0E141D | Main panels, dialogs, cards |
| `bg.base_darker` | #090D14 | Overview backdrop, OSD base |
| `bg.oled` | #040609 | True pitch-black OLED background (`--base oled`) |
| `bg.tile` | #151D2A | Quick-settings tiles, list rows |
| `bg.surface` / `hover` / `active` | #202D40 / #2A3A52 / #354A68 | Raised surfaces and interactive states |
| `accent.base` / `strong` / `dim` | #88C0D0 / #A3D4E2 / #5E81AC | Focus rings, selected items, sliders, links |
| `accent_flavors.frost` | #88C0D0 | Nordic Frost cyan accent |
| `accent_flavors.glacier` | #81A1C1 | Glacier ice blue accent |
| `accent_flavors.aurora` | #8FBCBB | Nordic aurora teal accent |
| `accent_flavors.arctic` | #5E81AC | Deep arctic blue accent |
| `accent_flavors.cyber` | #00D2FF | Luminescent electric cyan accent |
| `accent_flavors.blaze` | #D08770 | Nordic amber blaze accent |
| `window_controls` close/min/max | #BF616A / #EBCB8B / #A3BE8C | Window titlebar controls |
| `text.primary` / `secondary` / `disabled` | #ECEFF4 / #D8DEE9 / #7B88A1 | Foreground typography tiers |
| `status` destructive/success/warning | #BF616A / #A3BE8C / #EBCB8B | Semantic indicators and warnings |
| `border.default` / `subtle` | #25344A / #1A2535 | Separators, container edges |

All text/accent pairs verified ≥4.5:1 on their backgrounds (most ≥9:1 to 16:1).

## Form Controls & Interactive Components (GTK3 / GTK4 / Libadwaita)
- **Checkbuttons & Radios**:
  - Unchecked state: deep Nordic slate background (`#16202E`) encased in a distinct 1.5px border (`#435B7D`) to guarantee visibility on all card, dialog, and panel surfaces.
  - Checked state: bright Nordic Frost fill (`#88C0D0`) with a dark, high-contrast foreground glyph (`#090D14`, contrast ratio >9:1).
  - Hover / Focus state: luminous cyan glow (`box-shadow: 0 0 6px rgba(136, 192, 208, 0.35)`) and 2px focus rings (`outline-offset: 2px`).
  - Standardized symbolic icons: `object-select-symbolic`, `check-plain-symbolic`, `checkbox-checked-symbolic`, and `radio-checked-symbolic`.
- **Switches & Sliders**:
  - Switches: Nordic capsule design with distinct active frost fill (`#88C0D0`) and dark knob (`#090D14`) when toggled on; slate trough (`#16202E`) and light knob (`#ECEFF4`) when off.
  - Scales & Progress: rounded troughs with accent highlights and glowing circular sliders.
- **Dialogs & Popovers**:
  - Frosted dark slate surfaces (`#151D2A`) with subtle 1px border (`#25344A`) and deep 36px ambient shadows.
  - Multi-select card items (e.g. Shelly dependency selectors): structured cards with comfortable padding and margin separation to prevent scrollbar overlap.

## Icon Pack Architecture & Fallback
- **Index Inheritance Hierarchy**: `Inherits=Tela-circle,Adwaita,breeze-dark,breeze,hicolor`.
- **Standards Compliance**: Full FreeDesktop & KDE standards metadata (`DisplayDepth=32`, `LinkOverlay`, `LockOverlay`, `ZipOverlay`, size declarations, and `FollowsColorScheme=true`).
- **Complete Symbolic Suite**: Dedicated SVG glyphs for UI form controls, system actions, tray indicators, package managers (Shelly), and media downloaders (Tartube).
- **Coverage**: 409 hand-drawn app glyphs + 395 aliases (804 entries), 119 mimetypes from the badge engine, 26 GNOME Settings panel symbolics, 16 misc FreeDesktop symbolics. Popular-app batches live in `tools/icons/apps_popular_1..7.py` behind the shared tile builder `apps_popular_common.py`.
- **Graceful Fallback**: Native Nordic glyphs are prioritized; missing third-party applications seamlessly fall back to `Tela-circle` and `Adwaita` without missing icon placeholders.

## Modular Options & Tweaks System
- **Top bar / Panel styles**: `round-island` (16px curved floating bar), `pill` (999px capsule), `bottom-round` (16px bottom rounded corners), `flat` (edge-to-edge square bar).
- **Corner Curvature**: `round` (16px modern curves) vs `sharp` (0px sharp / non-rounded industrial aesthetic).
- **Window controls**: `standard` (native Adwaita icons) vs `macos` (Nordic traffic dots).
- **Theme sizing**: `standard` (comfortable density) vs `compact` (slim headerbars & padding).
- **Surface Display**: `--blur` (frosted glassmorphism translucency) vs `--no-blur` (solid opaque).
- **Base Palette**: `polar` (deep dark #0E141D), `classic` (Nord #2E3440), `cyber` (midnight neon #0A0E17), `oled` (pitch black #040609).
- **Accent Flavors**: `frost` (#88C0D0), `glacier` (#81A1C1), `aurora` (#8FBCBB), `arctic` (#5E81AC), `cyber` (#00D2FF), `blaze` (#D08770).

## Wallpaper Generation Rules
Procedural 4K (3840x2160) 3D Glacial Silk Bloom artworks generated via Cairo vectors and film grain in `tools/wallpaper/generate.py` (dark) and `tools/wallpaper/process_light.py` (light):
1. **Glacial Silk Bloom Prime (Art 1)**: Majestic centered 3D folded silk rosette sculpture with 3 tiers of flowing ribbons, volumetric ambient cyan aura, and specular rim illumination on Polar Night.
2. **Aurora Ribbon Drift (Art 2)**: Dynamic sweeping ribbons drifting in an S-curve across an auroral curtain veil with glowing ice filaments.
3. **Glacial Fold Sanctuary (Art 3)**: Macro intimate perspective on the heart of the folded bloom with deep ambient occlusion and crystalline translucent edge reflections.
4. **Ascending Frost Crest (Art 4)**: Architectural ascending helical ribbon swirls spiraling towards an arctic crest.
Matching Scandinavian daylight Snow Storm counterparts (`tools/wallpaper/process_light.py`), inverted high-contrast adaptive pairing, and 24-hour dynamic timed cycle XML (`tools/wallpaper/generate_dynamic.py`).

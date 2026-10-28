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

## Modular Options & Tweaks System
- **Top bar / Panel styles**: `round-island` (16px curved floating bar), `pill` (999px capsule), `bottom-round` (16px bottom rounded corners), `flat` (edge-to-edge square bar).
- **Corner Curvature**: `round` (16px modern curves) vs `sharp` (0px sharp / non-rounded industrial aesthetic).
- **Window controls**: `standard` (native Adwaita icons) vs `macos` (Nordic traffic dots).
- **Theme sizing**: `standard` (comfortable density) vs `compact` (slim headerbars & padding).
- **Surface Display**: `--blur` (frosted glassmorphism translucency) vs `--no-blur` (solid opaque).
- **Base Palette**: `polar` (deep dark #0E141D), `classic` (Nord #2E3440), `cyber` (midnight neon #0A0E17), `oled` (pitch black #040609).
- **Accent Flavors**: `frost` (#88C0D0), `glacier` (#81A1C1), `aurora` (#8FBCBB), `arctic` (#5E81AC), `cyber` (#00D2FF), `blaze` (#D08770).

## Wallpaper Generation Rules
Original procedural 4K artworks generated via `tools/wallpaper/generate.py`:
1. **Fjord Canopy (Art 1)**: Silhouetted mountain and glacial pine canopy with glowing Nordic cyan gradient.
2. **Radiant Aurora (Art 2)**: Vibrant Arctic aurora borealis ribbons over dark pine mountain ridge.
3. **Glacial Flow (Art 3)**: Minimalist fluid glacier contours in Nordic cyan and arctic blue.
4. **Topographic Frost (Art 4)**: Elevation isolines with glowing arctic mineral veins.
Plus matching adaptive Light/Day counterparts and 24-hour dynamic cycle XML.

# MT Nordic Blue — GNOME Dark Theme Suite

© Mayanktaker Computers & Web Development | https://mayanktaker.com

An atmospheric, modular Scandinavian-inspired desktop suite for GNOME: **Shell Theme + GTK 3/4 + Companion Icon Pack + Cursor Pack + Procedural 4K Wallpapers + App Ecosystem**.

Inspired by polar night, glacial ice, and Arctic light, **MT Nordic Blue** brings frosted glassmorphism, flexible layout geometry, high-contrast readability, and deep OLED comfort to Linux.

---

## ✨ Features & Customization Options

| Feature | Choices Available | Default | Description |
| :--- | :--- | :--- | :--- |
| **Blur & Glassmorphism** | `--blur` / `--no-blur` | **Frosted Glass** | 28px backdrop blur, translucent quick settings, panel, and dialogs. Full native & Blur my Shell compatibility. |
| **Corner Curvature** | `--corners round` / `sharp` | **Round (16px)** | Modern 16px smooth curved windows & dialogs OR 0px sharp non-rounded industrial/tiling corners. |
| **Theme Sizing Density** | `--size standard` / `compact` | **Standard** | Comfortable upstream GNOME proportions OR slim compact headerbars & tighter list rows. |
| **Top Bar / Tray Style** | `--panel round-island` / `pill` / `bottom-round` / `flat` | **Round Island** | Floating curved island (16px), 999px capsule pill, bottom-curved bar, or edge-to-edge flat bar. |
| **Window Title Controls** | `--controls standard` / `macos` | **Standard** | Clean Adwaita buttons OR Nordic traffic dots (Aurora Red `#BF616A`, Gold `#EBCB8B`, Green `#A3BE8C`). |
| **Base Palette Flavor** | `--base polar` / `classic` / `cyber` / `oled` | **Deep Polar** | Deep Polar Night (`#0E141D`), Classic Nord Slate (`#2E3440`), Arctic Cyber (`#0A0E17`), or OLED (`#040609`). |
| **Accent Color Flavor** | `--accent frost` / `glacier` / `aurora` / `arctic` / `cyber` / `blaze` | **Frost Cyan** | `#88C0D0` (Frost), `#81A1C1` (Glacier), `#8FBCBB` (Aurora), `#5E81AC` (Arctic), `#00D2FF` (Cyber), `#D08770` (Blaze). Recolors GNOME Shell (panel, popups, overview) and GTK together. |
| **Companion Icon Pack** | `--icons` / `--no-icons` | **Enabled** | Custom vector icons (`MT-Nordic-Blue-Icons`) with gradient folder plates, folder emblems, and 50+ app icons. |
| **Companion Cursor Pack** | Installed with icons | **Enabled** | Aerodynamic cursors (`MT-Nordic-Blue-Cursors`) with icy Nordic tips and smooth animated spinners. |
| **4K Wallpapers** | `--wallpaper 1` / `2` / `3` / `4` / `all` / `none` | **Fjord Canopy** | Procedural 3840x2160 wallpapers with matching light variants and 24-hour dynamic XML. |

---

## 🚀 Quick Start & Installation

### 1. Interactive Setup Wizard (Recommended)
Run without arguments in your terminal to launch the interactive step-by-step configuration wizard:
```bash
./install.sh
```
The wizard guides you through top bar style, corner curvature, titlebar buttons, sizing density, glassmorphism blur, palette flavor, icon/cursor suite, and 4K wallpapers.

### 2. Fast Command-Line Installation
Install with custom flags directly:
```bash
# Modern Glass Suite (Default)
./install.sh --panel round-island --corners round --blur --icons --wallpaper 1

# Sharp Industrial & Compact Suite (Tiling / Dev aesthetic)
./install.sh --panel flat --corners sharp --size compact --no-blur --icons

# Classic Nord Spec (#2E3440 slate base)
./install.sh --base classic --accent glacier --panel pill --controls macos

# Arctic Cyber Frost (Midnight navy with electric neon cyan)
./install.sh --base cyber --accent cyber --panel round-island --blur
```

---

## 🎨 Companion Icon & Cursor Packs

### MT-Nordic-Blue-Icons
- High-definition SVG folder templates with multi-stop radial and linear gradients, specular light highlights, and debossed place emblems.
- Custom categories: Places (Home, Desktop, Downloads, Documents, Music, Pictures, Videos, Trash), Devices (Internal HDD/SSD, USB, External Drives, Partitions), Actions, and MIME types.
- **50+ Custom Linux App Icons**: VS Code, Cursor, Antigravity, Terminal, Firefox, Chrome, Discord, Slack, Spotify, LibreOffice, GIMP, Inkscape, Blender, Steam, OBS Studio, and more!

### MT-Nordic-Blue-Cursors
- Aerodynamic precision pointers with Nordic Frost cyan borders and subtle drop shadows.
- Fluid animated `wait` and `progress` spinners with smooth circular rotations.
- 12 primary cursor categories with standard X11 and Wayland symlinks.

---

## 🖼️ 4K Procedural Wallpapers Suite

Generated in 4K resolution (3840x2160) from theme tokens with mathematical film grain to prevent banding:
1. **Fjord Canopy (Art 1)**: Mountain pine silhouettes against a radiant Nordic cyan moonlight gradient.
2. **Radiant Aurora (Art 2)**: Vibrant Arctic aurora borealis ribbons over snow-dusted alpine ridges.
3. **Glacial Flow (Art 3)**: Fluid Bauhaus-inspired minimal contours in icy Nordic tones.
4. **Topographic Frost (Art 4)**: Elevation isoline contours with glowing arctic mineral veins.
- **Adaptive Day/Night**: Includes matching light/dawn editions and a 24-hour GNOME dynamic background XML cycle (`mt-nordic-blue-timed.xml`).

---

## 💻 Full Application Ecosystem

In addition to GNOME Shell and GTK 3/4, MT Nordic Blue provides matching themes for:
- **Terminals**: Ghostty, Kitty, Alacritty, Foot, GNOME Terminal.
- **Text Editors / IDEs**: GNOME Text Editor (GtkSourceView-5), Gedit, Builder, VS Code / Cursor.
- **Shells**: Fish Shell.
- **System & Boot**: Fastfetch, GRUB2, Plymouth boot splash, SDDM, GDM, and KDE Plasma / Kvantum.

Install all application themes in one command:
```bash
tools/extras/install-all.sh
```

---

## 🛠️ Build Pipeline & Developer Tools

Rebuild the entire suite from source:
```bash
python3 build_all.py
```

Individual build commands:
- **WCAG Contrast Gate**: `python3 tools/dev/check_contrast.py`
- **GTK Theme**: `python3 tools/gtk/build.py`
- **GNOME Shell**: `python3 tools/shell/build.py --all`
- **Icons**: `python3 tools/icons/generate_icons.py`
- **Cursors**: `python3 tools/icons/generate_cursors.py`
- **Wallpapers**: `python3 tools/wallpaper/generate.py --which all` && `python3 tools/wallpaper/process_light.py`
- **Package Release**: `tools/release.sh 0.1.0`

---

## 📜 License & Credits

- **Code & Stylesheets**: GNU General Public License v3.0 ([GPL-3.0.txt](file:///mnt/Development/Linux_Projects/Gnome-Themes/MT-NORDIC-BLUE/LICENSES/GPL-3.0.txt))
- **Artwork, Icons, Wallpapers**: Creative Commons Attribution-ShareAlike 4.0 ([CC-BY-SA-4.0.txt](file:///mnt/Development/Linux_Projects/Gnome-Themes/MT-NORDIC-BLUE/LICENSES/CC-BY-SA-4.0.txt))
- © Mayanktaker Computers & Web Development | [https://mayanktaker.com](https://mayanktaker.com)

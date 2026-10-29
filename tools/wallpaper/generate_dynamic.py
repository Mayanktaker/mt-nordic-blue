# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Generates GNOME timed day/night transition XML and GNOME background properties.

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DIST_DIR = REPO_ROOT / "wallpaper" / "dist"
DIST_LIGHT_DIR = DIST_DIR / "light"

TOKENS = json.loads((REPO_ROOT / "palette" / "tokens.json").read_text())
TECH_SLUG = TOKENS.get("meta", {}).get("tech_name", "mt-nordic-blue").lower()
DISPLAY_NAME = TOKENS.get("meta", {}).get("name", "MT Nordic Blue")


def build_timed_xml(wallpaper_base_dir: str) -> str:
    # 24-hour timed transition XML between morning mist dawn and midnight dark.
    dawn_path = f"{wallpaper_base_dir}/light/{TECH_SLUG}-canopy-dawn-3840x2160.png"
    night_path = f"{wallpaper_base_dir}/{TECH_SLUG}-art-1-3840x2160.png"

    return f"""<?xml version="1.0"?>
<!DOCTYPE background SYSTEM "file:///usr/share/gnome-background-properties/gnome-wp-list.dtd">
<!-- © Mayanktaker Computers & Web Development | https://mayanktaker.com -->
<!-- {DISPLAY_NAME} 24-Hour Day/Night Cycle -->
<background>
  <starttime>
    <year>2026</year>
    <month>01</month>
    <day>01</day>
    <hour>07</hour>
    <minute>00</minute>
    <second>00</second>
  </starttime>
  <!-- Daytime (7:00 AM - 6:00 PM, 11 hours) -->
  <static>
    <duration>39600.0</duration>
    <file>{dawn_path}</file>
  </static>
  <!-- Dusk transition (6:00 PM - 7:00 PM, 1 hour) -->
  <transition type="overlay">
    <duration>3600.0</duration>
    <from>{dawn_path}</from>
    <to>{night_path}</to>
  </transition>
  <!-- Nighttime (7:00 PM - 6:00 AM, 11 hours) -->
  <static>
    <duration>39600.0</duration>
    <file>{night_path}</file>
  </static>
  <!-- Dawn transition (6:00 AM - 7:00 AM, 1 hour) -->
  <transition type="overlay">
    <duration>3600.0</duration>
    <from>{night_path}</from>
    <to>{dawn_path}</to>
  </transition>
</background>
"""


def build_gnome_properties_xml(wallpaper_base_dir: str) -> str:
    # GNOME Settings background properties listing adaptive pairs and timed cycle.
    w_dir = wallpaper_base_dir
    return f"""<?xml version="1.0"?>
<!DOCTYPE wallpapers SYSTEM "gnome-wp-list.dtd">
<!-- © Mayanktaker Computers & Web Development | https://mayanktaker.com -->
<wallpapers>
  <!-- Inverted High-Contrast Adaptive Pairs (Dark Wallpaper on Light Theme / Light Wallpaper on Dark Theme) -->
  <wallpaper deleted="false">
    <name>{DISPLAY_NAME} Glacial Silk Bloom Prime (Inverted High-Contrast)</name>
    <filename>{w_dir}/{TECH_SLUG}-art-1-3840x2160.png</filename>
    <filename-dark>{w_dir}/light/{TECH_SLUG}-canopy-dawn-3840x2160.png</filename-dark>
    <options>zoom</options>
    <shade_type>solid</shade_type>
    <pcolor>#0E141D</pcolor>
    <scolor>#0E141D</scolor>
  </wallpaper>
  <wallpaper deleted="false">
    <name>{DISPLAY_NAME} Aurora Ribbon Drift (Inverted High-Contrast)</name>
    <filename>{w_dir}/{TECH_SLUG}-art-2-3840x2160.png</filename>
    <filename-dark>{w_dir}/light/{TECH_SLUG}-celestial-rift-3840x2160.png</filename-dark>
    <options>zoom</options>
    <shade_type>solid</shade_type>
    <pcolor>#0E141D</pcolor>
    <scolor>#0E141D</scolor>
  </wallpaper>
  <wallpaper deleted="false">
    <name>{DISPLAY_NAME} Glacial Fold Sanctuary (Inverted High-Contrast)</name>
    <filename>{w_dir}/{TECH_SLUG}-art-3-3840x2160.png</filename>
    <filename-dark>{w_dir}/light/{TECH_SLUG}-cosmic-dawn-3840x2160.png</filename-dark>
    <options>zoom</options>
    <shade_type>solid</shade_type>
    <pcolor>#0E141D</pcolor>
    <scolor>#0E141D</scolor>
  </wallpaper>
  <wallpaper deleted="false">
    <name>{DISPLAY_NAME} Ascending Frost Crest (Inverted High-Contrast)</name>
    <filename>{w_dir}/{TECH_SLUG}-art-4-3840x2160.png</filename>
    <filename-dark>{w_dir}/light/{TECH_SLUG}-botanical-horizon-3840x2160.png</filename-dark>
    <options>zoom</options>
    <shade_type>solid</shade_type>
    <pcolor>#0E141D</pcolor>
    <scolor>#0E141D</scolor>
  </wallpaper>

  <!-- Adaptive Natural Light/Dark Pairs (GNOME 42+ automatic switch) -->
  <wallpaper deleted="false">
    <name>{DISPLAY_NAME} Glacial Silk Bloom Prime (Adaptive Day/Night)</name>
    <filename>{w_dir}/light/{TECH_SLUG}-canopy-dawn-3840x2160.png</filename>
    <filename-dark>{w_dir}/{TECH_SLUG}-art-1-3840x2160.png</filename-dark>
    <options>zoom</options>
    <shade_type>solid</shade_type>
    <pcolor>#0E141D</pcolor>
    <scolor>#0E141D</scolor>
  </wallpaper>
  <wallpaper deleted="false">
    <name>{DISPLAY_NAME} Aurora Ribbon Drift (Adaptive Light/Dark)</name>
    <filename>{w_dir}/light/{TECH_SLUG}-celestial-rift-3840x2160.png</filename>
    <filename-dark>{w_dir}/{TECH_SLUG}-art-2-3840x2160.png</filename-dark>
    <options>zoom</options>
    <shade_type>solid</shade_type>
    <pcolor>#0E141D</pcolor>
    <scolor>#0E141D</scolor>
  </wallpaper>
  <wallpaper deleted="false">
    <name>{DISPLAY_NAME} Glacial Fold Sanctuary (Adaptive Light/Dark)</name>
    <filename>{w_dir}/light/{TECH_SLUG}-cosmic-dawn-3840x2160.png</filename>
    <filename-dark>{w_dir}/{TECH_SLUG}-art-3-3840x2160.png</filename-dark>
    <options>zoom</options>
    <shade_type>solid</shade_type>
    <pcolor>#0E141D</pcolor>
    <scolor>#0E141D</scolor>
  </wallpaper>
  <wallpaper deleted="false">
    <name>{DISPLAY_NAME} Ascending Frost Crest (Adaptive Light/Dark)</name>
    <filename>{w_dir}/light/{TECH_SLUG}-botanical-horizon-3840x2160.png</filename>
    <filename-dark>{w_dir}/{TECH_SLUG}-art-4-3840x2160.png</filename-dark>
    <options>zoom</options>
    <shade_type>solid</shade_type>
    <pcolor>#0E141D</pcolor>
    <scolor>#0E141D</scolor>
  </wallpaper>

  <!-- 24-Hour Continuous Dynamic Cycle -->
  <wallpaper deleted="false">
    <name>{DISPLAY_NAME} 24-Hour Adaptive Cycle</name>
    <filename>{w_dir}/{TECH_SLUG}-timed.xml</filename>
    <options>zoom</options>
    <shade_type>solid</shade_type>
    <pcolor>#0E141D</pcolor>
    <scolor>#0E141D</scolor>
  </wallpaper>

  <!-- Standalone 4K Dark Artworks -->
  <wallpaper deleted="false">
    <name>{DISPLAY_NAME} Glacial Silk Bloom Prime (Dark 4K)</name>
    <filename>{w_dir}/{TECH_SLUG}-art-1-3840x2160.png</filename>
    <options>zoom</options>
    <pcolor>#0E141D</pcolor>
    <scolor>#0E141D</scolor>
  </wallpaper>
  <wallpaper deleted="false">
    <name>{DISPLAY_NAME} Aurora Ribbon Drift (Dark 4K)</name>
    <filename>{w_dir}/{TECH_SLUG}-art-2-3840x2160.png</filename>
    <options>zoom</options>
    <pcolor>#0E141D</pcolor>
    <scolor>#0E141D</scolor>
  </wallpaper>
  <wallpaper deleted="false">
    <name>{DISPLAY_NAME} Glacial Fold Sanctuary (Dark 4K)</name>
    <filename>{w_dir}/{TECH_SLUG}-art-3-3840x2160.png</filename>
    <options>zoom</options>
    <pcolor>#0E141D</pcolor>
    <scolor>#0E141D</scolor>
  </wallpaper>
  <wallpaper deleted="false">
    <name>{DISPLAY_NAME} Ascending Frost Crest (Dark 4K)</name>
    <filename>{w_dir}/{TECH_SLUG}-art-4-3840x2160.png</filename>
    <options>zoom</options>
    <pcolor>#0E141D</pcolor>
    <scolor>#0E141D</scolor>
  </wallpaper>

  <!-- Standalone 4K Light Artworks -->
  <wallpaper deleted="false">
    <name>{DISPLAY_NAME} Glacial Snow Storm Bloom (Light 4K)</name>
    <filename>{w_dir}/light/{TECH_SLUG}-canopy-dawn-3840x2160.png</filename>
    <options>zoom</options>
    <pcolor>#E5E9F0</pcolor>
    <scolor>#E5E9F0</scolor>
  </wallpaper>
  <wallpaper deleted="false">
    <name>{DISPLAY_NAME} Daylight Aurora Ribbon Drift (Light 4K)</name>
    <filename>{w_dir}/light/{TECH_SLUG}-celestial-rift-3840x2160.png</filename>
    <options>zoom</options>
    <pcolor>#E5E9F0</pcolor>
    <scolor>#E5E9F0</scolor>
  </wallpaper>
  <wallpaper deleted="false">
    <name>{DISPLAY_NAME} Glacial Petal Core (Light 4K)</name>
    <filename>{w_dir}/light/{TECH_SLUG}-cosmic-dawn-3840x2160.png</filename>
    <options>zoom</options>
    <pcolor>#E5E9F0</pcolor>
    <scolor>#E5E9F0</scolor>
  </wallpaper>
  <wallpaper deleted="false">
    <name>{DISPLAY_NAME} Ascending Snow Storm Crest (Light 4K)</name>
    <filename>{w_dir}/light/{TECH_SLUG}-botanical-horizon-3840x2160.png</filename>
    <options>zoom</options>
    <pcolor>#E5E9F0</pcolor>
    <scolor>#E5E9F0</scolor>
  </wallpaper>
    <options>zoom</options>
    <pcolor>#E5E9F0</pcolor>
    <scolor>#E5E9F0</scolor>
  </wallpaper>
  <wallpaper deleted="false">
    <name>{DISPLAY_NAME} Botanical Horizon (Light 4K)</name>
    <filename>{w_dir}/light/{TECH_SLUG}-botanical-horizon-3840x2160.png</filename>
    <options>zoom</options>
    <pcolor>#E5E9F0</pcolor>
    <scolor>#E5E9F0</scolor>
  </wallpaper>
</wallpapers>
"""


def main():
    # Instantiates XML templates for installation and local distribution.
    DIST_DIR.mkdir(parents=True, exist_ok=True)

    template_dir = "@WALLPAPER_DIR@"
    timed_xml = build_timed_xml(template_dir)
    gnome_props = build_gnome_properties_xml(template_dir)

    (DIST_DIR / f"{TECH_SLUG}-timed.xml.in").write_text(timed_xml)
    (DIST_DIR / "gnome-background-properties.xml.in").write_text(gnome_props)

    local_base = str(DIST_DIR)
    (DIST_DIR / f"{TECH_SLUG}-timed.xml").write_text(build_timed_xml(local_base))
    (DIST_DIR / "gnome-background-properties.xml").write_text(build_gnome_properties_xml(local_base))

    print(f"Dynamic wallpaper XML templates generated in: {DIST_DIR}")


if __name__ == "__main__":
    main()

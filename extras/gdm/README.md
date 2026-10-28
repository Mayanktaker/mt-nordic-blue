# MT Nordic Blue — GDM Login Screen Setup

© Mayanktaker Computers & Web Development | https://mayanktaker.com

GNOME Display Manager (GDM) runs as a dedicated system user (`gdm`) and does not inherit user session themes by default.

To match your GDM login screen with MT Nordic Blue:

1. **Install GDM Settings (recommended GUI tool):**
   - Install via Flatpak: `flatpak install flathub io.github.realmazharhussain.GdmSettings`
   - Launch **Login Manager Settings** from the app grid.

2. **Configure Appearance:**
   - Set Shell Theme to `MT-Nordic-Blue`.
   - Set Icon Theme to `MT-Nordic-Blue-Icons`.
   - Set Cursor Theme to `MT-Nordic-Blue-Cursors`.
   - Set Background to `~/.themes/MT-Nordic-Blue/wallpapers/mt-nordic-blue-art-1-3840x2160.png`.
   - Click **Apply** in top-right corner.

3. **CLI Alternative (via gsettings for gdm user):**
   ```bash
   sudo machinectl shell gdm@ /bin/bash -c "gsettings set org.gnome.desktop.interface icon-theme 'MT-Nordic-Blue-Icons'"
   sudo machinectl shell gdm@ /bin/bash -c "gsettings set org.gnome.desktop.interface cursor-theme 'MT-Nordic-Blue-Cursors'"
   ```

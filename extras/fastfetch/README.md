# MT Nordic Blue — Fastfetch Showcase

© Mayanktaker Computers & Web Development | https://mayanktaker.com

Custom Fastfetch configuration with custom Nordic Blue ASCII logo and theme palette.

## Usage
Run directly:
```sh
fastfetch -c extras/fastfetch/config.jsonc
```

Or install as your default Fastfetch setup:
```sh
mkdir -p ~/.config/fastfetch
cp extras/fastfetch/config.jsonc ~/.config/fastfetch/config.jsonc
cp extras/fastfetch/mt-nordic-blue.txt ~/.config/fastfetch/mt-nordic-blue.txt
sed -i 's|"extras/fastfetch/mt-nordic-blue.txt"|"~/.config/fastfetch/mt-nordic-blue.txt"|' ~/.config/fastfetch/config.jsonc
```

# MT Nordic Blue — Firefox Theme (userChrome.css)

© Mayanktaker Computers & Web Development | https://mayanktaker.com

Companion dark theme for Mozilla Firefox matching the MT Nordic Blue palette.

## Installation
1. Open Firefox and navigate to `about:config`.
2. Search for `toolkit.legacyUserProfileCustomizations.stylesheets` and toggle it to `true`.
3. Open `about:support` and click **Open Directory** next to *Profile Directory*.
4. Create a folder named `chrome` if it doesn't exist:
   ```sh
   mkdir -p ~/.mozilla/firefox/*.default-release/chrome
   ```
5. Copy `userChrome.css` into that directory:
   ```sh
   cp extras/firefox/userChrome.css ~/.mozilla/firefox/*.default-release/chrome/
   ```
6. Restart Firefox.

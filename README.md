# iSHUpdater
Updates the MOTD and Alpine in iSH for you. Currently this isn't very flexible, but I intend to make it more so.

## Requirements 
- APK (to install Python/Git, which you'll need to run this); see below
- Git (to download the files)
- Python 3.4+ (`apk add python3` will do the trick)

The required Python packages are built in.

### Note for App Store users
If you've downloaded iSH from the App Store, by default APK isn't included. To install it, follow the steps [here](https://github.com/ish-app/ish/wiki/Installing-apk-on-the-App-Store-Version). (Unconfimed: this doesn't apply to Testflight/AltStore users.)

## Usage
After cloning and `cd`ing to the relevant directory:
`python3 updater.py [--help | -all | -noapk | -nomotd]`

### Flags
- `all` updates everything (ie both Alpine and the MOTD).
- `noapk` ignores Apline and only updates the MOTD.
- `nomotd` ignores the MOTD and only updates Alpine

### Notes
- If (like me) you use the edge repository for Apline and simply want to update everything, type "edge" into the prompts.

## Bugs/feature requests
You can [**open an issue**](https://github.com/rexogamer/ishupdater/issues/new) or contact me via [**one of these methods**](https://github.com/Rexogamer/rexogamer/blob/master/README.md#contacting-me).

# Asset Inventory and Management

## Overview

The game loads local image, audio, and font files from the repository root. These files are runtime dependencies. Renaming, moving, or deleting one without updating its path in `alien_invasion.py` can prevent launch or remove a visual/audio element.

## Asset Inventory

| File | Format | Runtime role |
|---|---|---|
| `background.jpg` | JPEG | Full-window background |
| `icon.png` | PNG | Window icon |
| `spaceship.png` | PNG | Player sprite |
| `ufo.png` | PNG | Enemy sprite reused for each UFO |
| `bullet.png` | PNG | Projectile sprite |
| `background.wav` | WAV | Repeating background music |
| `bullet.wav` | WAV | Fired projectile effect |
| `explosion.wav` | WAV | Successful hit effect |
| `Roboto-Medium.ttf` | TTF | Score and QUIT text |
| `Roboto-Bold.ttf` | TTF | GAMEOVER heading |

## Loading Behavior

The script uses relative file names such as `background.jpg`, `ufo.png`, and `Roboto-Medium.ttf`. The paths resolve from the process working directory. Run from the repository root with `python alien_invasion.py` to preserve the expected layout.

## Replacing Images

Keep filenames stable where possible. Preserve transparency for sprites, confirm image dimensions and visual scale, and verify the ship/enemy remain within the expected movement bounds. If a name or directory changes, update every source reference and this inventory.

## Replacing Audio

Use audio files supported by the Pygame mixer on target platforms. Confirm background music can loop and short effects play without blocking the game. The current source does not expose mute/volume settings or a complete missing-audio fallback.

## Fonts

The medium font is used for the score and button; the bold font is used for game-over text. Verify the text fits the expected screen area after any replacement.

## Size and Performance

The background WAV asset is comparatively large. Re-encoding may reduce repository size, but do not change its format or quality without testing playback in Pygame across intended operating systems.

## Provenance and Redistribution

Before redistributing the game, verify the rights to each image, audio clip, and font. A file being present in a repository does not establish its license or ownership. Add notices only where provenance is verified. The project MIT license does not automatically relicense third-party assets whose terms differ.
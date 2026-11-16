# Packaging Guide

## Current Status

The repository contains Python source and local runtime assets. It does not currently contain a PyInstaller specification, standalone executable, installer, or automated packaging workflow. The following is a plan for future distribution, not a claim that a ready-to-download application exists.

## Why Packaging Needs Care

The game depends on multiple local images, WAV files, and TTF fonts. A packaged executable that omits these resources or places them where the program cannot locate them will fail at runtime. The current source resolves assets relative to the process working directory, which is fragile for a bundled application.

## Candidate Tool

PyInstaller is one possible Python application bundler. Select and pin a tool only after testing it with the project's Python and Pygame versions. Build separately for each target operating system unless a documented workflow proves cross-compilation works.

## Required Resources

Include `background.jpg`, `icon.png`, `spaceship.png`, `ufo.png`, `bullet.png`, `background.wav`, `bullet.wav`, `explosion.wav`, `Roboto-Medium.ttf`, and `Roboto-Bold.ttf`.

## Recommended Packaging Sequence

1. Decide target OS and architectures.
2. Pin/test Python, Pygame, and bundler versions.
3. Refactor asset resolution to a deterministic bundle-relative directory.
4. Add a packaging configuration/specification.
5. Include every required image, sound, and font.
6. Build from a clean checkout.
7. Launch from a directory unrelated to the source checkout.
8. Verify display, controls, audio, collisions, game over, and exit.
9. Scan the artifact for unexpected files.
10. Publish checksums and release notes.

## Validation Matrix

| Check | Expected |
|---|---|
| Fresh machine | Launches without development Python environment |
| Resource bundle | All runtime files load |
| Working directory | Launch works outside the source root |
| Input | Keyboard and mouse controls respond |
| Display | Window opens at expected dimensions |
| Audio | Music and effects play |
| Exit | Window-close and QUIT button work |
| Distribution | Artifact extracts/launches as documented |

## Platform and Licensing Notes

Build and test Windows, macOS, and Linux artifacts on their respective supported platforms. Verify rights for all bundled assets before redistribution. Packaging does not change third-party asset license obligations.
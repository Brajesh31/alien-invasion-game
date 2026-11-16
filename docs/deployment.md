# 🚀 Deployment and Distribution Model

## Application Type

Alien Invasion Game is a local desktop application. It is not a website, API, hosted service, or multiplayer server. Runtime is a Python process that opens a Pygame display window and loads local assets.

## Source-Based Distribution

A source distribution should contain the Python script, every required runtime asset, installation instructions, and license. Users need a supported Python installation, Pygame, a graphical desktop session, and audio output for the full experience.

Run from the repository root because the current program resolves asset filenames against the process working directory.

## Runtime Assumptions

A desktop session is required to create the window, receive keyboard/mouse input, draw the game, and initialize the mixer. A headless server should not be advertised as a supported play environment unless a virtual display and audio strategy are specifically tested.

## Asset Inclusion

A release must include the background, window icon, player, UFO, and bullet images; background and effects WAV files; and both TTF fonts. Renaming or moving these files requires coordinated source changes.

## Platform Validation

Test each operating system claimed as supported. Verify window creation, keyboard/mouse input, images, fonts, background music, sound effects, collisions, game-over behavior, and clean exit. Python and Pygame being installable on a platform does not prove the complete game works there.

## Standalone Builds

The repository does not currently include an executable, installer, or packaging specification. See [Packaging](packaging.md) before creating a standalone release.

## Release Safety

Distribute assets only when their provenance and redistribution terms are understood. Keep a known-good source archive or executable so a broken release can be rolled back.

# Release and Maintenance Process

## Release Scope

A release consists of the Python source and the runtime assets required to start the desktop game. The repository does not currently publish an installer, standalone executable, or automated test artifact.

## 1. Prepare a Change

- Confirm the change has a clear gameplay, quality, or documentation goal.
- Identify affected variables, helper functions, and main-loop stages.
- Confirm all required local image, font, and audio files are present.
- Check asset rights and distribution terms when assets are added or replaced.
- Avoid unrelated asset re-encoding or generated files.

## 2. Validate the Game

Create and activate a virtual environment, install Pygame, and launch from the repository root:

```bash
python -m pip install pygame
python alien_invasion.py
```

Follow the manual checklist in [Testing](testing.md). Verify affected interactions. A documentation-only change does not need gameplay code changes, but links and commands should still be checked.

## 3. Review the Repository Diff

Check for accidental local environment/editor files, modified or missing runtime assets, broken filenames/case mismatches, unintended game-loop changes, whitespace/indentation issues, asset licensing changes, and unsupported release claims.

## 4. Release Notes

Record meaningful changes in the Unreleased section of the root changelog. When publishing a release, use a date and describe the behavior or maintenance outcome. Do not call a roadmap item completed until it exists and has been tested.

## 5. Source Distribution

A source release should include the script, all runtime assets, installation instructions, and repository license. Users need Python, Pygame, and a compatible display/audio environment.

## 6. Packaged Distribution

A standalone executable is a separate release artifact. Build on the target operating system, bundle every asset, test from an unrelated working directory, and verify that the output runs on a clean machine. See [Packaging](packaging.md).

## 7. Post-Release Verification

Confirm release files are downloadable, all assets are included, the documented startup command works, keyboard and mouse input function, audio plays, scoring/collision/game-over/exit behave correctly, and release notes match the artifact.

## 8. Rollback

Keep the previous known-good source archive or executable. If a new release fails, withdraw the problematic artifact and point users to the previous verified version while the issue is corrected.

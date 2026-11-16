# 🧑‍💻 Development Workflow

## Project Characteristics

The game is a single-script Pygame program. Initialization, assets, global state, helper functions, game loop, and shutdown live in `alien_invasion.py`. The script enters its loop at module execution time. Importing it therefore starts the game and is not suitable for ordinary isolated unit tests.

## Environment

```bash
python -m venv .venv
# Activate the environment for your shell
python -m pip install pygame
python alien_invasion.py
```

See [Installation](installation.md) for platform-specific activation commands.

## Safe Change Process

1. Read the related code and identify all global state it reads/writes.
2. Check the order of event handling, movement, collision, and rendering.
3. Preserve asset names or update every reference.
4. Run from the repository root.
5. Verify affected gameplay and at least one edge case.
6. Confirm the window still closes cleanly.
7. Update README and related docs.

## Gameplay Change Notes

Movement changes must be checked against ship bounds and UFO direction changes. Projectile changes must preserve ready/fire transitions and top-edge reset. Collision changes should be visually checked because they use distance thresholds rather than sprite masks. Score changes must not count the same hit twice. Game-over changes must preserve quit and window-close paths.

## Code Quality

- Keep indentation consistent. The current loop has mixed tab/space indentation in places.
- Avoid unnecessary mutable globals.
- Keep asset paths portable.
- Avoid expensive resource loading every frame.
- Avoid blocking operations inside the event loop.
- Preserve clean shutdown.
- Do not add dependencies for behavior already provided by Python/Pygame.

## Testability Limitation

The script initializes Pygame and enters the loop at import time. Future testability work should add a main guard and separate pure collision/state helpers from display/audio startup. No automated test suite is currently configured.

## Contribution Validation

Launch the game and follow [Testing](testing.md). Include Python/Pygame versions and the gameplay states tested.

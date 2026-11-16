# ✅ Testing and Quality Assurance

## Current Automated Coverage

The repository currently has no test directory or declared test runner. The README timestamp workflow is not a gameplay test. The script initializes Pygame and enters the main loop at module execution time, so importing it in an ordinary unit test would start the game. A headless CI agent generally cannot exercise the interactive display/audio experience without additional setup.

## Manual Test Environment

Use a desktop operating system, supported Python, Pygame installed in the active environment, all local runtime assets, a display, and audio where available. Record Python and Pygame versions with bug reports.

## Startup Test

1. Activate the virtual environment.
2. Run `python alien_invasion.py` from the repository root.
3. Confirm the window opens at 750 × 570.
4. Confirm the background, spaceship, UFOs, and score render.
5. Confirm music starts where audio is available.

## Input Test

- Hold Left Arrow and confirm left movement.
- Hold Right Arrow and confirm right movement.
- Confirm ship boundaries prevent moving beyond the configured range.
- Press Space and confirm one bullet moves upward.
- Press Space while the bullet is active and confirm another bullet is not created.
- Wait for the projectile to leave the top edge and confirm firing becomes available again.

## Enemy Test

Observe that twelve UFOs appear in the upper region, move horizontally, change direction and descend at boundaries, and increase speed after a hit. Initial positions are random, so exact coordinates differ between runs.

## Collision and Score Test

Fire at an enemy. Confirm the explosion sound where available, bullet reset, enemy relocation, enemy speed increase, and score increment. A missed shot must not increase the score.

## Game-Over Test

Allow an enemy to collide with the ship. Confirm movement stops, GAMEOVER and QUIT appear, and background music stops. Click the QUIT button and separately test the window close event.

## Regression Checklist

| Area | Expected |
|---|---|
| Startup | Window appears without missing-resource errors |
| Assets | Images, fonts, and sounds load |
| Input | Left, right, and Space work |
| Boundaries | Ship stays within horizontal range |
| Projectile | One active bullet and correct reset |
| Enemies | Horizontal movement and downward boundary step |
| Bullet hit | Enemy relocates and score increments once |
| Ship hit | Game-over display and movement stop |
| Audio | Music/effects play where supported |
| Exit | Button and window close work |

## Future Automated Tests

To make unit tests possible:
1. Move Pygame initialization into an explicit function.
2. Add an `if __name__ == "__main__":` guard.
3. Separate pure collision calculations from rendering.
4. Represent gameplay state in testable structures.
5. Inject deterministic randomness for tests.
6. Add tests for collision thresholds, bullet lifecycle, boundary rules, and score updates.
7. Use an off-screen display only for tests requiring Pygame surfaces.

Do not claim automated gameplay tests passed until they exist and have run.

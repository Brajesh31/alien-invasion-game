# 🧯 Troubleshooting

## Pygame Module Is Missing

If Python reports `ModuleNotFoundError: No module named 'pygame'`, install Pygame into the active interpreter:

```bash
python -m pip install pygame
python -m pip show pygame
```

Confirm the same interpreter runs the script and installs the dependency.

## Asset Not Found

The script loads images, audio, and fonts using relative paths. Change to the project root and launch with `python alien_invasion.py`. Verify spelling and capitalization of filenames, especially on case-sensitive operating systems.

## No Game Window Appears

Pygame requires a display. CI runners, SSH shells, servers, and headless containers may not have one. Use a desktop session or configure a virtual display deliberately for a test environment.

## Display Initialization Fails

Check whether a desktop session is active, the display server is available, and the process is allowed to create a window. Read the full Pygame/SDL error before changing source code.

## Audio Is Silent

Check system volume, output device, mixer initialization, and WAV file availability. The current code assumes audio initialization succeeds and does not provide a complete silent-mode fallback.

## Font Loading Fails

Confirm both TTF font files exist at the repository root and are valid. Do not move them without updating source paths.

## Gameplay Speed Varies

Movement is measured per loop iteration. No explicit frame-rate cap or delta-time calculation is used. A clock-based loop is future work, not a current setting.

## Bullet Does Not Fire

Ensure the game window has focus and the bullet has returned to the `ready` state. Only one active projectile is supported.

## Score Does Not Change

The score increments only when the distance-based collision threshold is satisfied. The code does not use pixel-perfect collision detection.

## Game-Over Button Does Not Exit

Move the pointer inside the visible QUIT button and click. Closing the window is an alternative exit path.

## Indentation or Syntax Error

The current main loop contains mixed indentation in the UFO section. Inspect tabs and spaces and use spaces consistently in future source edits.

## Useful Bug Report

Include Python/Pygame versions, operating system, working directory, launch command, reproduction steps, expected/actual behavior, and sanitized traceback. Mention whether display and audio devices are available.

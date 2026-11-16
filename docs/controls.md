# Player Controls

## Keyboard

| Input | Action |
|---|---|
| Left Arrow | Move spaceship left while held |
| Right Arrow | Move spaceship right while held |
| Space | Fire a bullet when the projectile is ready |

Input is read using Pygame keyboard-state polling inside the main loop. The game does not currently expose a remapping or settings interface.

## Movement

The player starts around x = 350 and y = 450. The horizontal coordinate changes by the configured movement amount once per main-loop iteration. The x coordinate is clamped between 10 and 680. Vertical movement is not implemented.

## Firing

Only one projectile is tracked. Space is accepted only when `bullet_state` is `ready`. While a projectile is moving, additional Space presses do not create another bullet. The projectile becomes ready again after reaching the top boundary.

## Mouse

A red QUIT control is drawn after game-over behavior is triggered. The code checks the current mouse position and left-button state and exits when the pointer is inside the button rectangle.

## Window

Closing the window sends a Pygame QUIT event and ends the main loop.

## Controls Not Yet Implemented

There is no pause/resume, restart, settings menu, controller support, fullscreen toggle, volume control, or remappable keyboard layout in the current script. These are possible enhancements, not present-day controls.

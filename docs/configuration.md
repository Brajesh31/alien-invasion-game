# ⚙️ Configuration and Runtime Parameters

## Current Model

The game does not read a runtime configuration file or environment variables. Window size, positions, movement speeds, enemy count, collision thresholds, and asset filenames are assigned directly in `alien_invasion.py`. The `.env.example` file only states that no variables are currently needed; the program does not load it.

## Runtime Values

| Parameter | Current value or behavior | Meaning |
|---|---|---|
| Window | 750 × 570 | Display dimensions |
| Caption | `alien invasion` | Window title |
| Ship start | x=350, y=450 | Initial player location |
| Ship movement | 8 per loop iteration | Horizontal coordinate change |
| UFO count | 12 | Number of enemies |
| UFO initial x | Random 0–600 | Horizontal start range |
| UFO initial y | Random 30–100 | Vertical start range |
| UFO initial speed | 4 | Initial horizontal movement |
| UFO boundary descent | 50 | Vertical step when direction changes |
| Bullet movement | 15 per loop iteration | Upward coordinate change |
| Bullet collision threshold | 27 | Distance comparison |
| Ship collision threshold | 30 | Distance comparison |
| Ship horizontal bounds | 10–680 | Player x clamp |
| UFO horizontal bounds | 10 and 680 | Direction-change checks |

## Changing Values

Edit the corresponding assignment in `alien_invasion.py` and search all references before changing it. Changing `ufoNum` affects list initialization and the update loop. Movement values are per-loop changes, not pixels per second. Collision thresholds alter perceived hitboxes.

## Future Settings

A future settings module could expose validated window size, audio volume, movement speed, and enemy count. It should provide safe defaults and should not add a remote service or credentials requirement.

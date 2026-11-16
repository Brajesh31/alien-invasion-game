# Gameplay Mechanics

## Game Space

The Pygame display is 750 by 570 pixels. The player ship is positioned near the bottom of the screen, while the UFOs begin in the upper region. Sprite drawing uses image top-left coordinates. Collision checks use the coordinates supplied by the game logic rather than pixel masks.

## Player Movement

The ship starts at x = 350 and y = 450. Left Arrow subtracts the configured movement amount from x, and Right Arrow adds it. The current step is 8 per main-loop iteration. The x coordinate is constrained between 10 and 680. There is no vertical movement.

## UFO Initialization

Twelve UFO entries are created. Each receives a random x coordinate from 0 to 600, a random y coordinate from 30 to 100, and an initial horizontal speed of 4. The sprite, x coordinate, y coordinate, and speed are held in parallel lists at matching indices.

## UFO Movement

Each loop updates an enemy's horizontal coordinate using its velocity. At or below the left boundary of 10, the velocity is set to 5 and the UFO moves down 50 pixels. At or above the right boundary of 680, the velocity is set to -5 and the UFO moves down 50 pixels. A successful bullet hit relocates that UFO to a random initial region and increments its velocity by one.

## Projectile Lifecycle

Only one projectile is represented. The global `bullet_state` begins as `ready`. Pressing Space while ready stores the ship's current x coordinate, plays the bullet sound, and calls the firing helper. The helper changes the state to `fire`. The active bullet moves upward by 15 units per main-loop iteration. When its y coordinate reaches or passes zero, it resets to y = 450 and becomes ready again.

## Bullet Collision

The helper calculates Euclidean distance:

`d = sqrt((ufo_x - bullet_x)^2 + (ufo_y - bullet_y)^2)`

A distance below 27 is considered a hit. The hit path plays the explosion sound, resets the bullet, relocates the UFO, increases that UFO's speed by one, and increments the score. It does not use exact sprite masks.

## Ship Collision

A distance below 30 between UFO and player coordinates is treated as a ship collision. The code sets UFO, ship, and bullet movement speeds to zero, renders the current score and GAMEOVER text, draws a QUIT button, and stops background music.

## Score

Score begins at zero and increases by one for each accepted bullet collision. It is rendered using Roboto-Medium.ttf. It is not saved after the process exits.

## Difficulty and Timing

Enemy speed increases after a hit. The loop has no explicit frame-rate cap or delta-time calculation, so per-iteration movement can vary in perceived speed across machines. There are no explicit levels or waves.

## Change Checklist

When adjusting a mechanic, review every variable it reads/writes, loop ordering, boundary behavior, state reset, sound effects, score behavior, and game-over behavior. Test both successful and unsuccessful interactions.
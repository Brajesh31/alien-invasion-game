# Glossary

| Term | Meaning in this project |
|---|---|
| Pygame | Python library used for windowing, input, graphics, fonts, and audio |
| Surface | Pygame object used to represent a drawable image or display |
| Main loop | Repeated section that reads events, updates state, draws objects, and refreshes the window |
| Sprite | Image used to visually represent a game object |
| Player ship | Spaceship controlled by the user |
| UFO | Enemy object that moves horizontally and descends at boundaries |
| Projectile / bullet | Player-fired image that travels upward |
| Bullet state | Global value `ready` or `fire` indicating whether a new projectile can be created |
| Collision threshold | Distance limit used by helper functions to decide whether two objects have collided |
| Euclidean distance | Straight-line distance between two coordinate points |
| HUD | Heads-up display, in this game the score shown on the play screen |
| Frame | One iteration of drawing/updating the game display |
| Frame-based movement | Movement measured in position changes per loop iteration rather than elapsed time |
| Mixer | Pygame subsystem used for playback of WAV audio |
| Asset | Image, sound, or font file loaded by the game |
| Game over | Behavior triggered when a UFO collides with the player |
| Working directory | Directory from which Python is launched; relative asset paths resolve from here |
| Headless environment | Runtime without a graphical desktop display |
| Delta time | Elapsed time between updates, commonly used to make movement independent of frame rate |
| Persistent score | Score saved outside the current process; not implemented in this game |

# 🔌 API Boundary

## Network API

No network API is implemented in the inspected repository. The game runs locally as a Python/Pygame process. There are no HTTP endpoints, REST/GraphQL routes, sockets, remote authentication, multiplayer transport, cloud score submission, or external service integrations.

## Local Helper Functions

| Function | Purpose |
|---|---|
| `fire_bullet(x, y)` | Changes projectile state and draws it |
| `collision(...)` | Checks distance between a projectile and UFO |
| `ship_collision(...)` | Checks distance between player and UFO |
| `show_score(...)` | Draws the current score |
| `gameover()` | Draws the game-over message |
| `button()` | Draws and checks the QUIT button |

These are internal Python helpers. They share module-level variables and the display surface. They are not a stable public library API.

## Future Networking

If online scores, player accounts, or multiplayer are introduced, document server ownership, authentication, authorization, request/response schemas, encryption, validation, retry behavior, rate limits, abuse prevention, and data retention. Do not advertise online functionality until it exists and has been tested.

# Alien Invasion Game

Alien Invasion Game is a small Python/Pygame arcade game in which the player moves a spaceship, fires bullets, and avoids or destroys UFOs. Images, fonts, and sound effects are kept as local assets.

## Setup

Requirements: Python 3.10+ and Pygame.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install pygame
python alien_invasion.py
```

Use the left and right arrow keys to move, press Space to fire, and close the game window to exit. The program expects to run from the repository root so relative asset paths resolve.

## Development

The current game is a single script and executes its loop at import time. Future changes should separate initialization, game state, input, collision, rendering, and cleanup so they can be tested independently.

See [docs/architecture.md](docs/architecture.md), [docs/development.md](docs/development.md), and [docs/troubleshooting.md](docs/troubleshooting.md).

Maintained by Brajesh Kumar (`brajesh31`).

Last updated: 2026-10-26 09:41 UTC

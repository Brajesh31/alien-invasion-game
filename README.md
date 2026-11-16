# 👾 Alien Invasion Game

<p align="center">
  <strong>A classic desktop arcade shooter built with Python and Pygame.</strong><br/>
  Move your spaceship, fire at incoming UFOs, avoid collisions, and survive as long as you can.
</p>

<p align="center">
  <a href="https://github.com/Brajesh31/alien-invasion-game/stargazers"><img src="https://img.shields.io/github/stars/Brajesh31/alien-invasion-game?style=for-the-badge" alt="GitHub stars"></a>
  <a href="https://github.com/Brajesh31/alien-invasion-game/issues"><img src="https://img.shields.io/github/issues/Brajesh31/alien-invasion-game?style=for-the-badge" alt="Open issues"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/Brajesh31/alien-invasion-game?style=for-the-badge" alt="MIT License"></a>
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge" alt="Python">
  <img src="https://img.shields.io/badge/Pygame-desktop%20game-green?style=for-the-badge" alt="Pygame">
</p>

---

## 📚 Table of Contents

- [Overview](#-overview)
- [Gameplay](#-gameplay)
- [Controls](#-controls)
- [Game Rules and Mechanics](#-game-rules-and-mechanics)
- [Technology](#-technology)
- [How the Game Works](#-how-the-game-works)
- [Project Structure](#-project-structure)
- [Assets](#-assets)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Running the Game](#-running-the-game)
- [Configuration and Runtime Behavior](#-configuration-and-runtime-behavior)
- [Development Guide](#-development-guide)
- [Testing and Quality Assurance](#-testing-and-quality-assurance)
- [Troubleshooting](#-troubleshooting)
- [Packaging and Distribution](#-packaging-and-distribution)
- [Known Limitations](#-known-limitations)
- [Roadmap](#-roadmap)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [License and Maintainer](#-license-and-maintainer)

## 🌌 Overview

**Alien Invasion Game** is a small desktop arcade shooter implemented in one Python script using Pygame. The player controls a spaceship near the bottom of the window. A formation of UFOs moves horizontally across the screen. The player fires a projectile to hit the UFOs, gains points for successful hits, and loses the game when an enemy collides with the ship.

The project uses local files for its graphics, audio, and fonts. It does not require a web server, database, account system, or network connection during normal gameplay. The game is intended to run as an interactive desktop application in a graphical environment.

The current implementation is deliberately simple: initialization, game state, input handling, collision checks, drawing, and the main loop live together in `alien_invasion.py`. This repository documents that implementation as it exists. Proposed architectural improvements are listed separately in [ROADMAP.md](ROADMAP.md).

## 🕹️ Gameplay

The player starts with a spaceship positioned near the lower edge of the game window. Twelve UFO sprites are initialized in the upper region. Each UFO moves horizontally. When an enemy reaches a horizontal boundary, its horizontal direction is changed and its vertical position is advanced.

The player can fire a bullet while the bullet state is ready. A projectile travels upward. When the distance between a projectile and a UFO becomes smaller than the configured collision threshold, the game:
1. Plays the explosion sound.
2. Resets the projectile to its ready position.
3. Places the hit UFO at a new random position.
4. Increases that UFO's movement speed.
5. Increments the score.

The score is drawn in the upper-left corner. If a UFO collides with the player's ship, enemy movement and player/bullet movement are stopped, the game-over message is displayed, background music is stopped, and a quit button is shown.

## 🎮 Controls

| Input | Action |
|---|---|
| Left Arrow | Move the spaceship left |
| Right Arrow | Move the spaceship right |
| Space | Fire when the bullet is ready |
| Window close button | Close the game window |
| Mouse click on QUIT | Exit from the game-over screen |

Movement is continuous while the corresponding arrow key is held. The current game loop does not implement a dedicated pause or restart key.

## 🧠 Game Rules and Mechanics

### Player movement
- The ship begins at approximately `(350, 450)`.
- Horizontal movement is controlled by the arrow keys.
- The configured movement step is 8 pixels per frame.
- The ship's horizontal coordinate is constrained to the interval from 10 to 680.
- Vertical player movement is not implemented.

### UFO formation
- The game initializes 12 UFO sprites.
- Each UFO is assigned a random horizontal starting coordinate between 0 and 600.
- Each UFO begins at a random vertical coordinate between 30 and 100.
- Initial horizontal movement speed is 4.
- At the left or right boundary, the movement speed is reassigned to a fixed direction value and the UFO moves down by 50 pixels.
- A successful bullet hit relocates a UFO to a random starting region and increases its speed by one.

### Projectile
- Only one projectile state is tracked globally.
- `ready` means a new bullet can be fired.
- `fire` means the projectile is travelling upward.
- Pressing Space while the bullet is already travelling does not create another projectile.
- When the projectile reaches the top boundary, its vertical position is reset and it becomes ready again.

### Collisions
The current implementation uses Euclidean distance between sprite coordinates rather than pixel-perfect mask collision or rectangle overlap.

The bullet collision helper compares the UFO and bullet coordinates and reports a hit when the distance is below 27. The ship collision helper uses a threshold below 30.

These thresholds are simple gameplay approximations. They do not account for each sprite's exact transparent bounds.

### Scoring
- The score starts at zero.
- Each successful bullet-to-UFO collision increases the score by one.
- The score remains in memory for the active process.
- No high-score file, leaderboard, or persistent profile is implemented.

### Game over
When a UFO triggers ship collision, the game sets all UFO speeds, ship speed, and bullet speed to zero. It draws the score and game-over message, shows a quit button, and stops the background music.

There is no restart flow in the current implementation. Closing the window is also supported.

## 🧰 Technology

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pygame | Window, input events, surfaces, rendering, fonts, and audio |
| `random` | Random initial and respawn positions |
| `math` | Distance calculations for collisions |
| Pygame mixer | Background music and sound effects |
| PNG / JPG | Game sprites, icon, and background image |
| WAV | Background music and effects |
| TTF | Score and game-over typography |

The script uses Python standard-library modules alongside Pygame. No additional application framework, web service, or database is part of the runtime.

## ⚙️ How the Game Works

The program follows this high-level sequence:

```text
Start Python process
       |
       v
Initialize Pygame
       |
       v
Create window and load assets
       |
       v
Initialize player, UFOs, bullet and score
       |
       v
+-------------------------------+
| Main game loop                |
|                               |
| 1. Clear and draw background  |
| 2. Process window events      |
| 3. Read keyboard state        |
| 4. Move player                |
| 5. Fire/update bullet         |
| 6. Move UFOs                  |
| 7. Check collisions           |
| 8. Update score/game-over     |
| 9. Draw sprites and score     |
| 10. Refresh display           |
+-------------------------------+
       |
       v
Window closed / loop exits
       |
       v
Quit Pygame
```

Detailed state and helper-function descriptions are available in [Architecture](docs/architecture.md) and [Gameplay Mechanics](docs/gameplay-mechanics.md).

## 📁 Project Structure

```text
alien-invasion-game/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── workflows/
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/
│   ├── README.md
│   ├── installation.md
│   ├── architecture.md
│   ├── gameplay-mechanics.md
│   ├── controls.md
│   ├── assets.md
│   ├── development.md
│   ├── testing.md
│   ├── troubleshooting.md
│   ├── deployment.md
│   ├── packaging.md
│   ├── configuration.md
│   ├── security.md
│   ├── api.md
│   ├── database.md
│   ├── glossary.md
│   ├── release-process.md
│   └── faq.md
├── alien_invasion.py
├── background.jpg
├── background.wav
├── bullet.png
├── bullet.wav
├── explosion.wav
├── icon.png
├── spaceship.png
├── ufo.png
├── Roboto-Bold.ttf
├── Roboto-Medium.ttf
├── .env.example
├── .gitignore
├── CHANGELOG.md
├── CITATION.cff
├── CODEOWNERS
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── ROADMAP.md
├── SECURITY.md
└── SUPPORT.md
```

All game resources are stored in the repository root and loaded using relative paths. Run the game from that directory unless a future asset-path refactor changes the resource-loading strategy.

## 🧩 Assets

| File | Role |
|---|---|
| `background.jpg` | Game background image |
| `icon.png` | Window icon |
| `spaceship.png` | Player sprite |
| `ufo.png` | Enemy sprite, reused for each UFO |
| `bullet.png` | Player projectile |
| `background.wav` | Repeating background music |
| `bullet.wav` | Fired-bullet sound |
| `explosion.wav` | Hit/explosion sound |
| `Roboto-Medium.ttf` | Score and button text |
| `Roboto-Bold.ttf` | Game-over message |

See [Asset Guide](docs/assets.md) for file formats, loading behavior, replacement guidelines, and distribution considerations.

## 💻 Requirements

- Python 3.10 or newer is the documented baseline.
- Pygame installed in the active Python environment.
- A desktop operating system with a graphical display.
- Audio output is recommended for the intended experience.
- The repository's local assets must be present and readable.

The program creates a 750 by 570 pixel window. A headless server or terminal-only session may not be able to launch the game because it requires a display and an interactive event loop.

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Brajesh31/alien-invasion-game.git
cd alien-invasion-game
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```bat
py -3 -m venv .venv
.venv\Scripts\activate.bat
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Pygame

```bash
python -m pip install --upgrade pip
python -m pip install pygame
```

### 4. Run the game

```bash
python alien_invasion.py
```

Run this command from the repository root. The current script references image, audio, and font filenames relative to the working directory.

A more detailed walkthrough is in [Installation Guide](docs/installation.md).

## ▶️ Running the Game

The game opens a desktop window. Use the left and right arrow keys to move, and hold or press Space to fire when the projectile is ready. The score appears in the top-left corner.

The game ends when an enemy collides with the player. The screen shows the game-over message and a QUIT button. You can close the window using the operating system's window controls.

The game is not designed as a command-line application. Running it in a non-interactive CI runner is not a valid gameplay test.

## 🔧 Configuration and Runtime Behavior

There is no runtime configuration file or environment-variable interface in the current game. `.env.example` is a placeholder documenting that no environment values are required.

Window dimensions, initial positions, entity count, movement speeds, and collision thresholds are defined directly in `alien_invasion.py`. Changing these values currently requires editing the script.

The game does not persist scores, player profiles, settings, or save files. The current score and entity state are reset when the Python process starts.

See [Configuration](docs/configuration.md).

## 🧑‍💻 Development Guide

The game is currently a single script. Keep changes focused and preserve the working-directory assumptions unless intentionally improving resource loading.

A typical development sequence:

```bash
python -m venv .venv
# Activate the environment using the command for your platform
python -m pip install pygame
python alien_invasion.py
```

When modifying gameplay, inspect the related state variables and helper functions together. Changes to projectile lifecycle affect firing and collision. Changes to UFO movement affect boundary handling and difficulty. Changes to collision thresholds affect score and game-over behavior.

The script currently starts Pygame and enters its game loop at module execution time. It is therefore not safe to import as a normal library module for isolated tests. Future refactoring should introduce a guarded entry point and separable game-state logic.

See [Development Workflow](docs/development.md).

## ✅ Testing and Quality Assurance

There is no automated test suite configured in the current repository. Manual testing is therefore required for gameplay changes.

At minimum, verify:
- Game starts from the repository root.
- Window dimensions, caption, and icon are correct.
- Background and sprites load.
- Background music starts and effects play.
- Left and right movement work.
- Ship remains within horizontal boundaries.
- Space fires only when the projectile is ready.
- Projectile returns to ready state at the top.
- UFOs change horizontal direction at boundaries and descend.
- Bullet collision increments score and respawns the affected UFO.
- Ship collision stops movement and displays game-over UI.
- The quit button and window close event exit cleanly.

See [Testing Guide](docs/testing.md) for a repeatable QA checklist and future automation recommendations.

## 🧯 Troubleshooting

| Symptom | Likely cause | First check |
|---|---|---|
| `ModuleNotFoundError: pygame` | Pygame missing from active Python environment | Activate venv and install Pygame |
| Missing image/audio/font | Game started from the wrong directory or file absent | Run from repo root and inspect assets |
| No window appears | Headless environment or display issue | Use a desktop session |
| No sound | Audio device/mixer issue | Check system output and WAV files |
| Game exits during startup | Pygame/display initialization failure | Inspect terminal traceback |
| Game appears frozen | Main loop is waiting for interactive input/events | Focus the game window and test controls |

For more detailed diagnostic steps, read [Troubleshooting](docs/troubleshooting.md).

## 📦 Packaging and Distribution

The repository currently provides source code and local assets. It does not include a packaged executable or a configured installer.

A future standalone distribution can use a Python packaging tool such as PyInstaller, but packaging should be treated as a separate task. All image, audio, and font resources must be included and resolved correctly in the packaged runtime. The build should be validated on each supported operating system.

See [Packaging Guide](docs/packaging.md).

## ⚠️ Known Limitations

- Gameplay, initialization, and rendering are implemented in a single script.
- The script enters the game loop at import time.
- There is one global projectile state, so multiple simultaneous bullets are not supported.
- The game has no pause, restart, menu, or difficulty-selection screen.
- Scores are not saved after the process exits.
- There is no automated unit or gameplay test suite.
- Collision detection is based on point distance thresholds, not sprite masks.
- Timing and movement are based on per-frame updates without a controlled frame clock.
- Asset paths depend on the current working directory.
- The current code should be checked for indentation consistency before extending the loop.

These are observations about the current implementation, not claims that the proposed fixes have already been made.

## 🗺️ Roadmap

See [ROADMAP.md](ROADMAP.md) for planned improvements such as separating game state from the loop, deterministic timing, persistent scores, restart/pause behavior, asset loading resilience, and test coverage.

## 📚 Documentation

| Guide | Purpose |
|---|---|
| [Documentation Index](docs/README.md) | Navigation across all guides |
| [Installation](docs/installation.md) | Environment setup and startup |
| [Architecture](docs/architecture.md) | Script structure and state flow |
| [Gameplay Mechanics](docs/gameplay-mechanics.md) | Movement, enemies, bullets, collisions, scoring |
| [Controls](docs/controls.md) | Keyboard and game-over controls |
| [Assets](docs/assets.md) | Images, fonts, sounds, and replacement advice |
| [Configuration](docs/configuration.md) | Hard-coded runtime parameters |
| [Development](docs/development.md) | Safe code change workflow |
| [Testing](docs/testing.md) | Manual QA and future automation |
| [Troubleshooting](docs/troubleshooting.md) | Setup and runtime failure diagnosis |
| [Deployment](docs/deployment.md) | Desktop distribution model |
| [Packaging](docs/packaging.md) | Bundling the game and local resources |
| [API](docs/api.md) | Explicitly documents the absence of a network API |
| [Database](docs/database.md) | Explicitly documents the absence of persistence |
| [Glossary](docs/glossary.md) | Terms used in code and gameplay |
| [Release Process](docs/release-process.md) | Release readiness and validation |
| [FAQ](docs/faq.md) | Common questions |

## 🤝 Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing changes. Include the controls and gameplay states affected, steps to reproduce, and manual verification results. Do not bundle unrelated asset or formatting changes.

## 📄 License and Maintainer

The repository includes an MIT License. See [LICENSE](LICENSE) for the complete terms.

Maintained by **Brajesh Kumar**: [@Brajesh31](https://github.com/Brajesh31).

---

<p align="center">Defend the skies. Watch your aim. Keep the invasion under control. 👾</p>

Last updated: 2026-11-16 03:05 UTC

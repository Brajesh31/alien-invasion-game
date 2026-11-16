# 🚀 Installation and First Launch

## Requirements

- Python 3.10+ as the documented baseline.
- Pygame in the active Python environment.
- Desktop operating system with a graphical display.
- Local PNG, JPG, WAV, and TTF runtime assets.
- Audio output recommended.

Check Python with `python --version`. Depending on platform, use `python3` or `py`.

## Clone

```bash
git clone https://github.com/Brajesh31/alien-invasion-game.git
cd alien-invasion-game
```

## Virtual Environment

Windows PowerShell:

```powershell
py -3 -m venv .venv
.venv\\Scripts\\Activate.ps1
```

Windows Command Prompt:

```bat
py -3 -m venv .venv
.venv\\Scripts\\activate.bat
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Install and Run

```bash
python -m pip install --upgrade pip
python -m pip install pygame
python alien_invasion.py
```

Run from the repository root. The game opens a 750 × 570 window titled `alien invasion` and loads local resources using relative paths.

## First-Run Checklist

- [ ] Window opens.
- [ ] Background and sprites appear.
- [ ] Score is visible.
- [ ] Background audio starts where supported.
- [ ] Left/right movement works.
- [ ] Space fires a bullet.
- [ ] A successful hit increments score.
- [ ] Window close exits.

## Headless Environments

The game is interactive and requires a display. CI, server, SSH, or container environments may not provide one. A successful Pygame installation alone does not prove the display can initialize.

## Environment Updates

Activate the same virtual environment before updating Pygame. Check the installed version with `python -m pip show pygame`. There is no dependency lockfile, so record Python and Pygame versions for reproducibility.

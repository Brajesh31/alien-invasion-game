# 🤝 Contributing to Alien Invasion Game

Thank you for considering a contribution. This guide describes how to propose focused changes to the Python/Pygame desktop game.

## Project Scope

The project is a single-player arcade shooter implemented in `alien_invasion.py`. It uses local image, audio, and font assets. It currently has no web API, database, account system, or network gameplay.

Contributions should clearly distinguish an actual implemented mechanic from a future proposal. Do not represent pause, restart, persistent score, multiple bullets, or a packaged executable as existing features unless they have been implemented and verified.

## Development Requirements

- Python 3.10+ as the documented baseline.
- Pygame installed in a virtual environment.
- A desktop display for interactive verification.
- Audio output for full sound testing.
- Git for source control.

## Local Setup

```bash
git clone https://github.com/Brajesh31/alien-invasion-game.git
cd alien-invasion-game
python -m venv .venv
# Activate the environment for your shell
python -m pip install pygame
python alien_invasion.py
```

See [Installation](docs/installation.md) for Windows, macOS, and Linux commands.

## Contribution Workflow

1. Review current source and existing issues before starting.
2. Create a focused branch from the latest `main`.
3. Identify state variables and all relevant main-loop stages.
4. Keep changes limited to the issue being addressed.
5. Preserve asset paths or update all references consistently.
6. Test on a desktop environment.
7. Update documentation when behavior, controls, mechanics, dependencies, or assets change.
8. Submit a pull request with manual test evidence.

## Code Expectations

- Preserve consistent indentation. The current game loop includes mixed tab/space indentation that should be handled carefully.
- Keep resource paths portable.
- Avoid expensive asset loading inside the per-frame loop.
- Avoid blocking operations in the event loop.
- Preserve both the window-close and game-over quit paths.
- Do not introduce dependencies without a clear reason.
- Avoid unverified third-party assets.
- Do not commit virtual environments, caches, editor state, or build output.

## Testing Expectations

There is no automated gameplay test suite in the current repository. Before submitting gameplay changes, run the game and verify:
- startup and asset loading;
- left/right movement and ship bounds;
- Space firing and bullet reset;
- UFO movement and boundary descent;
- bullet collision and score increment;
- ship collision and game-over behavior;
- background/effect audio where supported;
- quit button and window close.

Include Python/Pygame versions and the operating system in your pull request.

## Asset Contributions

For every new or replacement asset:
- identify its intended runtime role;
- preserve transparency where needed;
- check file size and format;
- ensure the code references the correct path;
- verify it at the actual display size;
- confirm redistribution rights and record verified licensing information.

A file being present in the repository is not proof that it may be redistributed.

## Pull Request Checklist

- [ ] The change has a clear scope.
- [ ] Existing gameplay outside that scope was preserved.
- [ ] The game launches from the repository root.
- [ ] Relevant input, collision, scoring, and exit paths were tested.
- [ ] All referenced assets are present.
- [ ] Documentation is updated.
- [ ] No personal files, secrets, or generated environment directories are included.
- [ ] Asset provenance and redistribution were reviewed.

Use the repository pull request template.

## Security Reports

Do not publish exploitable details or sensitive data in an issue. Follow [SECURITY.md](SECURITY.md) for private reporting.

## License

The repository includes an MIT License. Contributions are subject to the repository's license terms and any applicable rights in contributed assets.

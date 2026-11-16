# 📚 Documentation Index

Welcome to the Alien Invasion Game documentation. These guides explain the current Python/Pygame desktop game, how to run it, how its gameplay loop works, and how to maintain or distribute it.

## Core Guides

| Document | Description |
|---|---|
| [Installation](installation.md) | Python environment creation, Pygame installation, startup |
| [Architecture](architecture.md) | Program entry, initialization, state, helpers, frame loop |
| [Gameplay Mechanics](gameplay-mechanics.md) | Ship movement, UFO behavior, bullet lifecycle, collisions, score |
| [Controls](controls.md) | Player input, game-over interaction, exit behavior |
| [Assets](assets.md) | Image, font, and audio inventory and safe replacement |
| [Configuration](configuration.md) | Current hard-coded settings and runtime assumptions |
| [Development](development.md) | Workflow for modifying a single-script Pygame project |
| [Testing](testing.md) | Manual test plan and automation boundaries |
| [Troubleshooting](troubleshooting.md) | Common installation, display, sound, and asset failures |
| [Deployment](deployment.md) | Desktop distribution and supported runtime assumptions |
| [Packaging](packaging.md) | Future executable packaging guidance |
| [API](api.md) | Clarifies that no network API exists |
| [Database](database.md) | Clarifies that there is no database or persistent profile |
| [Security](security.md) | Local application security and asset handling |
| [Glossary](glossary.md) | Gameplay and implementation terminology |
| [Release Process](release-process.md) | Release checklist and versioning guidance |
| [FAQ](faq.md) | Frequently asked questions |

## Repository Policies

- [Root README](../README.md)
- [Contributing](../CONTRIBUTING.md)
- [Code of Conduct](../CODE_OF_CONDUCT.md)
- [Security Policy](../SECURITY.md)
- [Support](../SUPPORT.md)
- [Changelog](../CHANGELOG.md)
- [Roadmap](../ROADMAP.md)
- [MIT License](../LICENSE)

## Recommended Reading Paths

**Players:** read the [Controls](controls.md) and [FAQ](faq.md).

**New developers:** read [Installation](installation.md), [Architecture](architecture.md), [Gameplay Mechanics](gameplay-mechanics.md), and [Development](development.md).

**Maintainers:** read [Assets](assets.md), [Testing](testing.md), [Troubleshooting](troubleshooting.md), and [Release Process](release-process.md).

**Distribution work:** read [Deployment](deployment.md) and [Packaging](packaging.md).

## Documentation Accuracy Rules

- Document current code, not planned behavior.
- Keep proposed changes in the roadmap until implemented.
- Do not invent an API, database, save format, or configuration capability.
- Check actual filenames and runtime behavior before documenting a change.
- Keep asset licensing and provenance explicit when known. Do not guess ownership.
- Update the README and relevant guides whenever controls, mechanics, dependencies, or file layout change.

Maintained by Brajesh Kumar.

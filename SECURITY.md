# 🔐 Security Policy

## Project Scope

Alien Invasion Game is currently a local Python/Pygame desktop application. The inspected source does not implement accounts, networking, payments, remote services, or database persistence. Its main trust surface is the Python runtime, local assets, and any distributed package.

## Reporting a Vulnerability

Please report suspected security issues privately to Brajesh Kumar (`@Brajesh31`) through a private GitHub contact channel. Do not publish exploit steps, malicious files, private data, or working attack payloads in a public issue.

Include:
- A clear description of the issue.
- Affected file or behavior.
- Reproduction steps using a safe local environment.
- Impact and attacker prerequisites.
- Sanitized screenshots or terminal output.
- Suggested mitigation, if known.

## Security Expectations

- Obtain source from the intended repository.
- Review changes before running scripts from untrusted branches.
- Use a virtual environment to isolate Python dependencies.
- Install dependencies from trusted package sources.
- Keep Python, Pygame, and the operating system updated.
- Do not run the game with elevated privileges unless required.
- Treat downloaded or replacement assets as untrusted until verified.
- Do not include private files, credentials, or unrelated binary artifacts.

## Data and Privacy

The current game stores score and gameplay state in memory only. It does not have user profiles, analytics, or online services. If any of these features are introduced, document the data collected, purpose, retention, security controls, and user choices.

## Third-Party Assets

Before distributing the game, verify the license and redistribution rights for images, music, sound effects, and fonts. The root MIT license does not automatically override the terms of bundled third-party assets.

## Coordinated Disclosure

Please allow reasonable time for investigation and remediation before public disclosure. Avoid sharing sensitive issue details in public discussions.

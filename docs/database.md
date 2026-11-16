# 🗄️ Database and Persistence Boundary

## Current Storage

The game does not use a database. There is no database driver, schema, migration, ORM, account repository, or remote persistence layer.

The score is held in the module-level `score` variable during the process. Player, UFO, and projectile state also remain in memory. All of it is lost after the game exits.

## No Save or Profile System

The current implementation does not save high scores, player profiles, preferences, unlocked levels, progress, or session history. It does not synchronize data between devices.

## Future Local High Scores

If score persistence is introduced, a small local file may be sufficient. Define a versioned format, validate it when loading, and handle missing, malformed, or unwritable files. Consider whether user-edited score files undermine the intended integrity of a high-score feature.

## Future Online Leaderboards

An online leaderboard would introduce a backend, network API, identity model, score validation, abuse prevention, and privacy/retention obligations. Client-reported scores cannot be trusted without server-side validation.

## Documentation Requirement

If a database is added, update this page with the verified engine/version, schema diagram, entities, migrations, indexes, backup/restore strategy, retention, and access controls. Do not invent SQL or tables for a database that does not exist.

# 🗺️ Roadmap

This roadmap captures possible improvements identified from the current single-script Pygame implementation. Items are proposed work, not existing functionality or delivery commitments.

## 🔴 Priority 1: Reliability and Testability

- [ ] Resolve mixed tabs/spaces in the main loop in a separately reviewed source change.
- [ ] Add a guarded application entry point so importing modules does not start gameplay.
- [ ] Separate Pygame initialization and cleanup from game-state logic.
- [ ] Add a controlled game clock and time-based movement.
- [ ] Add tests for collision helpers, bullet lifecycle, boundaries, and scoring.
- [ ] Add a clear, consistent shutdown path for display and audio.

## 🟠 Priority 2: Gameplay Flow

- [ ] Add pause and resume behavior.
- [ ] Add a restart flow after game over.
- [ ] Add a start/menu screen.
- [ ] Add configurable difficulty or enemy waves.
- [ ] Review UFO descent and a possible loss condition.
- [ ] Consider support for multiple projectiles as an explicit design change.

## 🟡 Priority 3: Player Experience

- [ ] Add persistent local high scores.
- [ ] Add sound volume and mute controls.
- [ ] Add keyboard remapping or alternate controls.
- [ ] Improve accessibility and display scaling.
- [ ] Add more explicit feedback for game state transitions.

## 🟢 Priority 4: Maintainability and Distribution

- [ ] Introduce structured player/enemy/projectile state.
- [ ] Add an asset loader with working-directory-independent paths.
- [ ] Add dependency/version documentation.
- [ ] Evaluate standalone packaging after resource loading is made portable.
- [ ] Verify and document licensing for distributed image, audio, and font assets.
- [ ] Add release artifacts and checksums after packaging is tested.

## Definition of Done

A roadmap item is complete only after implementation is reviewed, affected gameplay is tested, documentation is updated, required asset rights are checked, and remaining limitations are recorded.

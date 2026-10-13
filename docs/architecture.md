# Architecture

The game currently has one executable script. It initializes Pygame and assets, maintains player/UFO/bullet state, processes events, performs collision checks, renders the frame, and plays audio.

Future refactoring should isolate state, update logic, rendering, input, and resource cleanup.

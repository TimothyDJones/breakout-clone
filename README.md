# Breakout Clone
A [PyGame](https://www.pygame.org/) clone of the classic [Breakout](https://en.m.wikipedia.org/wiki/Breakout_(video_game)) arcade game based on [video tutorial](https://www.youtube.com/watch?v=H4Vkcs6eM0w) from [Chris Franklin](https://medium.com/weekly-python/). Game assets from [Kenney.nl](https://www.kenney.nl/assets/).

## Tutorial Steps
1. Create Python virtual environment, activate it, and install PyGame.
    ```bash
    mkdir breakout-clone
    cd breakout-clone
    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install pygame
2. Create `/assets` directory and copy graphics and font files from Kenney.nl into it.
3. Create `/game` directory and create the `game` module file `__init__.py` inside of it. In `game\__init__.py`, create the framework of the *Game* class with three functions: *handle_events*, *update*, and *draw*.
4. Create `main.py` in project root directory. In `main.py`, import the *Game* class and set up the game loop.
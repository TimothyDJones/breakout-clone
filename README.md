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
5. Add `import` for PyGame library and add `__init__` method to `game\__init__.py`. In the *handle_events* method, create a loop for pulling any events that have happened since the last time the loop was run and check for any events of type `pygame.QUIT`.
6. Create a new file named `constants.py` in the project root. In it, create a *Constants* class with values for *screen_height* and *screen_width*.
7. In `game\__init__.py`, in the `__init__` method, initialize PyGame and then create the `self.screen` object using the constants for the screen size to define the size and then the `self.clock` object for the game timer. Next, set the `self.bg_color` to black for the background color, used to clear the screen, and `self.font` to the Kenney Future font in the `/assets` directory. Finally, to actually have something display on the screen, update the *draw* method. For now, we simply fill it with the background color.

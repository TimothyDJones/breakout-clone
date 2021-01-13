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
8. Create a new file `game\player.py` for the new *Player* class which inherits from the PyGame [**Sprite** class](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite). In the `__init__` method, we load the paddle image, `self.image`, from the `/asset` directory. Subsequently, we define the paddle position/geometry parameters. Then, we add *update*, *move_right*, and *move_left* methods. The movement methods simply move the paddle a fixed number of pixels specified in the *Constants* class and the *update* method redraws the paddle at the new position.
9. After the *Player* class is created, we import it into the *Game* class. To ensure that the game displays well, we use sprite [**Groups**](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group), so that they all draw at one time. Next, in the *Game* *handle_events* method, add handler for key presses and check specifically for left arrow (`K_LEFT`) and right arrow (`K_RIGHT`) to call the *move_left* and *move_right* methods for the paddle, respectively. Finally, we revise the *Game* *update* and *draw* methods appropriately to handle the `self.all_sprites` objects so that they refresh during each cycle.
10. Similarly to the *Player* class, we create the *Ball* class inherited from the PyGame Sprite class. We start it at the center of the screen. The other parameters are similar to the paddle (*Player* class), except the `self.velocity`, which is an array (list). The ball bounces around the screen, but we must prevent it from ever drifting vertically or horizontally. Likewise, if the ball goes off the screen at the bottom, we need to do something about it, so we have a utility method called *is_off_screen*.
11. As before with the *Player* class, once the *Ball* class is complete, we can import it into the *Game* class. In the *Game* class, if the ball goes off the screen at the bottom, we have the player lose a life and reset the ball.
12. Now, we move to checking for collision between the ball and the paddle. This is handled in the *check_collide_paddle* method of the *Ball* class that takes the `paddle` object as a parameter.

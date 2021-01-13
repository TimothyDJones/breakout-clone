import pygame
import sys

# TODO: Load game assets/components.
from game.constants import Constants
from game.player import Player

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(Constants.screen_width, Constants.screen_height))
        self.clock = pygame.time.Clock()

        self.bg_color = pygame.Color("black")
        self.font = pygame.font.Font("assets/Kenney_Future.ttf", 16)

        self.player = Player()

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

    def handle_events(self):
        keys = pygame.key.get_pressed()     # Convenience method for *all* key presses
        if keys[pygame.K_LEFT]:
            self.player.move_left()
        if keys[pygame.K_RIGHT]:
            self.player.move_right()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

    def update(self):
        self.all_sprites.update()
        pygame.display.update()
        self.clock.tick(120)

    def draw(self):
        self.screen.fill(self.bg_color)
        self.all_sprites.draw(self.screen)
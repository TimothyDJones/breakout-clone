import pygame
import sys

# TODO: Load game assets/components.
from game.constants import Constants

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(Constants.screen_width, Constants.screen_height))
        self.clock = pygame.time.Clock()

        self.bg_color = pygame.Color("black")
        self.font = pygame.font.Font("assets/Kenney_Future.ttf", 16)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

    def update(self):
        pass

    def draw(self):
        self.screen.fill(self.bg_color)
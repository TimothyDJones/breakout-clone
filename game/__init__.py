import pygame
import sys

# TODO: Load game assets/components.
from game.constants import Constants
from game.player import Player
from game.ball import Ball
from game.bricks import Bricks

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(Constants.screen_width, Constants.screen_height))
        self.clock = pygame.time.Clock()

        self.bg_color = pygame.Color("black")
        self.font = pygame.font.Font("assets/Kenney_Future.ttf", 16)
        self.game_over = False

        self.player = Player()
        self.ball = Ball()

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player, self.ball)

        self.bricks = Bricks(self.all_sprites)

    def reset(self):
        self.game_over = False
        self.player = Player()
        self.ball = Ball()

        self.all_sprites.empty()
        self.all_sprites.add(self.player, self.ball)
        self.bricks = Bricks(self.all_sprites)

    def handle_events(self):
        keys = pygame.key.get_pressed()     # Convenience method for *all* key presses
        if keys[pygame.K_LEFT]:
            self.player.move_left()
        if keys[pygame.K_RIGHT]:
            self.player.move_right()
        if self.game_over and keys[pygame.K_SPACE]:
            self.reset()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

    def update(self):
        if self.ball.is_off_screen():
            self.player.lose_life()
            if self.player.lives <= 0:
                self.game_over = True
            self.ball.reset()
        self.ball.check_collide_paddle(self.player)
        self.bricks.check_collisions(self.ball)
        self.all_sprites.update()
        pygame.display.update()
        self.clock.tick(120)

    def draw(self):
        self.screen.fill(self.bg_color)
        if self.game_over:
            text = self.font.render("Game Over!", True, "white")
            self.screen.blit(text, (Constants.screen_width / 2 - 75, Constants.screen_height / 2))
        else:
            self.all_sprites.draw(self.screen)
            text = self.font.render("Lives: {0}".format(self.player.lives), True, "white")
            self.screen.blit(text, (25, Constants.screen_height - 30))
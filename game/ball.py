import pygame
from random import randint
from game.constants import Constants

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_pos = Constants.screen_width / 2
        self.y_pos = Constants.screen_height / 2
        self.image = pygame.image.load("assets/ballBlue.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.velocity = [randint(2, 4), randint(-4, 4)]
        self.rect.center = (self.x_pos, self.y_pos)

    def update(self):
        if self.x_pos < 11 or self.x_pos > Constants.screen_width - 11:
            self.velocity[0] = -self.velocity[0]    # Switch direction
        if self.y_pos < 11:     # Top of screen
            self.velocity[1] = -self.velocity[1]

        # Prevent velocities from getting stuck at 0.
        if self.velocity[0] == 0:
            self.velocity[0] += 1
        if self.velocity[1] == 0:
            self.velocity[1] += 1
        
        # Update position based on velocity.
        self.x_pos += self.velocity[0]
        self.y_pos += self.velocity[1]
        self.rect.center = (self.x_pos, self.y_pos)
    
    def reset(self):
        self.velocity = [randint(2, 4), randint(-4, 4)]
        self.x_pos = Constants.screen_width / 2
        self.y_pos = Constants.screen_height / 2        
        self.rect.center = (self.x_pos, self.y_pos)

    def check_collide_paddle(self, paddle):
        if self.rect.colliderect(paddle.rect):
            if abs(self.rect.bottom - paddle.rect.top) < Constants.collision_threshold \
                and self.velocity[1] > 0:
                self.velocity[1] = -self.velocity[1]
                self.velocity[0] += paddle.direction
                if self.velocity[0] > Constants.max_ball_speed:
                    self.velocity[0] = Constants.max_ball_speed
                if self.velocity[0] < -Constants.max_ball_speed:
                    self.velocity[0] = -Constants.max_ball_speed
            else:
                self.velocity[0] *= -1
    def is_off_screen(self):
        return self.y_pos > Constants.screen_height
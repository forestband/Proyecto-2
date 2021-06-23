import pygame

import random


class Mob(pygame.sprite.Sprite):
    def __init__(self, window, image_name):
        pygame.sprite.Sprite.__init__(self)
        self.window = window
        self.image = pygame.image.load(f'images/{image_name}')
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(self.window.width - self.rect.width)
        self.rect.y = random.randrange(-100, -32)
        self.y_speed = random.randrange(1, 8)
        self.x_speed = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if self.rect.top > self.window.height + 10:
            self.rect.x = random.randrange(self.window.width - self.rect.width)
            self.rect.y = random.randrange(-100, -32)
            self.y_speed = random.randrange(1, 8)
            self.x_speed = random.randrange(-3, 3)
        if self.rect.right > self.window.width:
            self.y_speed = random.randrange(-6, 8)
            self.x_speed = random.randrange(-5, -3)
        if self.rect.top < 0 - 40:
            self.rect.x = random.randrange(self.window.width - self.rect.width)
            self.rect.y = random.randrange(-100, -32)
            self.y_speed = random.randrange(1, 8)
            self.x_speed = random.randrange(-3, 3)
        if self.rect.right < 0:
            self.y_speed = random.randrange(-6, 8)
            self.x_speed = random.randrange(3, 5)

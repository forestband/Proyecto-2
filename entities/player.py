import pygame
from window import Window


class Player(pygame.sprite.Sprite):
    lives = 3
    points = 0

    def __init__(self, window: Window):
        pygame.sprite.Sprite.__init__(self)
        self.window = window
        self.image = pygame.image.load("images/jogging.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = self.window.width / 2
        self.rect.bottom = self.window.height - 10
        self.x_speed = 0
        self.y_speed = 0

    def setImage(self, image_name):
        self.image = pygame.image.load(f"images/{image_name}")
        self.rect = self.image.get_rect()
        self.rect.centerx = self.window.width / 2
        self.rect.bottom = self.window.height - 10

    def update(self):

        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    self.y_speed = -5
                    pass
                if e.key == pygame.K_DOWN:
                    self.y_speed = 5
                    pass
                if e.key == pygame.K_RIGHT:
                    self.x_speed = 5
                    pass
                if e.key == pygame.K_LEFT:
                    self.x_speed = -5
                    pass
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_UP or e.key == pygame.K_DOWN:
                    self.y_speed = 0
                elif e.key == pygame.K_RIGHT or e.key == pygame.K_LEFT:
                    self.x_speed = 0

        self.rect.x += self.x_speed
        self.rect.bottom += self.y_speed
        if self.rect.right > self.window.width:
            self.rect.right = self.window.width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 800:
            self.rect.bottom = 800

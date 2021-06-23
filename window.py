import pygame


class Window:
    width = 600
    height = 800
    window = pygame.display.set_mode((width, height))

    White = (255, 255, 255)
    Black = (0, 0, 0)
    Red = (255, 0, 0)
    Green = (0, 255, 0)
    Blue = (0, 0, 255)

    def __init__(self):
        pygame.mixer.init()
        pygame.display.set_caption("Operation Moon Light")

    def __call__(self, *args, **kwargs):
        return self.window

    def set_bg(self, bg):
        self.window.blit(bg,[0,0])

    def add_text(self, text, textRect):
        self.window.blit(text, textRect)

    def getWindow(self):
        return self.window
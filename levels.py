import pygame
from entities.player import Player
from entities.mob import Mob
from window import Window
from time import sleep
from Sorting import quick_score_sort
from Sorting import find_score_position
pygame.init()


class Level:
    points = 0
    time = 0
    clock = pygame.time.Clock()
    font = pygame.font.Font('freesansbold.ttf', 24)
    sprites = pygame.sprite.Group()
    constant_username = ''

    WIDTH = 600
    HEIGHT = 800
    FPS = 60

    # Colores
    White = (255, 255, 255)
    Black = (0, 0, 0)
    Red = (255, 0, 0)
    Green = (0, 255, 0)
    Blue = (0, 0, 255)

    def __init__(self, username: str, window: Window, player: Player, background, mob, final: bool = False):
        print("CREATED LEVEL")
        self.window = window
        self.player = player
        self.mob_name = mob
        self.player_group = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        self.final = final
        self.player_group.add(self.player)
        self.sprites.add(self.player)
        self.background = pygame.image.load(f"images/{background}")
        self.constant_username = username

    def start(self, mobs_to_spawn, points_per_second):
        self.spawnMobs(mobs_to_spawn)

        while True:
            self.clock.tick(60)
            self.sprites.update()

            if self.gameover(170, 360):
                self.player.x_speed = 0
                self.player.y_speed = 0
                self.time = 0
                self.player.rect.centerx = self.window.width / 2
                self.player.rect.bottom = self.window.height - 10
                listening = True
                wrote_score = False
                while listening:
                    # save the score before resetting the variables
                    # automatically closes the file
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            if not wrote_score:
                                with open("scores.txt", 'a') as file:
                                    file.write(self.constant_username + " " + str(self.player.points) + '\n')
                                # esperamos a que el buffer del archivo se cierre
                                quick_score_sort("scores.txt")
                                wrote_score = True
                            return False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_p:
                                if not wrote_score:
                                    with open("scores.txt", 'a') as file:
                                        file.write(self.constant_username + " " + str(self.player.points) + '\n')
                                    # esperamos a que el buffer del archivo se cierre
                                    quick_score_sort("scores.txt")
                                    wrote_score = True
                                self.player.lives = 3
                                self.points = 0
                                self.time = 0
                                listening = False
                                break

                            elif event.key == pygame.K_ESCAPE:
                                self.player.points += self.points
                                self.mobs.empty()
                                return False
            collision = pygame.sprite.groupcollide(self.mobs, self.player_group, True, False)
            if collision:
                self.spawnMobs(len(collision))
                self.player.lives -= len(collision)

            if pygame.time.get_ticks() % 100 == 0:
                self.time += 1
                self.points += points_per_second

            if self.win(250, 360):
                # Add logic for the win
                if self.final:
                    sleep(5)
                self.mobs.remove(self.mobs)
                self.sprites.remove(self.mobs)
                self.player.points += self.points
                return True

            self.window().fill(self.Black)
            self.window().blit(self.background, (0, 0))
            self.showLives(10, 776)
            self.showName(200, 10)
            self.showScore(125, 776)
            self.showTime(420, 776)
            self.retry(50, 520)
            self.close(300, 520)
            position = find_score_position(self.constant_username)
            if position <= 7:
                self.showTop7(20, 300, position)
            
            self.sprites.draw(self.window())
            pygame.display.flip()

    def spawnMobs(self, mobs):
        for _ in range(mobs):
            m = Mob(self.window, self.mob_name)
            self.sprites.add(m)
            self.mobs.add(m)

    def win(self, x, y):
        if self.time >= 60:
            Win = pygame.font.Font('freesansbold.ttf', 40).render("Win", True, (255, 255, 255))
            self.window().blit(Win, (x, y))
            return True
        return False

    def retry(self, x, y):
        if self.player.lives == 0:
            Retry = pygame.font.Font('freesansbold.ttf', 25).render("Press P to Retry", True, (255, 255, 255))
            self.window().blit(Retry, (x, y))

    def close(self, x, y):
        if self.player.lives == 0:
            close_program = pygame.font.Font('freesansbold.ttf', 25).render("Press ESC to close", True,
                                                                            (255, 255, 255))
            self.window().blit(close_program, (x, y))
            return True
        return False

    def gameover(self, x, y):
        if self.player.lives <= 0:
            Game_over = pygame.font.Font('freesansbold.ttf', 40).render("Game Over", True, (255, 255, 255))
            self.window().blit(Game_over, (x, y))
            return True
        return False

    def showLives(self, x, y):
        if self.player.lives > 0:
            lives = self.font.render("Vidas :" + str(self.player.lives), True, (255, 255, 255))
            self.window().blit(lives, (x, y))
        else:
            lives = self.font.render("Vidas : 0", True, (255, 255, 255))
            self.window().blit(lives, (x, y))

    def showScore(self, x, y):
        score = self.font.render("Puntaje :" + str(self.points + self.player.points), True, (255, 255, 255))
        self.window().blit(score, (x, y))

    def showTop7(self, x, y, position):
        text = "Está entre los mejores 7 resultados! posición: #" + str(position) + " Puntos: " + str(self.points)
        notice = self.font.render(text, True, (255, 255, 255))
        self.window().blit(notice, (x, y))

    def showTime(self, x, y):
        time = self.font.render("Tiempo :" + str(self.time), True, (255, 255, 255))
        self.window().blit(time, (x, y))

    def showName(self, x, y):
        name = self.font.render("Name: " + self.constant_username, True, (255, 255, 255))
        self.window().blit(name, (x, y))
import pygame
from tkinter import *
import random
import tkinter
import winsound
WIDTH = 600
HEIGHT = 800
FPS = 60

#Colores
White = (255,255,255)
Black = (0,0,0)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)

#crear la ventana
pygame.init()
pygame.mixer.init()
Ventana = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Operation Moon Light 2.0")
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 24)
def Game_Win(x,y):   
    if segundos == 60:
        Win = pygame.font.Font('freesansbold.ttf', 40).render("Win", True, (255,255,255))
        Ventana.blit(Win, (x,y))
def retry(x,y):
    if vidas_valor == 0:
        Retry = pygame.font.Font('freesansbold.ttf', 25).render("Press P to Retry", True, (255,255,255))
        Ventana.blit(Retry, (x,y))
def cerrar(x,y):
    if vidas_valor == 0:
        cerrarprograma = pygame.font.Font('freesansbold.ttf', 25).render("Press ESC to close", True, (255,255,255))
        Ventana.blit(cerrarprograma, (x,y))
def Game_over(x,y):   
    if vidas_valor == 0:
        Game_over2 = pygame.font.Font('freesansbold.ttf', 40).render("Game Over", True, (255,255,255))
        Ventana.blit(Game_over2, (x,y))
def mostrarvidas(x,y):
    if vidas_valor>= 0:
        Vidas = font.render("Vidas :" + str(vidas_valor), True, (255,255,255))
        Ventana.blit(Vidas, (x,y))
    if vidas_valor <= 0:
        Vidas2 = font.render("Vidas : 0", True, (255,255,255))
        Ventana.blit(Vidas2, (x,y))
def mostrarpuntos(x,y):
    Puntaje = font.render("Puntaje :" + str(puntos), True, (255,255,255))
    Ventana.blit(Puntaje, (x,y))
#def mostrarvidasenemigo1(x,y):
 #   Vidasenemigo = font.render("Enemigo:" + str(Vidas_enemigo), True, (255,255,255))
  #  Ventana.blit(Vidasenemigo, (x,y))
def mostrarsegundos(x,y):
    segundos1 = font.render("Tiempo :" + str(segundos), True, (255,255,255))
    Ventana.blit(segundos1, (x,y))

        
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedY = 0
    def update(self):
        self.speedx = 0
        self.speedY = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        if keystate[pygame.K_DOWN]:
            self.speedY = 5
        if keystate[pygame.K_UP]:
            self.speedY = -5
        self.rect.x += self.speedx
        self.rect.bottom += self.speedY
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if  self.rect.top < 0:
           self.rect.top = 0
        if self.rect.bottom > 800:
            self.rect.bottom = 800


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("asteroid.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -32)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)
    
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -32)
            self.speedy = random.randrange(1, 8)
            self.speedx = random.randrange(-3, 3)
        if self.rect.right > WIDTH:
            self.speedy = random.randrange(-6, 8)
            self.speedx = random.randrange(-5, -3)
        if self.rect.top < 0 - 40:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -32)
            self.speedy = random.randrange(1, 8)
            self.speedx = random.randrange(-3, 3)
        if self.rect.right < 0:
            self.speedy = random.randrange(-6, 8)
            self.speedx = random.randrange(3, 5)





segundos = 0
Fondo = pygame.image.load("planeta1.jpg")
fondo_rect = Fondo.get_rect()
puntos = 0
vidas_valor = 3

Todo_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
jugador = Jugador()
Player = pygame.sprite.Group()
Player.add(jugador)
Todo_sprites.add(jugador)
for i in range(9):
    m = Mob() 
    Todo_sprites.add(m)
    mobs.add(m)

    #loop
abierto = True
while abierto:
        
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            abierto = False



        if vidas_valor <= 0:
            vidas_valor = 0
            jugador.speedx = 0
            jugador.speedY = 0
            segundos = 0
            jugador.rect.centerx = WIDTH / 2
            jugador.rect.bottom = HEIGHT - 10
            if event.key == pygame.K_p:
                    vidas_valor = 3
                    puntos = 0

                    jugador.speedx = 0
                    jugador.speedY = 0

            elif event.key == pygame.K_ESCAPE:
                abierto = False

  
              
        if segundos >= 60:
            segundos = 60
            puntos = (60* 5) + (vidas_valor* 5)   
            vidas_valor = vidas_valor
            mobs.empty()
            if event.key == pygame.K_ESCAPE:
                abierto = False
          

        

    Todo_sprites.update()
    haycolision = pygame.sprite.groupcollide(mobs,Player, True, False)
    for golpe in haycolision:
        m = Mob()
        Todo_sprites.add(m)
        mobs.add(m)
    if haycolision:
            vidas_valor -= 1

            


    if pygame.time.get_ticks() % 100 == 0:
            segundos += 20
            puntos = segundos * 5


            

                
    Ventana.fill(Black)
    Ventana.blit(Fondo, (0,0))
    mostrarvidas(10,776)
    mostrarpuntos(125,776)
    #mostrarvidasenemigo1(260,776)
    mostrarsegundos(420,776)
    Game_over(170, 360)
    retry(50, 520)
    cerrar(300,520)
    Game_Win(250, 360)
    Todo_sprites.draw(Ventana)
    pygame.display.flip()


pygame.quit() 

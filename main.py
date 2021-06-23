import pygame
from levels import Level
from window import Window
from entities.player import Player
from Sorting import *
import sys


def startGame(window, player, user):
    win = True
    players = ["moto.png", "jogging.png", "spaceship.png"]
    mobs = ["car.png", "medicine-ball.png", "asteroid.png"]
    backgrounds = ["calle3.jpg", "Cancha3.jpg", "planeta1.jpg"]
    player_name = user
    for i in range(0, 3):
        final = False
        if i == 2:
            final = True
        player.setImage(players[i])
        if not Level(player_name, window, player, backgrounds[i], mobs[i], final=final).start((2*i)+2, (2*i)+1):
            print("Lost")
            win = not win
            break

    if win:
        # Do the wining stuff

        with open("scores.txt", 'r+') as file:
            print("writing name and score to file...")
            file.write(player_name + " " + str(Level.points) + '\n')
            quick_score_sort("scores.txt")
        position = find_score_position(player_name)
        if position <= 7:
            Level.showTop7(150, 300, position)
         #automatically closes the file
        print("WIN")
    else:
        # Do the loosing stuff
        print("LOST")


def about(window):
    country = "Costa Rica"
    uni = "Instituto Tecnológico de Costa Rica."
    career = "Ingeniería en Computadores."
    course = "Taller de Programación, 2021, Grupo 3."
    prof = "Profesor Leonardo Araya."
    version = "Version 1.0.0."
    author = "Authors: Michael Marcía Suárez 2021138556"
    author2 = "Andrés Vásquez Hidalgo 2021527170."
    instruction = "Instructions: Use the arrow keys to move the player."
    ins2 = "dodge the enemies to survive the level."
    back = "Press 'ESC' to return to the main window."
    font = pygame.font.Font('freesansbold.ttf', 18)

    text1 = font.render(country, True, (255, 255, 255))  # blanco
    country_rect = text1.get_rect()
    country_rect = (5,20)

    text2 = font.render(uni, True, (255, 255, 255))  # blanco
    uni_rect = text2.get_rect()
    uni_rect = (5,40)

    text3 = font.render(career, True, (255, 255, 255))  # blanco
    career_rect = text3.get_rect()
    career_rect = (5,60)

    text4 = font.render(course, True, (255, 255, 255))  # blanco
    course_rect = text4.get_rect()
    course_rect = (5,80)

    text5 = font.render(prof, True, (255, 255, 255))  # blanco
    prof_rect = text5.get_rect()
    prof_rect = (5,100)

    text6 = font.render(version, True, (255, 255, 255))  # blanco
    version_rect = text6.get_rect()
    version_rect = (5,120)

    text7 = font.render(author, True, (255, 255, 255))  # blanco
    author_rect = text7.get_rect()
    author_rect = (5,140)
    text8 = font.render(author2, True, (255, 255, 255))  # blanco
    author2_rect = text7.get_rect()
    author2_rect = (5, 160)

    text9 = font.render(instruction, True, (255, 255, 255))  # blanco
    instructions_rect = text8.get_rect()
    instructions_rect = (5,180)
    text10 = font.render(ins2, True, (255, 255, 255))  # blanco
    ins2_rect = text8.get_rect()
    ins2_rect = (5, 200)

    text11 = font.render(back, True, (255, 255, 255))  # blanco
    back_rect = text9.get_rect()
    back_rect = (5,400)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        window.set_bg(pygame.image.load("images/home.jpg").convert())
        window.add_text(text1, country_rect)
        window.add_text(text2, uni_rect)
        window.add_text(text3, career_rect)
        window.add_text(text4, course_rect)
        window.add_text(text5, prof_rect)
        window.add_text(text6, version_rect)
        window.add_text(text7, author_rect)
        window.add_text(text8, author2_rect)
        window.add_text(text9, instructions_rect)
        window.add_text(text10, ins2_rect)
        window.add_text(text11, back_rect)
        pygame.display.update()


def top_scores(window):
    font = pygame.font.Font('freesansbold.ttf', 18)
    file = "scores.txt"
    quick_score_sort(file)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        window.set_bg(pygame.image.load("images/home.jpg").convert())
        opened_file = open(file, 'r')
        list = opened_file.readlines()
        opened_file.close()
        y_place = 20
        i = 0
        for line in list:
            if i < 7: #makes sure to only write the top 7 scores
                line.replace('\n','')
                text = font.render(line, True, (255, 255, 255))
                text_rect = (200, y_place)
                window.add_text(text, text_rect)
                y_place += 45
                i += 1

        pygame.display.update()



def main():
    window = Window()
    # Poner imagen del background y textos
    background = pygame.image.load("images/home.jpg").convert()
    disclaimer = "Please input a player name before starting"
    button_text = "Press 'SPACE' to start, '0' to go to about window."
    scores_text = "Press '9' to go to top scores"
    font = pygame.font.Font('freesansbold.ttf', 24)
    text = font.render(button_text, True, (255, 255, 255))  # blanco y negro
    t_rect = text.get_rect()
    t_rect.center = (300, 400)

    text2 = font.render(scores_text, True, (255, 255, 255))
    text2_rect = text2.get_rect()
    text2_rect.center = (300, 450)

    font = pygame.font.Font('freesansbold.ttf', 24)
    text3 = font.render(disclaimer, True, (255, 255, 255))  # blanco y negro
    dis_rect = text3.get_rect()
    dis_rect.center = (300, 50)

    # crear el text input para el nombre del jugador
    font_base = pygame.font.Font(None, 20)
    player_name = ''
    input_rect = pygame.Rect(250, 150, 100, 32)
    color_active = pygame.Color("lightskyblue3") #se activa cuando el usuario da click en la input box
    color_passive = pygame.Color("chartreuse4") #se usa como el color default de la input box

    color = color_passive

    active = False

    listening = True
    while listening:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_name != '':
                    listening = False
                    break
                if event.key == pygame.K_0:
                    player_name = ''
                    about(window)
                if event.key == pygame.K_9:
                    top_scores(window)
                    player_name = ''
                elif event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_BACKSPACE:
                    #obtener el input de 0 a -1 o el final.
                    player_name = player_name[:-1]
                else:
                    player_name += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
        if active:
            color = color_active
        else:
            color = color_passive

        #dibujar la input box
        pygame.draw.rect(window.getWindow(), color, input_rect)
        text_surface = font_base.render(player_name, True, (255, 255, 255))
        window.getWindow().blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        input_rect.w = max(100, text_surface.get_width()+10)
        pygame.display.flip()
        clock = pygame.time.Clock()
        clock.tick(60)
        window.set_bg(background)
        window.add_text(text, t_rect)
        window.add_text(text2, text2_rect)
        window.add_text(text3, dis_rect)
        #pygame.display.update()
        pygame.display.flip()
    player = Player(window)
    startGame(window, player, player_name)


if __name__ == '__main__':
    main()

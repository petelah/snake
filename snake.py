import pygame
import json
from datetime import datetime
from os import getcwd, path
from random import choice

from player_two import snake
from dot import dot
from pygame_textinput import *
from utils import load_hs, save_hs

# Init pygame
pygame.init()

# CONSTANTS
WIDTH = 500
HEIGHT = 550
font = pygame.font.SysFont('helvetica', 30, True)
hsfont = pygame.font.SysFont('helvetica', 45, True)

# Game clock
clock = pygame.time.Clock()

# Create TextInput-object
textinput = TextInput(text_color=(0,255,0), cursor_color=(0,255,0),
                      font_family="helvetica", font_size=45, max_string_length=5)

# Create screen
window = pygame.display.set_mode((WIDTH, HEIGHT))
# Sets caption for window
pygame.display.set_caption("Snake-lah")

# Init
snakey = snake(300, 410, 10, 10)
apple = dot(250, 250)
score = 0
speed = 1



def main_menu():

    # Menu bar location
    barXpos = 50
    barYpos = 230
    barLength = 115

    while True:
        window.fill((0, 0, 0))
        pygame.draw.rect(window, (0, 255, 0), (4, 55, 491, 490), 10)
        startText = font.render('START', 1, (0, 255, 0))
        window.blit(startText, (50, 200))
        exitText = font.render('EXIT', 1, (0, 255, 0))
        window.blit(exitText, (350, 200))
        pygame.draw.rect(window, (0, 255, 0), (barXpos, barYpos, barLength, 5))

        clock.tick(60)
        pygame.display.update()

        # Look for quit types
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            barXpos = 350
            barYpos = 230
            barLength = 80
        if keys[pygame.K_LEFT]:
            barXpos = 50
            barYpos = 230
            barLength = 115
        if keys[pygame.K_RETURN]:
            if barXpos == 50:
                main_game()
            if barXpos == 350:
                return False

def game_over(score):
    # Menu bar location
    barXpos = 50
    barYpos = 230
    barLength = 115
    run = True
    hs = {'PETE1': [60, '27.04.2020'], 'Marcy': [700, '20.04.2020']}
    show_text = True
    highscores = load_hs()
    highscores = {k: v for k, v in sorted(highscores.items(), key=lambda item: item[1], reverse=True)}

    while run:
        window.fill((0, 0, 0))
        pygame.draw.rect(window, (0, 255, 0), (4, 55, 491, 490), 10)
        goText = hsfont.render('HIGHSCORES', 1, (0, 255, 0))
        window.blit(goText, (75, 65))
        hsname = font.render('NAME', 1, (0, 255, 0))
        hslvl = font.render('LVL', 1, (0, 255, 0))
        hsdate = font.render('DATE', 1, (0, 255, 0))
        window.blit(hsname, (25, 120))
        window.blit(hsdate, (300, 120))
        window.blit(hslvl, (175, 120))
        error_border = (255,0,0)
        norm_border = (0,255,0)

        events = pygame.event.get()

        if show_text:
            pygame.draw.rect(window, (255, 0, 0), (25, 475, 450, 50), 5)
            # Feed it with events every frame
            textinput.update(events)
            # Blit its surface onto the screen
            window.blit(textinput.get_surface(), (30, 480))

        i = 0
        for k,v in highscores.items():
            name = font.render(f'{k}', 1, (0, 255, 0))
            nscore = font.render(f'{v[0]}', 1, (0, 255, 0))
            date = font.render(f'{v[1]}', 1, (0, 255, 0))
            window.blit(name, (25, 150+i))
            window.blit(nscore, (175, 150 + i))
            window.blit(date, (300, 150 + i))
            i += 25

        #pygame.draw.rect(window, (0, 255, 0), (barXpos, barYpos, barLength, 5))
        clock.tick(60)
        pygame.display.update()

        # Look for quit types
        for event in events:
            if event.type == pygame.QUIT:
                exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return False
        if keys[pygame.K_RETURN]:
            highscores[textinput.get_text()] = [f"{score}", f"{datetime.now().strftime('%d.%m.%Y')}"]
            save_hs(highscores)
            show_text = False

def main_game():
    run = True
    global score
    global speed
    tickspeed = 15
    while run:
        window.fill((0, 0, 0))
        scoreText = font.render('SCORE: ' + str(score), 1, (0, 255, 0))
        speedText = font.render('LEVEL: ' + str(speed), 1, (0, 255, 0))
        window.blit(scoreText, (250, 25))
        window.blit(speedText, (50, 25))

        snakey.draw(window)
        apple.draw(window)
        pygame.draw.rect(window, (0, 255, 0), (4, 55, 491, 490), 10)
        pygame.display.update()
        clock.tick(tickspeed)


        # Check score
        if score > 10:
            tickspeed = 20
            speed = 2
        elif score > 25:
            tickspeed = 25
            speed = 3
        elif score > 50:
            tickspeed = 30
            speed = 4

        # Look for quit types
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            score = 0
            snakey.length = [[300,410],[]]
            return False

        if keys[pygame.K_UP] and snakey.south == False:
            snakey.north = True
            snakey.south = False
            snakey.east = False
            snakey.west = False
        if keys[pygame.K_DOWN] and snakey.north == False:
            snakey.north = False
            snakey.south = True
            snakey.east = False
            snakey.west = False
        if keys[pygame.K_LEFT] and snakey.west == False:
            snakey.north = False
            snakey.south = False
            snakey.east = True
            snakey.west = False
        if keys[pygame.K_RIGHT] and snakey.east == False:
            snakey.north = False
            snakey.south = False
            snakey.east = False
            snakey.west = True

        # Check to see if the snake hits the side
        if snakey.length[0][0] == 0 or snakey.length[0][0] == 500 or \
                snakey.length[0][1] == 50 or snakey.length[0][1] == 550:
            #print('hit')
            snakey.length = [[300, 410], []]
            # goto gameover menu
            game_over(score)
            score = 0
            # return to main menu
            return False

        if (snakey.length[0][0], snakey.length[0][1]) == (apple.x, apple.y):
            # addTail
            snakey.addTail()
            apple.iseaten = True
            score += 1
            if apple.iseaten == True:
                x = apple.randspawn(snakey.length[0][0], snakey.length[0][1], snakey.length)
                #print(x)
                apple.x = x[0]
                apple.y = x[1]
                apple.draw(window)
        # Check to see if snake hit itself
        if len(snakey.length) > 3:
            if snakey.length[0] in snakey.length[2:]:
                # goto gameover menu
                game_over(score)
                score = 0
                # return to main menu
                return False




main_menu()

pygame.quit()

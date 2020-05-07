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
    barXpos = 200
    barYpos = 130
    barLength = 115

    # Dict of locations & current location
    menuLocs = {
        'START' : [200, 130, 115],
        'HIGHSCORES' : [150, 230, 230],
        'EXIT' : [220, 330, 80]
    }
    current_loc = 'START'

    while True:
        window.fill((0, 0, 0))
        pygame.draw.rect(window, (0, 255, 0), (4, 55, 491, 490), 10)
        startText = font.render('START', 1, (0, 255, 0))
        window.blit(startText, (200, 100))
        exitText = font.render('EXIT', 1, (0, 255, 0))
        window.blit(exitText, (220, 300))
        pygame.draw.rect(window, (0, 255, 0), (barXpos, barYpos, barLength, 5))
        highscoreText = font.render('HIGHSCORES', 1, (0, 255, 0))
        window.blit(highscoreText, (150, 200))
        pygame.draw.rect(window, (0, 255, 0), (barXpos, barYpos, barLength, 5))

        clock.tick(60)
        pygame.display.update()

        # Look for quit types
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            # Check for keyboard input when keydown
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if current_loc == 'START':
                        barXpos = menuLocs.get('HIGHSCORES')[0]
                        barYpos = menuLocs.get('HIGHSCORES')[1]
                        barLength = menuLocs.get('HIGHSCORES')[2]
                        current_loc = 'HIGHSCORES'
                    elif current_loc == 'HIGHSCORES':
                        barXpos = menuLocs.get('EXIT')[0]
                        barYpos = menuLocs.get('EXIT')[1]
                        barLength = menuLocs.get('EXIT')[2]
                        current_loc = 'EXIT'
                    elif current_loc == 'EXIT':
                        barXpos = menuLocs.get('EXIT')[0]
                        barYpos = menuLocs.get('EXIT')[1]
                        barLength = menuLocs.get('EXIT')[2]
                        current_loc = 'EXIT'
                elif event.key == pygame.K_UP:
                    if current_loc == 'START':
                        barXpos = menuLocs.get('START')[0]
                        barYpos = menuLocs.get('START')[1]
                        barLength = menuLocs.get('START')[2]
                        current_loc = 'START'
                    elif current_loc == 'HIGHSCORES':
                        barXpos = menuLocs.get('START')[0]
                        barYpos = menuLocs.get('START')[1]
                        barLength = menuLocs.get('START')[2]
                        current_loc = 'START'
                    elif current_loc == 'EXIT':
                        barXpos = menuLocs.get('HIGHSCORES')[0]
                        barYpos = menuLocs.get('HIGHSCORES')[1]
                        barLength = menuLocs.get('HIGHSCORES')[2]
                        current_loc = 'HIGHSCORES'
                elif event.key == pygame.K_RETURN:
                    if current_loc == 'START':
                        main_game()
                    elif current_loc == 'HIGHSCORES':
                        game_over(score, show_text=False)
                    else:
                        return False
                elif event.key == pygame.K_ESCAPE:
                    return False


def game_over(score, show_text):
    run = True
    show_text = show_text
    highscores = load_hs()

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

        keys = pygame.key.get_pressed()

        if show_text:
            pygame.draw.rect(window, (255, 0, 0), (25, 475, 450, 50), 5)
            # Feed it with events every frame
            textinput.update(events)
            # Blit its surface onto the screen
            window.blit(textinput.get_surface(), (30, 480))
            if keys[pygame.K_RETURN]:
                highscores[textinput.get_text()] = [f"{score}", f"{datetime.now().strftime('%d.%m.%Y')}"]
                save_hs(highscores)
                show_text = False

        i = 0
        for k, v in sorted(highscores.items(), key=lambda item: item[1], reverse=True)[:10]:
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

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
            game_over(score, show_text=True)
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
                game_over(score, show_text=True)
                score = 0
                # return to main menu
                return False

main_menu()

pygame.quit()

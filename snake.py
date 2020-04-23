import pygame
from random import choice

from player_two import snake
from dot import dot

# init pygame
pygame.init()

# CONSTANTS
WIDTH = 500
HEIGHT = 550
font = pygame.font.SysFont('helvetica', 30, True)

# game clock
clock = pygame.time.Clock()

# create screen
window = pygame.display.set_mode((WIDTH, HEIGHT))
# Sets caption for window
pygame.display.set_caption("Snake-lah")

def gameOver():
    go = True
    snakey.length = []
    while go:
        clock.tick(6)
        window.fill((0, 0, 0))
        if keys[pygame.K_SPACE]:
            print('continue')
            go = False
        if keys[pygame.K_ESCAPE]:
            run = False
        goText = font.render('GAME OVER', 1, (0, 255, 0))
        retryText = font.render('RETRY: SPACEBAR', 1, (0, 255, 0))
        quitText = font.render('QUIT: ESC', 1, (0, 255, 0))
        window.blit(goText, (250, 25))
        window.blit(retryText, (50, 25))
        window.blit(quitText, (50, 25))
        pygame.display.update()

# def gameReset():
#     global snakey = snake(300, 410, 10, 10)
#     global apple = dot(250, 250)
#     global score = 0
#     global speed = 1



def redrawGameWindow():
    window.fill((0, 0, 0))
    scoreText = font.render('SCORE: ' + str(score), 1, (0, 255, 0))
    speedText = font.render('SPEED: ' + str(speed), 1, (0, 255, 0))
    window.blit(scoreText, (250, 25))
    window.blit(speedText, (50, 25))
    snakey.draw(window)
    apple.draw(window)
    pygame.draw.rect(window, (0, 255, 0), (4, 55, 491, 490), 10)
    pygame.display.update()

run = True

snakey = snake(300, 410, 10, 10)
apple = dot(250, 250)
score = 0
speed = 1




while run:
    clock.tick(6)
    # look for quit types
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False


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
    if snakey.length[0][0] == 0 or snakey.length[0][0] == 500 or snakey.length[0][1] == 50 or snakey.length[0][1] == 550:
        print('hit')
        # gameReset()
    if (snakey.length[0][0], snakey.length[0][1]) == (apple.x, apple.y):
        # addTail
        snakey.addTail()
        apple.iseaten = True
        score += 1
        if apple.iseaten == True:
            x = apple.rando(snakey.length[0][0],snakey.length[0][1])
            print(x)
            apple.x = x[0]
            apple.y = x[1]
            apple.draw(window)
    redrawGameWindow()


pygame.quit()
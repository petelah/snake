import pygame
from random import choice

class dot(object):
    def __init__(self, x, y):
        self.x = choice(range(1, 45))*10
        self.y = choice(range(6, 54))*10
        self.width = 10
        self.height = 10
        self.isdrawn = True
        self.eaten = False

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, self.width, self.height))
        #print(f"x{self.x} y{self.y}")

    def randSpawn(coordList):
        xList = []
        yList = []
        for x in coordList:
            try:
                xList.append(x[0])
                yList.append(x[1])
            except IndexError:
                pass
        x = 11
        y = 11

        while str(x)[-1] != '0' and x not in xList:
            x = choice(range(1, 99))*10
        while str(y)[-1] != '0' and y not in yList:
            y = choice(range(6, 99))*10
        return [x, y]

    @staticmethod
    def rando(posx, posy):
        nx = posx
        ny = posy
        while nx == posx:
            nx = choice(range(1, 45)) * 10
        while ny == posy:
            ny = choice(range(6, 54)) * 10
        return nx, ny
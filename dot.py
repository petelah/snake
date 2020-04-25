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

    @staticmethod
    def randspawn(posx, posy, tail):
        nx = posx
        ny = posy
        while True:
            while nx == posx:
                nx = choice(range(1, 45)) * 10
            while ny == posy:
                ny = choice(range(6, 54)) * 10
            if [nx, ny] not in tail:
                break
        return nx, ny
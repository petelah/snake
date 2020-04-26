import pygame

class snake(object):
    def __init__(self, x, y, width, height):
        self.x = width
        self.y = height
        self.length = [[x,y],[]]
        self.north = True
        self.south = False
        self.east = False
        self.west = False
        self.vel = 10

    def draw(self, window):

        if self.north:
            self.length[0][1] -= self.vel
            self.length.insert(0,[self.length[0][0],self.length[0][1]])
            if len(self.length) > 1:
                self.length.pop(-1)
        elif self.south:
            self.length[0][1] += self.vel
            self.length.insert(0, [self.length[0][0], self.length[0][1]])
            self.length.pop(-1)
        elif self.east:
            self.length[0][0] -= self.vel
            self.length.insert(0, [self.length[0][0], self.length[0][1]])
            self.length.pop(-1)
        elif self.west:
            self.length[0][0] += self.vel
            self.length.insert(0, [self.length[0][0], self.length[0][1]])
            self.length.pop(-1)


        for vert in self.length:
            #
            pygame.draw.rect(window, (0,255,0), (vert[0],vert[1],self.x,self.y))



    def addTail(self):
        #add last position the head was minus the direction it was going

        self.length.append([])


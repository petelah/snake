import pygame

class snake(object):
    def __init__(self, x, y, width, height):
        self.x = width
        self.y = height
        self.posx = x
        self.posy = y
        self.tail = []
        self.north = True
        self.south = False
        self.east = False
        self.west = False
        self.vel = 10

    def draw(self, window):
        posx = self.posx
        posy = self.posy

        if self.north:
            self.posy -= self.vel
        elif self.south:
            self.posy += self.vel
        elif self.east:
            self.posx -= self.vel
        elif self.west:
            self.posx += self.vel
        pygame.draw.rect(window, (0, 255, 0), (self.posx, self.posy, self.x, self.y))



        #add for loop to draw tail





            # for vert in self.tail:
            #     pygame.draw.rect(window,(0,255,0),(vert[0],vert[1],self.x,self.y))

    def hit(self):
        pass

    def addTail(self):
        #add last position the head was minus the direction it was going

        posy = self.posy
        posx = self.posx
        if self.north:
            #self.posy -= 10
            posy += self.vel
        elif self.south:
            #self.posy += 10
            posy -= self.vel
        elif self.east:
            #self.posx -= 10
            posx += self.vel
        elif self.west:
            #self.posx += 10
            posx -= self.vel
        #self.tail.insert(0, [posx, posy])
        self.tail.append([])




        #move all pieces back one
        #if len(self.tail) > 1:


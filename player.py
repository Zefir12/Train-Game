from funkcje import *


class Player:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.startx = self.x
        self.starty = self.y
        self.offx = 0
        self.offy = 0
        self.id = id
        self.color = [90,20,5]
        self.size= size/3
        self.speed = 2
        self.leftblock = 1
        self.rightblock = 1
        self.upblock = 1
        self.downblock = 1


    def move(self):
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.startx -= self.speed*self.leftblock
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.startx += self.speed*self.rightblock
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.starty -= self.speed*self.upblock
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.starty += self.speed*self.downblock

    def update(self):
        self.x = self.startx + self.offx*2
        self.y = self.starty + self.offy*2

    def terrainblock(self):
        self.leftblock = 1
        self.rightblock = 1
        self.upblock = 1
        self.downblock = 1

    def draw(self):
        pygame.draw.rect(obraz, self.color, [self.x, self.y, self.size*2, self.size*2])
        pygame.draw.circle(obraz, [0,0,0], [int(self.x+self.size), int(self.y+self.size)], int(self.size))
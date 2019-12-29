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


    def move(self):
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.startx -= self.speed
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.startx += self.speed
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.starty -= self.speed
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.starty += self.speed

    def update(self):
        self.x = self.startx + self.offx*2
        self.y = self.starty + self.offy*2

    def draw(self):
        pygame.draw.circle(obraz, self.color, [int(self.x), int(self.y)], int(self.size))
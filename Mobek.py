from funkcje import *
import random
class Mobek():
    def __init__(self,x,y,id,speed=0,dmg=0,hp=100,look=0):
        self.x = x
        self.y = y
        self.startx = self.x
        self.starty = self.y
        self.offx = 0
        self.offy = 0
        self.speed = speed
        self.dmg = dmg
        self.hp = hp
        self.look = look
        self.id = id
        self.size = size/3
        self.move = random.randint(20,40)
        self.direction = random.randint(1,4)
        self.speed = 1
        self.hardMove = 0
        self.hardMoveSet = 2
    def update(self):
        self.x = self.startx + self.offx*2
        self.y = self.starty + self.offy*2
    def IA(self):
        self.move += self.hardMove
        if self.move != 0:
            if self.direction == 1:
                self.move -= 1
                self.startx -= self.speed
            if self.direction == 2:
                self.move -= 1
                self.starty -= self.speed
            if self.direction == 3:
                self.move -= 1
                self.startx += self.speed
            if self.direction == 4:
                self.move -= 1
                self.starty += self.speed
        else:
            self.move = random.randint(20, 100)
            self.direction = random.randint(1, 4)
    def draw(self):
            pygame.draw.circle(obraz, [0, 255, 0], [int(self.x), int(self.y)], int(self.size))
    def mapblock(self):
        if self.startx < 0 + size/3:
            self.startx += self.speed
        if self.startx > (wymiaryMapyx * size) - size/3:
            self.startx -= self.speed
        if self.starty < 0 + size/3:
            self.starty += self.speed
        if self.starty > (wymiaryMapyy * size) - size/3:
            self.starty -= self.speed
    def htiboxy(self, listaobiektow, rodzajterenu):
        for b in listaobiektow:
            if b.x - self.size < self.x - offpos[0] < b.x + b.size + self.size and b.y - self.size < self.y - offpos[1] < b.y + b.size + self.size:
                if b.terrain == rodzajterenu:
                    if self.x - offpos[0] + self.speed >= b.x:
                        self.startx += self.speed
                    if self.x - offpos[0] - self.speed <= b.x + b.size:
                        self.startx -= self.speed
                    if self.y - offpos[1] + self.speed >= b.y:
                        self.starty += self.speed
                    if self.y - offpos[1] - self.speed <= b.y + b.size:
                        self.starty -= self.speed

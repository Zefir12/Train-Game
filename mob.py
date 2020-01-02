from funkcje import *
import random

class Mob():
    def __init__(self, x, y, id, size, sizex, sizey,speed=0,dmg=1,hp=100,look=0):
        self.x = x
        self.y = y
        self.sizex = sizex
        self.sizey = sizey
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
        self.color = [0,255,0]
    def update(self):
        self.x = self.startx + self.offx*2
        self.y = self.starty + self.offy*2
    def AI(self):
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
            pygame.draw.circle(obraz, self.color, [int(self.x), int(self.y)], int(self.size))
    def mapblock(self):
        if self.startx < 0 + self.size:
            self.startx += self.speed
        if self.startx > (self.sizex * self.size*3) - self.size:
            self.startx -= self.speed
        if self.starty < 0 + self.size:
            self.starty += self.speed
        if self.starty > (self.sizey * self.size*3) - self.size:
            self.starty -= self.speed
    def hitboxy(self, listaobiektow, rodzajterenu):
        for b in listaobiektow:
            if b.x - self.size < self.x - self.offx < b.x + b.size + self.size and b.y - self.size < self.y - self.offy < b.y + b.size + self.size:
                if b.terrain == rodzajterenu:
                    if self.x - self.offx + self.speed >= b.x:
                        self.startx += self.speed
                    if self.x - self.offx - self.speed <= b.x + b.size:
                        self.startx -= self.speed
                    if self.y - self.offy + self.speed >= b.y:
                        self.starty += self.speed
                    if self.y - self.offy - self.speed <= b.y + b.size:
                        self.starty -= self.speed

    def hitV2(self,gracz):#,pozycjax, pozycjay, pozycjax2, pozycjay2, rozmiar):
        if (self.startx + self.size >= gracz.startx) and (self.startx - self.size <= gracz.startx) and (
                self.starty + self.size >= gracz.starty) and (self.starty - self.size <= gracz.starty):
            gracz.hp -= self.dmg
            self.color = [255, 0, 0]
        else:
            self.color = [0, 255, 0]
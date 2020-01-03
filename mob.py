from funkcje import *
import random

class Mob():
    def __init__(self, x, y, id, size, sizex, sizey,speed=1,dmg=1,hp=100,look=0):
        self.x = x
        self.y = y
        self.sizex = sizex
        self.sizey = sizey
        self.startx = self.x
        self.starty = self.y
        self.offx = 0
        self.offy = 0
        self.dmg = dmg
        self.hp = hp
        self.look = look
        self.id = id
        self.size = size/3
        self.speed = speed
        self.sleepColor = [0, 51, 0]
        self.attackColor = [0, 255, 0]
        self.triggeredColor = [0, 153, 0]
        self.color = self.sleepColor
        self.timeToMove = random.randint(60,120)
        self.distance = random.randint(30,60)
        self.direction = random.randint(0,3)
        self.range = 200

    def update(self):
        self.x = self.startx + self.offx*2
        self.y = self.starty + self.offy*2

    def AI(self, x, y):
        playerPos = abs(x) + abs(y)
        mobPos = abs(self.startx) + abs(self.starty)
        if mobPos - playerPos <= self.range and playerPos - mobPos <= self.range:
            self.timeToMove = random.randint(60,120)
            self.color = self.attackColor
            self.range = 300
            if x > self.startx:
                self.startx += self.speed
            elif x < self.startx:
                self.startx -= self.speed
            if y > self.starty:
                self.starty += self.speed
            elif y < self.starty:
                self.starty -= self.speed
        else:
            if self.color == self.attackColor:
                self.color = self.triggeredColor
            if self.timeToMove == 0:
                self.range = 200
                self.color = self.sleepColor
                if self.distance != 0:
                    if self.direction == 0:
                        self.startx += self.speed
                    elif self.direction == 1:
                        self.starty += self.speed
                    elif self.direction == 2:
                        self.startx -= self.speed
                    else:
                        self.starty -=self.speed
                    self.distance -= 1
                else:
                    self.distance = random.randint(30,60)
                    self.direction = random.randint(0,3)
                    self.timeToMove = random.randint(60,120)
            else:
                self.timeToMove -= 1

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

    def hitV2(self,x,y):
        if (self.startx + self.size * 2 >= x) and (self.startx - self.size * 2 <= x) and (
                self.starty + self.size * 2 >= y) and (self.starty - self.size * 2 <= y):
            return self.dmg
        else:
            return 0
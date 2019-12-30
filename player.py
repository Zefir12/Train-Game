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
        self.color = [90, 20, 5]
        self.size = size/3
        self.speed = 2
        self.leftblock = 1
        self.rightblock = 1
        self.upblock = 1
        self.downblock = 1
        self.kierunek = 0
        self.hand = (0, 0)
        self.eq = []
        self.wielkoscEQ = 10
        for i in range(10):
            self.eq.append(0)

    def move(self):
        if pygame.key.get_pressed()[pygame.K_a]:
            self.startx -= self.speed*self.leftblock
            self.kierunek = 0
        if pygame.key.get_pressed()[pygame.K_d]:
            self.startx += self.speed*self.rightblock
            self.kierunek = 1
        if pygame.key.get_pressed()[pygame.K_w]:
            self.starty -= self.speed*self.upblock
            self.kierunek = 2
        if pygame.key.get_pressed()[pygame.K_s]:
            self.starty += self.speed*self.downblock
            self.kierunek = 3

    def update(self):
        self.x = self.startx + self.offx*2
        self.y = self.starty + self.offy*2

    def drawHand(self):
        pygame.draw.circle(obraz,[255,0,0], [int(self.hand[0]), int(self.hand[1])], int(self.size/3))

    def setHand(self, rodzajchodzenia):
        if self.kierunek == 0:
            self.hand = (self.x + self.size*rodzajchodzenia - self.size*2, self.y + self.size*rodzajchodzenia)
        if self.kierunek == 1:
            self.hand = (self.x + self.size*rodzajchodzenia + self.size*2, self.y + self.size*rodzajchodzenia)
        if self.kierunek == 2:
            self.hand = (self.x + self.size*rodzajchodzenia, self.y + self.size*rodzajchodzenia - self.size * 2)
        if self.kierunek == 3:
            self.hand = (self.x + self.size*rodzajchodzenia, self.y + self.size*rodzajchodzenia + self.size * 2)

    def handWorking(self,listaobiektow):
        for b in listaobiektow:
            if b.terrain != 1:
                if b.x < self.hand[0] - offpos[0] < b.x + b.size and b.y < self.hand[1] - offpos[1] < b.y + b.size:
                    b.znieszczenie += 1
                    if b.znieszczenie == 120:
                        if b.terrain == 2:
                            self.eq[0] += 1
                        if b.terrain == 4:
                            self.eq[1] += 1
                        b.terrain = 1




    def terrainblock(self):
        self.leftblock = 1
        self.rightblock = 1
        self.upblock = 1
        self.downblock = 1

    def mapblock(self):
        if self.startx < 0 + size/3:
            self.startx += self.speed
        if self.startx > (wymiaryMapyx * size) - size/3:
            self.startx -= self.speed
        if self.starty < 0 + size/3:
            self.starty += self.speed
        if self.starty > (wymiaryMapyy * size) - size/3:
            self.starty -= self.speed

    def mapblock2(self):
        if self.startx < 0:
            self.startx += self.speed
        if self.startx > (wymiaryMapyx * size) - self.size*2:
            self.startx -= self.speed
        if self.starty < 0:
            self.starty += self.speed
        if self.starty > (wymiaryMapyy * size) - self.size*2:
            self.starty -= self.speed

    def htiboxy(self, listaobiektow, rodzajterenu):
        for b in listaobiektow:
            if b.x - self.size < self.x - offpos[0] < b.x + b.size + self.size and b.y - self.size < self.y - offpos[1] < b.y + b.size + self.size:
                if b.terrain == rodzajterenu:
                    if (self.x - offpos[0] + self.speed >= b.x):
                        self.startx += self.speed
                    if (self.x - offpos[0] - self.speed <= b.x + b.size):
                        self.startx -= self.speed
                    if (self.y - offpos[1] + self.speed >= b.y):
                        self.starty += self.speed
                    if (self.y - offpos[1] - self.speed <= b.y + b.size):
                        self.starty -= self.speed

    def hitboxy2(self, listaobiektow, rodzajterenu):
        leftTopTop = False
        leftTopLeft = False
        rightTopTop = False
        rightTopRight = False
        rightBotRight = False
        rightBotBot = False
        leftBotBot = False
        leftBotLeft = False

        for b in listaobiektow:
            if b.terrain == rodzajterenu:
                if b.x < self.x - offpos[0] - 1 < b.x + b.size and b.y < self.y - offpos[1] + 1 < b.y + b.size:
                    leftTopLeft = True
                if b.x < self.x - offpos[0] + 1 < b.x + b.size and b.y < self.y - offpos[1] - 1 < b.y + b.size:
                    leftTopTop = True
                if b.x < self.x + self.size * 2 - offpos[0] - 1 < b.x + b.size and b.y < self.y - offpos[
                    1] - 1 < b.y + b.size:
                    rightTopTop = True
                if b.x < self.x + self.size * 2 - offpos[0] + 1 < b.x + b.size and b.y < self.y - offpos[
                    1] + 1 < b.y + b.size:
                    rightTopRight = True
                if b.x < self.x + self.size * 2 - offpos[
                    0] + 1 < b.x + b.size and b.y < self.y + self.size * 2 - offpos[1] - 1 < b.y + b.size:
                    rightBotRight = True
                if b.x < self.x + self.size * 2 - offpos[
                    0] - 1 < b.x + b.size and b.y < self.y + self.size * 2 - offpos[1] + 1 < b.y + b.size:
                    rightBotBot = True
                if b.x < self.x - offpos[0] + 1 < b.x + b.size and b.y < self.y + self.size * 2 - offpos[
                    1] + 1 < b.y + b.size:
                    leftBotBot = True
                if b.x < self.x - offpos[0] - 1 < b.x + b.size and b.y < self.y + self.size * 2 - offpos[
                    1] - 1 < b.y + b.size:
                    leftBotLeft = True

        self.leftblock = 1
        self.upblock = 1
        self.rightblock = 1
        self.downblock = 1
        if leftTopTop and leftTopLeft:
            self.leftblock = 0
            self.upblock = 0
        elif rightTopTop and rightTopRight:
            self.upblock = 0
            self.rightblock = 0
        elif rightBotBot and rightBotRight:
            self.rightblock = 0
            self.downblock = 0
        elif leftBotBot and leftBotLeft:
            self.downblock = 0
            self.leftblock = 0
        elif leftTopTop or rightTopTop:
            self.upblock = 0
        elif rightTopRight or rightBotRight:
            self.rightblock = 0
        elif rightBotBot or leftBotBot:
            self.downblock = 0
        elif leftBotLeft or leftTopLeft:
            self.leftblock = 0

    def draw(self):
        if chodzenie == 0:
            pygame.draw.circle(obraz, [0, 0, 0], [int(self.x), int(self.y)], int(self.size))
        else:
            pygame.draw.rect(obraz, self.color, [self.x, self.y, self.size*2, self.size*2])

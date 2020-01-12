from funkcje import *

class Arrow:
    def __init__(self, id, x, y, directionx, directiony, pointx, pointy, velocity):
        self.id = id
        self.color = [0, 0, 250]
        self.x = x
        self.y = y
        self.radius = 6
        self.directionx = directionx
        self.directiony = directiony
        self.startx = self.x
        self.starty = self.y
        self.offx = 0
        self.offy = 0
        self.offxP = 0
        self.offyP = 0
        self.exist = 1
        self.listpositions = []
        self.direction = [x - pointx, y - pointy]
        self.velocity = velocity


        sum = abs(self.directionx) + abs(self.directiony)
        if sum != 0:
            self.vx = (self.directionx / sum)
            self.vy = (self.directiony / sum)
            if self.vx > 0.8:
                self.vx = 0.8
            if self.vy > 0.8:
                self.vy = 0.8
            if self.vx < -0.8:
                self.vx = -0.8
            if self.vy < -0.8:
                self.vy = -0.8
            self.vx *= self.velocity
            self.vy *= self.velocity
        else:
            self.vx = 0
            self.vy = 0

    def update(self):
        self.startx += self.vx
        self.starty += self.vy
        self.x = self.startx + self.offx*2
        self.y = self.starty + self.offy*2

    def draw(self):
        pygame.draw.circle(obraz, self.color, [int(self.x), int(self.y)], int(self.radius))

    def colision(self, listblocks, listzombies):
        for b in listzombies:
            if ((b.x - self.x)**2 + (b.y - self.y)**2)**0.5 < (b.size + self.radius):
                b.startx += self.vx/100
                b.starty += self.vy/100
                b.hp -= 20
                self.exist = 0

    def aftereffects(self):
        self.listpositions.append((self.x, self.y))
        if len(self.listpositions) > 7:
            pygame.draw.circle(obraz, [100, 0, 0], [int(self.listpositions[len(self.listpositions) - 2][0]), int(self.listpositions[len(self.listpositions) - 2][1])], int(self.radius * 0.9))
            pygame.draw.circle(obraz, [120, 0, 0], [int(self.listpositions[len(self.listpositions) - 3][0]), int(self.listpositions[len(self.listpositions) - 3][1])], int(self.radius * 0.8))
            pygame.draw.circle(obraz, [150, 0, 0], [int(self.listpositions[len(self.listpositions) - 4][0]), int(self.listpositions[len(self.listpositions) - 4][1])], int(self.radius * 0.7))
            pygame.draw.circle(obraz, [180, 0, 0], [int(self.listpositions[len(self.listpositions) - 5][0]), int(self.listpositions[len(self.listpositions) - 5][1])], int(self.radius * 0.6))
            pygame.draw.circle(obraz, [210, 0, 0], [int(self.listpositions[len(self.listpositions) - 6][0]), int(self.listpositions[len(self.listpositions) - 6][1])], int(self.radius * 0.5))
            pygame.draw.circle(obraz, [230, 0, 0], [int(self.listpositions[len(self.listpositions) - 7][0]), int(self.listpositions[len(self.listpositions) - 7][1])], int(self.radius * 0.4))

    def drawLine(self):
        self.listpositions.append((self.x, self.y))
        if len(self.listpositions) > 5:
            pygame.draw.line(obraz, [180, 0, 0], [int(self.listpositions[len(self.listpositions) - 5][0]), int(self.listpositions[len(self.listpositions) - 5][1])], [int(self.x), int(self.y)],4)

    def drawLineVector(self):
        pygame.draw.line(obraz, [180, 0, 0], [self.x, self.y], [], 4)
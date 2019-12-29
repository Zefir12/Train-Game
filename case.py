from funkcje import *

class Case:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id
        self.startx = self.x
        self.starty = self.y
        self.offx = 0
        self.offy = 0
        self.color = [0,0,0]
        self.size = size
        self.terrain = 0



    def update(self):
        self.x = self.startx + self.offx
        self.y = self.starty + self.offy

    def drawHighlight(self):
        pygame.draw.rect(obraz, [0, 40, 100], [self.x + self.offx, self.y + self.offy, self.size, self.size],6)

    def drawTerrain(self):
        if self.terrain == 1:
            pygame.draw.rect(obraz, [0, 90, 0], [self.x + self.offx, self.y+self.offy, self.size, self.size])
        elif self.terrain == 2:
            pygame.draw.rect(obraz, [40, 0, 10], [self.x+ self.offx, self.y+self.offy, self.size, self.size])

    def drawCase(self):
        pygame.draw.rect(obraz, self.color, [self.x + self.offx, self.y+self.offy, self.size, self.size], 1)

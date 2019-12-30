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
        self.colorgreen = [0,90,0]
        self.size = size
        self.terrain = 0

    def update(self):
        self.x = self.startx + self.offx
        self.y = self.starty + self.offy

    def drawHighlight(self, r, g, b):
        pygame.draw.rect(obraz, [r, g, b], [self.x + self.offx, self.y + self.offy, self.size, self.size],6)

    def xd3d(self,x,y):
        if self.terrain != 0:
            #pygame.draw.rect(obraz, self.color, [self.x + self.offx + x, self.y + self.offy + y, self.size, self.size])
            pygame.draw.polygon(obraz, [90,90,90], [(self.x + self.offx, self.y+self.offy+self.size), (self.x+self.offx+x, self.y + self.offy + y+self.size), (self.x + self.offx + x + self.size,self.y + self.offy + y+self.size), (self.x + self.offx + self.size, self.y+self.offy+self.size)])
            pygame.draw.polygon(obraz, [100,100,100], [(self.x+self.offx+x, self.y + self.offy + y), (self.x+self.offx+x, self.y + self.offy + y + size), (self.x+self.offx, self.y + self.offy + self.size), (self.x + self.offx, self.y+self.offy)])



    def drawUnder(self):
        if self.terrain == 1:
            pygame.draw.circle(obraz, [0, 90, 0], [int(self.x + size / 2 + self.offx), int(self.y + size / 2 + self.offy)],
                               int(size))

    def drawTerrain(self):
        if self.terrain == 1:
            pygame.draw.rect(obraz, self.colorgreen, [self.x + self.offx, self.y+self.offy, self.size, self.size])
        elif self.terrain == 2:
            pygame.draw.rect(obraz, [40, 0, 10], [self.x + self.offx, self.y+self.offy, self.size, self.size])
        elif self.terrain == 3: #
            pygame.draw.rect(obraz, [0, 100, 100], [self.x + self.offx, self.y+self.offy, self.size, self.size])


    def drawCase(self):
        if self.terrain != 0:
            pygame.draw.rect(obraz, self.color, [self.x + self.offx, self.y+self.offy, self.size, self.size], 1)

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
        self.color = [0, 0, 0]
        self.colorgreen = [0, 90, 0]
        self.colordarkgreen = [0, 50, 0]
        self.colorgray = [96,96,96]
        self.colorblue = [0,226,255]
        self.size = size
        self.terrain = 0
        self.shade1 = False
        self.shade2 = False
        self.caseNeighbours = [None, None, None, None]
        self.durability = 0

    def update(self):
        self.x = self.startx + self.offx
        self.y = self.starty + self.offy

    def drawHighlight(self, r, g, b):
        pygame.draw.rect(obraz, [r, g, b], [self.x + self.offx, self.y + self.offy, self.size, self.size],6)

    def xd3d(self,x,y):
        if self.shade1:
            pygame.draw.polygon(obraz, [70, 70, 70], [(self.x + self.offx, self.y+self.offy+self.size), (self.x+self.offx+x, self.y + self.offy + y+self.size), (self.x + self.offx + x + self.size,self.y + self.offy + y+self.size), (self.x + self.offx + self.size, self.y+self.offy+self.size)])
        if self.shade2:
            pygame.draw.polygon(obraz, [100, 100, 100], [(self.x+self.offx+x, self.y + self.offy + y), (self.x+self.offx+x, self.y + self.offy + y + size), (self.x+self.offx, self.y + self.offy + self.size), (self.x + self.offx, self.y+self.offy)])

    def drawTerrain(self):
        if self.terrain == 1:
            pygame.draw.rect(obraz, self.colorgreen, [self.x + self.offx, self.y+self.offy, self.size, self.size])
        elif self.terrain == 2:
            pygame.draw.rect(obraz, self.colorgray, [self.x + self.offx, self.y+self.offy, self.size, self.size])
        elif self.terrain == 3:
            pygame.draw.rect(obraz, self.colorblue, [self.x + self.offx, self.y+self.offy, self.size, self.size])
        elif self.terrain == 4:
            pygame.draw.rect(obraz, self.colordarkgreen, [self.x + self.offx, self.y+self.offy, self.size, self.size])
        if watereffects:
            obraz.blit(water, [self.x + self.offx, self.y+self.offy, self.size, self.size])

    def drawCase(self):
        if self.terrain != 0:
            pygame.draw.rect(obraz, self.color, [self.x + self.offx, self.y+self.offy, self.size, self.size], 1)

    def drawId(self):
        napisy(self.id, self.x + offpos[0] + self.size/2, self.y + offpos[1] + self.size/2, 1)

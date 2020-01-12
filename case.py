from funkcje import *
from items import Item

class Case:
    def __init__(self, x, y, id, size):
        self.x = x
        self.y = y
        self.id = id
        self.startx = self.x
        self.starty = self.y
        self.offx = 0
        self.offy = 0
        self.coloroffset = [0, 0, 0]
        self.color = [0, 0, 0]
        self.colorgreen = [0, 90, 0]
        self.colordarkgreen = [0, 50, 0]
        self.colorgray = [96,96,96]
        self.colorblue = [0,226,255]
        self.colorbrown = [165,42,42]
        self.size = size
        self.terrain = 0
        self.shade1 = False
        self.shade2 = False
        self.shade3 = False
        self.shade4 = False
        self.caseNeighbours = [None, None, None, None]
        self.durability = 0
        self.chunk = None
        self.durability = 5
        self.destruction = 100
        self.item = None


    def update(self):
        self.x = self.startx + self.offx
        self.y = self.starty + self.offy
        if self.destruction < 1:
            if self.terrain == 4:
                self.terrain = 1
                self.item = Item(3)


    def drawHighlight(self, r, g, b, x, y, thickness):
        pygame.draw.rect(obraz, [r, g, b], [self.x + self.offx, self.y + self.offy, self.size, self.size], thickness)
        if Settings.sztuczne3d:
            if self.shade1:
                if y > 0:
                    pygame.draw.polygon(obraz, [r, g, b], [(self.x + self.offx, self.y + self.offy + self.size),
                                                              (self.x + self.offx + x, self.y + self.offy + y + self.size), (
                                                              self.x + self.offx + x + self.size,
                                                              self.y + self.offy + y + self.size),
                                                              (self.x + self.offx + self.size, self.y + self.offy + self.size)], thickness)
            if self.shade2:
                if x < 0:
                    pygame.draw.polygon(obraz, [r, g, b], [(self.x + self.offx + x, self.y + self.offy + y),
                                                                 (self.x + self.offx + x, self.y + self.offy + y + self.size),
                                                                 (self.x + self.offx, self.y + self.offy + self.size),
                                                                 (self.x + self.offx, self.y + self.offy)], thickness)
            if self.shade3:
                if y < 0:
                    pygame.draw.polygon(obraz, [r, g, b], [(self.x + self.offx, self.y + self.offy), (self.x+self.offx + x, self.y + self.offy + y), (self.x + self.offx  + self.size + x, self.y + self.offy + y), (self.x + self.offx  + self.size, self.y + self.offy)], thickness)
            if self.shade4:
                if x > 0:
                    pygame.draw.polygon(obraz, [r, g, b], [(self.x + self.offx + self.size, self.y + self.offy + self.size), (self.x + self.offx + self.size + x, self.y + self.offy + self.size + y), (self.x + self.offx + self.size + x, self.y+self.offy + y), (self.x + self.offx + self.size, self.y + self.offy)], thickness)


    def xd3d(self, x, y, coloroffset):
        if self.shade1:
            if y > 0:
                pygame.draw.polygon(obraz, [70 + int(70 * coloroffset[0]), 70 + int(70 * coloroffset[1]), 70 + int(70 * coloroffset[2])], [(self.x + self.offx, self.y + self.offy + self.size), (self.x+self.offx + x, self.y + self.offy + y + self.size), (self.x + self.offx + x + self.size,self.y + self.offy + y+self.size), (self.x + self.offx + self.size, self.y+self.offy+self.size)])
        if self.shade2:
            if x < 0:
                pygame.draw.polygon(obraz, [130 + int(130 * coloroffset[0]), 130 + int(130 * coloroffset[1]), 130 + int(130 * coloroffset[2])], [(self.x + self.offx + x, self.y + self.offy + y), (self.x+self.offx + x, self.y + self.offy + y + self.size), (self.x + self.offx, self.y + self.offy + self.size), (self.x + self.offx, self.y+self.offy)])
        if self.shade4:
            if x > 0:
                pygame.draw.polygon(obraz, [20 + int(20 * coloroffset[0]), 20 + int(20 * coloroffset[1]), 20 + int(20 * coloroffset[2])], [(self.x + self.offx + self.size, self.y + self.offy + self.size), (self.x + self.offx + self.size + x, self.y + self.offy + self.size + y), (self.x + self.offx + self.size + x, self.y+self.offy + y), (self.x + self.offx + self.size, self.y + self.offy)])
        if self.shade3:
            if y < 0:
                pygame.draw.polygon(obraz, [70 + int(70 * coloroffset[0]), 70 + int(70 * coloroffset[1]), 70 + int(70 * coloroffset[2])], [(self.x + self.offx, self.y + self.offy), (self.x+self.offx + x, self.y + self.offy + y), (self.x + self.offx  + self.size + x, self.y + self.offy + y), (self.x + self.offx  + self.size, self.y + self.offy)])

    def drawTerrain(self, coloroffset):
        if self.terrain == 1:
            self.color = self.colorgreen
        elif self.terrain == 2:
            self.color = self.colorgray
        elif self.terrain == 3:
            self.color = self.colorblue
        elif self.terrain == 4:
            self.color = self.colordarkgreen
        elif self.terrain == 5:
            self.color = self.colorbrown
        if self.terrain != 0:
            pygame.draw.rect(obraz, [self.color[0] + int(self.color[0] * coloroffset[0]), self.color[1] + int(self.color[1] * coloroffset[1]), self.color[2] + int(self.color[2] * coloroffset[2])], [self.x + self.offx, self.y + self.offy, self.size, self.size])
        if Settings.watereffects:
            obraz.blit(water, [self.x + self.offx, self.y+self.offy, self.size, self.size])

    def drawItems(self, coloroffset):
        if self.item is not None:
            pygame.draw.rect(obraz, [self.item.color[0] + int(self.item.color[0] * coloroffset[0]), self.item.color[1] + int(self.item.color[1] * coloroffset[1]), self.item.color[2] + int(self.item.color[2] * coloroffset[2])], [self.x + self.offx + self.size/4, self.y + self.offy + self.size/4, self.size/2, self.size/2])


    def drawCase(self):
        if self.terrain != 0:
            pygame.draw.rect(obraz, self.color, [self.x + self.offx, self.y+self.offy, self.size, self.size], 1)

    def drawDestruction(self):
        if self.destruction < 100:
            pygame.draw.rect(obraz, [200-self.destruction, 0, 0], [self.x + self.offx, self.y + self.offy, self.size, self.size], int((100 - self.destruction)/10))

    def drawId(self):
        napisy(self.id, self.x + Settings.offpos[0] + self.size/2, self.y + Settings.offpos[1] + self.size/2, 1)

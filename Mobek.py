from funkcje import *

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
    def update(self):
        self.x = self.startx + self.offx*2
        self.y = self.starty + self.offy*2
    def draw(self):
            pygame.draw.circle(obraz, [0, 255, 0], [int(self.x), int(self.y)], int(self.size))
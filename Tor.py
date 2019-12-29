class tor:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.id = id
        self.color = [255,0,0]
    def draw(self):
        pygame.draw.circle(obraz, self.color, [int(self.x), int(self.y)], int(self.size))


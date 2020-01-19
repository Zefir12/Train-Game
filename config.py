# Settigns
class Settings:
    def __init__(self):
        self.szerokoscOkna = 1600
        self.wysokoscOkna = 900
        self.offpos = [0, 0]
        self.chodzenie = 0
        self.drawterrain = True
        self.szachownica = False
        self.sztuczne3d = True
        self.showId = False
        self.showidNeighbours = False
        self.watereffects = False
        self.drawChunkBorders = False
        self.cameraspeed = 20
        self.shadowDepth = 9
        self.freecamera = False
        self.timespeed = 0.004



        ######potrzebne mi do menu, nie ruszać xd!
        self.offsetstartingmenux = (self.szerokoscOkna - 1920)/2
        self.offsetstartingmenuy = (self.wysokoscOkna - 900)/2
        self.offsetmenux = 0
        self.offsetmenuy = 0
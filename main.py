from funkcje import *
from case import Case
from player import Player
import pickle


with open('mapa.txt', 'rb') as obiekt:
    listMapy = pickle.load(obiekt)

maciek = Player(size/2, size/2, 0)


def main(Run,offpos):
    while Run:
        mouse = pygame.mouse.get_pos()
        redraw_game(80, 80, 80)
        offpos[0], offpos[1] = moving(offpos[0], offpos[1], 3)

        for b in listMapy:
            b.offx, b.offy = offpos[0], offpos[1]
            b.update()
            b.drawTerrain()
            b.drawCase()

        for b in listMapy:
            if b.x < mouse[0] - offpos[0] < b.x + b.size and b.y < mouse[1] - offpos[1] < b.y + b.size:
                b.drawHighlight()

        maciek.offx, maciek.offy = offpos[0], offpos[1]
        maciek.move()
        maciek.update()
        maciek.draw()

        for b in listMapy:
            if b.x - size/3 < maciek.x - offpos[0] and b.terrain == 0 and b.y - size/3 < maciek.y - offpos[1] or b.x + size/3 > maciek.x - offpos[0] and b.y + size/3 > maciek.y - offpos[1]:
                b.drawHighlight()






        off()





main(True, offpos)
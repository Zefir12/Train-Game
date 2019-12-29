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

        if maciek.x < size*4:
            offpos[0] += 1
            maciek.x += 1
        if maciek.x > szerokoscOkna - size*4:
            offpos[0] -= 1
            maciek.x -= 1
        if maciek.y < size*4:
            offpos[1] += 1
            maciek.y += 1
        if maciek.y > wysokoscOkna - size*4:
            offpos[1] -= 1
            maciek.y -= 1

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
        maciek.terrainblock()
        maciek.draw()


        for b in listMapy:
            if b.x - maciek.size < maciek.x - offpos[0] < b.x + b.size + maciek.size and b.y - maciek.size < maciek.y - offpos[1] < b.y + b.size + maciek.size:
                if b.terrain == 0:

                    if b.x + size/2 - maciek.x < 0:
                        maciek.leftblock = 0
                    if b.x + size/2 - maciek.x > 0:
                        maciek.rightblock = 0
                    if b.y + size/2 - maciek.y < 0:
                        maciek.upblock = 0
                    if b.y + size/2 - maciek.y > 0:
                        maciek.downblock = 0



                    b.drawHighlight()






        off()





main(True, offpos)
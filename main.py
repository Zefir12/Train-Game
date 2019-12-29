from funkcje import *
from case import Case
from player import Player
import pickle


with open('mapa.txt', 'rb') as obiekt:
    listMapy = pickle.load(obiekt)


maciek = Player(size/2, size/2, 0)
for b in listMapy:
    if b.x < maciek.x - offpos[0] < b.x + b.size and b.y < maciek.y - offpos[1] < b.y + b.size:
        b.terrain = 1


def main(Run,offpos):
    i = 0
    while Run:
        mouse = pygame.mouse.get_pos()
        i += 1
        if i > 250:
            i = 0
        redraw_game(i, 80, 80)
        offpos[0], offpos[1] = moving(offpos[0], offpos[1], 3)

        if maciek.x < size*8:
            offpos[0] += 1
            maciek.x += 1
        if maciek.x > szerokoscOkna - size*8:
            offpos[0] -= 1
            maciek.x -= 1
        if maciek.y < size*8:
            offpos[1] += 1
            maciek.y += 1
        if maciek.y > wysokoscOkna - size*8:
            offpos[1] -= 1
            maciek.y -= 1

        for b in listMapy:
            b.offx, b.offy = offpos[0], offpos[1]
            b.update()
            b.drawTerrain()
            b.drawCase()

        for b in listMapy:
            if b.x < mouse[0] - offpos[0] < b.x + b.size and b.y < mouse[1] - offpos[1] < b.y + b.size:
                b.drawHighlight(0, 40, 100)

        maciek.offx, maciek.offy = offpos[0], offpos[1]
        maciek.move()
        maciek.update()
        maciek.terrainblock()
        if chodzenie == 0:
            maciek.mapblock()
            maciek.htiboxy(listMapy)
        else:
            maciek.mapblock2()
            maciek.hitboxy2(listMapy)
        maciek.draw()


        off()





main(True, offpos)
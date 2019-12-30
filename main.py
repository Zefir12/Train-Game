from funkcje import *
from case import Case
from player import Player
import pickle


with open('mapa.txt', 'rb') as obiekt:
    listMapy = pickle.load(obiekt)


maciek = Player(size/2, wymiaryMapyy*size - size/2, 0)
for b in listMapy:
    if b.x < maciek.x - offpos[0] < b.x + b.size and b.y < maciek.y - offpos[1] < b.y + b.size:
        b.terrain = 1


def main(Run,offpos):
    while Run:
        mouse = pygame.mouse.get_pos()
        redraw_game(0, 20, 80)
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


        for b in listMapy:
            if zaokraglanie:
                b.drawUnder()
            if sztuczne3d:
                b.xd3d(-20, 40)


        for b in listMapy:
            b.drawTerrain()
            if szachownica:
                b.drawCase()

        for b in listMapy:
            if b.x < mouse[0] - offpos[0] < b.x + b.size and b.y < mouse[1] - offpos[1] < b.y + b.size:
                b.drawHighlight(0, 40, 100)

        maciek.offx, maciek.offy = offpos[0], offpos[1]
        maciek.move()
        maciek.update()
        maciek.setHand(chodzenie)
        maciek.drawHand()
        maciek.terrainblock()
        maciek.handWorking(listMapy)
        if chodzenie == 0:
            maciek.mapblock()
            maciek.htiboxy(listMapy,0)
        else:
            maciek.mapblock2()
            maciek.hitboxy2(listMapy,0)
        maciek.draw()


        off()





main(True, offpos)
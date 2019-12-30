from funkcje import *
from case import Case
from player import Player
import pickle


with open('mapa.txt', 'rb') as obiekt:
    listMapyAll = pickle.load(obiekt)


maciek = Player(size/2, wymiaryMapyy*size - size/2, 0)
for b in listMapyAll:
    if b.x < maciek.x - offpos[0] < b.x + b.size and b.y < maciek.y - offpos[1] < b.y + b.size:
        b.terrain = 1


def main(Run,offpos):
    i=0
    ii=0
    listMapy = []
    while Run:
        mouse = pygame.mouse.get_pos()
        clock.tick(60)
        redraw_game(i, 20, 80)
        i += 1
        if i > 250:
            i = 0

        offpos[0], offpos[1] = moving(offpos[0], offpos[1], 3)
        if ii < 6:
            ii+=1
        else:
            ii=0
        if ii == 0:
            listMapy = []
            for b in listMapyAll:
                if b.x + offpos[0] >= -100 and b.x + offpos[0] <= szerokoscOkna + 100 and b.y + offpos[1] >= -100 and b.y + offpos[1] <= wysokoscOkna + 100:
                    listMapy.append(b)

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
            if sztuczne3d:
                b.xd3d(-10, 20)

        for b in listMapy:
            if drawterrain:
                b.drawTerrain()
            if szachownica:
                b.drawCase()

        for b in listMapy:
            if showId:
                b.drawId()
            if b.x < mouse[0] - offpos[0] < b.x + b.size and b.y < mouse[1] - offpos[1] < b.y + b.size:
                b.drawHighlight(0, 40, 100)
                napisy(b.caseNeighbours, 0, 0, 0)





        maciek.offx, maciek.offy = offpos[0], offpos[1]
        maciek.move()
        maciek.update()
        maciek.setHand(chodzenie)
        maciek.drawHand()
        maciek.terrainblock()
        maciek.handWorking(listMapy)
        if chodzenie == 0:
            maciek.mapblock()
            maciek.htiboxy(listMapy, 0)
            maciek.htiboxy(listMapy, 2)
            maciek.htiboxy(listMapy, 4)
        else:
            maciek.mapblock2()
            maciek.hitboxy2(listMapy, 0)
            maciek.htiboxy2(listMapy, 2)
            maciek.htiboxy2(listMapy, 4)
        maciek.draw()


        off()





main(True, offpos)
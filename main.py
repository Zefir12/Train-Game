from funkcje import *
from case import Case
from player import Player
import pickle



with open('chunks.txt', 'rb') as obiekt:
    listCHUNKS = pickle.load(obiekt)


maciek = Player(size/2, wymiaryMapyy*size - size/2, 0)


def main(Run, offpos):
    i=0
    while Run:

        listVisibleBlocks = []
        for b in listCHUNKS:
            if 0 - size * 7 < b.x + offpos[0] * 2 < szerokoscOkna - size and 0 - size * 7 < b.y + offpos[1] * 2 < wysokoscOkna - size:
                for bb in b.caselist:
                    listVisibleBlocks.append(bb)

        mouse = pygame.mouse.get_pos()
        clock.tick(60)
        redraw_game(i, 20, 80)
        i += 1
        if i > 250:
            i = 0

        offpos[0], offpos[1] = moving(offpos[0], offpos[1], cameraspeed)

        if maciek.x < size*8:
            offpos[0] += 1
        if maciek.x > szerokoscOkna - size*8:
            offpos[0] -= 1
        if maciek.y < size*8:
            offpos[1] += 1
        if maciek.y > wysokoscOkna - size*8:
            offpos[1] -= 1



        for b in listVisibleBlocks:
            b.offx, b.offy = offpos[0], offpos[1]
            b.update()

        for b in listVisibleBlocks:
            if sztuczne3d:
                b.xd3d((szerokoscOkna/2 - (b.x + offpos[0]))/30, (wysokoscOkna/2-(b.y + offpos[1]))/20)

        for b in listVisibleBlocks:
            if drawterrain:
                b.drawTerrain()
            if szachownica:
                b.drawCase()

        for b in listVisibleBlocks:
            if showId:
                b.drawId()
            if b.x < mouse[0] - offpos[0] < b.x + b.size and b.y < mouse[1] - offpos[1] < b.y + b.size:
                b.drawHighlight(0, 40, 100, shade[0], shade[1], 2)
                napisy(b.caseNeighbours, 0, 0, 0)
            if b.x < maciek.hand[0] - offpos[0] < b.x + b.size and b.y < maciek.hand[1] - offpos[1] < b.y + b.size:
                if b.terrain != 0:
                    b.drawHighlight(200, 40, 10, shade[0], shade[1], 3)
            for number in range(10):
                if b.destruction < 100:
                    b.destruction += 1
            b.drawDestruction()

        if drawChunkBorders:
            for b in listCHUNKS:
                pygame.draw.rect(obraz, [200, 0, 0], [b.x + offpos[0]*2, b.y + offpos[1]*2, size*8, size*8], 2)


        maciek.offx, maciek.offy = offpos[0], offpos[1]
        maciek.move()
        maciek.update()
        maciek.setHand(chodzenie)
        maciek.drawHand()
        maciek.terrainblock()
        maciek.handWorking(listVisibleBlocks, 1, 11)
        if chodzenie == 0:
            maciek.mapblock()
            maciek.htiboxy(listVisibleBlocks, 0)
            maciek.htiboxy(listVisibleBlocks, 2)
            maciek.htiboxy(listVisibleBlocks, 4)
        else:
            maciek.mapblock2()
            maciek.hitboxy2(listVisibleBlocks, 0)
            maciek.hitboxy2(listVisibleBlocks, 2)
            maciek.hitboxy2(listVisibleBlocks, 4)
        maciek.draw()

        Run = off()


main(True, offpos)
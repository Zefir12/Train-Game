from funkcje import *
from case import Case
from player import Player
import pickle





maciek = Player(Settings.size/2, Settings.wymiaryMapyy*Settings.size - Settings.size/2, 0)


def main(Run, offpos, listCHUNKS):
    i = 0
    while Run:

        listVisibleBlocks = []
        for b in listCHUNKS:
            if 0 - Settings.size * 8 < b.x + offpos[0] * 2 < Settings.szerokoscOkna + Settings.size and 0 - Settings.size * 9 < b.y + offpos[1] * 2 < Settings.wysokoscOkna + Settings.size:
                for bb in b.caselist:
                    listVisibleBlocks.append(bb)

        mouse = pygame.mouse.get_pos()
        clock.tick(60)
        redraw_game(i, 20, 80)
        i += 1
        if i > 250:
            i = 0

        offpos[0], offpos[1] = moving(offpos[0], offpos[1], Settings.cameraspeed)

        if maciek.x < Settings.size*8:
            offpos[0] += 1
        if maciek.x > Settings.szerokoscOkna - Settings.size*8:
            offpos[0] -= 1
        if maciek.y < Settings.size*8:
            offpos[1] += 1
        if maciek.y > Settings.wysokoscOkna - Settings.size*8:
            offpos[1] -= 1



        for b in listVisibleBlocks:
            b.offx, b.offy = offpos[0], offpos[1]
            b.update()

        for b in listVisibleBlocks:
            if Settings.sztuczne3d:
                b.xd3d((Settings.szerokoscOkna/2 - (b.x + offpos[0]))/Settings.shadowDepth, (Settings.wysokoscOkna/2-(b.y + offpos[1]))/Settings.shadowDepth)

        for b in listVisibleBlocks:
            if Settings.drawterrain:
                b.drawTerrain()
            if Settings.szachownica:
                b.drawCase()

        for b in listVisibleBlocks:
            if Settings.showId:
                b.drawId()
            if b.x < mouse[0] - offpos[0] < b.x + b.size and b.y < mouse[1] - offpos[1] < b.y + b.size:
                b.drawHighlight(0, 40, 100, (Settings.szerokoscOkna/2 - (b.x + offpos[0]))/Settings.shadowDepth,  (Settings.wysokoscOkna/2-(b.y + offpos[1]))/Settings.shadowDepth, 2)
                napisy(b.caseNeighbours, 0, 0, 0)
            if b.x < maciek.hand[0] - offpos[0] < b.x + b.size and b.y < maciek.hand[1] - offpos[1] < b.y + b.size:
                if b.terrain != 0:
                    b.drawHighlight(200, 40, 10, (Settings.szerokoscOkna/2 - (b.x + offpos[0]))/Settings.shadowDepth,  (Settings.wysokoscOkna/2-(b.y + offpos[1]))/Settings.shadowDepth, 3)
            for number in range(10):
                if b.destruction < 100:
                    b.destruction += 1
            b.drawDestruction()

        if Settings.drawChunkBorders:
            for b in listCHUNKS:
                pygame.draw.rect(obraz, [200, 0, 0], [b.x + offpos[0]*2, b.y + offpos[1]*2, Settings.size*8, Settings.size*8], 2)


        maciek.offx, maciek.offy = offpos[0], offpos[1]
        maciek.move()
        maciek.update()
        maciek.setHand(Settings.chodzenie)
        maciek.drawHand()
        maciek.terrainblock()
        maciek.handWorking(listVisibleBlocks, 1, 11)
        if Settings.chodzenie == 0:
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



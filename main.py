from funkcje import *
from case import Case
from player import Player
from mob import Mob
from items import Item
import pickle





def main(Run, offpos, map):
    maciek = Player((map.wymiaryMapyx / 2)*map.size, (map.wymiaryMapyy / 2)*map.size, 0, map.size, map.wymiaryMapyx, map.wymiaryMapyy)
    zombie = Mob((map.wymiaryMapyx / 2)*map.size, (map.wymiaryMapyy / 2)*map.size, 0, map.size, map.wymiaryMapyx, map.wymiaryMapyy)
    listITEMS = []
    while Run:
        listVisibleBlocks = []
        for b in map.chunklist:
            if 0 - map.size * 8 < b.x + offpos[0] * 2 < Settings.szerokoscOkna + map.size and 0 - map.size * 9 < b.y + offpos[1] * 2 < Settings.wysokoscOkna + map.size:
                for bb in b.caselist:
                    listVisibleBlocks.append(bb)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        clock.tick(60)
        redraw_game(0, 80, 80)

        if Settings.freecamera:
            offpos[0], offpos[1] = moving(offpos[0], offpos[1], Settings.cameraspeed)
            if maciek.x < map.size*8:
                offpos[0] += 1
            if maciek.x > Settings.szerokoscOkna - map.size*8:
                offpos[0] -= 1
            if maciek.y < map.size*8:
                offpos[1] += 1
            if maciek.y > Settings.wysokoscOkna - map.size*8:
                offpos[1] -= 1
        else:
            offpos[0], offpos[1] = (-maciek.startx)/2 + Settings.szerokoscOkna/4, (-maciek.starty)/2 + Settings.wysokoscOkna/4


        for b in listVisibleBlocks:
            b.offx, b.offy = offpos[0], offpos[1]
            b.update()

        for b in listVisibleBlocks:
            if Settings.sztuczne3d:
                b.xd3d((Settings.szerokoscOkna/2 - (b.x + offpos[0]))/Settings.shadowDepth, (Settings.wysokoscOkna/2-(b.y + offpos[1]))/Settings.shadowDepth)

        for b in listVisibleBlocks:
            if Settings.drawterrain:
                b.drawTerrain()
                b.drawItems()

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
            for b in map.chunklist:
                pygame.draw.rect(obraz, [200, 0, 0], [b.x + offpos[0]*2, b.y + offpos[1]*2, map.size*8, map.size*8], 2)

        for b in listITEMS:
            b.draw()

        maciek.offx, maciek.offy = offpos[0], offpos[1]
        maciek.move()
        maciek.update()
        maciek.setHand(Settings.chodzenie)
        maciek.drawHand()
        maciek.terrainblock()
        maciek.handWorking(listVisibleBlocks)
        maciek.handPicking(listVisibleBlocks)

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

        zombie.offx, zombie.offy = offpos[0], offpos[1]
        zombie.draw()
        zombie.update()
        zombie.AI()
        zombie.mapblock()
        zombie.hitboxy(listVisibleBlocks, 0)
        zombie.hitboxy(listVisibleBlocks, 2)
        zombie.hitboxy(listVisibleBlocks, 4)
        zombie.hitV2(maciek)



        maciek.drawInventory()
        Run = off()



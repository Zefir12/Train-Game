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
        listBlock = []

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
            if b.x < maciek.x - offpos[0] < b.x + b.size and b.y < maciek.y - offpos[1] < b.y + b.size:
                if b.terrain == 0:
                    listBlock.append(b)

            if b.x < maciek.x + maciek.size*2 - offpos[0] < b.x + b.size and b.y < maciek.y + maciek.size*2 - offpos[1] < b.y + b.size:
                if b.terrain == 0:
                    listBlock.append(b)

            if b.x < maciek.x + maciek.size*2 - offpos[0] < b.x + b.size and b.y < maciek.y - offpos[1] < b.y + b.size:
                if b.terrain == 0:
                    listBlock.append(b)

            if b.x < maciek.x - offpos[0] < b.x + b.size and b.y < maciek.y + maciek.size*2 - offpos[1] < b.y + b.size:
                if b.terrain == 0:
                    listBlock.append(b)


        for b in listBlock:
            
            b.drawHighlight()







        off()





main(True, offpos)
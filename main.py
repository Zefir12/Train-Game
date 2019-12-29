from funkcje import *
from case import Case
from player import Player
import pickle

with open('mapa.txt', 'rb') as obiekt:
    listMapy = pickle.load(obiekt)

maciek = Player(size / 2, size / 2, 0)

def dupa():
    leftTopTop = False
    leftTopLeft = False
    rightTopTop = False
    rightTopRight = False
    rightBotRight = False
    rightBotBot = False
    leftBotBot = False
    leftBotLeft = False

    for b in listMapy:
        if b.terrain == 0:
            if b.x < maciek.x - offpos[0] - 1 < b.x + b.size and b.y < maciek.y - offpos[1] + 1 < b.y + b.size:
                leftTopLeft = True

            if b.x < maciek.x - offpos[0] + 1 < b.x + b.size and b.y < maciek.y - offpos[1] - 1 < b.y + b.size:
                leftTopTop = True

            if b.x < maciek.x + maciek.size * 2 - offpos[0] - 1 < b.x + b.size and b.y < maciek.y - offpos[
                1] - 1 < b.y + b.size:
                rightTopTop = True

            if b.x < maciek.x + maciek.size * 2 - offpos[0] + 1 < b.x + b.size and b.y < maciek.y - offpos[
                1] + 1 < b.y + b.size:
                rightTopRight = True

            if b.x < maciek.x + maciek.size * 2 - offpos[
                0] + 1 < b.x + b.size and b.y < maciek.y + maciek.size * 2 - offpos[1] - 1 < b.y + b.size:
                rightBotRight = True

            if b.x < maciek.x + maciek.size * 2 - offpos[
                0] - 1 < b.x + b.size and b.y < maciek.y + maciek.size * 2 - offpos[1] + 1 < b.y + b.size:
                rightBotBot = True

            if b.x < maciek.x - offpos[0] + 1 < b.x + b.size and b.y < maciek.y + maciek.size * 2 - offpos[
                1] + 1 < b.y + b.size:
                leftBotBot = True

            if b.x < maciek.x - offpos[0] - 1 < b.x + b.size and b.y < maciek.y + maciek.size * 2 - offpos[
                1] - 1 < b.y + b.size:
                leftBotLeft = True

    maciek.leftblock = 1
    maciek.upblock = 1
    maciek.rightblock = 1
    maciek.downblock = 1
    if leftTopTop and leftTopLeft:
        maciek.leftblock = 0
        maciek.upblock = 0
    elif rightTopTop and rightTopRight:
        maciek.upblock = 0
        maciek.rightblock = 0
    elif rightBotBot and rightBotRight:
        maciek.rightblock = 0
        maciek.downblock = 0
    elif leftBotBot and leftBotLeft:
        maciek.downblock = 0
        maciek.leftblock = 0
    elif leftTopTop or rightTopTop:
        maciek.upblock = 0
    elif rightTopRight or rightBotRight:
        maciek.rightblock = 0
    elif rightBotBot or leftBotBot:
        maciek.downblock = 0
    elif leftBotLeft or leftTopLeft:
        maciek.leftblock = 0

def main(Run, offpos):
    while Run:
        maciek.mapblock()
        mouse = pygame.mouse.get_pos()
        redraw_game(80, 80, 80)
        offpos[0], offpos[1] = moving(offpos[0], offpos[1], 3)
        listBlock = []

        if maciek.x < size * 4:
            offpos[0] += 1
            maciek.x += 1
        if maciek.x > szerokoscOkna - size * 4:
            offpos[0] -= 1
            maciek.x -= 1
        if maciek.y < size * 4:
            offpos[1] += 1
            maciek.y += 1
        if maciek.y > wysokoscOkna - size * 4:
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
        off()
        dupa()

main(True, offpos)
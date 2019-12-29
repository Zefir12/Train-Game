from config import *
import pygame
import sys


pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
czcionka = pygame.font.Font("Czcionki/Montserrat-ExtraBold.otf", 10)
czcionkaBIG = pygame.font.Font("Czcionki/Montserrat-ExtraBold.otf", 40)
obraz = pygame.display.set_mode([szerokoscOkna, wysokoscOkna])


def napisy(co, x, y,rozmiar):
    nazwa = str(co)
    kolor_napisu = [0, 0, 0]
    if rozmiar == 1:
        label2 = czcionka.render(nazwa, 1, kolor_napisu)
    else:
        label2 = czcionkaBIG.render(nazwa, 1, kolor_napisu)
    obraz.blit(label2, [x, y])


def przycisk(x,y,sizex,sizey,zmiennax,zmiennay, event):
    pygame.draw.rect(obraz, [0, 0, 0], [x, y, sizex, sizey])
    if x < zmiennax < x+sizex and y < zmiennay < y + sizey and event:
        return False
    else:
        return True

def redraw_game(r, g, b):
    pygame.Surface.fill(obraz, [r, g, b])


def off():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    pygame.display.flip()
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        return False
    else:
        return True

def moving(x, y, speed):
    if pygame.key.get_pressed()[pygame.K_a]:
        x += speed
    if pygame.key.get_pressed()[pygame.K_d]:
        x -= speed
    if pygame.key.get_pressed()[pygame.K_w]:
        y += speed
    if pygame.key.get_pressed()[pygame.K_s]:
        y -= speed
    return x, y


def hitBox(pozycjax, pozycjay, pozycjax2, pozycjay2, rozmiar):
    if (pozycjax + rozmiar >= pozycjax2) and (pozycjax - rozmiar <= pozycjax2) and (
            pozycjay + rozmiar >= pozycjay2) and (pozycjay - rozmiar <= pozycjay2):
        return 1
def dupa(listaMapy):
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
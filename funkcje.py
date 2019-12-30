from config import *
import pygame
import sys


pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
czcionka = pygame.font.Font("Czcionki/Montserrat-ExtraBold.otf", 10)
czcionkaBIG = pygame.font.Font("Czcionki/Montserrat-ExtraBold.otf", 40)
obraz = pygame.display.set_mode([szerokoscOkna, wysokoscOkna])
water = pygame.image.load('water.png')


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

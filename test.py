from opensimplex import OpenSimplex
import random
import pygame
from config import Settings
import sys

Settings = Settings()

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
czcionka = pygame.font.Font("Czcionki/Montserrat-ExtraBold.otf", 10)
czcionkaBIG = pygame.font.Font("Czcionki/Montserrat-ExtraBold.otf", 40)
obraz = pygame.display.set_mode([1000, 1000])

rozmiarpiksela = 5

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


class Klocek():
    def __init__(self, x, y, value, value2, value3):
        self.x = x
        self.y = y
        self.value = value
        self.value2 = value2
        self.value3 = value3
        self.color = [0, 0, 0]

    def rysuj(self):
        pygame.draw.rect(obraz, self.color, [self.x, self.y, rozmiarpiksela, rozmiarpiksela])

    def update(self):
        if self.value < 0.3:
            self.color = [0, 0, self.value * 400,0]
        else:
            self.color = [self.value*255,self.value*255,0]
        if self.value2 > 0.5 and 0.6 > self.value > 0.3 and self.value3 > 0.3:
            self.color = [0, self.value*150, 0]
        if self.value > 0.83:
            self.color = [70, 70,70]
        if self.value > 0.88:
            self.color = [200, 200,200]


def noise(nx, ny, gen):
    # Rescale from -1.0:+1.0 to 0.0:1.0
    return gen.noise2d(nx, ny) / 2.0 + 0.5


def losowando(frequency, sizex, sizey):
    value = []
    gen = OpenSimplex(seed=random.randint(0, 1000))
    for y in range(sizex):
        value.append([0] * sizey)
        for x in range(sizey):
            nx = x / sizex - 0.5
            ny = y / sizey - 0.5
            value[y][x] = noise((frequency * nx)*0.85 + (frequency * nx * 8)*0.15, (frequency * ny)*0.85 + (frequency * ny * 8)*0.15, gen)
    return value

def gene():
    klocki = []
    wymiarx = 200
    wymiary = 200
    value = losowando(4, wymiarx, wymiary)
    value2 = losowando(15, wymiarx, wymiary)
    value3 = losowando(20, wymiarx, wymiary)

    i = 0
    ii = 0
    for b in range(wymiarx):
        for bb in range(wymiary):
            klocki.append(Klocek(b*rozmiarpiksela, bb*rozmiarpiksela, value[ii][i], value2[ii][i], value3[ii][i]))
            i += 1
        ii += 1
        i = 0
    return klocki

Run = True
klocki = gene()
for b in klocki:
    b.update()
while Run:
    click = pygame.mouse.get_pressed()
    redraw_game(200, 0, 0)
    if click[0]:
        klocki = gene()
        for b in klocki:
            b.update()
    for b in klocki:
        b.rysuj()

    Run = off()
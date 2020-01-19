from config import Settings
import pygame
import sys

Settings = Settings()

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
czcionka = pygame.font.Font("Czcionki/Montserrat-ExtraBold.otf", 10)
czcionkaBIG = pygame.font.Font("Czcionki/Montserrat-ExtraBold.otf", 40)
obraz = pygame.display.set_mode([Settings.szerokoscOkna, Settings.wysokoscOkna])
water = pygame.image.load('Graphics/water.png')
backgroundmenu = pygame.image.load('Graphics/backgroundmenu.png')


def napisy(co, x, y,rozmiar):
    nazwa = str(co)
    kolor_napisu = [0, 0, 0]
    if rozmiar == 1:
        label2 = czcionka.render(nazwa, 1, kolor_napisu)
    else:
        label2 = czcionkaBIG.render(nazwa, 1, kolor_napisu)
    obraz.blit(label2, [x, y])


def przycisk(x, y, sizex, sizey, zmiennax, zmiennay, event, zmiennatrue=True, zmiennafalse=False, r=0, g=0, b=0, text=None, textsize=1):
    pygame.draw.rect(obraz, [r, g, b], [x, y, sizex, sizey])
    if text is not None:
        napisy(text, x, y, textsize)
    if x < zmiennax < x+sizex and y < zmiennay < y + sizey and event:
        return zmiennatrue
    else:
        return zmiennafalse

def redraw_game(r, g, b, image=False, x=0, y=0):
    if image is False:
        pygame.Surface.fill(obraz, [r, g, b])
    else:
        obraz.blit(image, [x, y])


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
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        x += speed
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        x -= speed
    if pygame.key.get_pressed()[pygame.K_UP]:
        y += speed
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        y -= speed
    return x, y

def timefunction(timeoftheday, timezmienna, speed):
    if timezmienna == 0:
        if timeoftheday < 0:
            timeoftheday += speed
        else:
            timezmienna = 1
    else:
        if timeoftheday > -0.94:
            timeoftheday -= speed
        else:
            timezmienna = 0
    if timeoftheday > 0:
        timeoftheday = 0
    if timeoftheday < -0.94:
        timeoftheday = -0.94

    return timeoftheday, timezmienna

def drawMouse(x, y, radius, color, thickness, linelongness):
    pygame.draw.circle(obraz, color, [int(x), int(y)], int(radius), thickness)
    pygame.draw.line(obraz, color, [x - radius * linelongness, y], [x + radius * linelongness, y])
    pygame.draw.line(obraz, color, [x, y - radius * linelongness], [x, y + radius * linelongness])

def menubackgroundoffset(speed, x, y):
    if Settings.offsetmenux > x:
        Settings.offsetmenux -= speed
    if Settings.offsetmenux < x:
        Settings.offsetmenux += speed
    if Settings.offsetmenuy > y:
        Settings.offsetmenuy -= speed
    if Settings.offsetmenuy < y:
        Settings.offsetmenuy += speed
from funkcje import *
from mapGen import mapGeneration
from main import main


def settingsMenu(Run):
    while Run:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        redraw_game(54, 37, 20)

        napisy(round(1/Settings.shadowDepth,4), Settings.szerokoscOkna / 2 - 160, Settings.wysokoscOkna / 3, 0)
        if przycisk(Settings.szerokoscOkna / 2, Settings.wysokoscOkna / 3, 40, 40, mouse[0], mouse[1], click[0], r=100, g=100,
                    b=100, text="-", textsize=0):
            Settings.shadowDepth += 1
        if przycisk(Settings.szerokoscOkna / 2 - 200, Settings.wysokoscOkna / 3, 40, 40, mouse[0], mouse[1], click[0], r=100, g=100,
                    b=100, text="+", textsize=0):
            if Settings.shadowDepth > 1:
                Settings.shadowDepth -= 1

        napisy(Settings.cameraspeed, Settings.szerokoscOkna / 2 - 160, Settings.wysokoscOkna / 3 + 50, 0)
        if przycisk(Settings.szerokoscOkna / 2, Settings.wysokoscOkna / 3 + 50, 40, 40, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="-", textsize=0):
            if Settings.cameraspeed > 1:
                Settings.cameraspeed -= 1
        if przycisk(Settings.szerokoscOkna / 2 - 200, Settings.wysokoscOkna / 3 + 50, 40, 40, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="+", textsize=0):
            Settings.cameraspeed += 1


        if przycisk(Settings.szerokoscOkna - 200, Settings.wysokoscOkna - 60, 200, 60, mouse[0], mouse[1],
                    click[0], r=100, g=100, b=100, text="Back", textsize=0):
            break

        off()


def savingMenu(Map1, Map2, Map3):
    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        redraw_game(54, 37, 20)
        if przycisk(100, 100, 280, 60, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="New World 1", textsize=0):
            Map1.size = 10
            Map1.number = 1
            Map1.wymiaryMapyx = 100
            Map1.wymiaryMapyy = 100
            Map1.chunklist, Map1.zombielist = mapGeneration(Map1.size, Map1.wymiaryMapyx, Map1.wymiaryMapyy)
        if przycisk(100, 200, 280, 60, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="New World 2", textsize=0):
            Map2.size = 50
            Map2.number = 2
            Map2.wymiaryMapyx = 160
            Map2.wymiaryMapyy = 160
            Map2.chunklist, Map2.zombielist = mapGeneration(Map2.size, Map2.wymiaryMapyx, Map2.wymiaryMapyy)
        if przycisk(100, 300, 280, 60, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="New World 3", textsize=0):
            Map3.size = 50
            Map3.number = 3
            Map3.wymiaryMapyx = 160
            Map3.wymiaryMapyy = 160
            Map3.chunklist, Map3.zombielist = mapGeneration(Map3.size, Map3.wymiaryMapyx, Map3.wymiaryMapyy)


        if przycisk(Settings.szerokoscOkna - 200, Settings.wysokoscOkna - 60, 200, 60, mouse[0], mouse[1], click[0],
                    r=100, g=100, b=100, text="Back", textsize=0):
            break
        off()


def playingMenu(Map1, Map2, Map3):
    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        redraw_game(54, 37, 20)
        if przycisk(100, 100, 200, 60, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="World 1", textsize=0):
            main(True, Settings.offpos, Map1)
        if przycisk(100, 200, 200, 60, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="World 2", textsize=0):
            main(True, Settings.offpos, Map2)
        if przycisk(100, 300, 200, 60, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="World 3", textsize=0):
            main(True, Settings.offpos, Map3)


        if przycisk(Settings.szerokoscOkna - 200, Settings.wysokoscOkna - 60, 200, 60, mouse[0], mouse[1], click[0],
                    r=100, g=100, b=100, text="Back", textsize=0):
            break
        off()

from main import *
from submenus import *
from mapGen import mapGeneration
from map import Map



RunSettings = True
menuPart = 1

try:
    with open('Maps/map1.txt', 'rb') as obiekt:
        Map1 = pickle.load(obiekt)
except:
    Map1 = Map('Mapa1', 1)
try:
    with open('Maps/map2.txt', 'rb') as obiekt:
        Map2 = pickle.load(obiekt)
except:
    Map2 = Map('Mapa2', 2)
try:
    with open('Maps/map3.txt', 'rb') as obiekt:
        Map3 = pickle.load(obiekt)
except:
    Map3 = Map('Mapa3', 3)

zmiennax = 0
zmiennay = 0
while True:
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    redraw_game(54, 37, 20, image=backgroundmenu, x=Settings.offsetstartingmenux + Settings.offsetmenux,
                y=Settings.offsetstartingmenuy + Settings.offsetmenuy)
    menubackgroundoffset(10, zmiennax, zmiennay)
    if Settings.offsetmenux == zmiennax and Settings.offsetmenuy == zmiennay:
        canClick = True
    else:
        canClick = False

    if menuPart == 1:
        if przycisk(Settings.szerokoscOkna/2 - 100 + Settings.offsetmenux*6, Settings.wysokoscOkna/3 + Settings.offsetmenuy*6, 200, 60, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="play", textsize=0) and canClick:
            zmiennax = -160
            zmiennay = -160

        if przycisk(Settings.szerokoscOkna/2 - 100 + Settings.offsetmenux*6, Settings.wysokoscOkna/3 + Settings.offsetmenuy*6 + 100, 200, 60, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="settings", textsize=0) and canClick:
            zmiennax = 160
            zmiennay = 0

        if przycisk(Settings.szerokoscOkna/2 - 100 + Settings.offsetmenux*6, Settings.wysokoscOkna/3 + Settings.offsetmenuy*6 + 200, 200, 60, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="new map", textsize=0) and canClick:
            zmiennax = 0
            zmiennay = -160

        if przycisk(Settings.szerokoscOkna/2 - 100 + Settings.offsetmenux*6, Settings.wysokoscOkna/3 + Settings.offsetmenuy*6 + 300, 200, 60, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="exit", textsize=0) and canClick:
            break

        ####Settings part
        napisy(round(1/Settings.shadowDepth, 4), Settings.offsetmenux*6 - 360, Settings.wysokoscOkna / 3, 0)
        if przycisk(Settings.offsetmenux*6 - 200, Settings.wysokoscOkna / 3, 40, 40, mouse[0], mouse[1], click[0], r=100, g=100,
                    b=100, text="-", textsize=0) and canClick:
            Settings.shadowDepth += 1
        if przycisk(Settings.offsetmenux*6 - 400, Settings.wysokoscOkna / 3, 40, 40, mouse[0], mouse[1], click[0], r=100, g=100,
                    b=100, text="+", textsize=0) and canClick:
            if Settings.shadowDepth > 1:
                Settings.shadowDepth -= 1

        napisy(Settings.cameraspeed, Settings.offsetmenux*6 - 360, Settings.wysokoscOkna / 3 + 50, 0)
        if przycisk(Settings.offsetmenux*6 - 200, Settings.wysokoscOkna / 3 + 50, 40, 40, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="-", textsize=0) and canClick:
            if Settings.cameraspeed > 1:
                Settings.cameraspeed -= 1
        if przycisk(Settings.offsetmenux*6 - 400, Settings.wysokoscOkna / 3 + 50, 40, 40, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="+", textsize=0) and canClick:
            Settings.cameraspeed += 1


        if przycisk(Settings.szerokoscOkna - 200, Settings.wysokoscOkna - 60, 200, 60, mouse[0], mouse[1],
                    click[0], r=100, g=100, b=100, text="Back", textsize=0) and canClick:
            zmiennax = 0
            zmiennay = 0


        ####Playing part
        if przycisk(1600 + Settings.offsetmenux*6, 1050 + Settings.offsetmenuy*6, 200, 60, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="World 1", textsize=0) and canClick:
            main(True, Settings.offpos, Map1)
        if przycisk(1600 + Settings.offsetmenux*6, 1150 + Settings.offsetmenuy*6, 200, 60, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="World 2", textsize=0) and canClick:
            main(True, Settings.offpos, Map2)
        if przycisk(1600 + Settings.offsetmenux*6, 1250 + Settings.offsetmenuy*6, 200, 60, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="World 3", textsize=0) and canClick:
            main(True, Settings.offpos, Map3)


        ####Saving Part
        if przycisk(600 + Settings.offsetmenux*6, 1100 + Settings.offsetmenuy*6, 280, 60, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="New World 1", textsize=0) and canClick:
            Map1.size = 10
            Map1.number = 1
            Map1.wymiaryMapyx = 100
            Map1.wymiaryMapyy = 100
            Map1.chunklist, Map1.zombielist = mapGeneration(Map1.size, Map1.wymiaryMapyx, Map1.wymiaryMapyy)
        if przycisk(600 + Settings.offsetmenux*6, 1200 + Settings.offsetmenuy*6, 280, 60, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="New World 2", textsize=0) and canClick:
            Map2.size = 50
            Map2.number = 2
            Map2.wymiaryMapyx = 160
            Map2.wymiaryMapyy = 160
            Map2.chunklist, Map2.zombielist = mapGeneration(Map2.size, Map2.wymiaryMapyx, Map2.wymiaryMapyy)
        if przycisk(600 + Settings.offsetmenux*6, 1300 + Settings.offsetmenuy*6, 280, 60, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="New World 3", textsize=0) and canClick:
            Map3.size = 50
            Map3.number = 3
            Map3.wymiaryMapyx = 160
            Map3.wymiaryMapyy = 160
            Map3.chunklist, Map3.zombielist = mapGeneration(Map3.size, Map3.wymiaryMapyx, Map3.wymiaryMapyy)



        off()
from main import *
from settings import *
from mapGen import mapGeneration
from map import Map


RunSettings = True

try:
    with open('Maps/map1.txt', 'rb') as obiekt:
        Map1 = pickle.load(obiekt)
except:
    Map1 = Map('Mapa1', 0)
try:
    with open('Maps/map2.txt', 'rb') as obiekt:
        Map2 = pickle.load(obiekt)
except:
    Map2 = Map('Mapa2', 0)
try:
    with open('Maps/map3.txt', 'rb') as obiekt:
        Map3 = pickle.load(obiekt)
except:
    Map3 = Map('Mapa3', 0)


while True:
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    redraw_game(54, 37, 20)

    if przycisk(Settings.szerokoscOkna/2 - 100, Settings.wysokoscOkna/3, 200, 60, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="play", textsize=0):
        main(True, Settings.offpos, Map1)
    if przycisk(Settings.szerokoscOkna/2 - 100, Settings.wysokoscOkna/3 + 100, 200, 60, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="settings", textsize=0):
        settingsMenu(RunSettings)
    if przycisk(Settings.szerokoscOkna/2 - 100, Settings.wysokoscOkna/3 + 200, 200, 60, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="new map", textsize=0):
        Map1.size = 40
        Map1.wymiaryMapyx = 100
        Map1.wymiaryMapyy = 100
        Map1.chunklist = mapGeneration(Map1.size, Map1.wymiaryMapyx, Map1.wymiaryMapyy)
    if przycisk(Settings.szerokoscOkna/2 - 100, Settings.wysokoscOkna/3 + 300, 200, 60, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="exit", textsize=0):
        with open('Maps/map1.txt', 'wb') as obiekt:
            pickle.dump(Map1, obiekt)
        with open('Maps/map2.txt', 'wb') as obiekt:
            pickle.dump(Map2, obiekt)
        with open('Maps/map3.txt', 'wb') as obiekt:
            pickle.dump(Map3, obiekt)
        break

    off()


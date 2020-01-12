
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


while True:
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    redraw_game(54, 37, 20)
    if menuPart == 1:
        if przycisk(Settings.szerokoscOkna/2 - 100, Settings.wysokoscOkna/3, 200, 60, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="play", textsize=0):
            playingMenu(Map1, Map2, Map3)

        if przycisk(Settings.szerokoscOkna/2 - 100, Settings.wysokoscOkna/3 + 100, 200, 60, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="settings", textsize=0):
            settingsMenu(RunSettings)

        if przycisk(Settings.szerokoscOkna/2 - 100, Settings.wysokoscOkna/3 + 200, 200, 60, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="new map", textsize=0):
            savingMenu(Map1, Map2, Map3)

        if przycisk(Settings.szerokoscOkna/2 - 100, Settings.wysokoscOkna/3 + 300, 200, 60, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="exit", textsize=0):
            break
        off()
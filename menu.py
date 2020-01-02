from main import *
from settings import *
from mapGen import mapGeneration
AppWindow = True
RunSettings = True

with open('chunks.txt', 'rb') as obiekt:
    listCHUNKS = pickle.load(obiekt)

while AppWindow:
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    redraw_game(54, 37, 20)

    #włączenie gry
    if przycisk(Settings.szerokoscOkna/2 - 100, Settings.wysokoscOkna/3, 200, 60, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="start", textsize=0):
        main(True, Settings.offpos, listCHUNKS)
    if przycisk(Settings.szerokoscOkna/2 - 100, Settings.wysokoscOkna/3 + 100, 200, 60, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="settings", textsize=0):
        settingsMenu(RunSettings)
    if przycisk(Settings.szerokoscOkna/2 - 100, Settings.wysokoscOkna/3 + 200, 200, 60, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="new map", textsize=0):
        listCHUNKS = mapGeneration()
    if przycisk(Settings.szerokoscOkna/2 - 100, Settings.wysokoscOkna/3 + 300, 200, 60, mouse[0], mouse[1], click[0], r=100, g=100, b=100, text="exit", textsize=0):
        with open('chunks.txt', 'wb') as obiekt:
            pickle.dump(listCHUNKS, obiekt)
        break

    off()


from funkcje import *


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

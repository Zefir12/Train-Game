from funkcje import *
from case import Case
from chunk import Chunk
import random


def mapGeneration():
    listaMapy = []
    idCase = 0
    chances = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    a = random.randint(3, 8)
    rozmiarmin = 0
    rozmiarmax = 3
    listakregi = [(0, Settings.wymiaryMapyy*Settings.size), (Settings.wymiaryMapyx*Settings.size/6*5, Settings.wymiaryMapyy * Settings.size/2)]
    liczbaskal = 3
    rozmiarskalmin = 3
    rozmiarskalmax = 4
    liczbaforest = 8
    rozmiarforestmin = 1
    rozmiarforestmax = 5
    listaforest = []
    listaskaly = []




    for b in range(Settings.wymiaryMapyx):
        for bb in range(Settings.wymiaryMapyy):
            listaMapy.append(Case(b*Settings.size, bb*Settings.size, idCase))
            idCase += 1
    print('Stworzylo grid mapy')

    for b in range(a):
        c = random.randint(0, idCase)
        for bb in listaMapy:
            if bb.id == c:
                listakregi.append((bb.x, bb.y))
    print('Wylosowalo kregi terenu')

    for b in listakregi:
        for bb in listaMapy:
            if (((b[0] - bb.x) ** 2) + ((b[1] - bb.y) ** 2)) < (bb.size * random.randint(rozmiarmax, rozmiarmax)*4)**2:
                bb.terrain = 1
    print('Stworzylo pierwsze polacie terenu')

    for b in listakregi:
        for bb in listakregi:
            temp = ((b[0]+bb[0])/2, (b[1]+bb[1])/2)
            for bbb in listaMapy:
                if (((temp[0] - bbb.x) ** 2) + ((temp[1] - bbb.y) ** 2)) < (bbb.size * random.randint(rozmiarmax, rozmiarmax) * 2) ** 2:
                    bbb.terrain = 1
    print('Rozlokowalo dodatkowe wyspy')

    for b in range(liczbaforest):
        while len(listaforest) < liczbaforest:
            c = random.randint(0, idCase)
            for bb in listaMapy:
                if bb.id == c:
                    if bb.terrain == 1:
                        listaforest.append((bb.x, bb.y))
    print('Wylosowalo centra lasow')
    pygame.draw.rect(obraz, [0,0,0], [0,0,300,300])
    for b in listaforest:
        for bb in listaMapy:
            if (((b[0] - bb.x) ** 2) + ((b[1] - bb.y) ** 2)) < (bb.size * random.randint(rozmiarforestmin, rozmiarforestmax) * 2) ** 2:
                if bb.terrain != 0:
                    bb.terrain = 4
    print('Rozlokowalo poszczegolne drzewa')

    for b in range(liczbaskal):
        while len(listaskaly) < liczbaskal:
            c = random.randint(0, idCase)
            for bb in listaMapy:
                if bb.id == c:
                    if bb.terrain == 1:
                        listaskaly.append((bb.x, bb.y))
    print('Stworzylo centra kamieni')

    for b in listaskaly:
        for bb in listaMapy:
            if (((b[0] - bb.x) ** 2) + ((b[1] - bb.y) ** 2)) < (bb.size * random.randint(rozmiarskalmin, rozmiarskalmax) * 3) ** 2:
                bb.terrain = 2
    print('Rozlokowalo kamienie')



    #############################################################################################################
    ### Creating neighbourhoods
    percent = 0
    for b in listaMapy:
        if percent < round(b.id/idCase * 100):
            percent = round(b.id/idCase * 100)
            print(str(percent) + '% wpisywania sasiadow do casow')

        if Settings.wymiaryMapyy < b.id:
            if listaMapy[b.id - Settings.wymiaryMapyy].terrain != 0:
                b.caseNeighbours[3] = listaMapy[b.id - Settings.wymiaryMapyy].id
            else:
                b.caseNeighbours[3] = None
                if b.terrain !=0:
                    b.shade2 = True
        if b.id < idCase - Settings.wymiaryMapyy:
            if listaMapy[b.id + Settings.wymiaryMapyy].terrain != 0:
                b.caseNeighbours[1] = listaMapy[b.id + Settings.wymiaryMapyy].id
            else:
                b.caseNeighbours[1] = None
                if b.terrain !=0:
                    b.shade4 = True
        if b.id < idCase - 1:
            if listaMapy[b.id + 1].terrain != 0:
                b.caseNeighbours[2] = listaMapy[b.id + 1].id
            else:
                b.caseNeighbours[2] = None
                if b.terrain !=0:
                    b.shade1 = True
        if b.id > 1:
            if listaMapy[b.id - 1].terrain != 0:
                b.caseNeighbours[0] = listaMapy[b.id - 1].id
            else:
                b.caseNeighbours[0] = None
                if b.terrain !=0:
                    b.shade3 = True
        if Settings.wymiaryMapyy > b.id:
            if listaMapy[b.id].terrain != 0:
                b.shade2 = True
        if (b.id + 1) % Settings.wymiaryMapyy == 0:
            b.caseNeighbours[2] = None
            if b.terrain != 0:
                b.shade1 = True
        if b.id % Settings.wymiaryMapyy == 0:
            b.caseNeighbours[0] = None
            if b.terrain != 0:
                b.shade3 = True


    ###############################################################################################################
    ### Creating chunks
    listaCHUNK = []
    chunkID = 0

    for b in range(0, int(Settings.wymiaryMapyx), 8):
        for bb in range(0, int(Settings.wymiaryMapyy), 8):
            listaCHUNK.append(Chunk(b * Settings.size, bb * Settings.size, chunkID))
            chunkID += 1
    print('Stworzylo chunki')

    percent = 0
    for b in listaCHUNK:
        if percent < round(b.id/chunkID * 100):
            percent = round(b.id/chunkID * 100)
            print(str(percent) + '% wpisywania blokow do chunkow')

        for bb in listaMapy:
            if b.x < bb.x+1 < b.x + Settings.size * 8 and b.y < bb.y+1 < b.y + Settings.size * 8:
                b.caselist.append(bb)



    print('Wpisalo bloki do odpowiednich chunkow')
    return listaCHUNK

#with open('chunks.txt', 'wb') as obiekt:
    #pickle.dump(listaCHUNK, obiekt)


"""
    for c in range(8):
        x = (((b.id ) * 64) - c*wymiaryMapyy)-1
        for cc in range(8):
            b.caselist.append(listaMapy[x - cc])
            
    WAZNE NIE RUSZAC!!
"""


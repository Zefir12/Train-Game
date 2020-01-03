from funkcje import *
from case import Case
from chunk import Chunk
from items import Item
import random
from opensimplex import OpenSimplex




def noise(nx, ny, gen):
    # Rescale from -1.0:+1.0 to 0.0:1.0
    return gen.noise2d(nx, ny) / 2.0 + 0.5


def losowando(frequency, sizex, sizey):
    value = []
    gen = OpenSimplex(seed=random.randint(0, 100))
    for y in range(sizex):
        value.append([0] * sizey)
        for x in range(sizey):
            nx = x / sizex - 0.5
            ny = y / sizey - 0.5
            value[y][x] = noise(frequency * nx * 2, frequency * ny, gen)
    return value

def mapGeneration(size,sizex,sizey):
    listaMapy = []
    idCase = 0


    value = losowando(8, sizex, sizey)
    value2 = losowando(16, sizex, sizey)
    value3 = losowando(9, sizex, sizey)
    value33 = losowando(9, sizex, sizey)
    valuerocks = losowando(5.2, sizex, sizey)
    valuerocks2 = losowando(20.3, sizex, sizey)
    valuesticks = losowando(50, sizex, sizey)
    i = 0
    ii = 0
    for b in range(sizex):
        for bb in range(sizey):
            listaMapy.append(Case(b*size, bb*size, idCase, size))
            if value[ii][i] > 0.4:
                listaMapy[len(listaMapy)-1].terrain = 1
            if value2[ii][i] > 0.4 and value[ii][i] > 0.4 and value3[ii][i] > 0.6 and value33[ii][i] > 0.2:
                listaMapy[len(listaMapy)-1].terrain = 4
            if value[ii][i] > 0.4 and valuerocks[ii][i] > 0.7 and valuerocks2[ii][i] > 0.2:
                listaMapy[len(listaMapy)-1].terrain = 2
            if sizex / 2 < ii < sizex / 3 and sizey / 2 < ii < sizey / 3 and listaMapy[len(listaMapy)-1].terrain == 1:
                pass
            if valuesticks[ii][i] > 0.88 and listaMapy[len(listaMapy)-1].terrain == 1:
                listaMapy[len(listaMapy) - 1].item = Item(1)
            if valuesticks[ii][i] < 0.096 and listaMapy[len(listaMapy)-1].terrain == 1:
                listaMapy[len(listaMapy) - 1].item = Item(2)
            idCase += 1
            i += 1
        ii += 1
        i = 0
    print('Stworzylo teren')







    #############################################################################################################
    ### Creating neighbourhoods
    percent = 0
    for b in listaMapy:
        if percent < round(b.id/idCase * 100):
            percent = round(b.id/idCase * 100)
            print(str(percent) + '% wpisywania sasiadow do casow')

        if sizey < b.id:
            if listaMapy[b.id - sizey].terrain != 0:
                b.caseNeighbours[3] = listaMapy[b.id - sizey].id
            else:
                b.caseNeighbours[3] = None
                if b.terrain !=0:
                    b.shade2 = True
        if b.id < idCase - sizey:
            if listaMapy[b.id + sizey].terrain != 0:
                b.caseNeighbours[1] = listaMapy[b.id + sizey].id
            else:
                b.caseNeighbours[1] = None
                if b.terrain != 0:
                    b.shade4 = True
        if b.id < idCase - 1:
            if listaMapy[b.id + 1].terrain != 0:
                b.caseNeighbours[2] = listaMapy[b.id + 1].id
            else:
                b.caseNeighbours[2] = None
                if b.terrain != 0:
                    b.shade1 = True
        if b.id > 1:
            if listaMapy[b.id - 1].terrain != 0:
                b.caseNeighbours[0] = listaMapy[b.id - 1].id
            else:
                b.caseNeighbours[0] = None
                if b.terrain !=0:
                    b.shade3 = True
        if sizey > b.id:
            if listaMapy[b.id].terrain != 0:
                b.shade2 = True
        if (b.id + 1) % sizey == 0:
            b.caseNeighbours[2] = None
            if b.terrain != 0:
                b.shade1 = True
        if b.id % sizey == 0:
            b.caseNeighbours[0] = None
            if b.terrain != 0:
                b.shade3 = True


    ###############################################################################################################
    ### Creating chunks
    listaCHUNK = []
    chunkID = 0

    for b in range(0, int(sizex), 8):
        for bb in range(0, int(sizey), 8):
            listaCHUNK.append(Chunk(b * size, bb * size, chunkID))
            chunkID += 1
    print('Stworzylo chunki')

    percent = 0
    for b in listaCHUNK:
        if percent < round(b.id/chunkID * 100):
            percent = round(b.id/chunkID * 100)
            print(str(percent) + '% wpisywania blokow do chunkow')

        for bb in listaMapy:
            if b.x < bb.x+1 < b.x + size * 8 and b.y < bb.y+1 < b.y + size * 8:
                b.caselist.append(bb)



    print('Wpisalo bloki do odpowiednich chunkow')
    return listaCHUNK




"""
    for c in range(8):
        x = (((b.id ) * 64) - c*wymiaryMapyy)-1
        for cc in range(8):
            b.caselist.append(listaMapy[x - cc])
            
    WAZNE NIE RUSZAC!!
"""


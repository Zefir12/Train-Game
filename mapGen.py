from config import *
from case import Case
import pickle
import random

listaMapy = []
idCase = 0
chances = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


for b in range(wymiaryMapyx):
    for bb in range(wymiaryMapyy):
        listaMapy.append(Case(b*size, bb*size, idCase))
        idCase += 1



a = random.randint(3,8)
rozmiarmin = 0
rozmiarmax = 3
listakregi = [(0, wymiaryMapyy*size), (wymiaryMapyx*size/6*5, wymiaryMapyy * size/2)]

liczbaskal = 3
rozmiarskalmin = 4
rozmiarskalmax = 5
liczbaforest = 8
rozmiarforestmin = 1
rozmiarforestmax = 5
listaforest = []
listaskaly = []



for b in range(a):
    c = random.randint(0, idCase)
    for bb in listaMapy:
        if bb.id == c:
            listakregi.append((bb.x, bb.y))

#stworzenie duzych wysp
for b in listakregi:
    for bb in listaMapy:
        if (((b[0] - bb.x) ** 2) + ((b[1] - bb.y) ** 2)) < (bb.size * random.randint(rozmiarmax, rozmiarmax)*4)**2:
            bb.terrain = 1

#dobicie dodatkowych wysepek pomiedzy duzymi wyspami
for b in listakregi:
    for bb in listakregi:
        temp = ((b[0]+bb[0])/2, (b[1]+bb[1])/2)
        for bbb in listaMapy:
            if (((temp[0] - bbb.x) ** 2) + ((temp[1] - bbb.y) ** 2)) < (bbb.size * random.randint(rozmiarmax, rozmiarmax) * 2) ** 2:
                bbb.terrain = 1

#tworzymy lasy
for b in range(liczbaforest):
    while len(listaforest) < liczbaforest:
        c = random.randint(0, idCase)
        for bb in listaMapy:
            if bb.id == c:
                if bb.terrain == 1:
                    listaforest.append((bb.x, bb.y))

for b in listaforest:
    for bb in listaMapy:
        if (((b[0] - bb.x) ** 2) + ((b[1] - bb.y) ** 2)) < (bb.size * random.randint(rozmiarforestmin, rozmiarforestmax) * 2) ** 2:
            bb.terrain = 4

#tworzymy kamyki
for b in range(liczbaskal):
    while len(listaskaly) < liczbaskal:
        c = random.randint(0, idCase)
        for bb in listaMapy:
            if bb.id == c:
                if bb.terrain == 1:
                    listaskaly.append((bb.x, bb.y))

for b in listaskaly:
    for bb in listaMapy:
        if (((b[0] - bb.x) ** 2) + ((b[1] - bb.y) ** 2)) < (bb.size * random.randint(rozmiarskalmin, rozmiarskalmax) * 3) ** 2:
            bb.terrain = 2
















#############################################################################################################
for b in listaMapy:
    for bb in listaMapy:
        if b.id - wymiaryMapyy == bb.id and b.terrain != 0:
            if bb.terrain != 0:
                b.caseNeighbours[3] = bb.id
        if b.id + wymiaryMapyy == bb.id and b.terrain != 0:
            if bb.terrain != 0:
                b.caseNeighbours[1] = bb.id
        if b.id + 1 == bb.id and b.terrain != 0:
            if bb.terrain != 0:
                b.caseNeighbours[2] = bb.id
        if b.id - 1 == bb.id and b.terrain != 0:
            if bb.terrain != 0:
                b.caseNeighbours[0] = bb.id

for b in listaMapy:
    if (b.id + 1)%wymiaryMapyy == 0 and b.terrain != 0:
        b.caseNeighbours[2] = None
    if (b.id)%wymiaryMapyy == 0 and b.terrain != 0:
        b.caseNeighbours[0] = None

for b in listaMapy:
    if b.caseNeighbours[2] is None and b.terrain != 0:
        b.shade1 = True
    if b.caseNeighbours[3] is None and b.terrain != 0:
        b.shade2 = True


for b in listaMapy:
    if b.terrain != 0:
        if b.id < wymiaryMapyy:
            b.shade = True


with open('mapa.txt', 'wb') as obiekt:
    pickle.dump(listaMapy, obiekt)
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

for b in listaMapy:
    b.terrain = random.choice(chances)

'''for b in listaMapy:
    for bb in listaMapy:
        if abs(b.x - bb.x) < 2*size and abs(b.y - bb.y) < 2*size and bb.terrain == 0 and b.terrain == 1:
            b.terrain = 3'''

a=2
for b in range(a):
    c = random.randint(0, idHEX)
    for bb in listHEX:
        if bb.id == c:
            listakregi.append((bb.center[0], bb.center[1]))


for b in listakregi:
    for bb in listHEX:
        if (((b[0] - bb.center[0]) ** 2) + ((b[1] - bb.center[1]) ** 2)) < (bb.size * 0.889 * random.randint(minrozmiarjezioro, maksrozmiarjezioro)*2) ** 2:
            bb.terrain = 3


with open('mapa.txt', 'wb') as obiekt:
    pickle.dump(listaMapy, obiekt)
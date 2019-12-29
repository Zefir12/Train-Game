from config import *
from case import Case
import pickle
import random

listaMapy = []
idCase = 0
chances = [0,1,1,1,1,1,1]


for b in range(wymiaryMapyx):
    for bb in range(wymiaryMapyy):
        listaMapy.append(Case(b*size, bb*size , idCase))
        idCase +=1

for b in listaMapy:
    b.terrain = random.choice(chances)

for b in listaMapy:
    for bb in listaMapy:
        pass




with open('mapa.txt', 'wb') as obiekt:
    pickle.dump(listaMapy, obiekt)
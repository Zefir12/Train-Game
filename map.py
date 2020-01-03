from config import *

class Map:
    def __init__(self, name, number, size=35, sizex=200, sizey=200):
        self.name = name
        self.number = number
        self.size = size
        self.wymiaryMapyx = sizex
        self.wymiaryMapyy = sizey
        self.chunklist = []

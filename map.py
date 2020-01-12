from config import *

class Map:
    def __init__(self, name, number, size=35, sizex=200, sizey=200):
        self.name = name
        self.number = number
        self.size = size
        self.coloroffset = 0
        self.wymiaryMapyx = sizex
        self.wymiaryMapyy = sizey
        self.chunklist = []
        self.zombielist = []
        self.timeoftheday = 0
        self.timezmienna = 1
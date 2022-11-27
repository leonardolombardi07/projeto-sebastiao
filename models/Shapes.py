from time import sleep
from graphics import *


class Tree(Rectangle):
    def __init__(self, coords1, coords2):
        p1 = Point(coords1[0], coords1[1])
        p2 = Point(coords2[0], coords2[1])
        Rectangle.__init__(self, p1, p2)
        self.setFill("brown")


class Dock(Rectangle):
    def __init__(self, coords1, coords2):
        p1 = Point(coords1[0], coords1[1])
        p2 = Point(coords2[0], coords2[1])
        Rectangle.__init__(self, p1, p2)
        self.setFill("red")


class Basket(Circle):
    def __init__(self, center, radius):
        Circle.__init__(self, Point(center[0]+0.5, center[1]+0.5), radius)
        self.setFill("orange")


class Bush(Circle):
    def __init__(self, center, radius):
        Circle.__init__(self, Point(center[0]+0.5, center[1]+0.5), radius)
        self.setFill("darkgreen")


class Grass(Rectangle):
    def __init__(self, coords1, coords2):
        p1 = Point(coords1[0], coords1[1])
        p2 = Point(coords2[0], coords2[1])
        Rectangle.__init__(self, p1, p2)
        self.setFill("green")


class Stone(Rectangle):
    def __init__(self, coords1, coords2):
        p1 = Point(coords1[0], coords1[1])
        p2 = Point(coords2[0], coords2[1])
        Rectangle.__init__(self, p1, p2)
        self.setFill("grey")

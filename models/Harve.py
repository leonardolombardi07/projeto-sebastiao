from time import sleep
from graphics import *


class Harve(Rectangle):
    def __init__(self, coords1, coords2):
        p1 = Point(coords1[0], coords1[1])
        p2 = Point(coords2[0], coords2[1])
        Rectangle.__init__(self, p1, p2)
        self.setFill("black")
        self.setOutline("green")
        self.setWidth(3)
        self.battery = 2

    def move_to(self, coords):
        dx = coords[0] - self.getP1().getX()
        dy = coords[1] - self.getP1().getY()
        self.move(dx, dy)

    def recharge_battery(self):
        self.setOutline("orange")
        sleep(2)
        self.battery = 2
        self.setOutline("green")

    def decrease_battery(self):
        self.battery = self.battery - 1
        if self.battery <= 1:
            self.setOutline("red")

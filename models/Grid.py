from graphics import *


class Node:
    def __init__(self, x, y, walkable=True):
        self.x = x
        self.y = y
        self.walkable = walkable


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.nodes = self.build_nodes(width, height)

    def build_nodes(self, width, height):
        return [[Node(x, y, walkable=True) for y in range(height)]
                for x in range(width)]

    def set_walkable_at(self, x, y, walkable):
        self.nodes[x][y].walkable = walkable

    def get_nonwalkable_nodes(self):
        nonwalkable_nodes = []
        for node_row in self.nodes:
            for node in node_row:
                if node.walkable == False:
                    x, y = node.x, node.y
                    nonwalkable_nodes.append((x, y))
        return nonwalkable_nodes

    def draw(self, win):
        for row in self.nodes:
            for node in row:
                x, y = node.x, node.y
                rec = Rectangle(Point(x, y), Point(x+1, y+1))
                rec.setOutline("black")
                rec.draw(win)

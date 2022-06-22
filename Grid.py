from Node import Node


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.nodes = self.build_nodes(width, height)

    def build_nodes(self, width, height):
        return [[Node(x, y, walkable=True) for y in range(height)]
                for x in range(width)]

    def get_node_at(self, x, y):
        return self.nodes[x][y]

    def is_walkable_at(self, x, y):
        return self.is_inside(x, y) and self.nodes[x][y].walkable

    def is_inside(self, x, y):
        return (x >= 0 and x < self.width) and (y >= 0 and y < self.height)

    def set_walkable_at(self, x, y, walkable):
        self.nodes[x][y].walkable = walkable

    def get_walkable_neighbors(self, node):
        x, y = node.x, node.y
        neighbors = []
        nodes = self.nodes

        # ↑
        if (self.is_walkable_at(x, y-1)):
            neighbors.append(neighbors.append(nodes[x][y-1]))

        # →
        if (self.is_walkable_at(x+1, y)):
            neighbors.append(nodes[x+1][y])

        # ↓
        if (self.is_walkable_at(x, y+1)):
            neighbors.append(nodes[x][y+1])

        # ←
        if (self.is_walkable_at(x-1, y)):
            neighbors.append(nodes[x-1][y])

        # ↖
        if (self.is_walkable_at(x-1, y-1)):
            neighbors.append(nodes[x-1][y-1])

        # ↗
        if (self.is_walkable_at(x+1, y-1)):
            neighbors.append(nodes[x+1][y-1])

        # ↘
        if (self.is_walkable_at(x+1, y+1)):
            neighbors.append(nodes[x+1][y+1])

        # ↙
        if (self.is_walkable_at(x-1, y+1)):
            neighbors.append(nodes[x-1][y+1])

        return neighbors

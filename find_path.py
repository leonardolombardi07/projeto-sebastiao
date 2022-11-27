from math import sqrt


def get_walkable_neighbours(current_node, nonwalkable_nodes):
    x, y = current_node

    # TODO: we should exclude neighbours that are out of the grid
    # maybe check if x and y are bigger than 0/positive?
    up = (x, y+1)
    up_right = (x+1, y+1)
    right = (x+1, y)
    down_right = (x+1, y-1)
    down = (x, y-1)
    down_left = (x-1, y-1)
    left = (x-1, y)
    up_left = (x-1, y+1)

    neighbours = [up, up_right, right, down_right,
                  down, down_left, left, up_left]

    for neighbour in neighbours:
        if neighbour in nonwalkable_nodes:
            neighbours.remove(neighbour)

    return neighbours


def get_shortest_distance_node(walkable_neighbours, destination):
    shortest_distance = 100000000000  # This could be infinity
    shortest_distance_node = None
    for neighbour in walkable_neighbours:
        x, y = neighbour
        dest_x, dest_y = destination
        dx, dy = dest_x-x, dest_y-y
        neighbour_distance = sqrt(dx**2 + dy**2)
        if neighbour_distance < shortest_distance:
            shortest_distance = neighbour_distance
            shortest_distance_node = neighbour

    if shortest_distance_node == None:
        raise Exception("Error: couldn't find shortest distance")
    else:
        return shortest_distance_node


def find_path(nonwalkable_nodes, origin, destination):
    path = [origin]
    current_node = origin

    while current_node != destination:
        walkable_neighbours = get_walkable_neighbours(
            current_node, nonwalkable_nodes)
        if len(walkable_neighbours) == 0:
            # Stuck. Non-existant path
            return []

        current_node = get_shortest_distance_node(
            walkable_neighbours, destination)
        path.append(current_node)

    return path

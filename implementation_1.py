from graphics import *
from Grid import Grid
from find_path import find_path
from time import sleep
from random import random
from math import floor
from constants import NUM_OF_COLUMNS, NUM_OF_ROWS, NODE_SIZE
from models import Basket, Dock, Harve, Tree


def create_docks(upper_dock_coords, lower_dock_coords,  win):
    width_in_num_of_nodes = 1

    end_upper_coords = [upper_dock_coords[0]+width_in_num_of_nodes,
                        upper_dock_coords[1]+width_in_num_of_nodes]
    upper_dock = Dock(upper_dock_coords, end_upper_coords)
    upper_dock.draw(win)

    end_lower_coords = [lower_dock_coords[0]+width_in_num_of_nodes,
                        lower_dock_coords[1]+width_in_num_of_nodes]
    lower_dock = Dock(lower_dock_coords, end_lower_coords)
    lower_dock.draw(win)


def create_tree(coords, grid, win):
    grid.set_walkable_at(coords[0], coords[1], False)

    width_in_num_of_nodes = 1
    end_coords = [coords[0]+width_in_num_of_nodes,
                  coords[1]+width_in_num_of_nodes]
    tree = Tree(coords, end_coords)
    tree.draw(win)


def create_robot(coords, win):
    width_in_num_of_nodes = 1
    end_coords = [coords[0]+width_in_num_of_nodes,
                  coords[1]+width_in_num_of_nodes]
    harve = Harve(coords, end_coords)
    harve.draw(win)
    return harve


def create_basket(coords, win):
    # Note: Not sure if this works with integer number of nodes
    radius_in_num_of_nodes = 1/2
    basket = Basket(coords, radius_in_num_of_nodes)
    basket.draw(win)
    return basket


def draw_grid(grid, win):
    for row in grid.nodes:
        for node in row:
            x, y = node.x, node.y
            rec = Rectangle(Point(x, y), Point(x+1, y+1))
            rec.setOutline("black")
            rec.draw(win)


def gridnodes_to_maze(nodes):
    maze = []
    for i in range(len(nodes)):
        maze.append([])
        node_row = nodes[i]
        for node in node_row:
            number = 0 if node.walkable == True else 1
            maze[i].append(number)
    return maze


def implementation_1():
    grid = Grid(NUM_OF_COLUMNS, NUM_OF_ROWS)
    win = GraphWin("Implementação 1", NUM_OF_COLUMNS *
                   NODE_SIZE, NUM_OF_ROWS*NODE_SIZE)
    win.setCoords(0, 0, NUM_OF_COLUMNS, NUM_OF_ROWS)

    # For development purposes only
    draw_grid(grid, win)

    upper_dock_coords, lower_dock_coords = (
        0, 0), (NUM_OF_COLUMNS-1, NUM_OF_ROWS-1)
    create_docks(upper_dock_coords, lower_dock_coords, win)

    # Note: this only the center if the number of columns and
    # number of rows is even
    center = [floor(NUM_OF_COLUMNS/2), floor(NUM_OF_ROWS/2)]
    create_tree(center, grid, win)

    while True:
        click = win.getMouse()

        destination = (floor(click.getX()), floor(click.getY()))
        basket = create_basket(destination, win)

        origin = upper_dock_coords if random() > 0.5 else lower_dock_coords
        robot = create_robot(origin, win)

        maze = gridnodes_to_maze(grid.nodes)
        path_to_basket = find_path(maze, origin, destination)
        for coords in path_to_basket:
            robot.move_to(coords)
            if coords == destination:
                sleep(2)
                basket.undraw()
                break

            sleep(0.2)

        path_to_origin = find_path(maze, destination, origin)
        for coords in path_to_origin:
            robot.move_to(coords)
            if coords == origin:
                break

            sleep(0.2)


implementation_1()

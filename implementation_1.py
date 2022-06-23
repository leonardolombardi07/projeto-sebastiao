from graphics import *
from Grid import Grid
from find_path import find_path
from time import sleep
from random import random
from math import floor
from constants import NUM_OF_COLUMNS, NUM_OF_ROWS, NODE_SIZE
from models import Basket, Dock, Harve, Tree


def create_docks(upper_dock_coords, lower_dock_coords,  win):
    end_upper_coords = [upper_dock_coords[0]+1,
                        upper_dock_coords[1]+1]
    upper_dock = Dock(upper_dock_coords, end_upper_coords)
    upper_dock.draw(win)

    end_lower_coords = [lower_dock_coords[0]+1,
                        lower_dock_coords[1]+1]
    lower_dock = Dock(lower_dock_coords, end_lower_coords)
    lower_dock.draw(win)


def create_tree(grid, win):
    # Note: this only the center if the number of columns and
    # number of rows is even
    coords = [floor(NUM_OF_COLUMNS/2), floor(NUM_OF_ROWS/2)]
    grid.set_walkable_at(coords[0], coords[1], False)
    end_coords = [coords[0]+1,
                  coords[1]+1]
    tree = Tree(coords, end_coords)
    tree.draw(win)


def create_robot(coords, win):
    end_coords = [coords[0]+1,
                  coords[1]+1]
    harve = Harve(coords, end_coords)
    harve.draw(win)
    return harve


def create_basket(coords, win):
    # Note: Not sure if this works with integer number of nodes
    basket = Basket(coords, 1/2)
    basket.draw(win)
    return basket


def implementation_1():
    grid = Grid(NUM_OF_COLUMNS, NUM_OF_ROWS)
    win = GraphWin("Implementação 1", NUM_OF_COLUMNS *
                   NODE_SIZE, NUM_OF_ROWS*NODE_SIZE)
    win.setCoords(0, 0, NUM_OF_COLUMNS, NUM_OF_ROWS)
    grid.draw(win)

    upper_dock_coords, lower_dock_coords = (
        0, 0), (NUM_OF_COLUMNS-1, NUM_OF_ROWS-1)
    create_docks(upper_dock_coords, lower_dock_coords, win)
    create_tree(grid, win)

    origin = upper_dock_coords if random() > 0.5 else lower_dock_coords
    robot = create_robot(origin, win)

    while True:
        click = win.getMouse()
        destination = (floor(click.getX()), floor(click.getY()))
        basket = create_basket(destination, win)
        nonwalkable_nodes = grid.get_nonwalkable_nodes()
        path_to_basket = find_path(nonwalkable_nodes, origin, destination)
        for coords in path_to_basket:
            robot.move_to(coords)
            if coords == destination:
                sleep(2)
                basket.undraw()
                break
            sleep(0.2)

        path_to_origin = list(reversed(path_to_basket))
        for coords in path_to_origin:
            robot.move_to(coords)
            if coords == origin:
                break
            sleep(0.2)


implementation_1()

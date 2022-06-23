from graphics import *
from Grid import Grid
from find_path import find_path
from time import sleep
from random import random
from math import floor
from constants import NUM_OF_COLUMNS, NUM_OF_ROWS, NODE_SIZE
from models import Basket, Bush, Dock, Grass, Harve, Stone, Tree


def create_docks(upper_dock_coords, lower_dock_coords,  win):
    end_upper_coords = [upper_dock_coords[0]+1,
                        upper_dock_coords[1]+1]
    upper_dock = Dock(upper_dock_coords, end_upper_coords)
    upper_dock.draw(win)

    end_lower_coords = [lower_dock_coords[0]+1,
                        lower_dock_coords[1]+1]
    lower_dock = Dock(lower_dock_coords, end_lower_coords)
    lower_dock.draw(win)


def create_obstacles(grid, win):
    # Note: this only the center if the number of columns and
    # number of rows is even
    tree_coords = [floor(NUM_OF_COLUMNS/2), floor(NUM_OF_ROWS/2)]
    tree_coords_end = [floor(NUM_OF_COLUMNS/2)+1, floor(NUM_OF_ROWS/2)+1]
    tree = Tree(tree_coords, tree_coords_end)
    grid.set_walkable_at(tree_coords[0], tree_coords[1], False)
    tree.draw(win)

    stone_coords = [3, 9]
    stone_coords_end = [4, 10]
    stone = Stone(stone_coords, stone_coords_end)
    grid.set_walkable_at(stone_coords[0], stone_coords[1], False)
    stone.draw(win)

    bush_coords = [5, 2]
    bush = Bush(bush_coords, 1/2)
    grid.set_walkable_at(bush_coords[0], bush_coords[1], False)
    bush.draw(win)

    grass_1_coords = [9, 7]
    grass_1_coords_end = [10, 8]
    grass_1 = Grass(grass_1_coords, grass_1_coords_end)
    grid.set_walkable_at(grass_1_coords[0], grass_1_coords[1], False)
    grass_1.draw(win)

    grass_2_coords = [2, 5]
    grass_2_coords_end = [3, 6]
    grass_2 = Grass(grass_2_coords, grass_2_coords_end)
    grid.set_walkable_at(grass_2_coords[0], grass_2_coords[1], False)
    grass_2.draw(win)


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


def implementation_2():
    grid = Grid(NUM_OF_COLUMNS, NUM_OF_ROWS)
    win = GraphWin("Implementação 2", NUM_OF_COLUMNS *
                   NODE_SIZE, NUM_OF_ROWS*NODE_SIZE)
    win.setCoords(0, 0, NUM_OF_COLUMNS, NUM_OF_ROWS)
    grid.draw(win)

    upper_dock_coords, lower_dock_coords = (
        0, 0), (NUM_OF_COLUMNS-1, NUM_OF_ROWS-1)
    create_docks(upper_dock_coords, lower_dock_coords, win)
    create_obstacles(grid, win)

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
                robot.decrease_battery()
                break
            sleep(0.2)

        path_to_origin = list(reversed(path_to_basket))
        for coords in path_to_origin:
            robot.move_to(coords)
            if coords == origin:
                robot.recharge_battery()
                break
            sleep(0.2)


implementation_2()

from graphics import *

from time import sleep
from math import floor
from random import random

from constants import NUM_OF_COLUMNS, NUM_OF_ROWS, NODE_SIZE
from find_path import find_path

from models.Shapes import Basket, Bush, Dock, Grass, Stone, Tree
from models.Harve import Harve
from models.Grid import Grid


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


def create_text_instruction(win):
    text = "Click anywhere on the window to create a basket and press enter for the robot to catch all the baskets"
    text_object = Text(Point(5.5, 3.5), text)
    text_object.setSize(10)
    text_object.draw(win)
    return text_object


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
    text_instruction = create_text_instruction(win)

    origin = upper_dock_coords if random() > 0.5 else lower_dock_coords
    robot = create_robot(origin, win)

    def catch_basket(origin, destination, path_to_basket, basket):
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

    while True:
        paths, baskets, destinations = [], [], []
        nonwalkable_nodes = grid.get_nonwalkable_nodes()

        while True:
            key = win.checkKey()
            click = win.checkMouse()

            if key == "Return":
                break

            if click == None:
                continue

            destination = (floor(click.getX()), floor(click.getY()))
            if destination in [*nonwalkable_nodes, upper_dock_coords, lower_dock_coords]:
                continue

            text_instruction.undraw()
            destinations.append(destination)

            basket = create_basket(destination, win)
            baskets.append(basket)

            path_to_basket = find_path(nonwalkable_nodes, origin, destination)
            paths.append(path_to_basket)

        for i, destination in enumerate(destinations):
            path, basket = paths[i], baskets[i]
            catch_basket(origin, destination, path, basket)

        win.close()
        break

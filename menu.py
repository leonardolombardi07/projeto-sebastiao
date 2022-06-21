from graphics import *
from implementation_1 import implementation_1
from implementation_2 import implementation_2
from implementation_3 import implementation_3
from implementation_4 import implementation_4

from units import WINDOW_WIDTH, WINDOW_HEIGHT, pc_h, px


def create_implementation_button(y, text, win):
    button = Rectangle(Point(30, y), Point(70, y + px(40)))
    button.setFill(color_rgb(50, 100, 200))
    button.setOutline("black")
    button.draw(win)
    button_text = Text(Point(50, y + px(20)), text)
    button_text.draw(win)


def menu():
    win = GraphWin("Menu", WINDOW_WIDTH, WINDOW_HEIGHT)
    win.setBackground("white")
    win.setCoords(0, 0, 100, 100)

    Text(Point(50, 90), "Escolha uma implementação").draw(win)
    create_implementation_button(75, "1a Implementação", win)
    create_implementation_button(55, "2a Implementação", win)
    create_implementation_button(35, "3a Implementação", win)
    create_implementation_button(15, "4a Implementação", win)

    while True:
        click = win.getMouse()
        click_x, click_y = click.getX(), click.getY()

        if 30 < click_x < 70:
            if 75 < click_y < 75+pc_h(40):
                win.close()
                implementation_1()
                break

            if 55 < click_y < 55+pc_h(40):
                win.close()
                implementation_2()
                break

            if 35 < click_y < 35+pc_h(40):
                win.close()
                implementation_3()
                break

            if 15 < click_y < 15+pc_h(40):
                win.close()
                implementation_4()
                break


menu()

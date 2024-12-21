from graphics import Window 
from point import *
from line import *
from cell import *


def main():
    win = Window(800,600)
    cell_1 = Cell(win)
    cell_1.draw(10, 90, 90, 10)
    
    # point_a = Point(90, 40)
    # point_b = Point(80, 30)
    # new_line = Line(point_a, point_b)
    # win.draw_line(new_line, "orange")
    win.wait_for_close()
    
if __name__ == "__main__":
    main()
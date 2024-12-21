from line import *
from point import *

""" The cell classis a datatype that
tries to represent a graphic square drawn on the window.
It has 4 attributes that determines if 
any one of its four edges is visible at any given time
and a set of private attributes that determines the point in space
of all four 'corners' of the square and a window object that it draws on"""

class Cell():
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.win = window
        self.visited = False
        
    def draw(self , x1, x2, y1, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        
        if self.has_left_wall:
            point_1 = Point(self._x1, self._y1)
            point_2 = Point(self._x1, self._y2)
            left_line = Line(point_1, point_2)
            self.win.draw_line(left_line)
        
        if self.has_right_wall:
            point_1 = Point(self._x2, self._y1)
            point_2 = Point(self._x2, self._y2)
            right_line = Line(point_1, point_2)
            self.win.draw_line(right_line)
            
        if self.has_top_wall:
            point_1 = Point(self._x1, self._y1)
            point_2 = Point(self._x2, self._y1)
            top_line = Line(point_1, point_2)
            self.win.draw_line(top_line)
            
        if self.has_bottom_wall:
            point_1 = Point(self._x1, self._y2)
            point_2 = Point(self._x2, self._y2)
            bottom_line = Line(point_1, point_2)
            self.win.draw_line(bottom_line)
            
    def draw_move(self, to_cell, undo = False):
        """ The idea behind this method is to have it draw a line from the
        center position of the cell, to the center of another cell(to_cell). It takes 
        an 'undo' optional argument that could either be True or False where if the 
        undo is true, the color of the line to be drawn should be 'red' and 'gray'
        otherwise"""
        half_width = abs(self._x1 - self._x2) // 2
        half_length = abs(self._y1 - self._y2) // 2
        x_center = half_width + self._x1
        y_center = half_length + self._y1
        
        to_cell_half_width = abs(to_cell._x1 - to_cell._x2) // 2
        to_cell_half_length = abs(to_cell._y1 - to_cell._y2) // 2
        to_cell_x_center = to_cell_half_width + to_cell._x1
        to_cell_y_center = to_cell_half_length + to_cell._y1
        
        line_color = ""
        if not undo:
            line_color = "red"
        else:
            line_color = "grey"
            
        path_line = Line(Point(x_center, y_center),
                         Point(to_cell_x_center,to_cell_y_center))
        
        self.win.draw_line(path_line, line_color)
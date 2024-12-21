from tkinter import Tk, BOTH, Canvas

""" A line takes two instances of 
a Point class. Its draw method takes the x and y 
coordinates of both Points, a Canvas object and a Fill Color
string. it uses the the Canvas objects 'create_line' method 
to draw a line to the Canvas object"""


class Line:
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b
    
    
    def draw(self, canvas, fill_color = "red"):
        canvas.create_line(self.point_a.x, self.point_b.x,
                           self.point_a.y, self.point_b.y,
                           fill = fill_color, width = 2)
        
        

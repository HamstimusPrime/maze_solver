from tkinter import Tk, BOTH, Canvas



class Window():
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.title("maze solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas =Canvas()
        self.__canvas.pack()
        self.__is_running = False
        
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
        
    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()
        print("window closed...")
            
    def close(self):
        self.__is_running = False
        
    def draw_line(self, line, fill_color = "green"):
        """The draw_line method takes an instance of a Line class(a line object)
        or a cell object, and a fill color as inputs and then calls the lines 
        'draw' method which takes a canvas (canvas is declared
        as a hidden attribute of the window class)as argument and fill color"""
        
        line.draw(self.__canvas, fill_color)
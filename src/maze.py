from cell import *
import time
import random

""" The maze class is responsible for
holding ALL of the cells in a given window in a 2D grid
made of a list of lists
[[x,x,x,x],
 [x,x,x,x],
 [x,x,x,x]]
It takes an x1 and y1 input(the position of the maze within the window), alongisde the number of rows,
columns, width and height of each cell(cell_size_x, and cell_size_y)
and a window object it would draw on
"""

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self.seed = seed
        if self.seed != None:
            self.seed = random.seed(self.seed) 
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
               
        
    def _create_cells(self):
        for i in range(self.num_cols):
            self._cells.append([])
            for _ in range(self.num_rows):
                self._cells[i].append(Cell(self.win))
                      
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)
                
    def _draw_cell(self, i, j):
        #cell size x1 would be the x position of the maze + the index of the cell * cell_size
        if self.win == None:
            return
        x_1 = self.x1 + (j * self.cell_size_x)
        x_2 = x_1 + self.cell_size_x
        y_1 = self.y1 + (i * self.cell_size_y)
        y_2 = y_1 + self.cell_size_y
        cell_lines = Line(Point(x_1, y_1), Point(x_2,y_2))
        cell_lines.draw(self.win)
        self._animate()
    
    def _animate(self):
        if self.win == None:
            return
        self.win.redraw()
        time.sleep(0.05)
        
    def _break_entrance_and_exit(self):
    
        entrance_cell = self._cells[0][0]   
        entrance_cell.has_top_wall = False
        self._draw_cell(0,0)
        
        exit_cell = self._cells[-1][-1]
        exit_cell.has_bottom_wall = False
        self._draw_cell(-1,-1)
        
    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            possible_moves = []
            
            if self._is_valid_cell(i - 1,j) and not self._cells[i - 1][j].visited:
                possible_moves.append((i - 1, j))
            
            if self._is_valid_cell(i + 1,j) and not self._cells[i + 1][j].visited:
                possible_moves.append((i + 1, j))
                
            if self._is_valid_cell(i, j - 1) and not self._cells[i][j - 1].visited:
                possible_moves.append((i,j - 1))
                
            if self._is_valid_cell(i,j + 1) and not self._cells[i][j + 1].visited:
                possible_moves.append((i,j + 1))
                
            if not possible_moves:
                self._draw_cell(i,j)
                return
            else:
                random_index = random.randrange(len(possible_moves))
                random_direction = possible_moves[random_index]
                
                #top
                if random_direction == (i - 1, j):
                    current_cell.has_top_wall = False
                    self._cells[i - 1][j].has_bottom_wall = False  
                    
                #bottom
                if random_direction == (i + 1, j):
                    current_cell.has_bottom_wall = False
                    self._cells[i + 1][j].has_top_wall = False
                    
                #left
                if random_direction == (i, j - 1):
                    current_cell.has_left_wall = False
                    self._cells[i][j - 1].has_right_wall = False
                    
                #right
                if random_direction == (i, j + 1):
                    current_cell.has_right_wall = False
                    self._cells[i][j + 1].has_left_wall = False
                    
                
                self._break_walls_r(random_direction[0], random_direction[1])
                
    def _is_valid_cell(self, i, j):
        valid_row =  i >= 0 and i < len(self._cells)
        valid_column = j >= 0 and j < len(self._cells[0])
        return valid_row and valid_column
    
    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False 
                
                
    def solve(self):
        self._solve_r(0, 0)
        
    def _solve_r(self, i , j):
        self._animate()
        
        self._cells[i][j].visited = True
        
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        
        if (
            i > 0
            and not self._cells[i][j].has_left_wall
            and not self._cells[i - 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        if (
            i < self.num_cols - 1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i + 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)
                
        if (
            j > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i][j - 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)
                
        if (
            j < self.num_rows - 1
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i][j + 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)
                
        return False
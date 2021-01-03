import pygame as py
from constants import*
import random

class Graphic:
    def __init__(self, win):
        self.win = win
    
    def draw_automatas(self, grid):
        for x in range(xCells):
            for y in range(yCells):
                if grid[x][y].state == True:
                    py.draw.rect(self.win, grid[x][y].color, (y * ASIZE, x * ASIZE, ASIZE, ASIZE))
                else:
                    py.draw.rect(self.win, BLACK, (y * ASIZE, x * ASIZE, ASIZE, ASIZE))
                # if random.random() >= 0.50:
                #     py.draw.rect(self.win, BLUE, (x * ASIZE, y * ASIZE, ASIZE, ASIZE))
                # else:
                #     py.draw.rect(self.win, BLACK, (x * ASIZE, y * ASIZE, ASIZE, ASIZE))
        py.display.update()
    
    



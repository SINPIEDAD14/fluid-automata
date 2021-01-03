# this file hold all the automatas
import random
from constants import*
import particles

class Automata:
    def __init__(self, xAddress, yAddress):
        self.state = False
        self.xAddress = xAddress
        self.yAddress = yAddress
        self.color = BLACK
    
    def follow_rules(self, grid):
        pass

    def _go_down(self, modifiedGrid, x,  y):
        modifiedGrid[x][y].state = False
        if modifiedGrid[x][y].color == BLUE:
             modifiedGrid[x + 1][y] = particles.Water(x + 1, y)
        else:
            modifiedGrid[x + 1][y] = particles.Sand(x + 1, y)        
        modifiedGrid[x + 1][y].state = True 
        return None
    
    def _go_left_or_right(self, modifiedGrid, x,  y):
        if random.random() >= 0.5:                                
            self._go_left(modifiedGrid, x, y)
        else:
            self._go_right(modifiedGrid, x, y)
        return None
    
    def _go_left(self, modifiedGrid, x,  y):
        modifiedGrid[x][y].state = False
        if modifiedGrid[x][y].color == BLUE:
            modifiedGrid[x + 1][y - 1] = particles.Water(x + 1, y - 1)
        else:
            modifiedGrid[x + 1][y - 1] = particles.Sand(x + 1, y - 1)

        modifiedGrid[x + 1][y - 1].state = True
        return None

    def _go_right(self, modifiedGrid, x,  y):
        modifiedGrid[x][y].state = False
        if modifiedGrid[x][y].color == BLUE:
            modifiedGrid[x + 1][y + 1] = particles.Water(x + 1, y + 1)
        else:
            modifiedGrid[x + 1][y + 1] = particles.Sand(x + 1, y + 1)
        modifiedGrid[x + 1][y + 1].state = True
        return None
    def _go_right_right(self, modifiedGrid, x,  y):
        modifiedGrid[x][y].state = False
        if modifiedGrid[x][y].color == BLUE:
            modifiedGrid[x][y + 1] = particles.Water(x, y + 1)
        else:
            modifiedGrid[x][y + 1] = particles.Sand(x, y + 1)
        modifiedGrid[x][y + 1].state = True
        return None
    def _go_left_left(self, modifiedGrid, x,  y):
        modifiedGrid[x][y].state = False
        if modifiedGrid[x][y].color == BLUE:
            modifiedGrid[x][y - 1] = particles.Water(x, y - 1)
        else:
            modifiedGrid[x][y - 1] = particles.Sand(x, y - 1)
        modifiedGrid[x][y - 1].state = True
        return None

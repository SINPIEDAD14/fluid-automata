# this class is a kind of automata
from automatas import*
import copy
from constants import*
import math

class Sand(Automata):  # this is an unimplemented automata of sand
    def __init__(self, xAddress, yAddress):
        super().__init__(xAddress, yAddress)
        self.color = BROWN
        self.id = 1
    
    def follow_rules(self, grid, saved_grids):
        if self.state == True:
            if self.yAddress == 0 or self.yAddress == yCells - 1:  # this is when we are in the borders
                # for the current position calculate how the particle will move
                try:
                    # if the square below the current one is empty go there
                    if (grid[self.xAddress + 1][self.yAddress].state == False):                        
                        self._go_down(grid, self.xAddress, self.yAddress)
                    # if we are in the right border
                    elif (grid[self.xAddress + 1][self.yAddress - 1].state == False)  and (self.yAddress == yCells - 1):
                        self._go_left(grid, self.xAddress, self.yAddress)
                    # if we are in the left border
                    elif (grid[self.xAddress + 1][self.yAddress + 1].state == False)  and (self.yAddress == 0):
                        self._go_right(grid, self.xAddress, self.yAddress)
                except:
                    pass
            else:  # this is when we are out of the border
                # if the square below the current one is empty go there
                try:
                    if (grid[self.xAddress + 1][self.yAddress].state == False):                        
                        self._go_down(grid, self.xAddress, self.yAddress)
                    # if the left and right squares below are empty
                    elif ((grid[self.xAddress + 1][self.yAddress + 1].state == False) and (grid[self.xAddress + 1][self.yAddress - 1].state == False)):
                        self._go_left_or_right(grid, self.xAddress, self.yAddress)
                    # if the left square below is empty
                    elif (grid[self.xAddress + 1][self.yAddress - 1].state == False):
                        self._go_left(grid, self.xAddress, self.yAddress)
                    # if the right square below is empty
                    elif (grid[self.xAddress + 1][self.yAddress + 1].state == False):
                        self._go_right(grid, self.xAddress, self.yAddress)
                except:
                    pass
        return grid

class Water(Automata):
    def __init__(self, xAddress, yAddress, mass = 0):
        super().__init__(xAddress, yAddress)        
        self.mass = mass
        self.id = 2
        self.color = BLACK

    def save_color(self):
        self.color = (0, 0, int(255 - self.mass*60))

class Ground(Automata):
    def __init__(self, xAddress, yAddress):
        super().__init__(xAddress, yAddress)
        self.color = BROWN_GROUND
        self.id = 3
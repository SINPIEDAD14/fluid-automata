# this class represent the world where the automatas live in
import numpy as np
from constants import*
import particles
import automatas
import copy
import random

class World:
    def __init__(self):
        self.grid = []
        self.generate_new_grid()
        self.num_states = 0
    
    def test_automata(self):
        self.grid[0][0] = particles.Sand()
    
    def generate_new_grid(self):
        for x in range(xCells):
            self.grid.append([])
            for y in range(yCells):
                self.grid[x].append(automatas.Automata(x, y))

    def __str__(self):
        return str(self.grid)

    def live_one_step(self):
        # here we go over each element within our grid and make it follow the rules upon its type
        tempGrid = copy.deepcopy(self.grid)  # we hardcopy the actual state
        for x in range(xCells):
            for y in range(yCells):
                self.grid[x][y].follow_rules(tempGrid)
        self.grid = tempGrid
        self.num_states += 1

    def follow_rules_old(self):
        tempGrid = copy.deepcopy(self.grid)  # we hardcopy the actual state
        for x in range(xCells):
            for y in range(yCells):
                if self.grid[x][y].state == True:          
                    if y == 0 or y == yCells - 1:  # this is when we are in the borders
                        try:
                            # if the square below the current one is empty go there
                            if (self.grid[x + 1][y].state == False) :                        
                                self._go_down(tempGrid, x, y)
                            # if we are in the right border
                            elif (self.grid[x + 1][y - 1].state == False)  and (y == yCells - 1):
                                self._go_left(tempGrid, x, y)
                            # if we are in the left border
                            elif (self.grid[x + 1][y + 1].state == False)  and (y == 0):
                                self._go_right(tempGrid, x, y)
                        except:
                            continue
                    else:  # this is when we are out of the border
                        # if the square below the current one is empty go there
                        try:
                            if (self.grid[x + 1][y].state == False):                        
                                self._go_down(tempGrid, x, y)
                            # if the left and right squares below are empty
                            elif ((self.grid[x + 1][y + 1].state == False) and (self.grid[x + 1][y - 1].state == False)) :
                                self._go_left_or_right(tempGrid, x, y)
                            # if the left square below is empty
                            elif (self.grid[x + 1][y - 1].state == False):
                                self._go_left(tempGrid, x, y)
                            # if the right square below is empty
                            elif (self.grid[x + 1][y + 1].state == False):
                                self._go_right(tempGrid, x, y)
                            # if all bellow is occupied go right or left
                            elif (self.grid[x][y + 1].state == False):
                                self._go_right_right(tempGrid, x, y)
                            elif (self.grid[x][y - 1].state == False):
                                self._go_left_left(tempGrid, x, y)
                        except:
                            continue
        self.grid = tempGrid
        
    def make_alive(self, xPos, yPos, particle_type):
        if particle_type[0] == 1:
            self.grid[xPos][yPos] = particles.Sand(xPos, yPos)
        else:
            self.grid[xPos][yPos] = particles.Water(xPos, yPos)
        self.grid[xPos][yPos].state = True
        print(particle_type[0])
        return None
'''
    def _go_down(self, modifiedGrid, x,  y):
        modifiedGrid[x][y].state = False
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
        modifiedGrid[x + 1][y - 1].state = True
        return None

    def _go_right(self, modifiedGrid, x,  y):
        modifiedGrid[x][y].state = False
        modifiedGrid[x + 1][y + 1].state = True
        return None
    def _go_right_right(self, modifiedGrid, x,  y):
        modifiedGrid[x][y].state = False
        modifiedGrid[x][y + 1].state = True
        return None
    def _go_left_left(self, modifiedGrid, x,  y):
        modifiedGrid[x][y].state = False
        modifiedGrid[x][y - 1].state = True
        return None

        '''
    


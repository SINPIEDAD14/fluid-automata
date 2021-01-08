# this class represent the world where the automatas live in
import numpy as np
from constants import*
import particles
import automatas
import copy
import random
import math

class World:
    MINFLOW = 0.01
    MAXSPEED = 1
    def __init__(self):
        self.grid = []        
        self.flow = 0
        self.max_mass = 1
        self.max_compress = 0.02
        self.generate_new_grid()  # create a new world        
    
    def test_automata(self):
        ''' this is to test our class'''
        self.grid[0][0] = particles.Sand()
    
    def generate_new_grid(self):
        ''' this generate the new world iterating over the whole grid'''
        for x in range(xCells):
            self.grid.append([])
            for y in range(yCells):
                self.grid[x].append(automatas.Automata(x, y))
    
    def reinit(self):
        self.__init__()

    def __str__(self):
        '''return the grid'''
        return str(self.grid)

    def live_one_step(self):
        ''' here we go over each element within our grid and make it follow the rules upon its type'''
        tempGrid = copy.deepcopy(self.grid)  # we hardcopy the actual state
        for x in range(xCells):
            for y in range(yCells):
                if self.grid[x][y].id != 2: continue  # if the cell is not water move on
                self.follow_rules(tempGrid, x, y)
                
        self.transform_into_air(tempGrid)  # clean the grid from water elements with almost no water
        self.generate_colors(tempGrid)  # paint every cell with a color corresponding to its mass
        self.grid = tempGrid
    
    def generate_colors(self, aGrid):
        ''' we go through every automata and give it its color'''
        for x in range(xCells):
            for y in range(yCells):
                if aGrid[x][y].id == 2:
                    aGrid[x][y].save_color()
    
    def follow_rules(self, grid, xAddress, yAddress):
        ''' rules for water, for the current position calculate how the particle will move'''
        self.flow = 0            
        if (xAddress + 1 < xCells):
            if (grid[xAddress + 1][yAddress].id != 3):  # if the square below the current one is empty go there                        
                self._go_down(xAddress, yAddress, grid)
        if grid[xAddress][yAddress].mass <= 0:
            return grid  # this is to exit the function if there is no flow remaining
        
        if (yAddress != 0): # if we are not in the left border
            if (grid[xAddress][yAddress - 1].id != 3):
                self._go_left(xAddress, yAddress, grid)
        if grid[xAddress][yAddress].mass <= 0:
            return grid  # this is to exit the function if there is no flow remaining
        # if we are not in the right border
        if (yAddress != yCells - 1):                    
            if (grid[xAddress][yAddress + 1].id != 3):
                self._go_right(xAddress, yAddress, grid)
        if grid[xAddress][yAddress].mass <= 0: 
            return grid  # this is to exit the function if there is no flow remaining
        # go up if the lower cell is too full
        if (xAddress != 0):
            if (grid[xAddress - 1][yAddress].id != 3):
                self._go_up(xAddress, yAddress, grid)
        return grid
        
    def make_alive(self, xPos, yPos, particle_type):
        ''' this makes a cell alive once we clicked it'''
        if particle_type[0] == 1:
            self.grid[xPos][yPos] = particles.Ground(xPos, yPos)
        else:
            self.grid[xPos][yPos] = particles.Water(xPos, yPos, 1)
        return None
    
    def transform_into_air(self, aGrid):
        ''' this will loop through the grid and transform those particle with too litle water into air'''
        for x in range(xCells):
            for y in range(yCells):
                if aGrid[x][y].id == 3 or aGrid[x][y].id == 0:
                    continue
                else:
                    if aGrid[x][y].mass < 0.001:
                        aGrid[x][y] = automatas.Automata(x, y)
        return None

    def _go_down(self, x,  y, grid):            
            if grid[x + 1][y].id != 2: # if the cell is not water
                grid[x + 1][y] = particles.Water(x + 1, y)
            self.flow = self._get_stable(grid[x][y].mass + grid[x + 1][y].mass) - grid[x + 1][y].mass
            if self.flow > self.MINFLOW:
                self.flow *= 0.6
            self.flow = self.constrain(self.flow, 0, min(self.MAXSPEED, grid[x][y].mass))
            grid[x][y].mass -= self.flow
            grid[x + 1][y].mass += self.flow
            return None

    def _go_left(self, x,  y, grid):        
        if grid[x][y - 1].id != 2: # if the cell is not water
            grid[x][y - 1] = particles.Water(x, y - 1)
        self.flow = (grid[x][y].mass - grid[x][y - 1].mass) / 4
        if self.flow > self.MINFLOW:
            self.flow *= 0.6
        self.flow = self.constrain(self.flow, 0, grid[x][y].mass)
        grid[x][y].mass -= self.flow
        grid[x][y - 1].mass += self.flow
        return None

    def _go_right(self, x,  y, grid):
        if grid[x][y + 1].id != 2:
            grid[x][y + 1] = particles.Water(x, y + 1)
        self.flow = (grid[x][y].mass - grid[x][y + 1].mass) / 4
        if self.flow > self.MINFLOW:
            self.flow *= 0.6
        self.flow = self.constrain(self.flow, 0, grid[x][y].mass)
        grid[x][y].mass -= self.flow
        grid[x][y + 1].mass += self.flow
        return None
    
    def _go_up(self, x,  y, grid):
        if grid[x - 1][y].id != 2:
            grid[x - 1][y] = particles.Water(x - 1, y)
        self.flow = grid[x][y].mass - self._get_stable(grid[x][y].mass + grid[x - 1][y].mass)
        if self.flow > self.MINFLOW:
            self.flow *= 0.6
        self.flow = self.constrain(self.flow, 0, grid[x][y].mass)
        grid[x][y].mass -= self.flow
        grid[x - 1][y].mass += self.flow
        return None

    
    def _get_stable(self, total_mass):
        if total_mass <= 1: return 1
        elif total_mass < 2 * self.max_mass + self.max_compress:
            stable = (math.pow(self.max_mass, 2) + total_mass * self.max_compress) / (self.max_mass + self.max_compress)
            return stable
        else:
            stable = (total_mass + self.max_compress) / 2
            return stable
    
    def constrain(self, num, min, max):
        ''' to constrain a value within a range'''
        if num < min:
            return 0
        elif num >= max:
            return max
        else:
            return num

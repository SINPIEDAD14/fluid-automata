# this file hold all the automatas
import random
from constants import*
import particles

class Automata:
    def __init__(self, xAddress, yAddress):
        self.xAddress = xAddress
        self.yAddress = yAddress
        self.color = BLACK
        self.id = 0
        self.mass = 0


import random
from tkinter import *

class Die:
    active = True
    number_of_sides: int
    def __init__(self,n):
        self.number_of_sides = n

    def roll(self):
        if self.active:
            return round(random.uniform(1,self.number_of_sides)+0.5)
        else:
            return
import pygame

from constants import *
from Node import Node


class Grid(list):
    def __init__(self):
        self.sideLength = 20
        
        for yCord in range(0, RESOLUTION[1], self.sideLength):
            row = int(yCord / self.sideLength)
            super().append([])
            
            for xCord in range(0, RESOLUTION[0], self.sideLength):
                col = int(xCord / self.sideLength)
                super().__getitem__(row).append(Node(xCord, yCord, self.sideLength, self.sideLength))
            
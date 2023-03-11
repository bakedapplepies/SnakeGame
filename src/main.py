import pygame
import time
import sys

from constants import *
from Grid import Grid


class Window(pygame.Surface):
    def __init__(self):
        # window setup
        pygame.init()
        pygame.Surface.__init__(self, RESOLUTION)
        
        # window variables
        self.begin = 0
        self.deltaTime = 0
        self.collectiveTimePerSec = 0
        self.currentFPS = 0
        self.running = True
        
        # game objects
        self.grid = Grid()
        
        pygame.display.set_caption("Snake Game")
        self.pygame_window: pygame.Surface = pygame.display.set_mode(RESOLUTION)
        
    def calculateFPS(self, deltaTime):
        self.currentFPS += 1
        self.collectiveTimePerSec += deltaTime
        if self.collectiveTimePerSec >= 1:
            self.showFPS()
            self.collectiveTimePerSec = 0
            self.currentFPS = 0
            
    def showFPS(self):
        pygame.display.set_caption(f"Snake Game - FPS: {self.currentFPS}")
        
    def Loop(self):
        while self.running:
            self.calculateFPS(self.deltaTime)
            self.deltaTime = time.time() - self.begin
            self.begin = time.time()
            
            self.PollInput()
            
            self. Render()
            pygame.display.update()
        
    def Render(self):
        self.pygame_window.fill(BLACK)
        
        # draw grid
        for row in self.grid:
            for node in row:
                pygame.draw.rect(self.pygame_window, WHITE, node, 1)
        
        self.blit(self.pygame_window, (0, 0))
    
    def PollInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or not self.running:
                pygame.quit()
                sys.exit()
    
    
if __name__ == "__main__":
    window = Window()
    window.Loop()
    
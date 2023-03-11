import pygame


class Node(pygame.Rect):
    def __init__(self, x, y, dx, dy):
        super().__init__(x, y, dx, dy)
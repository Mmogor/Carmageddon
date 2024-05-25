import random

import pygame
class House:
    def __init__(self, screen, img, x, y):
        zahlen = [0, 90, 180, 270]
        self.screen = screen
        self.img = pygame.transform.rotate(img, random.choice(zahlen))
        self.offset = 2
        self.x = x
        self.y = y

    def draw(self):

        self.screen.blit(self.img, (self.offset + self.x, self.offset + self.y))

import random

import pygame

from objects.car import Car


class House:
    def __init__(self, screen, img, x, y):
        zahlen = [0, 90, 180, 270]
        self.screen = screen
        self.img = pygame.transform.rotate(img, random.choice(zahlen))
        self.offset = 2
        self.x = x
        self.y = y
        self.streets = []
        self.cars = []

    def draw(self):
        self.screen.blit(self.img, (self.offset + self.x, self.offset + self.y))
        for car in self.cars:
            car.draw()

    def add_street(self, street):
        self.streets.append(street)

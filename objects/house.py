import random

import pygame
from utils.assets import house_red_img, house_blue_img


class House:
    def __init__(self, screen, color, x, y):
        zahlen = [0, 90, 180, 270]
        self.img = [house_red_img, house_blue_img]
        self.screen = screen
        self.img = pygame.transform.rotate(self.img[color.value - 1], random.choice(zahlen))
        self.color = color
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

import pygame

from utils.assets import *


class Street:
    def __init__(self, screen, img, x, y):
        self.screen = screen
        self.img = img
        self.offset_x = 12.5
        self.offset_y = 0
        self.x = x
        self.y = y
        self.r = False
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None

    def add_top(self, top):
        self.top = top

    def add_bottom(self, bottom):
        self.bottom = bottom

    def add_left(self, left):
        self.left = left

    def add_right(self, right):
        self.right = right

    def draw(self):
        self.screen.blit(self.img, (self.offset_x + self.x, self.offset_y + self.y))

    def rotate(self, n):
        self.r = True
        self.img = pygame.transform.rotate(self.img, 90 * n)
        self.offset_x = 0
        self.offset_y = 12.5

    def check(self, streets, houses):
        self.reset()

        for house in houses:
            if house.x == self.x:
                if house.y + 50 == self.y:
                    self.top = house
                elif house.y - 50 == self.y:
                    self.bottom = house
            elif house.y == self.y:
                if house.x + 50 == self.x:
                    self.left = house
                elif house.x - 50 == self.x:
                    self.right = house

        for street in streets:
            if street.x == self.x:
                if street.y + 50 == self.y:
                    self.top = street
                elif street.y - 50 == self.y:
                    self.bottom = street
            elif street.y == self.y:
                if street.x + 50 == self.x:
                    self.left = street
                elif street.x - 50 == self.x:
                    self.right = street

        if self.top is not None and self.bottom is not None and self.left is not None and self.right is not None:
            self.img = junction_img
            self.offset_x = 0
            self.offset_y = 0
            if type(self.right) is Street and not self.right.r:
                self.right.rotate(1)
            if type(self.right) is Street and not self.left.r:
                self.left.rotate(1)
        elif self.top is not None and self.right is not None and self.bottom is not None:
            self.img = t_junction_img
            self.rotate(1)
            self.offset_x = 12.5
            self.offset_y = 0
            if type(self.right) is Street and not self.right.r:
                self.right.rotate(1)
        elif self.right is not None and self.bottom is not None and self.left is not None:
            self.img = t_junction_img
            self.offset_x = 0
            self.offset_y = 12.5
            if type(self.right) is Street and not self.right.r:
                self.right.rotate(1)
            if type(self.right) is Street and not self.left.r:
                self.left.rotate(1)
        elif self.bottom is not None and self.left is not None and self.top is not None:
            self.img = t_junction_img
            self.rotate(3)
            self.offset_x = 0
            self.offset_y = 0
            if type(self.right) is Street and not self.left.r:
                self.left.rotate(1)
        elif self.left is not None and self.top is not None and self.right is not None:
            self.img = t_junction_img
            self.rotate(2)
            self.offset_x = 0
            self.offset_y = 0
            if type(self.right) is Street and not self.right.r:
                self.right.rotate(1)
            if type(self.right) is Street and not self.left.r:
                self.left.rotate(1)
        elif self.top is not None and self.right is not None:
            self.img = corner_img
            self.offset_x = 12.5
            self.offset_y = 0
            if type(self.right) is Street and not self.right.r:
                self.right.rotate(1)
        elif self.right is not None and self.bottom is not None:
            self.img = corner_img
            self.rotate(3)
            self.offset_x = 12.5
            self.offset_y = 12.5
            if type(self.right) is Street and not self.right.r:
                self.right.rotate(1)
        elif self.bottom is not None and self.left is not None:
            self.img = corner_img
            self.rotate(2)
            self.offset_x = 0
            self.offset_y = 12.5
            if type(self.right) is Street and not self.left.r:
                self.left.rotate(1)
        elif self.left is not None and self.top is not None:
            self.img = corner_img
            self.rotate(1)
            self.offset_x = 0
            self.offset_y = 0
            if type(self.right) is Street and not self.left.r:
                self.left.rotate(1)

    def reset(self):
        self.img = street_img
        self.offset_x = 12.5
        self.offset_y = 0
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None

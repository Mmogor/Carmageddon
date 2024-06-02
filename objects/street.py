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
        self.c = False
        self.tj = False
        self.j = False

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

    def check(self):
        if self.top is not None and self.bottom is not None and self.left is not None and self.right is not None:
            self.img = junction_img
            self.offset_x = 0
            self.offset_y = 0
            self.j = True
            if type(self.right) is Street and not self.right.r:
                self.right.rotate(1)
            if type(self.left) is Street and not self.left.r:
                self.left.rotate(1)
        elif self.top is not None and self.right is not None and self.bottom is not None:
            self.img = t_junction_img
            self.rotate(1)
            self.offset_x = 12.5
            self.offset_y = 0
            self.tj = True
            if type(self.right) is Street and not self.right.r:
                self.right.rotate(1)
        elif self.right is not None and self.bottom is not None and self.left is not None:
            self.img = t_junction_img
            self.offset_x = 0
            self.offset_y = 12.5
            self.tj = True
            if type(self.right) is Street and not self.right.r:
                self.right.rotate(1)
            if type(self.left) is Street and not self.left.r:
                self.left.rotate(1)
        elif self.bottom is not None and self.left is not None and self.top is not None:
            self.img = t_junction_img
            self.rotate(3)
            self.offset_x = 0
            self.offset_y = 0
            self.tj = True
            if type(self.left) is Street and not self.left.r:
                self.left.rotate(1)
        elif self.left is not None and self.top is not None and self.right is not None:
            self.img = t_junction_img
            self.rotate(2)
            self.offset_x = 0
            self.offset_y = 0
            self.tj = True
            if type(self.right) is Street and not self.right.r:
                self.right.rotate(1)
            if type(self.left) is Street and not self.left.r:
                self.left.rotate(1)
        elif self.top is not None and self.right is not None:
            self.img = corner_img
            self.offset_x = 12.5
            self.offset_y = 0
            self.c = True
            if type(self.right) is Street and not self.right.r:
                self.right.rotate(1)
        elif self.right is not None and self.bottom is not None:
            self.img = corner_img
            self.rotate(3)
            self.offset_x = 12.5
            self.offset_y = 12.5
            self.c = True
            if type(self.right) is Street and not self.right.r:
                self.right.rotate(1)
        elif self.bottom is not None and self.left is not None:
            self.img = corner_img
            self.rotate(2)
            self.offset_x = 0
            self.offset_y = 12.5
            self.c = True
            if type(self.left) is Street and not self.left.r:
                self.left.rotate(1)
        elif self.left is not None and self.top is not None:
            self.img = corner_img
            self.rotate(1)
            self.offset_x = 0
            self.offset_y = 0
            self.c = True
            if type(self.left) is Street and not self.left.r:
                self.left.rotate(1)

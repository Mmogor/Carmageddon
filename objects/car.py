import pygame


class Car:
    def __init__(self, screen, img, x, y, r):
        self.screen = screen
        self.img = img
        self.x = x
        self.y = y
        self.offset_x = 0
        self.offset_y = 0
        self.speed = 5
        if r:
            self.img = pygame.transform.rotate(self.img, 90)
            self.offset_y = 27
        else:
            self.offset_x = 27

    def draw(self):
        self.screen.blit(self.img, (self.offset_x + self.x, self.offset_y + self.y))

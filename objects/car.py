import pygame


class Car:
    def __init__(self, screen, img, color, _from, _to, x, y, r, house_x, house_y):
        self.screen = screen
        self.img = img
        self.color = color
        self._from = _from
        self._to = _to
        self.x = x
        self.y = y
        self.offset_x = 0
        self.offset_y = 0
        self.speed = 5
        if r:
            if house_x > x:
                self.offset_x = 30
                self.offset_y = 13
            else:
                self.offset_y = 27
            self.img = pygame.transform.rotate(self.img, 90)
        else:
            if house_y > y:
                self.offset_y = 30
                self.offset_x = 27
            else:
                self.offset_x = 13


    def draw(self):
        self.screen.blit(self.img, (self.offset_x + self.x, self.offset_y + self.y))

    def move(self):
        a_star.findPath(self._from, self._to, self.x, self.y)
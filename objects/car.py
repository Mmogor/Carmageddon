import random

import pygame

from objects.house import House


class Car:
    def __init__(self, screen, img, color, _from, _to, x, y, r, street, house_x, house_y):
        self.screen = screen
        self.img = img
        self.color = color
        self._from = _from
        self._to = _to
        self.x = x
        self.y = y
        self.dir = None
        self.temp_dir = int(random.uniform(1, 5))
        self.previous = _from
        self.street = street
        self.offset_x = 0
        self.offset_y = 0
        self.speed = 50

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

    def move(self, game):
        print(self.x, self.y)
        if self.street.j:
            self.dir = self.temp_dir
            if self.dir == 1:
                self.dir = 1
                self.y -= self.speed * (1 / 60)
                if self.y < self.street.top.y:
                    self.previous = self.street
                    self.street = self.street.top
                if type(self.street) is House and self._to is self.street:
                    game.score += 1
                    game.cars.remove(self)
                    del self
                else:
                    game.cars.remove(self)
                    del self
            elif self.dir == 2:
                self.dir = 2
                self.x += self.speed * (1 / 60)
                if self.x > self.street.right.x:
                    self.previous = self.street
                    self.street = self.street.right
                if type(self.street) is House and self._to is self.street:
                    game.score += 1
                    game.cars.remove(self)
                    del self
                else:
                    game.cars.remove(self)
                    del self
            elif self.dir == 3:
                self.dir = 3
                self.y += self.speed * (1 / 60)
                if self.y > self.street.bottom.y:
                    self.previous = self.street
                    self.street = self.street.bottom
                if type(self.street) is House and self._to is self.street:
                    game.score += 1
                    game.cars.remove(self)
                    del self
                else:
                    game.cars.remove(self)
                    del self
            elif self.dir == 4:
                self.dir = 4
                self.x -= self.speed * (1 / 60)
                if self.x < self.street.left.x:
                    self.previous = self.street
                    self.street = self.street.left
                if type(self.street) is House and self._to is self.street:
                    game.score += 1
                    game.cars.remove(self)
                    del self
                else:
                    game.cars.remove(self)
                    del self
        elif self.street.tj:
            pass
        elif self.street.c:
            pass
        elif self.street.r:
            if self._from.x > self.x:
                self.dir = 4
                self.x -= self.speed * (1 / 60)
                if self.x < self.street.left.x:
                    self.previous = self.street
                    self.street = self.street.left
                if type(self.street) is House and self._to is self.street:
                    game.score += 1
                    game.cars.remove(self)
                    del self
                else:
                    game.cars.remove(self)
                    del self
            else:
                self.dir = 2
                self.x += self.speed * (1 / 60)
                if self.x > self.street.right.x:
                    self.previous = self.street
                    self.street = self.street.right
                if type(self.street) is House and self._to is self.street:
                    game.score += 1
                    game.cars.remove(self)
                    del self
                else:
                    game.cars.remove(self)
                    del self
        else:
            if self._from.y < self.y:
                self.dir = 1
                self.y -= self.speed * (1 / 60)
                if self.y < self.street.top.y:
                    self.previous = self.street
                    self.street = self.street.top
                if type(self.street) is House and self._to is self.street:
                    game.score += 1
                    game.cars.remove(self)
                    del self
                else:
                    game.cars.remove(self)
                    del self
            else:
                self.dir = 3
                self.y += self.speed * (1 / 60)
                if self.y > self.street.bottom.y:
                    self.previous = self.street
                    self.street = self.street.bottom
                if type(self.street) is House and self._to is self.street:
                    game.score += 1
                    game.cars.remove(self)
                    del self
                else:
                    game.cars.remove(self)
                    del self

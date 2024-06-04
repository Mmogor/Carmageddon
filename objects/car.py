import pygame

from utils.assets import car_red_img, car_blue_img, car_purple_img, car_yellow_img


class Car:
    def __init__(self, screen, img, color, _from, _to, x, y, r, house_x, house_y, path):
        self.screen = screen
        self.imgs = [car_red_img, car_blue_img, car_yellow_img, car_purple_img]
        self.img = self.imgs[color.value - 1]
        self.color = color
        self._from = _from
        self._to = _to
        self.x = x
        self.y = y
        self.offset_x = 0
        self.offset_y = 0
        self.speed = 100
        self.path = path
        self.path_index = 2  # Start at the first point in the path
        print((_from.x, _from.y), (_to.x, _to.y), path)
        print(self.path[1:])
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

    def move(self, cars, game):
        # Check if path exists
        if not self.path:
            return  # No path available

        # Check if the car has reached its destination
        if self.path_index >= len(self.path):
            cars.remove(self)
            del self
            return

        # Get the next position in the path
        next_x, next_y = self.path[self.path_index]
        next_x *= 50
        next_y *= 50

        print("pos", (self.x, self.y), (next_x, next_y))

        # Check if the car has reached the next point
        if round(self.x) == next_x and round(self.y) == next_y:
            print(self.path_index)
            # Move to the next point in the path
            self.path_index += 1

            # Additional check to see if we have reached the final destination
            if self.path_index >= len(self.path):
                print("Car has reached its final destination.")
                game.score += abs(self._from.x - self._to.x) + abs(self._from.y - self._to.y)
                cars.remove(self)
                del self
                return

        # Calculate the direction to move (only in one axis)
        if self.x <= next_x:
            self.x += self.speed * (1 / 60)
        elif self.x >= next_x:
            self.x -= self.speed * (1 / 60)

        if self.y <= next_y:
            self.y += self.speed * (1 / 60)
        elif self.y >= next_y:
            self.y -= self.speed * (1 / 60)

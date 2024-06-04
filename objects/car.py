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
        self.path_index = 1  # Start at the first point in the path
        self.angle = 0  # Initialize the angle for the car's rotation

        # Calculate the initial angle based on the first path direction
        if len(self.path) > 1:
            next_x, next_y = self.path[1]
            next_x *= 50
            next_y *= 50
            dx = next_x - self.x
            dy = next_y - self.y

    def draw(self):
        rotated_img = pygame.transform.rotate(self.img, self.angle)
        self.screen.blit(rotated_img, (self.offset_x + self.x, self.offset_y + self.y))

    def move(self, cars, game):
        # Check if path exists
        if not self.path:
            return  # No path available

        # Check if the car has reached its destination
        if self.path_index >= len(self.path):
            cars.remove(self)
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
                return

            # Update angle to face the next point
            if self.path_index < len(self.path):
                next_x, next_y = self.path[self.path_index]
                next_x *= 50
                next_y *= 50
                dx = next_x - self.x
                dy = next_y - self.y
                self.angle = -pygame.math.Vector2(dx, dy).angle_to((1, 0))

        # Calculate the direction to move
        if round(self.x) < next_x:
            self.angle = 270
            self.offset_y = 27.5
            self.offset_x = 12.5
            self.x += self.speed * (1 / 60)
        elif round(self.x) > next_x:
            self.angle = 90
            self.offset_y = 12.5
            self.offset_x = 15
            self.x -= self.speed * (1 / 60)

        if round(self.y) < next_y:
            self.angle = 180
            self.offset_x = 12.5
            self.offset_y = 15
            self.y += self.speed * (1 / 60)
        elif round(self.y) > next_y:
            self.angle = 0
            self.offset_x = 27.5
            self.offset_y = 12.5
            self.y -= self.speed * (1 / 60)

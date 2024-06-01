import random

import config
from objects.house import House
from objects.street import Street
from utils.assets import house_img
from utils.assets import car_img
from utils.assets import street_img

street_counter = 0


class Scene:

    def __init__(self):
        self.last_car_spawn_time = 0

    def add_street(self, screen, runtime, streets, houses, x, y, game):
        if game.street_counter > 0:
            x -= x % config.GRID_SIZE
            y -= y % config.GRID_SIZE

            _r = False
            valid = True

            for st in streets:
                if st.x == x and st.y == y:
                    valid = False

            for house in houses:
                if house.x == x and house.y == y:
                    valid = False


        if valid:
            game.street_counter -= 1
            street = Street(screen, street_img, x, y)

            for house in houses:
                if house.y == y:
                    if house.x + config.GRID_SIZE == x:
                        house.add_street(street)
                        street.add_left(house)
                    elif house.x - config.GRID_SIZE == x:
                        house.add_street(street)
                        street.add_right(house)
                elif house.x == x:
                    if house.y + config.GRID_SIZE == y:
                        house.add_street(street)
                        street.add_top(house)
                    elif house.y - config.GRID_SIZE == y:
                        house.add_street(street)
                        street.add_bottom(house)


            for st in streets:
                if st.y == y:
                    if st.x + config.GRID_SIZE == x:
                        if st.r:
                            _r = True
                        st.add_right(street)
                        street.add_left(st)
                    if st.x - config.GRID_SIZE == x:
                        if st.r:
                            _r = True
                        st.add_left(street)
                        street.add_right(st)
                if st.x == x:
                    if st.y + config.GRID_SIZE == y:
                        st.add_bottom(street)
                        street.add_top(st)
                    if st.y - config.GRID_SIZE == y:
                        st.add_top(street)
                        street.add_bottom(st)

            if _r:
                street.rotate(1)

            street.check()

            if street.top is not None and type(street.top) is Street:
                street.top.check()
            if street.bottom is not None and type(street.bottom) is Street:
                street.bottom.check()
            if street.left is not None and type(street.left) is Street:
                street.left.check()
            if street.right is not None and type(street.right) is Street:
                street.right.check()

            print(type(street.top), street.bottom, street.left, street.right)
            streets.append(street)

    def update(self, game, screen, runtime, houses, streets):
        global street_counter
        if str(60 - (runtime // 1000)) == '0':
            street_counter += 10

        if len(houses) < config.MAX_HOUSES and runtime >= config.HOUSE_SPAWN_RATE:
            for i in (1, 2):
                find_x_y = True
                while find_x_y:
                    x = random.random() * config.SCREEN_WIDTH
                    x = x - (x % 50)
                    y = random.random() * config.SCREEN_HEIGHT
                    y = y - (y % 50)

                    find_x_y = False

                    for house in houses:
                        if house.x == x and house.y == y or house.x == x + 50 or house.x == x - 50 or house.y == y + 50 or house.y == y - 50:
                            find_x_y = True

                    for street in streets:
                        if street.x == x and street.y == y:
                            find_x_y = True

                houses.append(House(screen, house_img, x, y))

            game.reset_runtime()

            if runtime - self.last_car_spawn_time >= 2000:
                self.spawn_car_at_house(houses, car_img)
                self.last_car_spawn_time = runtime

    def spawn_car_at_house(self, houses, car_img):
        if houses:
            house = random.choice(houses)
            house.spawn_car(car_img)

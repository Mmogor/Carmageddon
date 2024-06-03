import random

import config
from a_star import a_star
from objects.car import Car
from objects.house import House
from objects.street import Street
from utils.assets import car_red_img
from utils.assets import street_img


class Scene:

    def __init__(self):
        pass

    def add_street(self, screen, runtime, streets, houses, x, y, game, grid):
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
                            _r = True
                            house.add_street(street)
                            street.add_left(house)
                        elif house.x - config.GRID_SIZE == x:
                            _r = True
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

                streets.append(street)
                grid[y // config.GRID_SIZE][x // config.GRID_SIZE] = 0
                print(grid)
                print

    def update(self, game, screen, runtime, houses, streets, cars, grid):
        if str(60 - (runtime // 1000)) == '0':
            game.street_counter += 10

        if len(houses) < config.MAX_HOUSES and runtime >= config.HOUSE_SPAWN_RATE:
            color = random.choice(list(config.Color))
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

                house = House(screen, color, x, y)
                houses.append(house)
                grid[int(y // config.GRID_SIZE)][int(x // config.GRID_SIZE)] = 0
                print(grid)
                print()

                for street in streets:
                    street.check()

                game.reset_runtime()

        if runtime % 2000 >= 1985:
            if houses:
                house_from = random.choice(houses)
                if house_from.streets:
                    street = random.choice(house_from.streets)
                    to = house_from
                    while to is house_from or to.color is not house_from.color:
                        to = random.choice(houses)

                    path = a_star.a_star((int(house_from.x // 50), int(house_from.y // 50)),
                                         (int(to.x // 50), int(to.y // 50)), grid)

                    if path:
                        car = Car(screen, car_red_img, house_from.color, house_from, to, street.x, street.y,
                                  street.r, house_from.x, house_from.y, path)

                        cars.append(car)
                        print(grid)

        for car in cars:
            car.move(cars, game)

    def remove_street(self, streets, houses, cars, x, y, game, grid):
        x -= x % config.GRID_SIZE
        y -= y % config.GRID_SIZE

        for street in streets:
            if street.x == x and street.y == y:
                if street.left is not None:
                    street.left.right = None
                if street.right is not None:
                    street.right.left = None
                if street.top is not None:
                    street.top.bottom = None
                if street.bottom is not None:
                    street.bottom.top = None

                for house in houses:
                    for st in house.streets:
                        if st is street:
                            house.streets.remove(st)
                            break

                for car in cars:
                    if car.x == x and car.y == y:
                        cars.remove(car)
                        del car
                        break

                streets.remove(street)
                grid[int(street.y // config.GRID_SIZE)][int(street.x // config.GRID_SIZE)] = 1

                print(game.grid)
                print()
                del street
                break

        game.street_counter += 1

        for street in streets:
            street.check()

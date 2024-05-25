import random

import config
from entities.house import House
from entities.street import Street
from utils.assets import house_img
from utils.assets import street_img

street_counter = 0


class Scene:

    def __init__(self):
        pass

    def add_street(self, screen, runtime, streets, houses, x, y):
        global street_counter
        if street_counter > 0:
            x -= x % 50
            y -= y % 50

            valid = True
            for st in streets:
                if st.x == x and st.y == y:
                    valid = False

            if valid:
                street_counter -= 1
                street = Street(screen, street_img, x, y)
                for house in houses:
                    if house.y == y and (house.x + 50 == x or house.x - 50 == x):
                        street.rotate()
                        house.add_street(street)
                    elif house.x == x and (house.y + 50 == y or house.y - 50 == y):
                        house.add_street(street)



                # for st in street:
                #     if st.x == x + 50 and st.y == y:
                #         st.upgrade()
                #     elif st.x == x - 50 and st.y == y:
                #         st.upgrade()

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

                houses.append(House(screen, house_img, x, y))

            game.reset_runtime()

import random

import pygame

import config
from entities import street
from entities.house import House
from entities.street import Street
from utils.assets import house_img
from utils.assets import street_img


street_counter = 10

class Scene:

    def __init__(self):
        pass

    def update(self, game, screen, runtime, houses, streets):
        global street_counter
        if str(60 - (runtime // 1000)) == '0':
            street_counter += 10

        if pygame.mouse.get_pressed()[0] == 1 and street_counter > 0:
            street_counter -= 1
            pos = pygame.mouse.get_pos()
            street.x = pos[0]
            street.y = pos[1]
            streets.append(Street(screen, street_img, pos[0] - pos[0] % 50, pos[1] - pos[1] % 50))

        print(street_counter)
        if len(houses) < config.MAX_HOUSES and runtime >= config.HOUSE_SPAWN_RATE:
            for i in (1, 2):
                find_x_y = True
                while find_x_y:
                    x = random.random() * config.SCREEN_WIDTH
                    x = x - (x % 50)
                    y = random.random() * config.SCREEN_HEIGHT
                    y = y - (y % 50)

                    print(x, y)

                    find_x_y = False

                    for house in houses:
                        if house.x == x and house.y == y or house.x == x + 50 or house.x == x - 50 or house.y == y + 50 or house.y == y - 50:
                            find_x_y = True

                houses.append(House(screen, house_img, x, y))

            game.reset_runtime()

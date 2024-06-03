import pygame

import config
from game import scene
from ui import ui


class Renderer:
    def __init__(self, screen: pygame.surface):
        self.screen = screen
        self.scene = scene.Scene()

    def render_grid(self):
        for i in range(1, config.SCREEN_WIDTH // config.GRID_SIZE):
            pygame.draw.line(self.screen, config.GRID_COLOR, (config.GRID_SIZE * i, 0),
                             (config.GRID_SIZE * i, config.SCREEN_HEIGHT))

        for i in range(1, config.SCREEN_HEIGHT // config.GRID_SIZE):
            pygame.draw.line(self.screen, config.GRID_COLOR, (0, config.GRID_SIZE * i),
                             (config.SCREEN_WIDTH, config.GRID_SIZE * i))

    def add_street(self, screen, runtime, street, houses, x, y, game, grid):
        self.scene.add_street(screen, runtime, street, houses, x, y, game, grid)

    def update(self, game, runtime, houses, streets, cars, grid):
        self.scene.update(game, self.screen, runtime, houses, streets, cars, grid)

        for house in houses:
            house.draw()

        for street in streets:
            street.draw()

        for car in cars:
            car.draw()

        if len(houses) < config.MAX_HOUSES:
            ui.render_spawn_timer(runtime, self.screen)

        ui.streets_left_counter(game.street_counter, self.screen)

    def remove_street(self, streets, houses, cars, x, y, game, grid):
        self.scene.remove_street(streets, houses, cars, x, y, game, grid)

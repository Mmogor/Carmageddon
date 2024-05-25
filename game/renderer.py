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

    def add_street(self, screen, runtime, street, houses, x, y):
        self.scene.add_street(screen, runtime, street, houses, x, y)

    def update(self, game, runtime, houses, streets):
        self.scene.update(game, self.screen, runtime, houses, streets)

        if len(houses) < config.MAX_HOUSES:
            ui.render_spawn_timer(runtime, self.screen)

        for house in houses:
            house.draw()

        for street in streets:
            street.draw()

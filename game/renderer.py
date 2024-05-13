import random

import pygame

import config
from entities.house import House
from game import scene
from utils.assets import house_img


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

    def update(self, game, runtime, houses):
        self.scene.update(game, self.screen, runtime, houses)

        for house in houses:
            house.draw()

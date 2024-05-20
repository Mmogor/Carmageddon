import pygame

import config
from entities.house import House
from entities.street import Street
from utils.assets import house_img
from .renderer import Renderer


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.running = True
        self.render_grid = False
        self.runtime = config.HOUSE_SPAWN_RATE
        self.houses = []
        self.street = []

    def start_game(self, screen: pygame.Surface):
        while self.running:
            renderer = Renderer(screen)

            screen.fill(config.BACKGROUND_COLOR)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:
                        self.render_grid = not self.render_grid

            if self.render_grid:
                renderer.render_grid()

            renderer.update(self, self.runtime, self.houses, self.street)

            pygame.display.update()
            self.runtime += self.clock.tick(config.FRAME_RATE)

    def reset_runtime(self):
        self.runtime = 0

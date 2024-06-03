import numpy as np
import pygame

import config
from .renderer import Renderer


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.running = True
        self.render_grid = False
        self.runtime = config.HOUSE_SPAWN_RATE
        self.houses = []
        self.streets = []
        self.cars = []
        self.street_counter = 0
        self.score = 0
        self.grid = np.empty((config.SCREEN_HEIGHT // config.GRID_SIZE, config.SCREEN_WIDTH // config.GRID_SIZE),
                             dtype=int)

        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[i])):
                self.grid[i][j] = 1

        print(self.grid)

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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        renderer.add_street(screen, self.runtime, self.streets, self.houses, pygame.mouse.get_pos()[0],
                                            pygame.mouse.get_pos()[1], self, self.grid)
                    elif event.button == 3:
                        renderer.remove_street(self.streets, self.houses, self.cars, pygame.mouse.get_pos()[0],
                                               pygame.mouse.get_pos()[1], self, self.grid)

            if self.render_grid:
                renderer.render_grid()

            renderer.update(self, self.runtime, self.houses, self.streets, self.cars, self.grid)

            pygame.display.update()
            self.runtime += self.clock.tick(config.FRAME_RATE)

    def reset_runtime(self):
        self.runtime = 0

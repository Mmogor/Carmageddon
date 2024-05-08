import pygame

import config
from entities.house import House
from utils.assets import house_img
from .renderer import Renderer


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.running = True
        self.render_grid = False
        self.runtime = 0

    def start_game(self, screen: pygame.Surface):
        while self.running:
            self.runtime += self.clock.get_time()
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

            renderer.update(self.runtime)

            house = House(screen, house_img, 0, 0)
            house.draw()

            pygame.display.update()
            self.clock.tick(config.FRAME_RATE)

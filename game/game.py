import pygame

from .renderer import Renderer


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.running = True
        self.render_grid = False

    def start_game(self, screen: pygame.Surface):
        while self.running:
            renderer = Renderer(screen)

            screen.fill("darkgreen")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.render_grid = not self.render_grid

            if self.render_grid:
                renderer.render_grid()

            pygame.display.flip()

            self.clock.tick(60)

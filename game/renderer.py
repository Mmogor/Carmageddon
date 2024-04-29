import pygame


class Renderer:
    def __init__(self, screen: pygame.surface):
        self.screen = screen

    def render_grid(self):
        for i in range(16):
            pygame.draw.line(self.screen, 'white', (50 * i, 0), (50 * i, 600))

        for i in range(12):
            pygame.draw.line(self.screen, 'white', (0, 50 * i), (800, 50 * i))

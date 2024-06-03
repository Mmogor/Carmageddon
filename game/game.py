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
        self.screen_width = 800
        self.screen_height = 600
        self.button_width = 200
        self.button_height = 50
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.blue = (0, 0, 255)
        self.font = pygame.font.Font(None, 74)
        self.button_font = pygame.font.Font(None, 50)
        self.score = 0
        self.grid = np.empty((config.SCREEN_HEIGHT // config.GRID_SIZE, config.SCREEN_WIDTH // config.GRID_SIZE),
                             dtype=int)

        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[i])):
                self.grid[i][j] = 1

        print(self.grid)

    def show_title_screen(self, screen: pygame.Surface):
        play_button_rect = pygame.Rect(
            (self.screen_width // 2 - self.button_width // 2, self.screen_height // 2 - self.button_height // 2 - 120),
            (self.button_width, self.button_height))
        how_to_play_button_rect = pygame.Rect(
            (self.screen_width // 2 - self.button_width // 2, self.screen_height // 2 - self.button_height // 2),
            (self.button_width, self.button_height))
        quit_button_rect = pygame.Rect(
            (self.screen_width // 2 - self.button_width // 2, self.screen_height // 2 - self.button_height // 2 + 120),
            (self.button_width, self.button_height))

        showing_title_screen = True

        while showing_title_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    showing_title_screen = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button_rect.collidepoint(event.pos):
                        showing_title_screen = False
                    elif quit_button_rect.collidepoint(event.pos):
                        self.running = False
                        showing_title_screen = False
                    elif how_to_play_button_rect.collidepoint(event.pos):
                        self.show_how_to_play_screen(screen)

            screen.fill(self.white)

            title_text = self.font.render("Carmageddon", True, self.black)
            title_rect = title_text.get_rect(center=(self.screen_width // 2, self.screen_height // 5))
            screen.blit(title_text, title_rect)

            pygame.draw.rect(screen, self.green, play_button_rect)
            play_text = self.button_font.render("Play", True, self.black)
            play_text_rect = play_text.get_rect(center=play_button_rect.center)
            screen.blit(play_text, play_text_rect)

            pygame.draw.rect(screen, self.black, how_to_play_button_rect)
            how_to_play_text = self.button_font.render("How to Play", True, self.white)
            how_to_play_text_rect = how_to_play_text.get_rect(center=how_to_play_button_rect.center)
            screen.blit(how_to_play_text, how_to_play_text_rect)

            pygame.draw.rect(screen, self.red, quit_button_rect)
            quit_text = self.button_font.render("Quit", True, self.black)
            quit_text_rect = quit_text.get_rect(center=quit_button_rect.center)
            screen.blit(quit_text, quit_text_rect)

            pygame.display.flip()

    def show_how_to_play_screen(self, screen: pygame.Surface):
        back_button_rect = pygame.Rect(
            (self.screen_width // 2 - self.button_width // 2, self.screen_height - self.button_height - 20),
            (self.button_width, self.button_height))
        showing_how_to_play_screen = True

        while showing_how_to_play_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    showing_how_to_play_screen = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button_rect.collidepoint(event.pos):
                        showing_how_to_play_screen = False

            screen.fill(self.white)

            instructions_text = self.font.render("How to Play", True, self.black)
            instructions_rect = instructions_text.get_rect(center=(self.screen_width // 2, self.screen_height // 4))
            screen.blit(instructions_text, instructions_rect)

            # Add your game instructions here
            instructions = [
                "Left click to add a street.",
                "Right click to remove a street.",
                "Press TAB to toggle grid."
            ]

            for i, instruction in enumerate(instructions):
                instruction_text = self.button_font.render(instruction, True, self.black)
                instruction_rect = instruction_text.get_rect(
                    center=(self.screen_width // 2, self.screen_height // 2 + i * 40))
                screen.blit(instruction_text, instruction_rect)

            pygame.draw.rect(screen, self.red, back_button_rect)
            back_text = self.button_font.render("Back", True, self.black)
            back_text_rect = back_text.get_rect(center=back_button_rect.center)
            screen.blit(back_text, back_text_rect)

            pygame.display.flip()

    def start_game(self, screen: pygame.Surface):
        self.show_title_screen(screen)
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

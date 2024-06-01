import pygame

import config


def render_spawn_timer(runtime, screen):
    my_font = pygame.font.SysFont("Courier", 18)

    label = my_font.render("New Houses in:", 1, config.FONT_COLOR)
    seconds_left = my_font.render(str(60 - (runtime // 1000)), 1, config.FONT_COLOR)

    screen.blit(label, (320, 20))
    screen.blit(seconds_left, (490, 20))

def streets_left_counter(streets_counter, screen):
    my_font = pygame.font.SysFont("Courier", 18)

    label = my_font.render("Number of streets:", 1, config.FONT_COLOR)
    streets_left = my_font.render(str(streets_counter), 1, config.FONT_COLOR)

    screen.blit(label, (550, 20))
    screen.blit(streets_left, (750, 20))


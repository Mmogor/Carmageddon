import pygame

import config


def render_spawn_timer(runtime, screen):
    my_font = pygame.font.SysFont("Courier", 18)

    rand_num_label = my_font.render("New Houses in:", 1, config.FONT_COLOR)
    dice_display = my_font.render(str(60 - (runtime // 1000)), 1, config.FONT_COLOR)

    screen.blit(rand_num_label, (320, 20))
    screen.blit(dice_display, (490, 20))

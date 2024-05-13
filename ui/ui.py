import pygame
import config
def render_spawn_timer(runtime, screen):
    myFont = pygame.font.SysFont("Courier", 18)

    randNumLabel = myFont.render("New Houses in:", 1, config.FONT_COLOR)
    diceDisplay = myFont.render(str(60 - (runtime // 1000)), 1, config.FONT_COLOR)

    screen.blit(randNumLabel, (320, 20))
    screen.blit(diceDisplay, (490, 20))
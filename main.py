import config
import pygame

pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
clock = pygame.time.Clock()
ORANGE = (255, 140, 0)
ROT = (255, 0, 0)
GRUEN = (0, 255, 0)
SCHWAZ = (0, 0, 0)
WEISS = (255, 255, 255)

pygame.display.set_caption("Carmageddon")
spielakritv = True
while spielakritv:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielakritv = False
        screen.fill(WEISS)
        pygame.display.flip()
        clock.tick(60)

pygame.quit()
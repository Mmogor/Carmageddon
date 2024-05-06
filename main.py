import pygame

import config
from game.game import Game

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption(config.SCREEN_TITLE)

    flags = pygame.SCALED
    main_screen: pygame.surface = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT), flags, vsync=1)

    game = Game()
    game.start_game(main_screen)

    pygame.quit()

# from utils.assets import corner_img, junction_img, t_junction_img
import pygame


class Street:
    def __init__(self, screen, img, x, y):
        self.screen = screen
        self.img = img
        self.offset = 12.5
        self.x = x
        self.y = y
        self.r = False
        self.c = False
        self.j = False

    def draw(self):
        if self.r:
            self.screen.blit(self.img, (self.x, self.offset + self.y))
        else:
            self.screen.blit(self.img, (self.offset + self.x, self.y))

    def upgrade(self):
        if not self.c:
            self.c = True
            # self.img = corner_img
            print("corner")
        elif self.c and not self.j:
            self.j = True
            # self.img = t_junction_img
            print("t_junction")
        elif self.c and self.j:
            # self.img = junction_img
            print("junction")

    def rotate(self):
        self.r = True
        self.img = pygame.transform.rotate(self.img, 90)

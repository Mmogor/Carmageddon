class Street:
    def __init__(self, screen, img, x, y):
        self.screen = screen
        self.img = img
        self.offset = 12.5
        self.x = x
        self.y = y

    def draw(self):
        self.screen.blit(self.img, (self.offset + self.x, self.y))

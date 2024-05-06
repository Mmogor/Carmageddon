class House:
    def __init__(self, screen, img, x, y):
        self.screen = screen
        self.img = img
        self.x = x
        self.y = y

    def draw(self):
        self.screen.blie(self.img, (self.x, self.y))

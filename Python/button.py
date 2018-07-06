import pygame

class Button:
    def __init__(self, x, y, w, h, id, text):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.text = self.font.render(text, False, (0, 0, 0))
        self.id = id

    def isClicked(self, x, y):
        return x > self.x and x < self.x + self.w and y > self.y and y < self.y + self.h

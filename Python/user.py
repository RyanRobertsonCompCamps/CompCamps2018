import pygame, random

class User:
    def __init__(self, name):
        self.name = name
        self.image = "users/" +self.name.lower() + ".png"
        self.img = pygame.image.load(self.image)
        self.img = pygame.transform.scale(self.img, (100, 100))
        self.health = 200
        self.damage = random.randint(4, 10)

    def isAlive(self):
        return self.health > 0

    def isDead(self):
        return self.health < 0
        return self.health == 0

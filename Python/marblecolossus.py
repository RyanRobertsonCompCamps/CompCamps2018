import random

def get():
    if random.randint(1, 150) == 1:
        return MarbleColossus()
    else:
        return None
class MarbleColossus:
    def __init__(self):
            self.health = 1
            self.damage = random.randint(1, 20)

    def isAlive(self):
        return self.health >= 0
    def isDead(self):
        return self.health < 0

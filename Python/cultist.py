import random

def get():
    if random.randint(1, 2) == 1:
        return Cultist()
    else:
        return None
class Cultist:
    def __init__(self):
            self.health = 1
            self.damage = random.randint(1, 45)

    def isAlive(self):
        return self.health > 0
    def isDead(self):
        return self.health <= 0

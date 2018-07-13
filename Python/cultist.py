import random

def get():
    if random.randint(1, 50) == 1:
        return Cultist()
    else:
        return None
class Cultist:
    def __init__(self):
            self.health = 150
            self.damage = random.randint(1, 35)

    def isAlive(self):
        return self.health > 0
    def isDead(self):
        return self.health <= 0

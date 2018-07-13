import random

def get():
    if random.randint(1, 250) == 1:
        return Voidentity()
    else:
        return None
class VoidEntity:
    def __init__(self):
            self.health = 750
            self.damage = random.randint(1, 50)

    def isAlive(self):
        return self.health >= 0

    def isDead(self):
        return self.health < 0

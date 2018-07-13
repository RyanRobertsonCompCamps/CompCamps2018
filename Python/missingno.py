import random

def get():
    if random.randint(1, 1500) == 1:
        return MissingNo()
    else:
        return None
class MissingNo:
    def __init__(self):
            self.health = 1
            self.damage = random.randint(1, 50)

    def isAlive(self):
        return self.health >= 0

    def isDead(self):
        return self.health < 0

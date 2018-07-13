import random
class Drop:
    def __init__(self, name, damage, healing, disposable = False):
        self.name = name
        self.damage = damage
        self.healing = healing
        self.disposable = disposable

drops = [
Drop("Staff of Unholy Sacrifice", 10, 30),#UNCOMMON
Drop("Vial of Pure Darkness", 0, 150, True)#RARE
Drop("Sword of the Colossus", 75, -5)
]
def getRandomDrop():
    return random.choice(drops)

def getDrop(name):
    for d in drops:
        if d.name == name:
            return i

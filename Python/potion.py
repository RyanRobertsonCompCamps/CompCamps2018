import random
class Potion:
    def __init__(self, name, damage, healing):
        self.name = name
        self.damage = damage
        self.healing = healing

potions = [
    Potion("Potion of Life", 0, 20),#UNCOMMON
    Potion("Health Potion", 0, 10),#COMMON
    Potion("Syringe", 2, 5),#COMMON                                   #TODO: make the potions to damage to enemies
    Potion("Vial of Pure Darkness", 0, 150)#RARE
]

def getRandomPotion():
    return random.choice(potions)

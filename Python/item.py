import random
class Item:
    def __init__(self, name, damage, healing, disposable = False):
        self.name = name
        self.damage = damage
        self.healing = healing
        self.disposable = disposable

items = [
    Item("Potion of Life", 0, 20, True),#UNCOMMON
    Item("Health Potion", 0, 10, True),#COMMON
    Item("Parasitic Poison", 100, 0),#UNCOMMON
    Item("Cosmic Egg", 10, -5, True),#COMMON
    Item("Black Dart", 2, -2, True),#COMMON
    Item("Syringe", 2, 5, True),#COMMON                                   #TODO: make the items to damage to enemies
    Item("Sword of the fallen Golem", 7, 0),#UNCOMMON
    Item("Carved Golem Remains", 5, 0),#COMMON
    Item("Staff of Unholy Sacrifice", 10, 30),#UNCOMMON
    Item("Wand of the Fallen Cultist", 5, 20),#UNCOMMON
    Item("Sword of the Fallen Warrior", 8, 0),#UNCOMMON
    Item("Waki of the Ancient Samurai", 6, 0),#COMMON
    Item("Dagger of the Titan", 7, 0),#COMMON
    Item("Marble Shield", 4, 0),#COMMON
    Item("Void Bow", 50, 100),#RARE
    Item("Vial of Pure Darkness", 0, 150, True)#RARE
]

def getRandomItem():
    return random.choice(items)

def getItem(name):
    for i in items:
        if i.name == name:
            return i

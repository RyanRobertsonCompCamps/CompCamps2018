import random, enemy, cultist, marblecolossus, voidentity, missingno

descriptions = ["a Room of"]
location_types = ["Marble."]

class Location:
    def __init__(self, seed):
        self.seed = seed
        random.seed(seed)
        self.name = "{} {}".format(
                random.choice(descriptions),
                random.choice(location_types)
        )
        self.enemy = enemy.get()
        self.cultist = cultist.get()
        self.marblecolossus = marblecolossus.get()
        self.voidentity = voidentity.get()
        self.missingno = missingno.get()

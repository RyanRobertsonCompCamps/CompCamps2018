import random, enemy

descriptions = ["a Room of"]
location_types = ["Marble"]

class Location:
    def __init__(self, seed):
        self.seed = seed
        random.seed(seed)
        self.name = "{} {}".format(
                random.choice(descriptions),
                random.choice(location_types)
        )
        self.enemy = enemy.get()

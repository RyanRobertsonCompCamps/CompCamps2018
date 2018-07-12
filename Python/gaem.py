    #LOST HALLS GAME!


import location, player, item, random, enemy
from datetime import datetime
print("As you enter the halls, you find a letter.")
print("DAY 1 LOG: As we travelled across the ocean to go to these halls, it looks kind of... empty. The walls, floor, and ceiling are all marble.")
print("DAY 2 LOG: So, we are currently good on food (for now) and currently are a little lost on finding this 'Marble Colossus'. It was apparently designed to protect the halls they say.")
print("DAY 5 LOG: We are running out of food. Our commander claims we're not lost and will find a way out. I just hope he's right")
print("DAY 6 LOG: We were just attacked by a massive golem. A warrior was killed in that fight. Without a proper burial, we'll just have to leave him there.")
print("DAY 20 LOG: Well, we are going in circles. we came across our fallen comrade about 2 times today and are currently feeding on the plagued rats in these marble halls.")
print("DAY ???: I am going full paranoid. Whenever we see these golems, we go full savage and only attack them. Like vicious animals.")
print("DAY ???: We are starting to hear voices under us. I could believe its just a hallucination. But the thing is we are all hearing it. We are very lost.")
print("We found this strange titan in a room. We found these flames in some vases They would sprint out of the dead end and apparently lead a way.")
print("You seem to hear a voice from afar. as if it was greeting you.")
print("Hello. You are in the lost halls. Nobody leaves this place. You will never get out with my marble colossus standing in the way!")
print("If you believe your omnipotent powers are true, defeat my colossus and meet me in my lair!")
seed = input("Enter a seed: ")

tile = location.Location(seed + "0,0")

user = player.Player(input("What is your name: "))
print("Type 'move' to get started! type your direction to move there.")

x = 0
y = 0
tiles = {}
searched_tiles = []
def move(direction):
    global x, y
    if direction == "n":
        y += 1
    elif direction == "e":
        x += 1
    elif direction == "s":
        y -= 1
    elif direction == "w":
        x -= 1
    key = "{}, {}".format(x, y)
    if key in tiles:
        return tiles[key]
    else:
        newtile = location.Location(seed + key)
        tiles[key] = newtile
        return newtile
running = True
while running and user.isAlive():
    print("You are in {}".format(tile.name))
    if tile.enemy and tile.enemy.isAlive():
        print("You found an enemy. They currently have {} Health.".format(tile.enemy.health))
    command = input("> ")
    if command == "items":
        if user.inventory:
            print("You have: {}".format(user.getItems()))
        else:
            print("You have no items.")
    elif command == "move":
        direction = input("N/E/S/W > ")[0].lower()
        if direction == "n":
            tile = move("n")
            print("Go north")

        elif direction == "e":
            tile = move("e")
            print("Go east")

        elif direction == "s":
            tile = move("s")
            print("Go south")

        elif direction == "w":
            tile = move("w")
            print("Go west")

        else:
            print("no")
    elif command == "search":
        if tile.seed in searched_tiles:
            print("There is nothing on the marble ground...")
            continue

        random.seed(seed + str(x) + str(y))
        if random.randint(1, 5) == 1:
            print("You found an item! type items to see what you got!")
            user.addItem(item.getRandomItem())
        else:
            print("There is nothing on the marble ground...")
        searched_tiles.append(tile.seed)
    elif command == "fight":
        random.seed(datetime.now())
        while tile.enemy.isAlive() and user.isAlive():
            print("You have {} health.".format(user.health))
            command = input("FIGHT MODE! > ")
            if command == "punch":
                if random.randint(1,5) < 5:
                    print("O     O     F")
                    tile.enemy.health -= 3
                else:
                    print("You missed your punch!")
            elif command == "slam":
                if random.randint(1,3) == 1:
                    print("You successfully slammed the enemy!")
                    tile.enemy.health -= 10
                else:
                    print("you suck heck")
            elif command.startswith("use"):
                _, i = command.split(" ", 1)
                if user.hasItem(i):
                    print("You used a {}".format(i))
                    user.use(i)
                    tile.enemy.health -= item.getItem(i).damage
                else:
                    print("You dont have {}!".format(i))
            if tile.enemy.isAlive():
                user.health -= tile.enemy.damage
            elif tile.enemy.isDead():
                print("the enemy is now dead. If you want, you can search further.")
    elif command.startswith("use"):
        _, i = command.split(" ", 1)
        if user.hasItem(i):
            print("You used a {}".format(i))
            user.use(i)
            user.removeItem(i)
        else:
            print("You dont have {}!".format(i))

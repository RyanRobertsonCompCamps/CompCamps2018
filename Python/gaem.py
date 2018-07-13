    #LOST HALLS GAME!


import location, player, item, random, enemy, cultist, marblecolossus, voidentity, missingno
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
    if tile.cultist and tile.cultist.isAlive():
        print("Wait, there are still survivors!?!?")
        print("You're here to kill me, aren't you? well, prepare for a fight! FOR MALUS!")
        print("NEW QUEST: Defeat the Cultist of Azamoth!")
        print("Type 'fight cultist' to begin the fight!")
    if tile.marblecolossus and tile.marblecolossus.isAlive():
        print("Welcome hero, this is where your futile life ends to the hands of the Marble Colossus!")
        print("NEW QUEST: Defeat the Marble Colossus")
        print("Type 'fight colossus' to start the battle.")
    if tile.voidentity and tile.voidentity.isAlive():
        print("Hello {}, I have missed you. Now, YOU ARE ESSENCE TO MY ARMY OF SHADOW!")
        print("NEW QUEST: Defeat the void entity!")
        print("type 'fight void entity' to begin the fight.")
    if tile.missingno and tile.missingno.isAlive():
        print("You found the MissigNo. Kill it for fantastic rewards!")
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
            print("You have already searched this area!")
            continue

        random.seed(seed + str(x) + str(y))
        if random.randint(1, 3) == 1:
            print("You found an item! type items to see what you got!")
            user.addItem(item.getRandomItem())
        else:
            print("There is nothing on the marble ground...")
        searched_tiles.append(tile.seed)
    elif command == "fight":
        random.seed(datetime.now())


        while tile.enemy.isAlive() and user.isAlive():
            print("You have {} health.".format(user.health))
            print("The Enemy has {} health.".format(tile.enemy.health))
            command = input("FIGHT MODE! > ")
            if command == "punch":
                if random.randint(1,5) < 5:
                    print("You landed your punch!")
                    tile.enemy.health -= random.randint(1, 5)
                else:
                    print("You missed your punch!")
            elif command == "slam":
                if random.randint(1,3) == 1:
                    print("You successfully slammed the enemy!")
                    tile.enemy.health -= 10
                else:
                    print("You missed the slam and took damage from hitting the floor!")
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


    elif command == "fight cultist":
        random.seed(datetime.now())

        while tile.cultist.isAlive() and user.isAlive():
            print("You have {} health.".format(user.health))
            print("The Cultist has {} health".format(tile.cultist.health))
            command = input("BOSS FIGHT! > ")
            if command == "punch":
                if random.randint(1,5) < 5:
                    print("You pathetic runt! You will pay for that!")
                    tile.cultist.health -= random.randint(1, 5)
                else:
                    print("You missed your punch!")
            elif command == "slam":
                if random.randint(1,3) == 1:
                    print("Ah! Azamoth, give me power!")
                    tile.cultist.health -= 10
                else:
                    print("You missed the slam and took damage from hitting the floor!")
            elif command.startswith("use"):
                _, i = command.split(" ", 1)
                if user.hasItem(i):
                    print("You used a {}".format(i))
                    user.use(i)
                    tile.cultist.health -= item.getItem(i).damage
                else:
                    print("You dont have {}!".format(i))
            if tile.cultist.isAlive():
                user.health -= tile.cultist.damage
            elif tile.cultist.isDead():
                print("Wait! That THING is still out there! with another cultist down, it is unstoppable! You have done a bad bidding to the Cult of Azamoth!")
                print("The Cultist dropped an item! type 'items' to see what you got!")
                user.addItem(item.getItem("Staff of Unholy Sacrifice"))
                user.addItem(item.getItem("Vial of Pure Darkness"))
            elif command.startswith("use"):
                _, i = command.split(" ", 1)
                if user.hasItem(i):
                    print("You used a {}".format(i))
                    user.use(i)
                    user.removeItem(i)
                else:
                    print("You dont have {}!".format(i))

    elif command == "fight colossus":
        random.seed(datetime.now())

        while tile.marblecolossus.isAlive() and user.isAlive():
            print("You have {} health.".format(user.health))
            print("The Marble Colossus has {} health.".format(tile.marblecolossus.health))
            command = input("BOSS FIGHT! > ")
            if command == "punch":
                if random.randint(1,5) < 5:
                    print("Call of voice, for naught. Plea of mercy, for naught. None may enter this chamber and live!")
                    tile.marblecolossus.health -= random.randint(1, 5)
                else:
                    print("You missed your punch!")
            elif command == "slam":
                if random.randint(1,3) == 1:
                    print("You have seen your last glimpse of sunlight!")
                    tile.marblecolossus.health -= 10
                else:
                    print("You missed the slam and took damage from hitting the floor!")
            elif command.startswith("use"):
                _, i = command.split(" ", 1)
                if user.hasItem(i):
                    print("You used a {}".format(i))
                    user.use(i)
                    tile.marblecolossus.health -= item.getItem(i).damage
                else:
                    print("You dont have {}!".format(i))
            if tile.marblecolossus.isAlive():
                user.health -= tile.marblecolossus.damage
            elif tile.marblecolossus.isDead():
                print("I feel myself… Slipping… Into the void… It is so… Dark…")
                print("*You hear a voice calling you in the void. You must find the Void and kill the entity that lives below*")
                print("The Marble Colossus has dropped an item! type 'items' to see what you got!")
                user.addItem(item.getItem("Sword of the Colossus"))

    elif command == "fight void entity":
        random.seed(datetime.now())

        while tile.voidentity.isAlive() and user.isAlive():
            print("Those who enter my realm have little value of their lives. You are going to be annihilated by me, the one who controlled the Marble Colossus and all life in the halls!")
            print("You have {} health.".format(user.health))
            print("The Void Entity has {} health.".format(tile.voidentity.health))
            command = input("BOSS FIGHT! > ")
            if command == "punch":
                if random.randint(1,5) < 5:
                    print("The likes of Esben and the Forgotten King were expendable vessels, just as you shall be!!")
                    print("You shall pay for freeing the Marble Colossus!")
                    tile.voidentity.health -= random.randint(1, 5)
                else:
                    print("You missed your punch!")
            elif command == "slam":
                if random.randint(1,3) == 1:
                    print("I have fed off the sorrow and hatred of the lost souls… AND I WILL FEED AGAIN!")
                    print("HA HA HA! You shall be enveloped by darkness")
                    tile.voidentity.health -= 10
                else:
                    print("You missed the slam and took damage from hitting the floor!")
            elif command.startswith("use"):
                _, i = command.split(" ", 1)
                if user.hasItem(i):
                    print("You used a {}.".format(i))
                    user.use(i)
                    tile.voidentity.health -= item.getItem(i).damage
                    print("AH! MINIONS! I WILL FEED YOU!")
                else:
                    print("You dont have {}!".format(i))
            if tile.voidentity.isAlive():
                print("HA HA HA! FEEL THE DARKNESS CONSUME YOU!")
                user.health -= tile.voidentity.damage
            elif tile.voidentity.isDead():
                print("No…NO! THIS IS NOT THE END!")
                print("You fool..you can never truly defeat me! I am in all of you! I AM all of you!")
                print("I am the embodiment of your own sin! To destroy me would be to destroy yourselves!")
                print("Naivety! You really think you have won? The inevitable has merely been delayed. One day you shall all be slain, and on that day I will claim your souls in vengeance.")

    elif command == "fight missingno":
        random.seed(datetime.now())

        while tile.missingno.isAlive() and user.isAlive():
            print("You have {} health.".format(user.health))
            print("The Missingno has {} health.".format(tile.missingno.health))
            command = input("! > ")
            if command == "punch":
                if random.randint(1,5) < 5:
                    tile.missingno.health -= random.randint(1, 5)
                else:
                    print("You missed your punch!")
            elif command == "slam":
                if random.randint(1,3) == 1:
                    print("!")
                    tile.missingno.health -= 10
                else:
                    print("You missed the slam and took damage from hitting the floor!")
            elif command.startswith("use"):
                _, i = command.split(" ", 1)
                if user.hasItem(i):
                    print("You used a {}".format(i))
                    user.use(i)
                    tile.missingno.health -= item.getItem(i).damage
                else:
                    print("You dont have {}!".format(i))
            if tile.missingno.isAlive():
                user.health -= tile.missingno.damage
            elif tile.missingno.isDead():
                print("The drop was a lie. Kill other things for fantastic rewards!")

    elif command.startswith("use"):
        _, i = command.split(" ", 1)
        if user.hasItem(i):
            print("You used a {}".format(i))
            user.use(i)
            user.removeItem(i)
        else:
            print("You dont have {}!".format(i))

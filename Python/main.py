name = input("Hello, what is your name? ")


def welcome(name):
    if name == "Ryan":
        print("hello Ryan")
    else:
        print("Welcome to CompCamps 2018, {}.".format(name))


welcome(name)

mits = ["Bennet", "Kaitlyn", "Rhiannon", "Austin", "McFly"]

for mit in mits:
    welcome(mit)

# Simple Critter
# Demonstrates a basic class and object

def talk():
    print("Hi, I'm an instance of class Critter.")


class Critter(object):
    """A virtual pet"""


# main
crit = Critter()
talk()

input("\n\nPress the enter key to exit.")

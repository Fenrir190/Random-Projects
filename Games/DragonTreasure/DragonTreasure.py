"""
This game is a where a player navigates a world inhabited by dragons. There are
friendly dragons who give you treasure and there are dragons who will attack you on
sight. Not all treasure is something benefical. This python game will simulate that world.
"""

# import packages
import random
import time
from Item import *
from Dragon import *
from Player import *

YES_CONST = "y"
NO_CONST = "n"
MIN_PATH_CONST = 2
MAX_PATH_CONST = 5
MAX_INVALID_RESPONSE_CONST = 3
numInvalidResponses = 0
treasures = []

"""
 Purpose: This function simply displays the intro to the game
 Precondition: None
 Postcondition: None
"""
def intro():
    print("You awaken to a world where dragons reign supreme...")
    print("in this world you'll find treasures that can help you stay alive")
    print("or possible lead you to your doom...")
    print("After some time you spot the only thing in your reach, a cave")
    print("You hear the sounds of loud soft breathing")
    print("You anticipate that dragons lurk inside.")
    print("Weighing your options, you wonder if you should go inside")
    initPathChoice()

def enterPath(path):
    print("Under Construction")

def pathChoice(numPaths):
    global numInvalidResponses
    global MIN_PATH_CONST
    global MAX_PATH_CONST

    print("After moving forward, you spot %d entrances..." %(numPaths))
    print("There's no turning back now. Which path will you take?")
    userChoice = int(input("Enter a number for the cave to proceed through > "))

    if(userChoice < MIN_PATH_CONST or userChoice > MAX_PATH_CONST):
        numInvalidResponses += 1
        if(numInvalidResponses == MAX_INVALID_RESPONSE_CONST):
            print("You've wasted enough time.")
            print("Soon you shall have all the time you want to waste away.")
            print("Or maybe not... Depends on your beliefs")
            print("You feel a chilling presence all around you drawing closer")
            print("but it's nothing you can quite see.")
            print("One thing's for certain.")
            print("The warm crimson flowing from your body and the cold sensation are not welcome.")
            print("Or maybe they are... Depends on your outlook.")
            print("GAME OVER")
        else:
            print("Where do you thing you are?\nNow isn't the time to idle")
            pathChoice(numPaths)

    else:
        enterPath(userChoice)

"""

"""
def initPathChoice():
    global YES_CONST
    global NO_CONST

    print("A choice must be made")
    print("Will you go inside the cave?")

    userChoice = str(input("y = yes\nn = no\n"))

    if((userChoice.lower() != YES_CONST) or (userChoice.lower() != NO_CONST)):
        print("A cowardly choice or wise one you shall never know...")
        print("Among the last sounds you hear in this world are a loud cracking and slashing sound")
        print("before the world around you goes black")
        print("GAME OVER")
    else:
        numPaths = random.randint(MIN_PATH_CONST, MAX_PATH_CONST)
        pathChoice(numPaths)


# Game Start
intro()

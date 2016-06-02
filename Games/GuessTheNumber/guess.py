# This is a simple game of guess the number.
# The user will guess a number between a given range.
# Level 1: Given the range, the user is allowed as many guesses as they want
# Level 2: Given a larger range, the user has 10 tries to guess the number
# Level 3: Given a range, the user has 10 tries to guess the number. However the
#          number is subject to change.

import random

print("Welcome to the guessing game version 1.0!\n")
print("You've the option of 3 levels to play\n")
print("Before we begin however, let's start with your name\n")

name = input("Please enter your name\n")

print("Greetings %s" % (name))

minRg = 0
maxRg = 0
randomNumber = 0
userGuess = -1
numberOfGuesses = 0

# Get the level from user
level = int(input(name + ", enter the level you desire > "))

if(level == 1 or level == 3):
    minRg = 0
    maxRg = 20
    randomNumber = random.randint(minRg, maxRg)
    numberOfTries = 5

    if(level == 1):
        print("Level set to easy\nYou have as many tries as you want to guess the number %s" % (name))
    if(level == 3):
        print("Level set to insane, hope you're sure about this %s" % (name))
        print("in this level, after 5 attempts a new number is selected")
        print("if you've still not guessed correct after %d turns, you lose" %(numberOfTries*2))

    print("Guess the number between %d and %d " % (minRg, maxRg))

    while(userGuess != randomNumber):
        userGuess = int(input())

        if(userGuess == randomNumber):
            print("You've guessed right %s!" %(name))
            if(numberOfGuesses == 0):
                print("And on you're first try too, wow!")
            else:
                print("It took you %d attempts" %(numberOfGuesses))
            print("Thanks for playing!")
        else:
            if(userGuess > randomNumber):
                if(userGuess > maxRg):
                    print("You've gone out of range")
                print("Too high")
            else:
                if(userGuess < minRg):
                    print("You've gone out of range")
                print("Too low")

        numberOfGuesses += 1

        if(numberOfGuesses == numberOfTries and level == 3):
            print("You've reached %d attempts. The number was %d \nRoulette spin!" %(numberOfGuesses, randomNumber))
            randomNumber = random.randint(minRg, maxRg)
        if(numberOfGuesses == (numberOfTries*2)):
            print("Max number of turns reached, you lose...")
            break

if(level == 2):
    numberOfTries = 10
    print("Level set to medium for you %s" % (name))
    print("in this level, you have %d attempts a new number is selected\n" %(numberOfTries))

    minRg = 0
    maxRg = 50
    randomNumber = random.randint(minRg, maxRg)

    print("Guess the number between %d and %d " % (minRg, maxRg))

    while(userGuess != randomNumber and numberOfGuesses != numberOfTries):
        userGuess = int(input())

        if(userGuess == randomNumber):
            print("You've guessed right %s!" %(name))
            if(numberOfGuesses == 0):
                print("And on you're first try too, wow!")
            else:
                print("It took you %d attempts" %(numberOfGuesses))
                print("Thanks for playing!")
        else:
            if(userGuess > randomNumber):
                if(userGuess > maxRg):
                    print("You've gone out of range")
                print("Too high")
            else:
                if(userGuess < minRg):
                    print("You've gone out of range")
                print("Too low")

            numberOfGuesses += 1
            if(numberOfGuesses == numberOfTries):
                print("Too bad, you're out of turns...")
                break

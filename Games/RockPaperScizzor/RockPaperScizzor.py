#!/usr/bin/python
import random
# Purpose: Simple Game of Rock Paper Scizzors
# Author: Jonathan Ellison

class RockPaperScizzor:
    def getOption(self):
        option = random.randrange(1, 4)
        return option

    def play(self):
        userOption = -1

        print("Today we're going to play rock, paper, scizzors!\n")
        print("To play, enter a number from 1 to 3\n")
        print("1 = Rock\n2 = Paper\n3 = Scizzors\nEnter 0 to quit")

        while userOption != 0:
            userOption = int(input("What is your selection? "))

            if userOption == 0: break
            if (userOption != 1 and userOption != 2 and userOption != 3):
                print("Invalid option!\nTry again!")
            else:
                compOption = self.getOption()
                self.determinVictor(userOption, compOption)

        print("Thanks for playing!")

    def determinVictor(self, userOption, compOption):
        if userOption == compOption: print("Draw!")
        elif (userOption == 1) and (compOption == 2): print("Computer chose Paper: You Lose!")
        elif (userOption == 1) and (compOption == 3): print("Computer chose Scizzors: You Win!")
        elif (userOption == 2) and (compOption == 1): print("Computer chose Rock: You Win!")
        elif (userOption == 2) and (compOption == 3): print("Computer chose Scizzors: You Lose!")
        elif (userOption == 3) and (compOption == 1): print("Computer chose Rock: You Lose!")
        elif (userOption == 3) and (compOption == 2): print("Computer chose Paper: You Win!")

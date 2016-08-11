# Purpose: This file contains all tools needed for user interaction.

import level
proceed_next_level = False

def begin_adventure( ):
    first_level = level.Forest(None)
    print("You awaken to find yourself in an unfamiliar %s." %first_level.level_name)
    print(first_level.start_text)

    while(proceed_next_level == False):
        level_progression = first_level.choose_direction()

        if(level_progression[0] == True):
            proceed_next_level == True

    continue_adventure(level_progression[1])

def continue_adventure(new_level):
    current_level = None

    if(new_level == 0):
        current_level = level.Valley()
    elif(new_level == 1):
        current_level = level.Cave()

    while(proceed_next_level == False):
        level_progression = current_level.choose_direction()

        if(level_progression[0] == True):
            proceed_next_level == True

    continue_adventure(level_progression[1])

begin_adventure()

# Purpose: This file contains all tools needed for user interaction.

import level

def begin_adventure( ):
    first_level = level.Forest()
    print("You awaken to find yourself in an unfamiliar %s." %first_level.level_name)
    print(first_level.start_text)
    first_level.choose_direction()

begin_adventure()

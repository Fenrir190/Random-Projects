import random

LEVEL_X_VALUE = 3
LEVEL_Y_VALUE = 3

directions = ["foward", "left", "backwards", "right"]

def navigate( level_obj, direction):
    """
    Purpose: This method calculates the new location of the player
    after a move.
    Return: Returns the new location of the player
    @param level_obj - an object of a level
    @param  direction - an integer denoting the direction the player will move
    """
    # print("Current Location of Player %d" %(area_map.index("x")))
    current_location = level_obj.area_map.index("x")
    start_location = current_location
    cross_border = False
    next_level = -1
    proc_rand_event = False

    if(direction == 0): # Moving Up
        if(current_location == 0 or current_location == 1 or current_location == 2):
            print(level_obj.border_reached_text)
        else:
            current_location = current_location - 3
    elif(direction == 1): # Moving left
        if(current_location == 0 or  current_location == 6):
            print(level_obj.border_reached_text)
        elif(current_location == 3):
            user_choice = int(input(level_obj.border_cross_text))

            if(user_choice == 1):
                next_level = 0
        else:
            current_location = current_location - 1
    elif(direction == 2): # Moving down
        if(current_location == 6 or current_location == 7 or current_location == 8):
            print(level_obj.border_reached_text)
        else:
            current_location = current_location + 3
    else: # Moving right
        if(current_location == 2  or current_location == 8):
            print(level_obj.border_reached_text)
        elif(current_location == 5):
            user_choice = int(input(level_obj.border_cross_text))

            if(user_choice == 1):
                next_level = 1
        else:
            current_location = current_location + 1

        if(level_obj.area_map[current_location] == "r"):
            proc_rand_event = True

    # Update Map
    level_obj.area_map[start_location] = ""
    level_obj.area_map[current_location] = "x"

    return [proc_rand_event, next_level]

class Forest:
    area_map = []
    level_name = "forest"
    border_reached_text = "You look onto the dense barrier of trees and turn back."
    border_cross_text = "You look on to see an unfamiliar area. Enter?\n1 = yes\n2 = no\n"
    start_text = "The light filtering through the leaves of the tall trees\n" \
    + "creates a subtle shimmering effect around you.\n" \
    + "The lush green grass is spotted with patches of soft soil.\n" \
    + "Were it not for the mysterious circumstance of how you\n" \
    + "got here, it'd make for a nice place to rest and enjoy the scene.\n" \
    + "you decide to explore but are not sure on how.\n" \
    + "Either leave it to fate(1) or pick direction(2).\n"

    def __init__(self, prev_level):
        if (prev_level != None):
            if(prev_level.level_name == "cave"):
                self.area_map = ["r","","r","","","x","r","","",]

            elif(prev_level.level_name == "valley"):
                self.area_map = ["r","","r","x","","","r","","",]
        else:
            self.area_map = ["r","","","","x","r","r","","",]


    def choose_direction(self):
        proceed_to_new_level = False
        next_level = -1
        direction = 0

        user_choice = input("1 = Leave it to fate\n2 = Decide for yourself\n")

        if(user_choice == "1"):
            direction = random.randint(0,3)

            print("Choosing to go the direction of the most interesting sound,\n" \
            + "you decide to go %s" %(directions[direction]))

            map_state = navigate(self, direction)

        elif(user_choice == "2"):
            direction = int(input("Which direction will you go?\n1=up\n2=left\n" \
            + "3=down\n4=right\n"))

            print("You decide to go %s" %(directions[direction-1]))

            map_state = navigate(self, direction)

        else:
            print("Where are you going?")

        if(map_state[1] != -1):
            proceed_to_new_level = True
            next_level = map_state[1]

        return [proceed_to_new_level, next_level]

class Cave:
    area_map = []
    level_name = "cave"
    border_reached_text = "You've reached the of the path. With nothing to see here you" \
    + "\nturn back."
    border_cross_text = "You peer out of the cave to see an unfamiliar area. Enter?\n1 = " \
    + "yes\n2 = no\n"
    start_text = "You hear deafening silence in the dimly lit room you find yourself in.\n" \
    + "You examine the craggy feel of the walls around and dirt beneath your feet\n" \
    + "You appear to be inside a cave. The silence is occassionally broken by some far\n" \
    + " off sound. You don't feel anything hostile in the area. In fact, it's rather peaceful.\n" \
    + "Your exploration of the cave commences. Not sure how to proceed you decide to\n"\
    + "Either leave it to fate(1) or pick direction(2).\n"

    def __init__(self, prev_level):
        if(prev_level != None):
            if(prev_level.level_name == "forest"):
                self.area_map = ["r","","r","","","x","r","","",]

            elif(prev_level.level_name == "valley"):
                self.area_map = ["r","","r","","","","r","","x",]
        else:
            self.area_map = ["r","","","","x","r","r","","",]

    def choose_direction(self):
        proceed_to_new_level == False
        next_level = -1
        direction = 0

        user_choice = input("1 = Leave it to fate\n2 = Decide for yourself\n")

        if(user_choice == "1"):
            direction = random.randint(0,3)

            print("Choosing to go the direction of the most interesting sound,\n" \
            + "you decide to go %s" %(directions[direction]))

            map_state = navigate(self, direction)

        elif(user_choice == "2"):
            direction = int(input("Which direction will you go?\n1=up\n2=left\n" \
            + "3=down\n4=right\n"))

            print("You decide to go %s" %(directions[direction-1]))

            map_state = navigate(self, direction)

        else:
            print("Where are you going?")

        if(map_state[1] != -1):
            proceed_to_new_level = True
            next_level = map_state[1]

        return [proceed_to_new_level, next_level]

class Valley:
    level_name = "valley"

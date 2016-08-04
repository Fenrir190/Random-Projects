import random

LEVEL_X_VALUE = 3
LEVEL_Y_VALUE = 3

directions = ["foward", "left", "backwards", "right"]

def navigate( area_map, direction):
    print("Till next time. Stay gold")

class Forest:
    area_map = ["r","","","","x","r","r","","",]
    level_name = "forest"
    start_text = "The light filtering through the leaves of the tall trees\n" \
    + "creates a subtle shimmering effect around you.\n" \
    + "The lush green grass is spotted with patches of soft soil.\n" \
    + "Were it not for the mysterious circumstance of how you\n" \
    + "got here, it'd make for a nice place to rest and enjoy the scene.\n" \
    + "you decide to explore but are not sure on how.\n" \
    + "Either leave it to fate(1) or pick direction(2).\n"

    def choose_direction(self):
        direction = 0
        user_choice = input("1 = Leave it to fate\n2 = Decide for yourself\n")

        if(user_choice == "1"):
            direction = random.randint(0,3)

            print("Choosing to go the direction of the most interesting sound,\n" \
            + "you decide to go %s" %(directions[direction]))

            navigate(self.area_map, direction)

        elif(user_choice == "2"):
            direction = int(input("Which direction will you go?\n1=up\n2=left\n" \
            + "3=down\n4=right\n"))

            print("You decide to go %s" %(directions[direction-1]))

            navigate(self.area_map, direction)

        else:
            print("Where are you going?")

class Cave:
    level_name = "cave"

class Valley:
    level_name = "valley"

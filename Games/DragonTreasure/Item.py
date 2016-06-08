"""
    This file is for housing all methods involving items found in the game
"""
from enum import Enum
import copy

class ItemType(Enum):
    weapon = 1
    healing = 2
    armor = 3
    poison = 4

class AddedEffect(Enum):
    attackUp = 1
    attackDown = 2
    defUp = 3
    defDown = 4
    spdUp = 5
    spdDown = 6
    paralysis = 7
    poison = 8
    freeze = 9
    burn = 10
    waterAug = 11
    fireAug = 12
    earthAug = 13
    windAug = 14
    dragonSlayer = 15
    regen = 16
    hpUp = 17
    hpDown = 18
    waterDef = 19
    fireDef = 20
    earthDef = 21
    windDef = 22
    mini = 23
    dragonMorph = 24

class Weapon:
    name = ""
    atk = 0
    spd = -1
    defense = -1
    addedEffect = []

    def __init__ ( self, name, atk, spd, defense, addedEffect= [] ):
        self.name = name
        self.atk = atk
        self.spd = spd
        self.defense = defense
        self.addedEffect = copy.deepcopy(addedEffect)

class Armor:
    name = ""
    defense = -10
    spd = -10
    addedEffect = []

    def __init__ ( self, name, spd, defense, addedEffect= [] ):
        self.name = name
        self.spd = spd
        self.defense = defense
        self.addedEffect = copy.deepcopy(addedEffect)

class Poison:
    dmgAmnt = 100
    fatal = True
    addedEffect = []

    def __init__ ( self, dmgAmnt, fatal, addedEffect= [] ):
        self.dmgAmnt = dmgAmnt
        self.fatal = fatal
        self.addedEffect = copy.deepcopy(addedEffect)

class HealingPotion:
    restoreAmnt = 0
    uses = 0
    addedEffect = []

    def __init__ ( self, restoreAmnt, uses, addedEffect= [] ):
        self.restoreAmnt = restoreAmnt
        self.uses = uses
        self.addedEffect = copy.deepcopy(addedEffect)

class Treasure:
    def __init__ ( self, **attribute ):
        self.__dict__.update(attribute)

    def __getAttribute__ ( self, item ):
        value = super().__getAttribute__( item )
        if( hasAttr (value, "__get__") ):
            return value.__get__(self, Treasure)
        else:
            return value

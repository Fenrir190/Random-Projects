"""
    This file houses all methods associated with dragons found throughout the game.
"""

from enum import Enum
from CharacterAttr import *

class Dragon:
    strength = 0
    defense = 0
    observation = 0
    dexterity = 0
    hp = 100
    mana = 50
    affinity = ""
    morality = ""
    element = ""

    def __init__ (strength, defense, observation, dexterity, hp, mana):
        self.strength = strength
        self.defense = defense
        self.observation = observation
        self.dexterity = dexterity
        self.hp = hp
        self.mana = mana
        self.affinity = random.choice(list(Affinity))
        self.morality = random.choice(list(Morality))
        self.element = random.choice(list(Element))

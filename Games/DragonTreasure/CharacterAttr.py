class Affinity(Enum):
    "1" = "Light"
    "2" = "Dark"
    "3" = "Neutral"

class Morality(Enum):
    "1" = "Law"
    "2" = "Chaos"
    "3" = "Evil"

class Element(Enum):
    "1" = "Fire"
    "2" = "Wind"
    "3" = "Water"
    "4" = "Earth"
    "5" = "Poison"
    "6" = "Metal"
    "7" = "Lightning"
    "8" = "Shadow"
    "9" = "Death"
    "10" = "Holy"
    "11" = "Astral"

class FusedElements(Enum):
    "1" = "Magma"
    "2" = "Steam"
    "3" = "Inferno"
    "4" = "Blast"
    "5" = "Storm"
    "6" = "Dust"
    "7" = "Ice"

class ElementalCombination:
    def elementalFusion(self, elem1, elem2):
        fusedElement = ""
        if(elem1 == Element.1 && elem2 == Element.4)
            fusedElement = FusedElements.1
        if(elem1 == Element.1 && elem2 == Element.3)
            fusedElement = FusedElements.2
        if(elem1 == Element.1 && elem2 == Element.2)
            fusedElement = FusedElements.3
        if(elem1 == Element.1 && elem2 == Element.7)
            fusedElement = FusedElements.4
        if(elem1 == Element.2 && elem2 == Element.7)
            fusedElement = FusedElements.5
        if(elem1 == Element.4 && elem2 == Element.2)
            fusedElement = FusedElements.6
        if(elem1 == Element.3 && elem2 == Element.2)
            fusedElement = FusedElements.7

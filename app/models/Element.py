from enum import Enum

class Element(Enum):
    WILD = "wild"
    FIRE = "fire"
    ICE = "ice"
    AIR = "air"
    EARTH = "earth"
    LIGHT = "light"
    DARK = "dark"

    @classmethod
    def from_string(cls, value):
        return cls[value.upper()]

    def __str__(self):
        return self.value
    
# SummonColor.py enum

from enum import Enum

class SummonColor(Enum):
    BLUE = "blue"
    GREEN = "green"
    YELLOW = "yellow"
    ORANGE = "orange"
    WHITE = "white"
    PURPLE = "purple"
    PINK = "pink"
    RED = "red"
    FH = "fh"
    CUSTOM = "custom"

    @classmethod
    def from_string(cls, color_string):
        return cls(color_string)
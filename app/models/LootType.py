# LootType.py

from enum import Enum

class LootType(Enum):
    MONEY = "money"
    LUMBER = "lumber"
    METAL = "metal"
    HIDE = "hide"
    ARROWVINE = "arrowvine"
    AXENUT = "axenut"
    CORPSECAP = "corpsecap"
    FLAMEFRUIT = "flamefruit"
    ROCKROOT = "rockroot"
    SNOWTHISTLE = "snowthistle"
    RANDOM_ITEM = "random_item"
    SPECIAL1 = "special1"
    SPECIAL2 = "special2"

    @staticmethod
    def from_string(value):
        return LootType(value)
# MonsterType.py

from enum import Enum

class MonsterType(Enum):
    NORMAL = "normal"
    ELITE = "elite"
    BOSS = "boss"

    @staticmethod
    def from_string(value):
        return MonsterType(value)
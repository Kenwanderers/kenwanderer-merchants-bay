# This should mimic the ConditionName.java enum in the GHS-Server project.

from enum import Enum

class ConditionName(Enum):
    STUN = "stun"
    IMMOBILIZE = "immobilize"
    DISARM = "disarm"
    WOUND = "wound"
    MUDDLE = "muddle"
    POISON = "poison"
    INVISIBLE = "invisible"
    STRENGTHEN = "strengthen"
    CURSE = "curse"
    BLESS = "bless"
    REGENERATE = "regenerate"
    CHILL = "chill"
    INFECT = "infect"
    WARD = "ward"
    BANE = "bane"
    BRITTLE = "brittle"
    IMPAIR = "impair"
    RUPTURE = "rupture"
    DODGE = "dodge"
    EMPOWER = "empower"
    ENFEEBLE = "enfeeble"
    POISON_X = "poison_x"
    WOUND_X = "wound_x"
    HEAL = "heal"
    SHIELD = "shield"
    INVALID = "invalid"

    @classmethod
    def from_string(cls, value):
        try:
            return cls[value.upper()]
        except KeyError:
            raise ValueError(f"{value} is not a valid condition name")

    def __str__(self):
        return self.value

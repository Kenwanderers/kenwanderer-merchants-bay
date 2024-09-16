# SummonState.py enum

from enum import Enum

class SummonState(Enum):
    NEW = "new"
    TRUE = "true"
    FALSE = "false"

    @classmethod
    def from_string(cls, state_string):
        return cls(state_string)
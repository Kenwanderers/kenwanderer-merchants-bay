from enum import Enum

class EntityConditionState(Enum):
    NEW = "new"
    NORMAL = "normal"
    EXPIRE = "expire"
    REMOVED = "removed"
    TURN = "turn"

    @classmethod
    def from_string(cls, value):
        return cls[value.upper()]

    def __str__(self):
        return self.value
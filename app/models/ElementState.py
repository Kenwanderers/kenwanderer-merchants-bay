from enum import Enum

class ElementState(Enum):
    STRONG = "strong"
    WANING = "waning"
    INERT = "inert"
    NEW = "new"
    CONSUMED = "consumed"
    PARTLY_CONSUMED = "partlyConsumed"
    ALWAYS = "always"

    @classmethod
    def from_string(cls, value):
        return cls[value.upper()]

    def __str__(self):
        return self.value
    
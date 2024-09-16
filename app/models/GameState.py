# GameState.py enum

from enum import Enum

class GameState(Enum):
    DRAW = "draw"
    NEXT = "next"
    
    def from_str(self, str):
        return GameState(str)
    
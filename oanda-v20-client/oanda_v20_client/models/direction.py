from enum import Enum


class Direction(str, Enum):
    LONG = "LONG"
    SHORT = "SHORT"

    def __str__(self) -> str:
        return str(self.value)

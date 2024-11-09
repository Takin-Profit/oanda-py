from enum import Enum


class TradePL(str, Enum):
    NEGATIVE = "NEGATIVE"
    POSITIVE = "POSITIVE"
    ZERO = "ZERO"

    def __str__(self) -> str:
        return str(self.value)

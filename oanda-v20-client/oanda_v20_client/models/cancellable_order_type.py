from enum import Enum


class CancellableOrderType(str, Enum):
    LIMIT = "LIMIT"
    MARKET_IF_TOUCHED = "MARKET_IF_TOUCHED"
    STOP = "STOP"
    STOP_LOSS = "STOP_LOSS"
    TAKE_PROFIT = "TAKE_PROFIT"
    TRAILING_STOP_LOSS = "TRAILING_STOP_LOSS"

    def __str__(self) -> str:
        return str(self.value)

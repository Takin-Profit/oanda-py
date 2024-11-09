from enum import Enum


class TradeStateFilter(str, Enum):
    ALL = "ALL"
    CLOSED = "CLOSED"
    CLOSE_WHEN_TRADEABLE = "CLOSE_WHEN_TRADEABLE"
    OPEN = "OPEN"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class TradeSummaryState(str, Enum):
    CLOSED = "CLOSED"
    CLOSE_WHEN_TRADEABLE = "CLOSE_WHEN_TRADEABLE"
    OPEN = "OPEN"

    def __str__(self) -> str:
        return str(self.value)

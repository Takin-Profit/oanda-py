from enum import Enum


class MarketOrderState(str, Enum):
    CANCELLED = "CANCELLED"
    FILLED = "FILLED"
    PENDING = "PENDING"
    TRIGGERED = "TRIGGERED"

    def __str__(self) -> str:
        return str(self.value)

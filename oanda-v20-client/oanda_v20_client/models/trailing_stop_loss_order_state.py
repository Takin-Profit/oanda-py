from enum import Enum


class TrailingStopLossOrderState(str, Enum):
    CANCELLED = "CANCELLED"
    FILLED = "FILLED"
    PENDING = "PENDING"
    TRIGGERED = "TRIGGERED"

    def __str__(self) -> str:
        return str(self.value)
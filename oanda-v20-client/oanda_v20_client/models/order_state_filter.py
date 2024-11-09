from enum import Enum


class OrderStateFilter(str, Enum):
    ALL = "ALL"
    CANCELLED = "CANCELLED"
    FILLED = "FILLED"
    PENDING = "PENDING"
    TRIGGERED = "TRIGGERED"

    def __str__(self) -> str:
        return str(self.value)

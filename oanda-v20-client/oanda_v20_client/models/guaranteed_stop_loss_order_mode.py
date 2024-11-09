from enum import Enum


class GuaranteedStopLossOrderMode(str, Enum):
    ALLOWED = "ALLOWED"
    DISABLED = "DISABLED"
    REQUIRED = "REQUIRED"

    def __str__(self) -> str:
        return str(self.value)

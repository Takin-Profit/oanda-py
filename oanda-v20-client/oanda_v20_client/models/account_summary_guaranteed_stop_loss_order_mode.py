from enum import Enum


class AccountSummaryGuaranteedStopLossOrderMode(str, Enum):
    ALLOWED = "ALLOWED"
    DISABLED = "DISABLED"
    REQUIRED = "REQUIRED"

    def __str__(self) -> str:
        return str(self.value)

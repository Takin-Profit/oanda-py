from enum import Enum


class TakeProfitOrderReason(str, Enum):
    CLIENT_ORDER = "CLIENT_ORDER"
    ON_FILL = "ON_FILL"
    REPLACEMENT = "REPLACEMENT"

    def __str__(self) -> str:
        return str(self.value)

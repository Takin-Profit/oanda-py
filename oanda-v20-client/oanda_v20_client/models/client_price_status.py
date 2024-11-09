from enum import Enum


class ClientPriceStatus(str, Enum):
    INVALID = "invalid"
    NON_TRADEABLE = "non-tradeable"
    TRADEABLE = "tradeable"

    def __str__(self) -> str:
        return str(self.value)

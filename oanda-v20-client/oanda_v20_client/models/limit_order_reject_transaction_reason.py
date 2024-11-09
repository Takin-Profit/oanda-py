from enum import Enum


class LimitOrderRejectTransactionReason(str, Enum):
    CLIENT_ORDER = "CLIENT_ORDER"
    REPLACEMENT = "REPLACEMENT"

    def __str__(self) -> str:
        return str(self.value)

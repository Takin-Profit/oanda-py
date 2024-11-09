from enum import Enum


class LimitOrderTransactionReason(str, Enum):
    CLIENT_ORDER = "CLIENT_ORDER"
    REPLACEMENT = "REPLACEMENT"

    def __str__(self) -> str:
        return str(self.value)

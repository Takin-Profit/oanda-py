from enum import Enum


class LimitOrderRejectTransactionPositionFill(str, Enum):
    DEFAULT = "DEFAULT"
    OPEN_ONLY = "OPEN_ONLY"
    REDUCE_FIRST = "REDUCE_FIRST"
    REDUCE_ONLY = "REDUCE_ONLY"

    def __str__(self) -> str:
        return str(self.value)

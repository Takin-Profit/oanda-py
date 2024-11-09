from enum import Enum


class LimitOrderRequestTriggerCondition(str, Enum):
    ASK = "ASK"
    BID = "BID"
    DEFAULT = "DEFAULT"
    INVERSE = "INVERSE"
    MID = "MID"

    def __str__(self) -> str:
        return str(self.value)

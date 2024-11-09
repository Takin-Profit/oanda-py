from enum import Enum


class PositionAggregationMode(str, Enum):
    ABSOLUTE_SUM = "ABSOLUTE_SUM"
    MAXIMAL_SIDE = "MAXIMAL_SIDE"
    NET_SUM = "NET_SUM"

    def __str__(self) -> str:
        return str(self.value)

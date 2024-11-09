from enum import Enum


class GetInstrumentCandlesResponse200Granularity(str, Enum):
    D = "D"
    H1 = "H1"
    H12 = "H12"
    H2 = "H2"
    H3 = "H3"
    H4 = "H4"
    H6 = "H6"
    H8 = "H8"
    M = "M"
    M1 = "M1"
    M10 = "M10"
    M15 = "M15"
    M2 = "M2"
    M30 = "M30"
    M4 = "M4"
    M5 = "M5"
    S10 = "S10"
    S15 = "S15"
    S30 = "S30"
    S5 = "S5"
    W = "W"

    def __str__(self) -> str:
        return str(self.value)

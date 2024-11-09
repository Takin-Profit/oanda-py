from enum import Enum


class InstrumentType(str, Enum):
    CFD = "CFD"
    CURRENCY = "CURRENCY"
    METAL = "METAL"

    def __str__(self) -> str:
        return str(self.value)

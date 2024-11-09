from enum import Enum


class StopLossOrderRejectTransactionTimeInForce(str, Enum):
    FOK = "FOK"
    GFD = "GFD"
    GTC = "GTC"
    GTD = "GTD"
    IOC = "IOC"

    def __str__(self) -> str:
        return str(self.value)

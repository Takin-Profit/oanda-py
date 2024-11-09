from enum import Enum


class MarketOrderRejectTransactionReason(str, Enum):
    CLIENT_ORDER = "CLIENT_ORDER"
    DELAYED_TRADE_CLOSE = "DELAYED_TRADE_CLOSE"
    MARGIN_CLOSEOUT = "MARGIN_CLOSEOUT"
    POSITION_CLOSEOUT = "POSITION_CLOSEOUT"
    TRADE_CLOSE = "TRADE_CLOSE"

    def __str__(self) -> str:
        return str(self.value)

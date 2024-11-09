from enum import Enum


class MarketOrderMarginCloseoutReason(str, Enum):
    MARGIN_CHECK_VIOLATION = "MARGIN_CHECK_VIOLATION"
    REGULATORY_MARGIN_CALL_VIOLATION = "REGULATORY_MARGIN_CALL_VIOLATION"
    REGULATORY_MARGIN_CHECK_VIOLATION = "REGULATORY_MARGIN_CHECK_VIOLATION"

    def __str__(self) -> str:
        return str(self.value)

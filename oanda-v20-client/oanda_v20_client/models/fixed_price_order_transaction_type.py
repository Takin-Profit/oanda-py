from enum import Enum


class FixedPriceOrderTransactionType(str, Enum):
    CLIENT_CONFIGURE = "CLIENT_CONFIGURE"
    CLIENT_CONFIGURE_REJECT = "CLIENT_CONFIGURE_REJECT"
    CLOSE = "CLOSE"
    CREATE = "CREATE"
    DAILY_FINANCING = "DAILY_FINANCING"
    DELAYED_TRADE_CLOSURE = "DELAYED_TRADE_CLOSURE"
    FIXED_PRICE_ORDER = "FIXED_PRICE_ORDER"
    LIMIT_ORDER = "LIMIT_ORDER"
    LIMIT_ORDER_REJECT = "LIMIT_ORDER_REJECT"
    MARGIN_CALL_ENTER = "MARGIN_CALL_ENTER"
    MARGIN_CALL_EXIT = "MARGIN_CALL_EXIT"
    MARGIN_CALL_EXTEND = "MARGIN_CALL_EXTEND"
    MARKET_IF_TOUCHED_ORDER = "MARKET_IF_TOUCHED_ORDER"
    MARKET_IF_TOUCHED_ORDER_REJECT = "MARKET_IF_TOUCHED_ORDER_REJECT"
    MARKET_ORDER = "MARKET_ORDER"
    MARKET_ORDER_REJECT = "MARKET_ORDER_REJECT"
    ORDER_CANCEL = "ORDER_CANCEL"
    ORDER_CANCEL_REJECT = "ORDER_CANCEL_REJECT"
    ORDER_CLIENT_EXTENSIONS_MODIFY = "ORDER_CLIENT_EXTENSIONS_MODIFY"
    ORDER_CLIENT_EXTENSIONS_MODIFY_REJECT = "ORDER_CLIENT_EXTENSIONS_MODIFY_REJECT"
    ORDER_FILL = "ORDER_FILL"
    REOPEN = "REOPEN"
    RESET_RESETTABLE_PL = "RESET_RESETTABLE_PL"
    STOP_LOSS_ORDER = "STOP_LOSS_ORDER"
    STOP_LOSS_ORDER_REJECT = "STOP_LOSS_ORDER_REJECT"
    STOP_ORDER = "STOP_ORDER"
    STOP_ORDER_REJECT = "STOP_ORDER_REJECT"
    TAKE_PROFIT_ORDER = "TAKE_PROFIT_ORDER"
    TAKE_PROFIT_ORDER_REJECT = "TAKE_PROFIT_ORDER_REJECT"
    TRADE_CLIENT_EXTENSIONS_MODIFY = "TRADE_CLIENT_EXTENSIONS_MODIFY"
    TRADE_CLIENT_EXTENSIONS_MODIFY_REJECT = "TRADE_CLIENT_EXTENSIONS_MODIFY_REJECT"
    TRAILING_STOP_LOSS_ORDER = "TRAILING_STOP_LOSS_ORDER"
    TRAILING_STOP_LOSS_ORDER_REJECT = "TRAILING_STOP_LOSS_ORDER_REJECT"
    TRANSFER_FUNDS = "TRANSFER_FUNDS"
    TRANSFER_FUNDS_REJECT = "TRANSFER_FUNDS_REJECT"

    def __str__(self) -> str:
        return str(self.value)

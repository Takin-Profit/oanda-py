from __future__ import annotations
from typing import Literal, Set, cast

OrderCancelRejectTransactionType = Literal[
    "CLIENT_CONFIGURE",
    "CLIENT_CONFIGURE_REJECT",
    "CLOSE",
    "CREATE",
    "DAILY_FINANCING",
    "DELAYED_TRADE_CLOSURE",
    "FIXED_PRICE_ORDER",
    "LIMIT_ORDER",
    "LIMIT_ORDER_REJECT",
    "MARGIN_CALL_ENTER",
    "MARGIN_CALL_EXIT",
    "MARGIN_CALL_EXTEND",
    "MARKET_IF_TOUCHED_ORDER",
    "MARKET_IF_TOUCHED_ORDER_REJECT",
    "MARKET_ORDER",
    "MARKET_ORDER_REJECT",
    "ORDER_CANCEL",
    "ORDER_CANCEL_REJECT",
    "ORDER_CLIENT_EXTENSIONS_MODIFY",
    "ORDER_CLIENT_EXTENSIONS_MODIFY_REJECT",
    "ORDER_FILL",
    "REOPEN",
    "RESET_RESETTABLE_PL",
    "STOP_LOSS_ORDER",
    "STOP_LOSS_ORDER_REJECT",
    "STOP_ORDER",
    "STOP_ORDER_REJECT",
    "TAKE_PROFIT_ORDER",
    "TAKE_PROFIT_ORDER_REJECT",
    "TRADE_CLIENT_EXTENSIONS_MODIFY",
    "TRADE_CLIENT_EXTENSIONS_MODIFY_REJECT",
    "TRAILING_STOP_LOSS_ORDER",
    "TRAILING_STOP_LOSS_ORDER_REJECT",
    "TRANSFER_FUNDS",
    "TRANSFER_FUNDS_REJECT",
]
ORDER_CANCEL_REJECT_TRANSACTION_TYPE_VALUES: Set[OrderCancelRejectTransactionType] = {
    "CLIENT_CONFIGURE",
    "CLIENT_CONFIGURE_REJECT",
    "CLOSE",
    "CREATE",
    "DAILY_FINANCING",
    "DELAYED_TRADE_CLOSURE",
    "FIXED_PRICE_ORDER",
    "LIMIT_ORDER",
    "LIMIT_ORDER_REJECT",
    "MARGIN_CALL_ENTER",
    "MARGIN_CALL_EXIT",
    "MARGIN_CALL_EXTEND",
    "MARKET_IF_TOUCHED_ORDER",
    "MARKET_IF_TOUCHED_ORDER_REJECT",
    "MARKET_ORDER",
    "MARKET_ORDER_REJECT",
    "ORDER_CANCEL",
    "ORDER_CANCEL_REJECT",
    "ORDER_CLIENT_EXTENSIONS_MODIFY",
    "ORDER_CLIENT_EXTENSIONS_MODIFY_REJECT",
    "ORDER_FILL",
    "REOPEN",
    "RESET_RESETTABLE_PL",
    "STOP_LOSS_ORDER",
    "STOP_LOSS_ORDER_REJECT",
    "STOP_ORDER",
    "STOP_ORDER_REJECT",
    "TAKE_PROFIT_ORDER",
    "TAKE_PROFIT_ORDER_REJECT",
    "TRADE_CLIENT_EXTENSIONS_MODIFY",
    "TRADE_CLIENT_EXTENSIONS_MODIFY_REJECT",
    "TRAILING_STOP_LOSS_ORDER",
    "TRAILING_STOP_LOSS_ORDER_REJECT",
    "TRANSFER_FUNDS",
    "TRANSFER_FUNDS_REJECT",
}


def check_order_cancel_reject_transaction_type(
    value: str,
) -> OrderCancelRejectTransactionType:
    if value in ORDER_CANCEL_REJECT_TRANSACTION_TYPE_VALUES:
        return cast(OrderCancelRejectTransactionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORDER_CANCEL_REJECT_TRANSACTION_TYPE_VALUES!r}"
    )

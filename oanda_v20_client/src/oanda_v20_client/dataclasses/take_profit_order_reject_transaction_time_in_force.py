from __future__ import annotations
from typing import Literal, Set, cast

TakeProfitOrderRejectTransactionTimeInForce = Literal["FOK", "GFD", "GTC", "GTD", "IOC"]
TAKE_PROFIT_ORDER_REJECT_TRANSACTION_TIME_IN_FORCE_VALUES: Set[
    TakeProfitOrderRejectTransactionTimeInForce
] = {"FOK", "GFD", "GTC", "GTD", "IOC"}


def check_take_profit_order_reject_transaction_time_in_force(
    value: str,
) -> TakeProfitOrderRejectTransactionTimeInForce:
    if value in TAKE_PROFIT_ORDER_REJECT_TRANSACTION_TIME_IN_FORCE_VALUES:
        return cast(TakeProfitOrderRejectTransactionTimeInForce, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TAKE_PROFIT_ORDER_REJECT_TRANSACTION_TIME_IN_FORCE_VALUES!r}"
    )
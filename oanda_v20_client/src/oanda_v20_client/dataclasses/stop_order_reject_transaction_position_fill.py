from __future__ import annotations
from typing import Literal, Set, cast

StopOrderRejectTransactionPositionFill = Literal[
    "DEFAULT", "OPEN_ONLY", "REDUCE_FIRST", "REDUCE_ONLY"
]
STOP_ORDER_REJECT_TRANSACTION_POSITION_FILL_VALUES: Set[
    StopOrderRejectTransactionPositionFill
] = {"DEFAULT", "OPEN_ONLY", "REDUCE_FIRST", "REDUCE_ONLY"}


def check_stop_order_reject_transaction_position_fill(
    value: str,
) -> StopOrderRejectTransactionPositionFill:
    if value in STOP_ORDER_REJECT_TRANSACTION_POSITION_FILL_VALUES:
        return cast(StopOrderRejectTransactionPositionFill, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STOP_ORDER_REJECT_TRANSACTION_POSITION_FILL_VALUES!r}"
    )

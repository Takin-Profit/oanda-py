from typing import Literal, Set, cast

MarketIfTouchedOrderPositionFill = Literal[
    "DEFAULT", "OPEN_ONLY", "REDUCE_FIRST", "REDUCE_ONLY"
]

MARKET_IF_TOUCHED_ORDER_POSITION_FILL_VALUES: Set[MarketIfTouchedOrderPositionFill] = {
    "DEFAULT",
    "OPEN_ONLY",
    "REDUCE_FIRST",
    "REDUCE_ONLY",
}


def check_market_if_touched_order_position_fill(
    value: str,
) -> MarketIfTouchedOrderPositionFill:
    if value in MARKET_IF_TOUCHED_ORDER_POSITION_FILL_VALUES:
        return cast(MarketIfTouchedOrderPositionFill, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MARKET_IF_TOUCHED_ORDER_POSITION_FILL_VALUES!r}"
    )
from __future__ import annotations
from typing import Literal, Set, cast

MarketIfTouchedOrderRejectTransactionRejectReason = Literal[
    "ACCOUNT_CONFIGURATION_LOCKED",
    "ACCOUNT_DEPOSIT_LOCKED",
    "ACCOUNT_LOCKED",
    "ACCOUNT_NOT_ACTIVE",
    "ACCOUNT_ORDER_CANCEL_LOCKED",
    "ACCOUNT_ORDER_CREATION_LOCKED",
    "ACCOUNT_WITHDRAWAL_LOCKED",
    "ADMIN_CONFIGURE_DATA_MISSING",
    "ALIAS_INVALID",
    "AMOUNT_INVALID",
    "AMOUNT_MISSING",
    "CLIENT_CONFIGURE_DATA_MISSING",
    "CLIENT_EXTENSIONS_DATA_MISSING",
    "CLIENT_ORDER_COMMENT_INVALID",
    "CLIENT_ORDER_ID_ALREADY_EXISTS",
    "CLIENT_ORDER_ID_INVALID",
    "CLIENT_ORDER_TAG_INVALID",
    "CLIENT_TRADE_COMMENT_INVALID",
    "CLIENT_TRADE_ID_ALREADY_EXISTS",
    "CLIENT_TRADE_ID_INVALID",
    "CLIENT_TRADE_TAG_INVALID",
    "CLOSE_TRADE_PARTIAL_UNITS_MISSING",
    "CLOSE_TRADE_TYPE_MISSING",
    "CLOSE_TRADE_UNITS_EXCEED_TRADE_SIZE",
    "CLOSEOUT_POSITION_DOESNT_EXIST",
    "CLOSEOUT_POSITION_INCOMPLETE_SPECIFICATION",
    "CLOSEOUT_POSITION_PARTIAL_UNITS_MISSING",
    "CLOSEOUT_POSITION_REJECT",
    "CLOSEOUT_POSITION_UNITS_EXCEED_POSITION_SIZE",
    "FUNDING_REASON_MISSING",
    "INSTRUMENT_MISSING",
    "INSTRUMENT_NOT_TRADEABLE",
    "INSTRUMENT_PRICE_UNKNOWN",
    "INSTRUMENT_UNKNOWN",
    "INSUFFICIENT_FUNDS",
    "INSUFFICIENT_MARGIN",
    "INTERNAL_SERVER_ERROR",
    "INVALID_REISSUE_IMMEDIATE_PARTIAL_FILL",
    "MARGIN_RATE_INVALID",
    "MARGIN_RATE_WOULD_TRIGGER_CLOSEOUT",
    "MARGIN_RATE_WOULD_TRIGGER_MARGIN_CALL",
    "MARKUP_GROUP_ID_INVALID",
    "ORDER_DOESNT_EXIST",
    "ORDER_FILL_POSITION_ACTION_INVALID",
    "ORDER_FILL_POSITION_ACTION_MISSING",
    "ORDER_ID_UNSPECIFIED",
    "ORDER_IDENTIFIER_INCONSISTENCY",
    "ORDER_PARTIAL_FILL_OPTION_INVALID",
    "ORDER_PARTIAL_FILL_OPTION_MISSING",
    "ORDERS_ON_FILL_DUPLICATE_CLIENT_ORDER_IDS",
    "PENDING_ORDERS_ALLOWED_EXCEEDED",
    "POSITION_AGGREGATION_MODE_INVALID",
    "PRICE_BOUND_INVALID",
    "PRICE_BOUND_PRECISION_EXCEEDED",
    "PRICE_DISTANCE_INVALID",
    "PRICE_DISTANCE_MAXIMUM_EXCEEDED",
    "PRICE_DISTANCE_MINIMUM_NOT_MET",
    "PRICE_DISTANCE_MISSING",
    "PRICE_DISTANCE_PRECISION_EXCEEDED",
    "PRICE_INVALID",
    "PRICE_MISSING",
    "PRICE_PRECISION_EXCEEDED",
    "REPLACING_ORDER_INVALID",
    "REPLACING_TRADE_ID_INVALID",
    "STOP_LOSS_ON_FILL_CLIENT_ORDER_COMMENT_INVALID",
    "STOP_LOSS_ON_FILL_CLIENT_ORDER_ID_INVALID",
    "STOP_LOSS_ON_FILL_CLIENT_ORDER_TAG_INVALID",
    "STOP_LOSS_ON_FILL_DISTANCE_INVALID",
    "STOP_LOSS_ON_FILL_DISTANCE_PRECISION_EXCEEDED",
    "STOP_LOSS_ON_FILL_GTD_TIMESTAMP_IN_PAST",
    "STOP_LOSS_ON_FILL_GTD_TIMESTAMP_MISSING",
    "STOP_LOSS_ON_FILL_GUARANTEED_LEVEL_RESTRICTION_EXCEEDED",
    "STOP_LOSS_ON_FILL_GUARANTEED_MINIMUM_DISTANCE_NOT_MET",
    "STOP_LOSS_ON_FILL_GUARANTEED_NOT_ALLOWED",
    "STOP_LOSS_ON_FILL_GUARANTEED_REQUIRED",
    "STOP_LOSS_ON_FILL_PRICE_AND_DISTANCE_BOTH_MISSING",
    "STOP_LOSS_ON_FILL_PRICE_AND_DISTANCE_BOTH_SPECIFIED",
    "STOP_LOSS_ON_FILL_PRICE_DISTANCE_MAXIMUM_EXCEEDED",
    "STOP_LOSS_ON_FILL_PRICE_INVALID",
    "STOP_LOSS_ON_FILL_PRICE_MISSING",
    "STOP_LOSS_ON_FILL_PRICE_PRECISION_EXCEEDED",
    "STOP_LOSS_ON_FILL_REQUIRED_FOR_PENDING_ORDER",
    "STOP_LOSS_ON_FILL_TIME_IN_FORCE_INVALID",
    "STOP_LOSS_ON_FILL_TIME_IN_FORCE_MISSING",
    "STOP_LOSS_ON_FILL_TRIGGER_CONDITION_INVALID",
    "STOP_LOSS_ON_FILL_TRIGGER_CONDITION_MISSING",
    "STOP_LOSS_ORDER_ALREADY_EXISTS",
    "STOP_LOSS_ORDER_GUARANTEED_HALTED_CREATE_VIOLATION",
    "STOP_LOSS_ORDER_GUARANTEED_HALTED_TIGHTEN_VIOLATION",
    "STOP_LOSS_ORDER_GUARANTEED_HEDGING_NOT_ALLOWED",
    "STOP_LOSS_ORDER_GUARANTEED_LEVEL_RESTRICTION_EXCEEDED",
    "STOP_LOSS_ORDER_GUARANTEED_MINIMUM_DISTANCE_NOT_MET",
    "STOP_LOSS_ORDER_GUARANTEED_NOT_ALLOWED",
    "STOP_LOSS_ORDER_GUARANTEED_PRICE_WITHIN_SPREAD",
    "STOP_LOSS_ORDER_GUARANTEED_REQUIRED",
    "STOP_LOSS_ORDER_NOT_CANCELABLE",
    "STOP_LOSS_ORDER_NOT_REPLACEABLE",
    "STOP_LOSS_ORDER_PRICE_AND_DISTANCE_BOTH_MISSING",
    "STOP_LOSS_ORDER_PRICE_AND_DISTANCE_BOTH_SPECIFIED",
    "TAKE_PROFIT_ON_FILL_CLIENT_ORDER_COMMENT_INVALID",
    "TAKE_PROFIT_ON_FILL_CLIENT_ORDER_ID_INVALID",
    "TAKE_PROFIT_ON_FILL_CLIENT_ORDER_TAG_INVALID",
    "TAKE_PROFIT_ON_FILL_GTD_TIMESTAMP_IN_PAST",
    "TAKE_PROFIT_ON_FILL_GTD_TIMESTAMP_MISSING",
    "TAKE_PROFIT_ON_FILL_PRICE_INVALID",
    "TAKE_PROFIT_ON_FILL_PRICE_MISSING",
    "TAKE_PROFIT_ON_FILL_PRICE_PRECISION_EXCEEDED",
    "TAKE_PROFIT_ON_FILL_TIME_IN_FORCE_INVALID",
    "TAKE_PROFIT_ON_FILL_TIME_IN_FORCE_MISSING",
    "TAKE_PROFIT_ON_FILL_TRIGGER_CONDITION_INVALID",
    "TAKE_PROFIT_ON_FILL_TRIGGER_CONDITION_MISSING",
    "TAKE_PROFIT_ORDER_ALREADY_EXISTS",
    "TIME_IN_FORCE_GTD_TIMESTAMP_IN_PAST",
    "TIME_IN_FORCE_GTD_TIMESTAMP_MISSING",
    "TIME_IN_FORCE_INVALID",
    "TIME_IN_FORCE_MISSING",
    "TRADE_DOESNT_EXIST",
    "TRADE_ID_UNSPECIFIED",
    "TRADE_IDENTIFIER_INCONSISTENCY",
    "TRADE_ON_FILL_CLIENT_EXTENSIONS_NOT_SUPPORTED",
    "TRAILING_STOP_LOSS_ON_FILL_CLIENT_ORDER_COMMENT_INVALID",
    "TRAILING_STOP_LOSS_ON_FILL_CLIENT_ORDER_ID_INVALID",
    "TRAILING_STOP_LOSS_ON_FILL_CLIENT_ORDER_TAG_INVALID",
    "TRAILING_STOP_LOSS_ON_FILL_GTD_TIMESTAMP_IN_PAST",
    "TRAILING_STOP_LOSS_ON_FILL_GTD_TIMESTAMP_MISSING",
    "TRAILING_STOP_LOSS_ON_FILL_PRICE_DISTANCE_INVALID",
    "TRAILING_STOP_LOSS_ON_FILL_PRICE_DISTANCE_MAXIMUM_EXCEEDED",
    "TRAILING_STOP_LOSS_ON_FILL_PRICE_DISTANCE_MINIMUM_NOT_MET",
    "TRAILING_STOP_LOSS_ON_FILL_PRICE_DISTANCE_MISSING",
    "TRAILING_STOP_LOSS_ON_FILL_PRICE_DISTANCE_PRECISION_EXCEEDED",
    "TRAILING_STOP_LOSS_ON_FILL_TIME_IN_FORCE_INVALID",
    "TRAILING_STOP_LOSS_ON_FILL_TIME_IN_FORCE_MISSING",
    "TRAILING_STOP_LOSS_ON_FILL_TRIGGER_CONDITION_INVALID",
    "TRAILING_STOP_LOSS_ON_FILL_TRIGGER_CONDITION_MISSING",
    "TRAILING_STOP_LOSS_ORDER_ALREADY_EXISTS",
    "TRAILING_STOP_LOSS_ORDERS_NOT_SUPPORTED",
    "TRIGGER_CONDITION_INVALID",
    "TRIGGER_CONDITION_MISSING",
    "UNITS_INVALID",
    "UNITS_LIMIT_EXCEEDED",
    "UNITS_MIMIMUM_NOT_MET",
    "UNITS_MISSING",
    "UNITS_PRECISION_EXCEEDED",
]
MARKET_IF_TOUCHED_ORDER_REJECT_TRANSACTION_REJECT_REASON_VALUES: Set[
    MarketIfTouchedOrderRejectTransactionRejectReason
] = {
    "ACCOUNT_CONFIGURATION_LOCKED",
    "ACCOUNT_DEPOSIT_LOCKED",
    "ACCOUNT_LOCKED",
    "ACCOUNT_NOT_ACTIVE",
    "ACCOUNT_ORDER_CANCEL_LOCKED",
    "ACCOUNT_ORDER_CREATION_LOCKED",
    "ACCOUNT_WITHDRAWAL_LOCKED",
    "ADMIN_CONFIGURE_DATA_MISSING",
    "ALIAS_INVALID",
    "AMOUNT_INVALID",
    "AMOUNT_MISSING",
    "CLIENT_CONFIGURE_DATA_MISSING",
    "CLIENT_EXTENSIONS_DATA_MISSING",
    "CLIENT_ORDER_COMMENT_INVALID",
    "CLIENT_ORDER_ID_ALREADY_EXISTS",
    "CLIENT_ORDER_ID_INVALID",
    "CLIENT_ORDER_TAG_INVALID",
    "CLIENT_TRADE_COMMENT_INVALID",
    "CLIENT_TRADE_ID_ALREADY_EXISTS",
    "CLIENT_TRADE_ID_INVALID",
    "CLIENT_TRADE_TAG_INVALID",
    "CLOSE_TRADE_PARTIAL_UNITS_MISSING",
    "CLOSE_TRADE_TYPE_MISSING",
    "CLOSE_TRADE_UNITS_EXCEED_TRADE_SIZE",
    "CLOSEOUT_POSITION_DOESNT_EXIST",
    "CLOSEOUT_POSITION_INCOMPLETE_SPECIFICATION",
    "CLOSEOUT_POSITION_PARTIAL_UNITS_MISSING",
    "CLOSEOUT_POSITION_REJECT",
    "CLOSEOUT_POSITION_UNITS_EXCEED_POSITION_SIZE",
    "FUNDING_REASON_MISSING",
    "INSTRUMENT_MISSING",
    "INSTRUMENT_NOT_TRADEABLE",
    "INSTRUMENT_PRICE_UNKNOWN",
    "INSTRUMENT_UNKNOWN",
    "INSUFFICIENT_FUNDS",
    "INSUFFICIENT_MARGIN",
    "INTERNAL_SERVER_ERROR",
    "INVALID_REISSUE_IMMEDIATE_PARTIAL_FILL",
    "MARGIN_RATE_INVALID",
    "MARGIN_RATE_WOULD_TRIGGER_CLOSEOUT",
    "MARGIN_RATE_WOULD_TRIGGER_MARGIN_CALL",
    "MARKUP_GROUP_ID_INVALID",
    "ORDER_DOESNT_EXIST",
    "ORDER_FILL_POSITION_ACTION_INVALID",
    "ORDER_FILL_POSITION_ACTION_MISSING",
    "ORDER_ID_UNSPECIFIED",
    "ORDER_IDENTIFIER_INCONSISTENCY",
    "ORDER_PARTIAL_FILL_OPTION_INVALID",
    "ORDER_PARTIAL_FILL_OPTION_MISSING",
    "ORDERS_ON_FILL_DUPLICATE_CLIENT_ORDER_IDS",
    "PENDING_ORDERS_ALLOWED_EXCEEDED",
    "POSITION_AGGREGATION_MODE_INVALID",
    "PRICE_BOUND_INVALID",
    "PRICE_BOUND_PRECISION_EXCEEDED",
    "PRICE_DISTANCE_INVALID",
    "PRICE_DISTANCE_MAXIMUM_EXCEEDED",
    "PRICE_DISTANCE_MINIMUM_NOT_MET",
    "PRICE_DISTANCE_MISSING",
    "PRICE_DISTANCE_PRECISION_EXCEEDED",
    "PRICE_INVALID",
    "PRICE_MISSING",
    "PRICE_PRECISION_EXCEEDED",
    "REPLACING_ORDER_INVALID",
    "REPLACING_TRADE_ID_INVALID",
    "STOP_LOSS_ON_FILL_CLIENT_ORDER_COMMENT_INVALID",
    "STOP_LOSS_ON_FILL_CLIENT_ORDER_ID_INVALID",
    "STOP_LOSS_ON_FILL_CLIENT_ORDER_TAG_INVALID",
    "STOP_LOSS_ON_FILL_DISTANCE_INVALID",
    "STOP_LOSS_ON_FILL_DISTANCE_PRECISION_EXCEEDED",
    "STOP_LOSS_ON_FILL_GTD_TIMESTAMP_IN_PAST",
    "STOP_LOSS_ON_FILL_GTD_TIMESTAMP_MISSING",
    "STOP_LOSS_ON_FILL_GUARANTEED_LEVEL_RESTRICTION_EXCEEDED",
    "STOP_LOSS_ON_FILL_GUARANTEED_MINIMUM_DISTANCE_NOT_MET",
    "STOP_LOSS_ON_FILL_GUARANTEED_NOT_ALLOWED",
    "STOP_LOSS_ON_FILL_GUARANTEED_REQUIRED",
    "STOP_LOSS_ON_FILL_PRICE_AND_DISTANCE_BOTH_MISSING",
    "STOP_LOSS_ON_FILL_PRICE_AND_DISTANCE_BOTH_SPECIFIED",
    "STOP_LOSS_ON_FILL_PRICE_DISTANCE_MAXIMUM_EXCEEDED",
    "STOP_LOSS_ON_FILL_PRICE_INVALID",
    "STOP_LOSS_ON_FILL_PRICE_MISSING",
    "STOP_LOSS_ON_FILL_PRICE_PRECISION_EXCEEDED",
    "STOP_LOSS_ON_FILL_REQUIRED_FOR_PENDING_ORDER",
    "STOP_LOSS_ON_FILL_TIME_IN_FORCE_INVALID",
    "STOP_LOSS_ON_FILL_TIME_IN_FORCE_MISSING",
    "STOP_LOSS_ON_FILL_TRIGGER_CONDITION_INVALID",
    "STOP_LOSS_ON_FILL_TRIGGER_CONDITION_MISSING",
    "STOP_LOSS_ORDER_ALREADY_EXISTS",
    "STOP_LOSS_ORDER_GUARANTEED_HALTED_CREATE_VIOLATION",
    "STOP_LOSS_ORDER_GUARANTEED_HALTED_TIGHTEN_VIOLATION",
    "STOP_LOSS_ORDER_GUARANTEED_HEDGING_NOT_ALLOWED",
    "STOP_LOSS_ORDER_GUARANTEED_LEVEL_RESTRICTION_EXCEEDED",
    "STOP_LOSS_ORDER_GUARANTEED_MINIMUM_DISTANCE_NOT_MET",
    "STOP_LOSS_ORDER_GUARANTEED_NOT_ALLOWED",
    "STOP_LOSS_ORDER_GUARANTEED_PRICE_WITHIN_SPREAD",
    "STOP_LOSS_ORDER_GUARANTEED_REQUIRED",
    "STOP_LOSS_ORDER_NOT_CANCELABLE",
    "STOP_LOSS_ORDER_NOT_REPLACEABLE",
    "STOP_LOSS_ORDER_PRICE_AND_DISTANCE_BOTH_MISSING",
    "STOP_LOSS_ORDER_PRICE_AND_DISTANCE_BOTH_SPECIFIED",
    "TAKE_PROFIT_ON_FILL_CLIENT_ORDER_COMMENT_INVALID",
    "TAKE_PROFIT_ON_FILL_CLIENT_ORDER_ID_INVALID",
    "TAKE_PROFIT_ON_FILL_CLIENT_ORDER_TAG_INVALID",
    "TAKE_PROFIT_ON_FILL_GTD_TIMESTAMP_IN_PAST",
    "TAKE_PROFIT_ON_FILL_GTD_TIMESTAMP_MISSING",
    "TAKE_PROFIT_ON_FILL_PRICE_INVALID",
    "TAKE_PROFIT_ON_FILL_PRICE_MISSING",
    "TAKE_PROFIT_ON_FILL_PRICE_PRECISION_EXCEEDED",
    "TAKE_PROFIT_ON_FILL_TIME_IN_FORCE_INVALID",
    "TAKE_PROFIT_ON_FILL_TIME_IN_FORCE_MISSING",
    "TAKE_PROFIT_ON_FILL_TRIGGER_CONDITION_INVALID",
    "TAKE_PROFIT_ON_FILL_TRIGGER_CONDITION_MISSING",
    "TAKE_PROFIT_ORDER_ALREADY_EXISTS",
    "TIME_IN_FORCE_GTD_TIMESTAMP_IN_PAST",
    "TIME_IN_FORCE_GTD_TIMESTAMP_MISSING",
    "TIME_IN_FORCE_INVALID",
    "TIME_IN_FORCE_MISSING",
    "TRADE_DOESNT_EXIST",
    "TRADE_ID_UNSPECIFIED",
    "TRADE_IDENTIFIER_INCONSISTENCY",
    "TRADE_ON_FILL_CLIENT_EXTENSIONS_NOT_SUPPORTED",
    "TRAILING_STOP_LOSS_ON_FILL_CLIENT_ORDER_COMMENT_INVALID",
    "TRAILING_STOP_LOSS_ON_FILL_CLIENT_ORDER_ID_INVALID",
    "TRAILING_STOP_LOSS_ON_FILL_CLIENT_ORDER_TAG_INVALID",
    "TRAILING_STOP_LOSS_ON_FILL_GTD_TIMESTAMP_IN_PAST",
    "TRAILING_STOP_LOSS_ON_FILL_GTD_TIMESTAMP_MISSING",
    "TRAILING_STOP_LOSS_ON_FILL_PRICE_DISTANCE_INVALID",
    "TRAILING_STOP_LOSS_ON_FILL_PRICE_DISTANCE_MAXIMUM_EXCEEDED",
    "TRAILING_STOP_LOSS_ON_FILL_PRICE_DISTANCE_MINIMUM_NOT_MET",
    "TRAILING_STOP_LOSS_ON_FILL_PRICE_DISTANCE_MISSING",
    "TRAILING_STOP_LOSS_ON_FILL_PRICE_DISTANCE_PRECISION_EXCEEDED",
    "TRAILING_STOP_LOSS_ON_FILL_TIME_IN_FORCE_INVALID",
    "TRAILING_STOP_LOSS_ON_FILL_TIME_IN_FORCE_MISSING",
    "TRAILING_STOP_LOSS_ON_FILL_TRIGGER_CONDITION_INVALID",
    "TRAILING_STOP_LOSS_ON_FILL_TRIGGER_CONDITION_MISSING",
    "TRAILING_STOP_LOSS_ORDER_ALREADY_EXISTS",
    "TRAILING_STOP_LOSS_ORDERS_NOT_SUPPORTED",
    "TRIGGER_CONDITION_INVALID",
    "TRIGGER_CONDITION_MISSING",
    "UNITS_INVALID",
    "UNITS_LIMIT_EXCEEDED",
    "UNITS_MIMIMUM_NOT_MET",
    "UNITS_MISSING",
    "UNITS_PRECISION_EXCEEDED",
}


def check_market_if_touched_order_reject_transaction_reject_reason(
    value: str,
) -> MarketIfTouchedOrderRejectTransactionRejectReason:
    if value in MARKET_IF_TOUCHED_ORDER_REJECT_TRANSACTION_REJECT_REASON_VALUES:
        return cast(MarketIfTouchedOrderRejectTransactionRejectReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MARKET_IF_TOUCHED_ORDER_REJECT_TRANSACTION_REJECT_REASON_VALUES!r}"
    )

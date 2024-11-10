from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.stop_loss_order_reject_transaction_reason import (
    check_stop_loss_order_reject_transaction_reason,
)
from ..models.stop_loss_order_reject_transaction_reason import (
    StopLossOrderRejectTransactionReason,
)
from ..models.stop_loss_order_reject_transaction_reject_reason import (
    check_stop_loss_order_reject_transaction_reject_reason,
)
from ..models.stop_loss_order_reject_transaction_reject_reason import (
    StopLossOrderRejectTransactionRejectReason,
)
from ..models.stop_loss_order_reject_transaction_time_in_force import (
    check_stop_loss_order_reject_transaction_time_in_force,
)
from ..models.stop_loss_order_reject_transaction_time_in_force import (
    StopLossOrderRejectTransactionTimeInForce,
)
from ..models.stop_loss_order_reject_transaction_trigger_condition import (
    check_stop_loss_order_reject_transaction_trigger_condition,
)
from ..models.stop_loss_order_reject_transaction_trigger_condition import (
    StopLossOrderRejectTransactionTriggerCondition,
)
from ..models.stop_loss_order_reject_transaction_type import (
    check_stop_loss_order_reject_transaction_type,
)
from ..models.stop_loss_order_reject_transaction_type import (
    StopLossOrderRejectTransactionType,
)
from typing import Union

if TYPE_CHECKING:
    from ..models.client_extensions import ClientExtensions


T = TypeVar("T", bound="StopLossOrderRejectTransaction")


@_attrs_define
class StopLossOrderRejectTransaction:
    """A StopLossOrderRejectTransaction represents the rejection of the creation of a StopLoss Order.

    Attributes:
        id (Union[Unset, str]): The Transaction's Identifier.
        time (Union[Unset, str]): The date/time when the Transaction was created.
        user_id (Union[Unset, int]): The ID of the user that initiated the creation of the Transaction.
        account_id (Union[Unset, str]): The ID of the Account the Transaction was created for.
        batch_id (Union[Unset, str]): The ID of the "batch" that the Transaction belongs to. Transactions in the same
            batch are applied to the Account simultaneously.
        request_id (Union[Unset, str]): The Request ID of the request which generated the transaction.
        type (Union[Unset, StopLossOrderRejectTransactionType]): The Type of the Transaction. Always set to
            "STOP_LOSS_ORDER_REJECT" in a StopLossOrderRejectTransaction.
        trade_id (Union[Unset, str]): The ID of the Trade to close when the price threshold is breached.
        client_trade_id (Union[Unset, str]): The client ID of the Trade to be closed when the price threshold is
            breached.
        price (Union[Unset, str]): The price threshold specified for the Stop Loss Order. If the guaranteed flag is
            false, the associated Trade will be closed by a market price that is equal to or worse than this threshold. If
            the flag is true the associated Trade will be closed at this price.
        distance (Union[Unset, str]): Specifies the distance (in price units) from the Account's current price to use as
            the Stop Loss Order price. If the Trade is short the Instrument's bid price is used, and for long Trades the ask
            is used.
        time_in_force (Union[Unset, StopLossOrderRejectTransactionTimeInForce]): The time-in-force requested for the
            StopLoss Order. Restricted to "GTC", "GFD" and "GTD" for StopLoss Orders.
        gtd_time (Union[Unset, str]): The date/time when the StopLoss Order will be cancelled if its timeInForce is
            "GTD".
        trigger_condition (Union[Unset, StopLossOrderRejectTransactionTriggerCondition]): Specification of which price
            component should be used when determining if an Order should be triggered and filled. This allows Orders to be
            triggered based on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (ask for sell, bid for buy)
            price depending on the desired behaviour. Orders are always filled using their default price component.
            This feature is only provided through the REST API. Clients who choose to specify a non-default trigger
            condition will not see it reflected in any of OANDA's proprietary or partner trading platforms, their
            transaction history or their account statements. OANDA platforms always assume that an Order's trigger condition
            is set to the default value when indicating the distance from an Order's trigger price, and will always provide
            the default trigger condition when creating or modifying an Order.
            A special restriction applies when creating a guaranteed Stop Loss Order. In this case the TriggerCondition
            value must either be "DEFAULT", or the "natural" trigger side "DEFAULT" results in. So for a Stop Loss Order for
            a long trade valid values are "DEFAULT" and "BID", and for short trades "DEFAULT" and "ASK" are valid.
        guaranteed (Union[Unset, bool]): Flag indicating that the Stop Loss Order is guaranteed. The default value
            depends on the GuaranteedStopLossOrderMode of the account, if it is REQUIRED, the default will be true, for
            DISABLED or ENABLED the default is false.
        reason (Union[Unset, StopLossOrderRejectTransactionReason]): The reason that the Stop Loss Order was initiated
        client_extensions (Union[Unset, ClientExtensions]): A ClientExtensions object allows a client to attach a
            clientID, tag and comment to Orders and Trades in their Account.  Do not set, modify, or delete this field if
            your account is associated with MT4.
        order_fill_transaction_id (Union[Unset, str]): The ID of the OrderFill Transaction that caused this Order to be
            created (only provided if this Order was created automatically when another Order was filled).
        intended_replaces_order_id (Union[Unset, str]): The ID of the Order that this Order was intended to replace
            (only provided if this Order was intended to replace an existing Order).
        reject_reason (Union[Unset, StopLossOrderRejectTransactionRejectReason]): The reason that the Reject Transaction
            was created
    """

    id: Union[Unset, str] = UNSET
    time: Union[Unset, str] = UNSET
    user_id: Union[Unset, int] = UNSET
    account_id: Union[Unset, str] = UNSET
    batch_id: Union[Unset, str] = UNSET
    request_id: Union[Unset, str] = UNSET
    type: Union[Unset, StopLossOrderRejectTransactionType] = UNSET
    trade_id: Union[Unset, str] = UNSET
    client_trade_id: Union[Unset, str] = UNSET
    price: Union[Unset, str] = UNSET
    distance: Union[Unset, str] = UNSET
    time_in_force: Union[Unset, StopLossOrderRejectTransactionTimeInForce] = UNSET
    gtd_time: Union[Unset, str] = UNSET
    trigger_condition: Union[Unset, StopLossOrderRejectTransactionTriggerCondition] = (
        UNSET
    )
    guaranteed: Union[Unset, bool] = UNSET
    reason: Union[Unset, StopLossOrderRejectTransactionReason] = UNSET
    client_extensions: Union[Unset, "ClientExtensions"] = UNSET
    order_fill_transaction_id: Union[Unset, str] = UNSET
    intended_replaces_order_id: Union[Unset, str] = UNSET
    reject_reason: Union[Unset, StopLossOrderRejectTransactionRejectReason] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        time = self.time

        user_id = self.user_id

        account_id = self.account_id

        batch_id = self.batch_id

        request_id = self.request_id

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        trade_id = self.trade_id

        client_trade_id = self.client_trade_id

        price = self.price

        distance = self.distance

        time_in_force: Union[Unset, str] = UNSET
        if not isinstance(self.time_in_force, Unset):
            time_in_force = self.time_in_force

        gtd_time = self.gtd_time

        trigger_condition: Union[Unset, str] = UNSET
        if not isinstance(self.trigger_condition, Unset):
            trigger_condition = self.trigger_condition

        guaranteed = self.guaranteed

        reason: Union[Unset, str] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason

        client_extensions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.client_extensions, Unset):
            client_extensions = self.client_extensions.to_dict()

        order_fill_transaction_id = self.order_fill_transaction_id

        intended_replaces_order_id = self.intended_replaces_order_id

        reject_reason: Union[Unset, str] = UNSET
        if not isinstance(self.reject_reason, Unset):
            reject_reason = self.reject_reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if time is not UNSET:
            field_dict["time"] = time
        if user_id is not UNSET:
            field_dict["userID"] = user_id
        if account_id is not UNSET:
            field_dict["accountID"] = account_id
        if batch_id is not UNSET:
            field_dict["batchID"] = batch_id
        if request_id is not UNSET:
            field_dict["requestID"] = request_id
        if type is not UNSET:
            field_dict["type"] = type
        if trade_id is not UNSET:
            field_dict["tradeID"] = trade_id
        if client_trade_id is not UNSET:
            field_dict["clientTradeID"] = client_trade_id
        if price is not UNSET:
            field_dict["price"] = price
        if distance is not UNSET:
            field_dict["distance"] = distance
        if time_in_force is not UNSET:
            field_dict["timeInForce"] = time_in_force
        if gtd_time is not UNSET:
            field_dict["gtdTime"] = gtd_time
        if trigger_condition is not UNSET:
            field_dict["triggerCondition"] = trigger_condition
        if guaranteed is not UNSET:
            field_dict["guaranteed"] = guaranteed
        if reason is not UNSET:
            field_dict["reason"] = reason
        if client_extensions is not UNSET:
            field_dict["clientExtensions"] = client_extensions
        if order_fill_transaction_id is not UNSET:
            field_dict["orderFillTransactionID"] = order_fill_transaction_id
        if intended_replaces_order_id is not UNSET:
            field_dict["intendedReplacesOrderID"] = intended_replaces_order_id
        if reject_reason is not UNSET:
            field_dict["rejectReason"] = reject_reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_extensions import ClientExtensions

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        time = d.pop("time", UNSET)

        user_id = d.pop("userID", UNSET)

        account_id = d.pop("accountID", UNSET)

        batch_id = d.pop("batchID", UNSET)

        request_id = d.pop("requestID", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, StopLossOrderRejectTransactionType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_stop_loss_order_reject_transaction_type(_type)

        trade_id = d.pop("tradeID", UNSET)

        client_trade_id = d.pop("clientTradeID", UNSET)

        price = d.pop("price", UNSET)

        distance = d.pop("distance", UNSET)

        _time_in_force = d.pop("timeInForce", UNSET)
        time_in_force: Union[Unset, StopLossOrderRejectTransactionTimeInForce]
        if isinstance(_time_in_force, Unset):
            time_in_force = UNSET
        else:
            time_in_force = check_stop_loss_order_reject_transaction_time_in_force(
                _time_in_force
            )

        gtd_time = d.pop("gtdTime", UNSET)

        _trigger_condition = d.pop("triggerCondition", UNSET)
        trigger_condition: Union[Unset, StopLossOrderRejectTransactionTriggerCondition]
        if isinstance(_trigger_condition, Unset):
            trigger_condition = UNSET
        else:
            trigger_condition = (
                check_stop_loss_order_reject_transaction_trigger_condition(
                    _trigger_condition
                )
            )

        guaranteed = d.pop("guaranteed", UNSET)

        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, StopLossOrderRejectTransactionReason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = check_stop_loss_order_reject_transaction_reason(_reason)

        _client_extensions = d.pop("clientExtensions", UNSET)
        client_extensions: Union[Unset, ClientExtensions]
        if isinstance(_client_extensions, Unset):
            client_extensions = UNSET
        else:
            client_extensions = ClientExtensions.from_dict(_client_extensions)

        order_fill_transaction_id = d.pop("orderFillTransactionID", UNSET)

        intended_replaces_order_id = d.pop("intendedReplacesOrderID", UNSET)

        _reject_reason = d.pop("rejectReason", UNSET)
        reject_reason: Union[Unset, StopLossOrderRejectTransactionRejectReason]
        if isinstance(_reject_reason, Unset):
            reject_reason = UNSET
        else:
            reject_reason = check_stop_loss_order_reject_transaction_reject_reason(
                _reject_reason
            )

        stop_loss_order_reject_transaction = cls(
            id=id,
            time=time,
            user_id=user_id,
            account_id=account_id,
            batch_id=batch_id,
            request_id=request_id,
            type=type,
            trade_id=trade_id,
            client_trade_id=client_trade_id,
            price=price,
            distance=distance,
            time_in_force=time_in_force,
            gtd_time=gtd_time,
            trigger_condition=trigger_condition,
            guaranteed=guaranteed,
            reason=reason,
            client_extensions=client_extensions,
            order_fill_transaction_id=order_fill_transaction_id,
            intended_replaces_order_id=intended_replaces_order_id,
            reject_reason=reject_reason,
        )

        stop_loss_order_reject_transaction.additional_properties = d
        return stop_loss_order_reject_transaction

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

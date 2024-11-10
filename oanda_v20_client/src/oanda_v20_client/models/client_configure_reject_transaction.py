from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.client_configure_reject_transaction_reject_reason import (
    check_client_configure_reject_transaction_reject_reason,
)
from ..models.client_configure_reject_transaction_reject_reason import (
    ClientConfigureRejectTransactionRejectReason,
)
from ..models.client_configure_reject_transaction_type import (
    check_client_configure_reject_transaction_type,
)
from ..models.client_configure_reject_transaction_type import (
    ClientConfigureRejectTransactionType,
)
from typing import Union


T = TypeVar("T", bound="ClientConfigureRejectTransaction")


@_attrs_define
class ClientConfigureRejectTransaction:
    """A ClientConfigureRejectTransaction represents the reject of configuration of an Account by a client.

    Attributes:
        id (Union[Unset, str]): The Transaction's Identifier.
        time (Union[Unset, str]): The date/time when the Transaction was created.
        user_id (Union[Unset, int]): The ID of the user that initiated the creation of the Transaction.
        account_id (Union[Unset, str]): The ID of the Account the Transaction was created for.
        batch_id (Union[Unset, str]): The ID of the "batch" that the Transaction belongs to. Transactions in the same
            batch are applied to the Account simultaneously.
        request_id (Union[Unset, str]): The Request ID of the request which generated the transaction.
        type (Union[Unset, ClientConfigureRejectTransactionType]): The Type of the Transaction. Always set to
            "CLIENT_CONFIGURE_REJECT" in a ClientConfigureRejectTransaction.
        alias (Union[Unset, str]): The client-provided alias for the Account.
        margin_rate (Union[Unset, str]): The margin rate override for the Account.
        reject_reason (Union[Unset, ClientConfigureRejectTransactionRejectReason]): The reason that the Reject
            Transaction was created
    """

    id: Union[Unset, str] = UNSET
    time: Union[Unset, str] = UNSET
    user_id: Union[Unset, int] = UNSET
    account_id: Union[Unset, str] = UNSET
    batch_id: Union[Unset, str] = UNSET
    request_id: Union[Unset, str] = UNSET
    type: Union[Unset, ClientConfigureRejectTransactionType] = UNSET
    alias: Union[Unset, str] = UNSET
    margin_rate: Union[Unset, str] = UNSET
    reject_reason: Union[Unset, ClientConfigureRejectTransactionRejectReason] = UNSET
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

        alias = self.alias

        margin_rate = self.margin_rate

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
        if alias is not UNSET:
            field_dict["alias"] = alias
        if margin_rate is not UNSET:
            field_dict["marginRate"] = margin_rate
        if reject_reason is not UNSET:
            field_dict["rejectReason"] = reject_reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        time = d.pop("time", UNSET)

        user_id = d.pop("userID", UNSET)

        account_id = d.pop("accountID", UNSET)

        batch_id = d.pop("batchID", UNSET)

        request_id = d.pop("requestID", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ClientConfigureRejectTransactionType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_client_configure_reject_transaction_type(_type)

        alias = d.pop("alias", UNSET)

        margin_rate = d.pop("marginRate", UNSET)

        _reject_reason = d.pop("rejectReason", UNSET)
        reject_reason: Union[Unset, ClientConfigureRejectTransactionRejectReason]
        if isinstance(_reject_reason, Unset):
            reject_reason = UNSET
        else:
            reject_reason = check_client_configure_reject_transaction_reject_reason(
                _reject_reason
            )

        client_configure_reject_transaction = cls(
            id=id,
            time=time,
            user_id=user_id,
            account_id=account_id,
            batch_id=batch_id,
            request_id=request_id,
            type=type,
            alias=alias,
            margin_rate=margin_rate,
            reject_reason=reject_reason,
        )

        client_configure_reject_transaction.additional_properties = d
        return client_configure_reject_transaction

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
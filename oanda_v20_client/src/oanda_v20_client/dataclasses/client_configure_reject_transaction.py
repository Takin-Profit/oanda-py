from __future__ import annotations
from typing import Dict, Any
import dataclasses
from dacite import from_dict
from .client_configure_reject_transaction_reject_reason import (
    ClientConfigureRejectTransactionRejectReason,
)
from .client_configure_reject_transaction_type import (
    ClientConfigureRejectTransactionType,
)
from types import UNSET, Unset
from typing import TypeVar
from typing import Union

T = TypeVar("T", bound="ClientConfigureRejectTransaction")


@dataclasses.dataclass
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
            Transaction was created"""

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

    def to_dict(self) -> Dict[str, Any]:
        """Convert the dataclass instance to a dictionary."""
        return dataclasses.asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ClientConfigureRejectTransaction":
        """Create a new instance from a dictionary."""
        return from_dict(data_class=cls, data=data)

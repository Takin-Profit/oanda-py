from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_request import OrderRequest


T = TypeVar("T", bound="CreateOrderBody")


@_attrs_define
class CreateOrderBody:
    """
    Attributes:
        order (Union[Unset, OrderRequest]): The base Order specification used when requesting that an Order be created.
            Each specific Order-type extends this definition.
    """

    order: Union[Unset, "OrderRequest"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_request import OrderRequest

        d = src_dict.copy()
        _order = d.pop("order", UNSET)
        order: Union[Unset, OrderRequest]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = OrderRequest.from_dict(_order)

        create_order_body = cls(
            order=order,
        )

        create_order_body.additional_properties = d
        return create_order_body

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
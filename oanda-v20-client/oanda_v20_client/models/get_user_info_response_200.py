from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_info import UserInfo


T = TypeVar("T", bound="GetUserInfoResponse200")


@_attrs_define
class GetUserInfoResponse200:
    """
    Attributes:
        user_info (Union[Unset, UserInfo]): A representation of user information, as provided to the user themself.
    """

    user_info: Union[Unset, "UserInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_info, Unset):
            user_info = self.user_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_info is not UNSET:
            field_dict["userInfo"] = user_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_info import UserInfo

        d = src_dict.copy()
        _user_info = d.pop("userInfo", UNSET)
        user_info: Union[Unset, UserInfo]
        if isinstance(_user_info, Unset):
            user_info = UNSET
        else:
            user_info = UserInfo.from_dict(_user_info)

        get_user_info_response_200 = cls(
            user_info=user_info,
        )

        get_user_info_response_200.additional_properties = d
        return get_user_info_response_200

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
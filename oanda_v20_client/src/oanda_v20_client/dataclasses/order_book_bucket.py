from __future__ import annotations
from typing import Dict, Any
import dataclasses
from dacite import from_dict
from types import UNSET, Unset
from typing import TypeVar
from typing import Union

T = TypeVar("T", bound="OrderBookBucket")


@dataclasses.dataclass
class OrderBookBucket:
    """The order book data for a partition of the instrument's prices.

    Attributes:
        price (Union[Unset, str]): The lowest price (inclusive) covered by the bucket. The bucket covers the price range
            from the price to price + the order book's bucketWidth.
        long_count_percent (Union[Unset, str]): The percentage of the total number of orders represented by the long
            orders found in this bucket.
        short_count_percent (Union[Unset, str]): The percentage of the total number of orders represented by the short
            orders found in this bucket."""

    price: Union[Unset, str] = UNSET
    long_count_percent: Union[Unset, str] = UNSET
    short_count_percent: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        """Convert the dataclass instance to a dictionary."""
        return dataclasses.asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "OrderBookBucket":
        """Create a new instance from a dictionary."""
        return from_dict(data_class=cls, data=data)

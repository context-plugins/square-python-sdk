from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OrderLineItemItemType(str, Enum):
    """Represents the line item type."""

    ITEM = "ITEM"
    """Indicates that the line item is an itemized sale."""

    CUSTOM_AMOUNT = "CUSTOM_AMOUNT"
    """Indicates that the line item is a non-itemized sale."""

    GIFT_CARD = "GIFT_CARD"
    """Indicates that the line item is a gift card sale. Gift cards sold through the Orders API are sold in an
    unactivated state and can be activated through the Gift Cards API using the line item ``uid``."""

    __str__ = str.__str__


OrderLineItemItemTypeOrStr: TypeAlias = Annotated[
    OrderLineItemItemType | str, open_enum_validator(OrderLineItemItemType)
]

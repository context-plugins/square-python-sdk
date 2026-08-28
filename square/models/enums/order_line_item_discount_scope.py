from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OrderLineItemDiscountScope(str, Enum):
    """Indicates whether this is a line-item or order-level discount."""

    OTHER_DISCOUNT_SCOPE = "OTHER_DISCOUNT_SCOPE"
    """Used for reporting only. The original transaction discount scope is currently not supported by the API."""

    LINE_ITEM = "LINE_ITEM"
    """The discount should be applied to only line items specified by ``OrderLineItemAppliedDiscount`` reference
    records."""

    ORDER = "ORDER"
    """The discount should be applied to the entire order."""

    __str__ = str.__str__


OrderLineItemDiscountScopeOrStr: TypeAlias = Annotated[
    OrderLineItemDiscountScope | str, open_enum_validator(OrderLineItemDiscountScope)
]

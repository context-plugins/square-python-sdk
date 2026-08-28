from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OrderLineItemDiscountType(str, Enum):
    """Indicates how the discount is applied to the associated line item or order."""

    UNKNOWN_DISCOUNT = "UNKNOWN_DISCOUNT"
    """Used for reporting only. The original transaction discount type is currently not supported by the API."""

    FIXED_PERCENTAGE = "FIXED_PERCENTAGE"
    """Apply the discount as a fixed percentage (such as 5%) off the item price."""

    FIXED_AMOUNT = "FIXED_AMOUNT"
    """Apply the discount as a fixed monetary value (such as $1.00) off the item price."""

    VARIABLE_PERCENTAGE = "VARIABLE_PERCENTAGE"
    """Apply the discount as a variable percentage based on the item price.

    The specific discount percentage of a ``VARIABLE_PERCENTAGE`` discount is assigned at the time of the purchase."""

    VARIABLE_AMOUNT = "VARIABLE_AMOUNT"
    """Apply the discount as a variable amount based on the item price.

    The specific discount amount of a ``VARIABLE_AMOUNT`` discount is assigned at the time of the purchase."""

    __str__ = str.__str__


OrderLineItemDiscountTypeOrStr: TypeAlias = Annotated[
    OrderLineItemDiscountType | str, open_enum_validator(OrderLineItemDiscountType)
]

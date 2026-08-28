from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CatalogDiscountType(str, Enum):
    """How to apply a CatalogDiscount to a CatalogItem."""

    FIXED_PERCENTAGE = "FIXED_PERCENTAGE"
    """Apply the discount as a fixed percentage (e.g., 5%) off the item price."""

    FIXED_AMOUNT = "FIXED_AMOUNT"
    """Apply the discount as a fixed amount (e.g., $1.00) off the item price."""

    VARIABLE_PERCENTAGE = "VARIABLE_PERCENTAGE"
    """Apply the discount as a variable percentage off the item price. The percentage will be specified at the time of
    sale."""

    VARIABLE_AMOUNT = "VARIABLE_AMOUNT"
    """Apply the discount as a variable amount off the item price. The amount will be specified at the time of sale."""

    __str__ = str.__str__


CatalogDiscountTypeOrStr: TypeAlias = Annotated[CatalogDiscountType | str, open_enum_validator(CatalogDiscountType)]

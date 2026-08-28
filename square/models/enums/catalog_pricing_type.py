from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CatalogPricingType(str, Enum):
    """Indicates whether the price of a CatalogItemVariation should be entered manually at the time of sale."""

    FIXED_PRICING = "FIXED_PRICING"
    """The catalog item variation's price is fixed."""

    VARIABLE_PRICING = "VARIABLE_PRICING"
    """The catalog item variation's price is entered at the time of sale."""

    __str__ = str.__str__


CatalogPricingTypeOrStr: TypeAlias = Annotated[CatalogPricingType | str, open_enum_validator(CatalogPricingType)]

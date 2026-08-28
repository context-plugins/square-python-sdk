from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CatalogCustomAttributeDefinitionSellerVisibility(str, Enum):
    """Defines the visibility of a custom attribute to sellers in Square client applications, Square APIs or in Square
    UIs (including Square Point of Sale applications and Square Dashboard)."""

    SELLER_VISIBILITY_HIDDEN = "SELLER_VISIBILITY_HIDDEN"
    """Sellers cannot read this custom attribute in Square client applications or Square APIs."""

    SELLER_VISIBILITY_READ_WRITE_VALUES = "SELLER_VISIBILITY_READ_WRITE_VALUES"
    """Sellers can read and write this custom attribute value in catalog objects, but cannot edit the custom attribute
    definition."""

    __str__ = str.__str__


CatalogCustomAttributeDefinitionSellerVisibilityOrStr: TypeAlias = Annotated[
    CatalogCustomAttributeDefinitionSellerVisibility | str,
    open_enum_validator(CatalogCustomAttributeDefinitionSellerVisibility),
]

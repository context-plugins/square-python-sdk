from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CatalogItemFoodAndBeverageDetailsDietaryPreferenceType(str, Enum):
    """The type of dietary preference for the ``FOOD_AND_BEV`` type of items and integredients."""

    STANDARD = "STANDARD"
    """A standard value from a pre-determined list."""

    CUSTOM = "CUSTOM"
    """A user-defined custom value."""

    __str__ = str.__str__


CatalogItemFoodAndBeverageDetailsDietaryPreferenceTypeOrStr: TypeAlias = Annotated[
    CatalogItemFoodAndBeverageDetailsDietaryPreferenceType | str,
    open_enum_validator(CatalogItemFoodAndBeverageDetailsDietaryPreferenceType),
]

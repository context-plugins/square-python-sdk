from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CatalogItemFoodAndBeverageDetailsDietaryPreferenceStandardDietaryPreference(str, Enum):
    """Standard dietary preferences for food and beverage items that are recommended on item creation."""

    DAIRY_FREE = "DAIRY_FREE"
    GLUTEN_FREE = "GLUTEN_FREE"
    HALAL = "HALAL"
    KOSHER = "KOSHER"
    NUT_FREE = "NUT_FREE"
    VEGAN = "VEGAN"
    VEGETARIAN = "VEGETARIAN"

    __str__ = str.__str__


CatalogItemFoodAndBeverageDetailsDietaryPreferenceStandardDietaryPreferenceOrStr: TypeAlias = Annotated[
    CatalogItemFoodAndBeverageDetailsDietaryPreferenceStandardDietaryPreference | str,
    open_enum_validator(CatalogItemFoodAndBeverageDetailsDietaryPreferenceStandardDietaryPreference),
]

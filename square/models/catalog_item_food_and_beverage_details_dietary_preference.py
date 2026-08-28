from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.catalog_item_food_and_beverage_details_dietary_preference_standard_dietary_preference import (
    CatalogItemFoodAndBeverageDetailsDietaryPreferenceStandardDietaryPreferenceOrStr,
)
from .enums.catalog_item_food_and_beverage_details_dietary_preference_type import (
    CatalogItemFoodAndBeverageDetailsDietaryPreferenceTypeOrStr,
)


class CatalogItemFoodAndBeverageDetailsDietaryPreference(SdkBaseModel):
    """Dietary preferences that can be assigned to an ``FOOD_AND_BEV`` item and its ingredients."""

    type_: Optional[CatalogItemFoodAndBeverageDetailsDietaryPreferenceTypeOrStr] = Field(default=UNSET, alias="type")
    """The type of dietary preference for the ``FOOD_AND_BEV`` type of items and integredients."""

    standard_name: Optional[CatalogItemFoodAndBeverageDetailsDietaryPreferenceStandardDietaryPreferenceOrStr] = UNSET
    """Standard dietary preferences for food and beverage items that are recommended on item creation."""

    custom_name: OptionalNullable[str] = UNSET
    """The name of a user-defined custom dietary preference. This should be null if it's a standard dietary
    preference."""


class CatalogItemFoodAndBeverageDetailsDietaryPreferenceDict(TypedDict):
    type_: NotRequired[CatalogItemFoodAndBeverageDetailsDietaryPreferenceTypeOrStr]
    standard_name: NotRequired[CatalogItemFoodAndBeverageDetailsDietaryPreferenceStandardDietaryPreferenceOrStr]
    custom_name: NotRequired[str | None]

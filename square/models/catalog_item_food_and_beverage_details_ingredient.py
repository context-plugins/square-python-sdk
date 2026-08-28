from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.catalog_item_food_and_beverage_details_dietary_preference_type import (
    CatalogItemFoodAndBeverageDetailsDietaryPreferenceTypeOrStr,
)
from .enums.catalog_item_food_and_beverage_details_ingredient_standard_ingredient import (
    CatalogItemFoodAndBeverageDetailsIngredientStandardIngredientOrStr,
)


class CatalogItemFoodAndBeverageDetailsIngredient(SdkBaseModel):
    """Describes the ingredient used in a ``FOOD_AND_BEV`` item."""

    type_: Optional[CatalogItemFoodAndBeverageDetailsDietaryPreferenceTypeOrStr] = Field(default=UNSET, alias="type")
    """The type of dietary preference for the ``FOOD_AND_BEV`` type of items and integredients."""

    standard_name: Optional[CatalogItemFoodAndBeverageDetailsIngredientStandardIngredientOrStr] = UNSET
    """Standard ingredients for food and beverage items that are recommended on item creation."""

    custom_name: OptionalNullable[str] = UNSET
    """The name of a custom user-defined ingredient. This should be null if it's a standard dietary preference."""


class CatalogItemFoodAndBeverageDetailsIngredientDict(TypedDict):
    type_: NotRequired[CatalogItemFoodAndBeverageDetailsDietaryPreferenceTypeOrStr]
    standard_name: NotRequired[CatalogItemFoodAndBeverageDetailsIngredientStandardIngredientOrStr]
    custom_name: NotRequired[str | None]

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .catalog_item_food_and_beverage_details_dietary_preference import (
    CatalogItemFoodAndBeverageDetailsDietaryPreference,
    CatalogItemFoodAndBeverageDetailsDietaryPreferenceDict,
)
from .catalog_item_food_and_beverage_details_ingredient import (
    CatalogItemFoodAndBeverageDetailsIngredient,
    CatalogItemFoodAndBeverageDetailsIngredientDict,
)


class CatalogItemFoodAndBeverageDetails(SdkBaseModel):
    """The food and beverage-specific details of a ``FOOD_AND_BEV`` item."""

    calorie_count: OptionalNullable[int] = UNSET
    """The calorie count (in the unit of kcal) for the ``FOOD_AND_BEV`` type of items."""

    dietary_preferences: OptionalNullable[list[CatalogItemFoodAndBeverageDetailsDietaryPreference]] = UNSET
    """The dietary preferences for the ``FOOD_AND_BEV`` item."""

    ingredients: OptionalNullable[list[CatalogItemFoodAndBeverageDetailsIngredient]] = UNSET
    """The ingredients for the ``FOOD_AND_BEV`` type item."""


class CatalogItemFoodAndBeverageDetailsDict(TypedDict):
    calorie_count: NotRequired[int | None]
    dietary_preferences: NotRequired[list[CatalogItemFoodAndBeverageDetailsDietaryPreferenceDict] | None]
    ingredients: NotRequired[list[CatalogItemFoodAndBeverageDetailsIngredientDict] | None]

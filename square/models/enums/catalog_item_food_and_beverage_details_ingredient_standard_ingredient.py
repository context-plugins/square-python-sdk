from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CatalogItemFoodAndBeverageDetailsIngredientStandardIngredient(str, Enum):
    """Standard ingredients for food and beverage items that are recommended on item creation."""

    CELERY = "CELERY"
    CRUSTACEANS = "CRUSTACEANS"
    EGGS = "EGGS"
    FISH = "FISH"
    GLUTEN = "GLUTEN"
    LUPIN = "LUPIN"
    MILK = "MILK"
    MOLLUSCS = "MOLLUSCS"
    MUSTARD = "MUSTARD"
    PEANUTS = "PEANUTS"
    SESAME = "SESAME"
    SOY = "SOY"
    SULPHITES = "SULPHITES"
    TREE_NUTS = "TREE_NUTS"

    __str__ = str.__str__


CatalogItemFoodAndBeverageDetailsIngredientStandardIngredientOrStr: TypeAlias = Annotated[
    CatalogItemFoodAndBeverageDetailsIngredientStandardIngredient | str,
    open_enum_validator(CatalogItemFoodAndBeverageDetailsIngredientStandardIngredient),
]

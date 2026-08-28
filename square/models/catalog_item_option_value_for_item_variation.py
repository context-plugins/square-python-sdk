from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CatalogItemOptionValueForItemVariation(SdkBaseModel):
    """A ``CatalogItemOptionValue`` links an item variation to an item option as an item option value. For example, a
    t-shirt item may offer a color option and a size option. An item option value would represent each variation of
    t-shirt: For example, "Color:Red, Size:Small" or "Color:Blue, Size:Medium"."""

    item_option_id: OptionalNullable[str] = UNSET
    """The unique id of an item option."""

    item_option_value_id: OptionalNullable[str] = UNSET
    """The unique id of the selected value for the item option."""


class CatalogItemOptionValueForItemVariationDict(TypedDict):
    item_option_id: NotRequired[str | None]
    item_option_value_id: NotRequired[str | None]

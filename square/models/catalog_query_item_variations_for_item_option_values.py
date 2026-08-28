from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CatalogQueryItemVariationsForItemOptionValues(SdkBaseModel):
    """The query filter to return the item variations containing the specified item option value IDs."""

    item_option_value_ids: Optional[list[str | None]] = UNSET
    """A set of ``CatalogItemOptionValue`` IDs to be used to find associated ``CatalogItemVariation``s. All
    ItemVariations that contain all of the given Item Option Values (in any order) will be returned."""


class CatalogQueryItemVariationsForItemOptionValuesDict(TypedDict):
    item_option_value_ids: NotRequired[list[str | None]]

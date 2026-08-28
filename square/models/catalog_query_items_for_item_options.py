from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CatalogQueryItemsForItemOptions(SdkBaseModel):
    """The query filter to return the items containing the specified item option IDs."""

    item_option_ids: Optional[list[str | None]] = UNSET
    """A set of ``CatalogItemOption`` IDs to be used to find associated ``CatalogItem``s. All Items that contain all of
    the given Item Options (in any order) will be returned."""


class CatalogQueryItemsForItemOptionsDict(TypedDict):
    item_option_ids: NotRequired[list[str | None]]

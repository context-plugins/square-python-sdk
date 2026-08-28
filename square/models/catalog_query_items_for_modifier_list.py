from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CatalogQueryItemsForModifierList(SdkBaseModel):
    """The query filter to return the items containing the specified modifier list IDs."""

    modifier_list_ids: list[str]
    """A set of ``CatalogModifierList`` IDs to be used to find associated ``CatalogItem``s."""


class CatalogQueryItemsForModifierListDict(TypedDict):
    modifier_list_ids: list[str]

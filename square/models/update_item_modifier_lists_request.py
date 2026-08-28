from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UpdateItemModifierListsRequest(SdkBaseModel):
    item_ids: list[str]
    """The IDs of the catalog items associated with the CatalogModifierList objects being updated."""

    modifier_lists_to_enable: Optional[list[str | None]] = UNSET
    """The IDs of the CatalogModifierList objects to enable for the CatalogItem. At least one of
    ``modifier_lists_to_enable`` or ``modifier_lists_to_disable`` must be specified."""

    modifier_lists_to_disable: Optional[list[str | None]] = UNSET
    """The IDs of the CatalogModifierList objects to disable for the CatalogItem. At least one of
    ``modifier_lists_to_enable`` or ``modifier_lists_to_disable`` must be specified."""


class UpdateItemModifierListsRequestDict(TypedDict):
    item_ids: list[str]
    modifier_lists_to_enable: NotRequired[list[str | None]]
    modifier_lists_to_disable: NotRequired[list[str | None]]

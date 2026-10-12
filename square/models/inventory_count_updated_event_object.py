from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .inventory_count import InventoryCount, InventoryCountDict


class InventoryCountUpdatedEventObject(SdkBaseModel):
    inventory_counts: OptionalNullable[list[InventoryCount]] = UNSET
    """The inventory counts."""


class InventoryCountUpdatedEventObjectDict(TypedDict):
    inventory_counts: NotRequired[list[InventoryCountDict] | None]

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .inventory_count import InventoryCount, InventoryCountDict


class InventoryCountUpdatedEventObject(SdkBaseModel):
    inventory_counts: Optional[list[InventoryCount | None]] = UNSET
    """The inventory counts."""


class InventoryCountUpdatedEventObjectDict(TypedDict):
    inventory_counts: NotRequired[list[InventoryCount | InventoryCountDict | None]]

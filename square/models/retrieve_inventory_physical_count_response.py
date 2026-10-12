from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .inventory_physical_count import InventoryPhysicalCount, InventoryPhysicalCountDict


class RetrieveInventoryPhysicalCountResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    count: Optional[InventoryPhysicalCount] = UNSET
    """Represents the quantity of an item variation that is physically present at a specific location, verified by a
    seller or a seller's employee. For example, a physical count might come from an employee counting the item
    variations on hand or from syncing with an external system."""


class RetrieveInventoryPhysicalCountResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    count: NotRequired[InventoryPhysicalCountDict]

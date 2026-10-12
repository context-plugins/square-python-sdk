from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .inventory_change import InventoryChange, InventoryChangeDict
from .inventory_count import InventoryCount, InventoryCountDict


class BatchChangeInventoryResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    counts: Optional[list[InventoryCount]] = UNSET
    """The current counts for all objects referenced in the request."""

    changes: Optional[list[InventoryChange]] = UNSET
    """Changes created for the request."""


class BatchChangeInventoryResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    counts: NotRequired[list[InventoryCountDict]]
    changes: NotRequired[list[InventoryChangeDict]]

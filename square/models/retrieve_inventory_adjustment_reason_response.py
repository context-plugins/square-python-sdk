from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .inventory_adjustment_reason import InventoryAdjustmentReason, InventoryAdjustmentReasonDict


class RetrieveInventoryAdjustmentReasonResponse(SdkBaseModel):
    """Represents an output from a call to `RetrieveInventoryAdjustmentReason
    <api-endpoint:Inventory-RetrieveInventoryAdjustmentReason>`__."""

    errors: Optional[list[Error]] = UNSET
    """Errors encountered when the request fails."""

    adjustment_reason: Optional[InventoryAdjustmentReason] = UNSET
    """Represents an inventory adjustment reason."""


class RetrieveInventoryAdjustmentReasonResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    adjustment_reason: NotRequired[InventoryAdjustmentReasonDict]

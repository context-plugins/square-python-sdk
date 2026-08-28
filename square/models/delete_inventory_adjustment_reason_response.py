from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .inventory_adjustment_reason import InventoryAdjustmentReason, InventoryAdjustmentReasonDict


class DeleteInventoryAdjustmentReasonResponse(SdkBaseModel):
    """Represents an output from a call to `DeleteInventoryAdjustmentReason
    <api-endpoint:Inventory-DeleteInventoryAdjustmentReason>`__."""

    errors: Optional[list[Error]] = UNSET
    """Errors encountered when the request fails."""

    adjustment_reason: Optional[InventoryAdjustmentReason] = UNSET
    """Represents an inventory adjustment reason."""


class DeleteInventoryAdjustmentReasonResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    adjustment_reason: NotRequired[InventoryAdjustmentReason | InventoryAdjustmentReasonDict]

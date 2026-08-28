from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .inventory_adjustment_reason import InventoryAdjustmentReason, InventoryAdjustmentReasonDict


class CreateInventoryAdjustmentReasonResponse(SdkBaseModel):
    """Represents an output from a call to `CreateInventoryAdjustmentReason
    <api-endpoint:Inventory-CreateInventoryAdjustmentReason>`__."""

    errors: Optional[list[Error]] = UNSET
    """Errors encountered when the request fails."""

    adjustment_reason: Optional[InventoryAdjustmentReason] = UNSET
    """Represents an inventory adjustment reason."""


class CreateInventoryAdjustmentReasonResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    adjustment_reason: NotRequired[InventoryAdjustmentReason | InventoryAdjustmentReasonDict]

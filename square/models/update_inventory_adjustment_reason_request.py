from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .inventory_adjustment_reason import InventoryAdjustmentReason, InventoryAdjustmentReasonDict
from .inventory_adjustment_reason_id import InventoryAdjustmentReasonId, InventoryAdjustmentReasonIdDict


class UpdateInventoryAdjustmentReasonRequest(SdkBaseModel):
    """Represents an input to a call to `UpdateInventoryAdjustmentReason
    <api-endpoint:Inventory-UpdateInventoryAdjustmentReason>`__."""

    reason_id: InventoryAdjustmentReasonId
    """Identifies a standard or custom inventory adjustment reason."""

    adjustment_reason: InventoryAdjustmentReason
    """Represents an inventory adjustment reason."""


class UpdateInventoryAdjustmentReasonRequestDict(TypedDict):
    reason_id: InventoryAdjustmentReasonIdDict
    adjustment_reason: InventoryAdjustmentReasonDict

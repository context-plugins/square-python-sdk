from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .inventory_adjustment_reason_id import InventoryAdjustmentReasonId, InventoryAdjustmentReasonIdDict


class RestoreInventoryAdjustmentReasonRequest(SdkBaseModel):
    """Represents an input to a call to `RestoreInventoryAdjustmentReason
    <api-endpoint:Inventory-RestoreInventoryAdjustmentReason>`__."""

    reason_id: InventoryAdjustmentReasonId
    """Identifies a standard or custom inventory adjustment reason."""


class RestoreInventoryAdjustmentReasonRequestDict(TypedDict):
    reason_id: InventoryAdjustmentReasonIdDict

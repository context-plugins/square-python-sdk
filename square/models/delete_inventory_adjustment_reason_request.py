from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .inventory_adjustment_reason_id import InventoryAdjustmentReasonId, InventoryAdjustmentReasonIdDict


class DeleteInventoryAdjustmentReasonRequest(SdkBaseModel):
    """Represents an input to a call to `DeleteInventoryAdjustmentReason
    <api-endpoint:Inventory-DeleteInventoryAdjustmentReason>`__."""

    reason_id: InventoryAdjustmentReasonId
    """Identifies a standard or custom inventory adjustment reason."""


class DeleteInventoryAdjustmentReasonRequestDict(TypedDict):
    reason_id: InventoryAdjustmentReasonIdDict

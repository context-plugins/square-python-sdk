from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .inventory_adjustment_reason_id import InventoryAdjustmentReasonId, InventoryAdjustmentReasonIdDict


class RetrieveInventoryAdjustmentReasonRequest(SdkBaseModel):
    """Represents an input to a call to `RetrieveInventoryAdjustmentReason
    <api-endpoint:Inventory-RetrieveInventoryAdjustmentReason>`__."""

    reason_id: InventoryAdjustmentReasonId
    """Identifies a standard or custom inventory adjustment reason."""


class RetrieveInventoryAdjustmentReasonRequestDict(TypedDict):
    reason_id: InventoryAdjustmentReasonIdDict

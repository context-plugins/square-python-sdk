from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .inventory_adjustment_reason import InventoryAdjustmentReason, InventoryAdjustmentReasonDict


class CreateInventoryAdjustmentReasonRequest(SdkBaseModel):
    """Represents an input to a call to `CreateInventoryAdjustmentReason
    <api-endpoint:Inventory-CreateInventoryAdjustmentReason>`__."""

    idempotency_key: str
    """A client-supplied, universally unique identifier to make this `CreateInventoryAdjustmentReason
    <api-endpoint:Inventory-CreateInventoryAdjustmentReason>`__ request idempotent."""

    adjustment_reason: InventoryAdjustmentReason
    """Represents an inventory adjustment reason."""


class CreateInventoryAdjustmentReasonRequestDict(TypedDict):
    idempotency_key: str
    adjustment_reason: InventoryAdjustmentReasonDict

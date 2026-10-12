from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .inventory_adjustment_reason import InventoryAdjustmentReason, InventoryAdjustmentReasonDict


class ListInventoryAdjustmentReasonsResponse(SdkBaseModel):
    """Represents an output from a call to `ListInventoryAdjustmentReasons
    <api-endpoint:Inventory-ListInventoryAdjustmentReasons>`__."""

    errors: Optional[list[Error]] = UNSET
    """Errors encountered when the request fails."""

    adjustment_reasons: Optional[list[InventoryAdjustmentReason]] = UNSET
    """The standard, system-generated, and custom inventory adjustment reasons available to the seller."""


class ListInventoryAdjustmentReasonsResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    adjustment_reasons: NotRequired[list[InventoryAdjustmentReasonDict]]

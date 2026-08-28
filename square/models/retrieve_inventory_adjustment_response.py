from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .inventory_adjustment import InventoryAdjustment, InventoryAdjustmentDict


class RetrieveInventoryAdjustmentResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    adjustment: Optional[InventoryAdjustment] = UNSET
    """Represents a change in state or quantity of product inventory at a particular time and location."""


class RetrieveInventoryAdjustmentResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    adjustment: NotRequired[InventoryAdjustment | InventoryAdjustmentDict]

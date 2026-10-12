from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.inventory_adjustment_reason_direction import InventoryAdjustmentReasonDirectionOrStr
from .inventory_adjustment_reason_id import InventoryAdjustmentReasonId, InventoryAdjustmentReasonIdDict


class InventoryAdjustmentReason(SdkBaseModel):
    """Represents an inventory adjustment reason."""

    id: InventoryAdjustmentReasonId
    """Identifies a standard or custom inventory adjustment reason."""

    name: OptionalNullable[str] = UNSET
    """The seller-facing name for a custom inventory adjustment reason. This field is empty for standard and
    system-generated adjustment reasons."""

    direction: Optional[InventoryAdjustmentReasonDirectionOrStr] = UNSET
    created_at: Optional[str] = UNSET
    """An RFC 3339-formatted timestamp that indicates when the custom adjustment reason was created. This field is empty
    for standard adjustment reasons."""

    updated_at: Optional[str] = UNSET
    """An RFC 3339-formatted timestamp that indicates when the custom adjustment reason was last updated. This field is
    empty for standard adjustment reasons."""

    is_deleted: OptionalNullable[bool] = UNSET
    """Indicates whether this custom inventory adjustment reason has been deleted. Deleted custom reasons can still be
    retrieved by ID, but are omitted from list responses unless deleted reasons are explicitly included. To restore a
    deleted custom reason, call `RestoreInventoryAdjustmentReason
    <api-endpoint:Inventory-RestoreInventoryAdjustmentReason>`__. This field is always ``false`` for standard and
    system-generated adjustment reasons."""


class InventoryAdjustmentReasonDict(TypedDict):
    id: InventoryAdjustmentReasonIdDict
    name: NotRequired[str | None]
    direction: NotRequired[InventoryAdjustmentReasonDirectionOrStr]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    is_deleted: NotRequired[bool | None]

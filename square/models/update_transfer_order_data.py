from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .update_transfer_order_line_data import UpdateTransferOrderLineData, UpdateTransferOrderLineDataDict


class UpdateTransferOrderData(SdkBaseModel):
    """Data model for updating a transfer order. All fields are optional."""

    source_location_id: OptionalNullable[str] = UNSET
    """The source `Location <entity:Location>`__ that will send the items. Must be an active location in your Square
    account with sufficient inventory of the requested items."""

    destination_location_id: OptionalNullable[str] = UNSET
    """The destination `Location <entity:Location>`__ that will receive the items. Must be an active location in your
    Square account."""

    expected_at: OptionalNullable[str] = UNSET
    """Expected transfer date in RFC 3339 format (e.g. "2023-10-01T12:00:00Z")."""

    notes: OptionalNullable[str] = UNSET
    """Optional notes about the transfer"""

    tracking_number: OptionalNullable[str] = UNSET
    """Shipment tracking number"""

    line_items: Optional[list[UpdateTransferOrderLineData | None]] = UNSET
    """List of items being transferred"""


class UpdateTransferOrderDataDict(TypedDict):
    source_location_id: NotRequired[str | None]
    destination_location_id: NotRequired[str | None]
    expected_at: NotRequired[str | None]
    notes: NotRequired[str | None]
    tracking_number: NotRequired[str | None]
    line_items: NotRequired[list[UpdateTransferOrderLineData | UpdateTransferOrderLineDataDict | None]]

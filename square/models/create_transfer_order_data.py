from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .create_transfer_order_line_data import CreateTransferOrderLineData, CreateTransferOrderLineDataDict


class CreateTransferOrderData(SdkBaseModel):
    """Data for creating a new transfer order to move `CatalogItemVariation <entity:CatalogItemVariation>`__s between
    `Location <entity:Location>`__s. Used with the `CreateTransferOrder
    <api-endpoint:TransferOrders-CreateTransferOrder>`__ endpoint."""

    source_location_id: str
    """The source `Location <entity:Location>`__ that will send the items. Must be an active location in your Square
    account with sufficient inventory of the requested items."""

    destination_location_id: str
    """The destination `Location <entity:Location>`__ that will receive the items. Must be an active location in your
    Square account"""

    expected_at: OptionalNullable[str] = UNSET
    """Expected transfer date in RFC 3339 format (e.g. "2023-10-01T12:00:00Z")."""

    notes: OptionalNullable[str] = UNSET
    """Optional notes about the transfer"""

    tracking_number: OptionalNullable[str] = UNSET
    """Optional shipment tracking number"""

    created_by_team_member_id: OptionalNullable[str] = UNSET
    """ID of the `TeamMember <entity:TeamMember>`__ creating this transfer order. Used for tracking and auditing
    purposes."""

    line_items: Optional[list[CreateTransferOrderLineData | None]] = UNSET
    """List of `CatalogItemVariation <entity:CatalogItemVariation>`__s to transfer, including quantities"""


class CreateTransferOrderDataDict(TypedDict):
    source_location_id: str
    destination_location_id: str
    expected_at: NotRequired[str | None]
    notes: NotRequired[str | None]
    tracking_number: NotRequired[str | None]
    created_by_team_member_id: NotRequired[str | None]
    line_items: NotRequired[list[CreateTransferOrderLineData | CreateTransferOrderLineDataDict | None]]

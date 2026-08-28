from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.transfer_order_status import TransferOrderStatusOrStr
from .transfer_order_line import TransferOrderLine, TransferOrderLineDict


class TransferOrder(SdkBaseModel):
    """Represents a transfer order for moving `CatalogItemVariation <entity:CatalogItemVariation>`__s between `Location
    <entity:Location>`__s. Transfer orders track the entire lifecycle of an inventory transfer, including:
    - What items and quantities are being moved
    - Source and destination locations
    - Current `TransferOrderStatus <entity:TransferOrderStatus>`__
    - Shipping information and tracking
    - Which `TeamMember <entity:TeamMember>`__ initiated the transfer

    This object is commonly used to:
    - Track `CatalogItemVariation <entity:CatalogItemVariation>`__ movements between `Location <entity:Location>`__s
    - Reconcile expected vs received quantities
    - Monitor transfer progress and shipping status
    - Audit inventory movement history"""

    id: Optional[str] = UNSET
    """Unique system-generated identifier for this transfer order. Use this ID for:
    - Retrieving transfer order details
    - Tracking status changes via webhooks
    - Linking transfers in external systems"""

    source_location_id: OptionalNullable[str] = UNSET
    """The source `Location <entity:Location>`__ sending the `CatalogItemVariation <entity:CatalogItemVariation>`__s.
    This location must:
    - Be active in your Square organization
    - Have sufficient inventory for the items being transferred
    - Not be the same as the destination location

    This field is not updatable."""

    destination_location_id: OptionalNullable[str] = UNSET
    """The destination `Location <entity:Location>`__ receiving the `CatalogItemVariation
    <entity:CatalogItemVariation>`__s. This location must:
    - Be active in your Square organization
    - Not be the same as the source location

    This field is not updatable."""

    status: Optional[TransferOrderStatusOrStr] = UNSET
    """Status values for transfer orders. Represents the current state of a `TransferOrder <entity:TransferOrder>`__ in
    its lifecycle from creation to completion. Each status determines what actions are available and how inventory is
    affected."""

    created_at: Optional[str] = UNSET
    """Timestamp when the transfer order was created, in RFC 3339 format. Used for:
    - Auditing transfer history
    - Tracking order age
    - Reporting and analytics"""

    updated_at: Optional[str] = UNSET
    """Timestamp when the transfer order was last updated, in RFC 3339 format. Updated when:
    - Order status changes
    - Items are received
    - Notes or metadata are modified"""

    expected_at: OptionalNullable[str] = UNSET
    """Expected transfer completion date, in RFC 3339 format. Used for:
    - Planning inventory availability
    - Scheduling receiving staff
    - Monitoring transfer timeliness"""

    completed_at: Optional[str] = UNSET
    """Timestamp when the transfer order was completed or canceled, in RFC 3339 format (e.g. "2023-10-01T12:00:00Z")."""

    notes: OptionalNullable[str] = UNSET
    """Optional notes about the transfer."""

    tracking_number: OptionalNullable[str] = UNSET
    """Shipment tracking number for monitoring transfer progress."""

    created_by_team_member_id: Optional[str] = UNSET
    """ID of the `TeamMember <entity:TeamMember>`__ who created this transfer order. This field is not writeable by the
    Connect V2 API."""

    line_items: Optional[list[TransferOrderLine | None]] = UNSET
    """List of `CatalogItemVariation <entity:CatalogItemVariation>`__s being transferred."""

    version: Optional[int] = UNSET
    """Version for optimistic concurrency control. This is a monotonically increasing integer that changes whenever the
    transfer order is modified. Use this when calling `UpdateTransferOrder
    <api-endpoint:TransferOrders-UpdateTransferOrder>`__ and other endpoints to ensure you're not overwriting concurrent
    changes."""


class TransferOrderDict(TypedDict):
    id: NotRequired[str]
    source_location_id: NotRequired[str | None]
    destination_location_id: NotRequired[str | None]
    status: NotRequired[TransferOrderStatusOrStr]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    expected_at: NotRequired[str | None]
    completed_at: NotRequired[str]
    notes: NotRequired[str | None]
    tracking_number: NotRequired[str | None]
    created_by_team_member_id: NotRequired[str]
    line_items: NotRequired[list[TransferOrderLine | TransferOrderLineDict | None]]
    version: NotRequired[int]

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .fulfillment_recipient import FulfillmentRecipient, FulfillmentRecipientDict


class FulfillmentShipmentDetails(SdkBaseModel):
    """Contains the details necessary to fulfill a shipment order."""

    recipient: Optional[FulfillmentRecipient] = UNSET
    """Information about the fulfillment recipient."""

    carrier: OptionalNullable[str] = UNSET
    """The shipping carrier being used to ship this fulfillment (such as UPS, FedEx, or USPS)."""

    shipping_note: OptionalNullable[str] = UNSET
    """A note with additional information for the shipping carrier."""

    shipping_type: OptionalNullable[str] = UNSET
    """A description of the type of shipping product purchased from the carrier (such as First Class, Priority, or
    Express)."""

    tracking_number: OptionalNullable[str] = UNSET
    """The reference number provided by the carrier to track the shipment's progress."""

    tracking_url: OptionalNullable[str] = UNSET
    """A link to the tracking webpage on the carrier's website."""

    placed_at: Optional[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ indicating when the
    shipment was requested. The timestamp must be in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z")."""

    in_progress_at: Optional[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ indicating when this
    fulfillment was moved to the ``RESERVED`` state, which indicates that preparation of this shipment has begun. The
    timestamp must be in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z")."""

    packaged_at: Optional[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ indicating when this
    fulfillment was moved to the ``PREPARED`` state, which indicates that the fulfillment is packaged. The timestamp
    must be in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z")."""

    expected_shipped_at: OptionalNullable[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ indicating when the
    shipment is expected to be delivered to the shipping carrier. The timestamp must be in RFC 3339 format (for example,
    "2016-09-04T23:59:33.123Z")."""

    shipped_at: Optional[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ indicating when this
    fulfillment was moved to the ``COMPLETED`` state, which indicates that the fulfillment has been given to the
    shipping carrier. The timestamp must be in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z")."""

    canceled_at: OptionalNullable[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ indicating the shipment
    was canceled. The timestamp must be in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z")."""

    cancel_reason: OptionalNullable[str] = UNSET
    """A description of why the shipment was canceled."""

    failed_at: Optional[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ indicating when the
    shipment failed to be completed. The timestamp must be in RFC 3339 format (for example,
    "2016-09-04T23:59:33.123Z")."""

    failure_reason: OptionalNullable[str] = UNSET
    """A description of why the shipment failed to be completed."""


class FulfillmentShipmentDetailsDict(TypedDict):
    recipient: NotRequired[FulfillmentRecipient | FulfillmentRecipientDict]
    carrier: NotRequired[str | None]
    shipping_note: NotRequired[str | None]
    shipping_type: NotRequired[str | None]
    tracking_number: NotRequired[str | None]
    tracking_url: NotRequired[str | None]
    placed_at: NotRequired[str]
    in_progress_at: NotRequired[str]
    packaged_at: NotRequired[str]
    expected_shipped_at: NotRequired[str | None]
    shipped_at: NotRequired[str]
    canceled_at: NotRequired[str | None]
    cancel_reason: NotRequired[str | None]
    failed_at: NotRequired[str]
    failure_reason: NotRequired[str | None]

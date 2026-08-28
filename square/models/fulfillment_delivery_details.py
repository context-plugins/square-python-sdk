from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.fulfillment_delivery_details_order_fulfillment_delivery_details_schedule_type import (
    FulfillmentDeliveryDetailsOrderFulfillmentDeliveryDetailsScheduleTypeOrStr,
)
from .fulfillment_recipient import FulfillmentRecipient, FulfillmentRecipientDict


class FulfillmentDeliveryDetails(SdkBaseModel):
    """Describes delivery details of an order fulfillment."""

    recipient: Optional[FulfillmentRecipient] = UNSET
    """Information about the fulfillment recipient."""

    schedule_type: Optional[FulfillmentDeliveryDetailsOrderFulfillmentDeliveryDetailsScheduleTypeOrStr] = UNSET
    """The schedule type of the delivery fulfillment."""

    placed_at: Optional[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ indicating when the
    fulfillment was placed. The timestamp must be in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z").

    Must be in RFC 3339 timestamp format, e.g., "2016-09-04T23:59:33.123Z"."""

    deliver_at: OptionalNullable[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ that represents the start
    of the delivery period. The application can set this field while the fulfillment ``state`` is ``PROPOSED``,
    ``RESERVED``, or ``PREPARED`` (any time before the terminal state such as ``COMPLETED``, ``CANCELED``, and
    ``FAILED``).

    The timestamp must be in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z").

    For fulfillments with the schedule type ``ASAP``, this is automatically set to the current time plus
    ``prep_time_duration``, if available."""

    prep_time_duration: OptionalNullable[str] = UNSET
    """The `duration <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ needed to prepare and
    deliver this fulfillment. The duration must be in RFC 3339 format (for example, "PT30M" for 30 minutes). Don't
    confuse "M" for months with "M" for minutes. "P5M" means 5 months, while "PT5M" means 5 minutes."""

    delivery_window_duration: OptionalNullable[str] = UNSET
    """The `duration <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ after ``deliver_at`` in
    which to deliver the order. Applications can set this field when the fulfillment ``state`` is ``PROPOSED``,
    ``RESERVED``, or ``PREPARED`` (any time before the terminal state such as ``COMPLETED``, ``CANCELED``, and
    ``FAILED``).

    The duration must be in RFC 3339 format (for example, "PT30M" for 30 minutes). Don't confuse "M" for months with "M"
    for minutes. "P5M" means 5 months, while "PT5M" means 5 minutes."""

    note: OptionalNullable[str] = UNSET
    """Provides additional instructions about the delivery fulfillment. It is displayed in the Square Point of Sale
    application and set by the API."""

    completed_at: OptionalNullable[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ indicates when the seller
    completed the fulfillment. This field is automatically set when fulfillment ``state`` changes to ``COMPLETED``. The
    timestamp must be in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z")."""

    in_progress_at: Optional[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ indicates when the seller
    started processing the fulfillment. This field is automatically set when the fulfillment ``state`` changes to
    ``RESERVED``. The timestamp must be in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z")."""

    rejected_at: Optional[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ indicating when the
    fulfillment was rejected. This field is automatically set when the fulfillment ``state`` changes to ``FAILED``. The
    timestamp must be in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z")."""

    ready_at: Optional[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ indicating when the
    seller marked the fulfillment as ready for courier pickup. This field is automatically set when the fulfillment
    ``state`` changes to PREPARED. The timestamp must be in RFC 3339 format (for example,
    "2016-09-04T23:59:33.123Z")."""

    delivered_at: Optional[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ indicating when the
    fulfillment was delivered to the recipient. The timestamp must be in RFC 3339 format (for example,
    "2016-09-04T23:59:33.123Z")."""

    canceled_at: Optional[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ indicating when the
    fulfillment was canceled. This field is automatically set when the fulfillment ``state`` changes to ``CANCELED``.

    The timestamp must be in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z")."""

    cancel_reason: OptionalNullable[str] = UNSET
    """The delivery cancellation reason. Max length: 100 characters."""

    courier_pickup_at: OptionalNullable[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ indicating when an order
    can be picked up by the courier for delivery. The timestamp must be in RFC 3339 format (for example,
    "2016-09-04T23:59:33.123Z")."""

    courier_pickup_window_duration: OptionalNullable[str] = UNSET
    """The `duration <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ after
    ``courier_pickup_at`` in which the courier should pick up the order. The duration must be in RFC 3339 format (for
    example, "PT30M" for 30 minutes). Don't confuse "M" for months with "M" for minutes. "P5M" means 5 months, while
    "PT5M" means 5 minutes."""

    is_no_contact_delivery: OptionalNullable[bool] = UNSET
    """Whether the delivery is preferred to be no contact."""

    dropoff_notes: OptionalNullable[str] = UNSET
    """A note to provide additional instructions about how to deliver the order."""

    courier_provider_name: OptionalNullable[str] = UNSET
    """The name of the courier provider."""

    courier_support_phone_number: OptionalNullable[str] = UNSET
    """The support phone number of the courier."""

    square_delivery_id: OptionalNullable[str] = UNSET
    """The identifier for the delivery created by Square."""

    external_delivery_id: OptionalNullable[str] = UNSET
    """The identifier for the delivery created by the third-party courier service."""

    managed_delivery: OptionalNullable[bool] = UNSET
    """The flag to indicate the delivery is managed by a third party (ie DoorDash), which means we may not receive all
    recipient information for PII purposes."""


class FulfillmentDeliveryDetailsDict(TypedDict):
    recipient: NotRequired[FulfillmentRecipient | FulfillmentRecipientDict]
    schedule_type: NotRequired[FulfillmentDeliveryDetailsOrderFulfillmentDeliveryDetailsScheduleTypeOrStr]
    placed_at: NotRequired[str]
    deliver_at: NotRequired[str | None]
    prep_time_duration: NotRequired[str | None]
    delivery_window_duration: NotRequired[str | None]
    note: NotRequired[str | None]
    completed_at: NotRequired[str | None]
    in_progress_at: NotRequired[str]
    rejected_at: NotRequired[str]
    ready_at: NotRequired[str]
    delivered_at: NotRequired[str]
    canceled_at: NotRequired[str]
    cancel_reason: NotRequired[str | None]
    courier_pickup_at: NotRequired[str | None]
    courier_pickup_window_duration: NotRequired[str | None]
    is_no_contact_delivery: NotRequired[bool | None]
    dropoff_notes: NotRequired[str | None]
    courier_provider_name: NotRequired[str | None]
    courier_support_phone_number: NotRequired[str | None]
    square_delivery_id: NotRequired[str | None]
    external_delivery_id: NotRequired[str | None]
    managed_delivery: NotRequired[bool | None]

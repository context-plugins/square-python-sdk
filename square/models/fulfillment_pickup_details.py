from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.fulfillment_pickup_details_schedule_type import FulfillmentPickupDetailsScheduleTypeOrStr
from .fulfillment_pickup_details_curbside_pickup_details import (
    FulfillmentPickupDetailsCurbsidePickupDetails,
    FulfillmentPickupDetailsCurbsidePickupDetailsDict,
)
from .fulfillment_recipient import FulfillmentRecipient, FulfillmentRecipientDict


class FulfillmentPickupDetails(SdkBaseModel):
    """Contains details necessary to fulfill a pickup order."""

    recipient: Optional[FulfillmentRecipient] = UNSET
    """Information about the fulfillment recipient."""

    expires_at: OptionalNullable[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ indicating when this
    fulfillment expires if it is not marked in progress. The timestamp must be in RFC 3339 format (for example,
    "2016-09-04T23:59:33.123Z"). The expiration time can only be set up to 7 days in the future. If ``expires_at`` is
    not set, any new payments attached to the order are automatically completed."""

    auto_complete_duration: OptionalNullable[str] = UNSET
    """The `duration <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ after which an in-progress
    pickup fulfillment is automatically moved to the ``COMPLETED`` state. The duration must be in RFC 3339 format (for
    example, "PT4H" for 4 hours).

    If not set, this pickup fulfillment remains in progress until it is canceled or completed."""

    schedule_type: Optional[FulfillmentPickupDetailsScheduleTypeOrStr] = UNSET
    """The schedule type of the pickup fulfillment."""

    pickup_at: OptionalNullable[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ that represents the start
    of the pickup window. Must be in RFC 3339 timestamp format, e.g., "2016-09-04T23:59:33.123Z".

    For fulfillments with the schedule type ``ASAP``, this is automatically set to the current time plus
    ``prep_time_duration``, if available."""

    pickup_window_duration: OptionalNullable[str] = UNSET
    """The `duration <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ in which the order should
    be picked up after the ``pickup_at`` timestamp. The duration must be in RFC 3339 format (for example, "PT30M" for 30
    minutes). Don't confuse "M" for months with "M" for minutes. "P5M" means 5 months, while "PT5M" means 5 minutes.

    Can be used as an informational guideline for merchants."""

    prep_time_duration: OptionalNullable[str] = UNSET
    """The `duration <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ needed to prepare this
    fulfillment. The duration must be in RFC 3339 format (for example, "PT30M" for 30 minutes). Don't confuse "M" for
    months with "M" for minutes. "P5M" means 5 months, while "PT5M" means 5 minutes."""

    note: OptionalNullable[str] = UNSET
    """A note to provide additional instructions about the pickup fulfillment displayed in the Square Point of Sale
    application and set by the API."""

    placed_at: Optional[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ indicating when the
    fulfillment was placed. The timestamp must be in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z")."""

    accepted_at: Optional[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ indicating when the
    fulfillment was marked in progress. The timestamp must be in RFC 3339 format (for example,
    "2016-09-04T23:59:33.123Z")."""

    rejected_at: Optional[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ indicating when the
    fulfillment was rejected. The timestamp must be in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z")."""

    ready_at: Optional[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ indicating when the
    fulfillment is marked as ready for pickup. The timestamp must be in RFC 3339 format (for example,
    "2016-09-04T23:59:33.123Z")."""

    expired_at: Optional[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ indicating when the
    fulfillment expired. The timestamp must be in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z")."""

    picked_up_at: Optional[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ indicating when the
    fulfillment was picked up by the recipient. The timestamp must be in RFC 3339 format (for example,
    "2016-09-04T23:59:33.123Z")."""

    canceled_at: Optional[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ indicating when the
    fulfillment was canceled. The timestamp must be in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z")."""

    cancel_reason: OptionalNullable[str] = UNSET
    """A description of why the pickup was canceled. The maximum length: 100 characters."""

    is_curbside_pickup: OptionalNullable[bool] = UNSET
    """If set to ``true``, indicates that this pickup order is for curbside pickup, not in-store pickup."""

    curbside_pickup_details: Optional[FulfillmentPickupDetailsCurbsidePickupDetails] = UNSET
    """Specific details for curbside pickup."""


class FulfillmentPickupDetailsDict(TypedDict):
    recipient: NotRequired[FulfillmentRecipientDict]
    expires_at: NotRequired[str | None]
    auto_complete_duration: NotRequired[str | None]
    schedule_type: NotRequired[FulfillmentPickupDetailsScheduleTypeOrStr]
    pickup_at: NotRequired[str | None]
    pickup_window_duration: NotRequired[str | None]
    prep_time_duration: NotRequired[str | None]
    note: NotRequired[str | None]
    placed_at: NotRequired[str]
    accepted_at: NotRequired[str]
    rejected_at: NotRequired[str]
    ready_at: NotRequired[str]
    expired_at: NotRequired[str]
    picked_up_at: NotRequired[str]
    canceled_at: NotRequired[str]
    cancel_reason: NotRequired[str | None]
    is_curbside_pickup: NotRequired[bool | None]
    curbside_pickup_details: NotRequired[FulfillmentPickupDetailsCurbsidePickupDetailsDict]

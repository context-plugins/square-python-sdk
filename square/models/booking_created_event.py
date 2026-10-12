from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .booking_created_event_data import BookingCreatedEventData, BookingCreatedEventDataDict


class BookingCreatedEvent(SdkBaseModel):
    """Published when a booking is created.

    To receive this event with buyer-level permissions, you must have ``APPOINTMENTS_READ`` set for the OAuth scope. To
    receive this event with seller-level permissions, you must have ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ``
    set for the OAuth scope."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the target seller associated with the event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of this event. The value is ``"booking.created"``."""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for the event."""

    created_at: Optional[str] = UNSET
    """The timestamp of when the event was created, in RFC 3339 format."""

    data: Optional[BookingCreatedEventData] = UNSET


class BookingCreatedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[BookingCreatedEventDataDict]

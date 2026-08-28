from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BookingCustomAttributeDeleteRequest(SdkBaseModel):
    """Represents an individual delete request in a `BulkDeleteBookingCustomAttributes
    <api-endpoint:BookingCustomAttributes-BulkDeleteBookingCustomAttributes>`__ request. An individual request contains
    a booking ID, the custom attribute to delete, and an optional idempotency key."""

    booking_id: str
    """The ID of the target `booking <entity:Booking>`__."""

    key: str
    """The key of the custom attribute to delete. This key must match the ``key`` of a custom attribute definition in
    the Square seller account. If the requesting application is not the definition owner, you must use the qualified
    key."""


class BookingCustomAttributeDeleteRequestDict(TypedDict):
    booking_id: str
    key: str

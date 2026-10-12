from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class BookingCustomAttributeDeleteResponse(SdkBaseModel):
    """Represents a response for an individual upsert request in a `BulkDeleteBookingCustomAttributes
    <api-endpoint:BookingCustomAttributes-BulkDeleteBookingCustomAttributes>`__ operation."""

    booking_id: Optional[str] = UNSET
    """The ID of the `booking <entity:Booking>`__ associated with the custom attribute."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred while processing the individual request."""


class BookingCustomAttributeDeleteResponseDict(TypedDict):
    booking_id: NotRequired[str]
    errors: NotRequired[list[ErrorDict]]

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .retrieve_booking_response import RetrieveBookingResponse, RetrieveBookingResponseDict


class BulkRetrieveBookingsResponse(SdkBaseModel):
    """Response payload for bulk retrieval of bookings."""

    bookings: Optional[dict[str, RetrieveBookingResponse]] = UNSET
    """Requested bookings returned as a map containing ``booking_id`` as the key and ``RetrieveBookingResponse`` as the
    value."""

    errors: Optional[list[Error]] = UNSET
    """Errors that occurred during the request."""


class BulkRetrieveBookingsResponseDict(TypedDict):
    bookings: NotRequired[dict[str, RetrieveBookingResponse | RetrieveBookingResponseDict]]
    errors: NotRequired[list[Error | ErrorDict]]

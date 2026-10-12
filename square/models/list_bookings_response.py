from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .booking import Booking, BookingDict
from .error import Error, ErrorDict


class ListBookingsResponse(SdkBaseModel):
    bookings: Optional[list[Booking]] = UNSET
    """The list of targeted bookings."""

    cursor: Optional[str] = UNSET
    """The pagination cursor to be used in the subsequent request to get the next page of the results. Stop retrieving
    the next page of the results when the cursor is not set."""

    errors: Optional[list[Error]] = UNSET
    """Errors that occurred during the request."""


class ListBookingsResponseDict(TypedDict):
    bookings: NotRequired[list[BookingDict]]
    cursor: NotRequired[str]
    errors: NotRequired[list[ErrorDict]]

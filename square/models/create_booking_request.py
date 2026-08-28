from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .booking import Booking, BookingDict


class CreateBookingRequest(SdkBaseModel):
    idempotency_key: Optional[str] = UNSET
    """A unique key to make this request an idempotent operation."""

    booking: Booking
    """Represents a booking as a time-bound service contract for a seller's staff member to provide a specified service
    at a given location to a requesting customer in one or more appointment segments."""


class CreateBookingRequestDict(TypedDict):
    idempotency_key: NotRequired[str]
    booking: Booking | BookingDict

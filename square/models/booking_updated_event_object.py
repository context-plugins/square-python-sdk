from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .booking import Booking, BookingDict


class BookingUpdatedEventObject(SdkBaseModel):
    booking: Optional[Booking] = UNSET
    """Represents a booking as a time-bound service contract for a seller's staff member to provide a specified service
    at a given location to a requesting customer in one or more appointment segments."""


class BookingUpdatedEventObjectDict(TypedDict):
    booking: NotRequired[Booking | BookingDict]

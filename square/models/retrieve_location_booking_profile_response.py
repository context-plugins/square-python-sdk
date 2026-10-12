from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .location_booking_profile import LocationBookingProfile, LocationBookingProfileDict


class RetrieveLocationBookingProfileResponse(SdkBaseModel):
    location_booking_profile: Optional[LocationBookingProfile] = UNSET
    """The booking profile of a seller's location, including the location's ID and whether the location is enabled for
    online booking."""

    errors: Optional[list[Error]] = UNSET
    """Errors that occurred during the request."""


class RetrieveLocationBookingProfileResponseDict(TypedDict):
    location_booking_profile: NotRequired[LocationBookingProfileDict]
    errors: NotRequired[list[ErrorDict]]

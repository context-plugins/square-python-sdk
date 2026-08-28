from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .location_booking_profile import LocationBookingProfile, LocationBookingProfileDict


class ListLocationBookingProfilesResponse(SdkBaseModel):
    location_booking_profiles: Optional[list[LocationBookingProfile]] = UNSET
    """The list of a seller's location booking profiles."""

    cursor: Optional[str] = UNSET
    """The pagination cursor to be used in the subsequent request to get the next page of the results. Stop retrieving
    the next page of the results when the cursor is not set."""

    errors: Optional[list[Error]] = UNSET
    """Errors that occurred during the request."""


class ListLocationBookingProfilesResponseDict(TypedDict):
    location_booking_profiles: NotRequired[list[LocationBookingProfile | LocationBookingProfileDict]]
    cursor: NotRequired[str]
    errors: NotRequired[list[Error | ErrorDict]]

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .business_booking_profile import BusinessBookingProfile, BusinessBookingProfileDict
from .error import Error, ErrorDict


class RetrieveBusinessBookingProfileResponse(SdkBaseModel):
    business_booking_profile: Optional[BusinessBookingProfile] = UNSET
    """A seller's business booking profile, including booking policy, appointment settings, etc."""

    errors: Optional[list[Error]] = UNSET
    """Errors that occurred during the request."""


class RetrieveBusinessBookingProfileResponseDict(TypedDict):
    business_booking_profile: NotRequired[BusinessBookingProfile | BusinessBookingProfileDict]
    errors: NotRequired[list[Error | ErrorDict]]

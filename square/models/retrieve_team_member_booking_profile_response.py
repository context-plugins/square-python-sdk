from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .team_member_booking_profile import TeamMemberBookingProfile, TeamMemberBookingProfileDict


class RetrieveTeamMemberBookingProfileResponse(SdkBaseModel):
    team_member_booking_profile: Optional[TeamMemberBookingProfile] = UNSET
    """The booking profile of a seller's team member, including the team member's ID, display name, description and
    whether the team member can be booked as a service provider."""

    errors: Optional[list[Error]] = UNSET
    """Errors that occurred during the request."""


class RetrieveTeamMemberBookingProfileResponseDict(TypedDict):
    team_member_booking_profile: NotRequired[TeamMemberBookingProfileDict]
    errors: NotRequired[list[ErrorDict]]

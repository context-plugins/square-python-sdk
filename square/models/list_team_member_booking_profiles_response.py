from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .team_member_booking_profile import TeamMemberBookingProfile, TeamMemberBookingProfileDict


class ListTeamMemberBookingProfilesResponse(SdkBaseModel):
    team_member_booking_profiles: Optional[list[TeamMemberBookingProfile]] = UNSET
    """The list of team member booking profiles. The results are returned in the ascending order of the time when the
    team member booking profiles were last updated. Multiple booking profiles updated at the same time are further
    sorted in the ascending order of their IDs."""

    cursor: Optional[str] = UNSET
    """The pagination cursor to be used in the subsequent request to get the next page of the results. Stop retrieving
    the next page of the results when the cursor is not set."""

    errors: Optional[list[Error]] = UNSET
    """Errors that occurred during the request."""


class ListTeamMemberBookingProfilesResponseDict(TypedDict):
    team_member_booking_profiles: NotRequired[list[TeamMemberBookingProfile | TeamMemberBookingProfileDict]]
    cursor: NotRequired[str]
    errors: NotRequired[list[Error | ErrorDict]]

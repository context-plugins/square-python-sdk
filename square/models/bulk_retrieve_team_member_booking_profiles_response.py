from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .retrieve_team_member_booking_profile_response import (
    RetrieveTeamMemberBookingProfileResponse,
    RetrieveTeamMemberBookingProfileResponseDict,
)


class BulkRetrieveTeamMemberBookingProfilesResponse(SdkBaseModel):
    """Response payload for the `BulkRetrieveTeamMemberBookingProfiles
    <api-endpoint:Bookings-BulkRetrieveTeamMemberBookingProfiles>`__ endpoint."""

    team_member_booking_profiles: Optional[dict[str, RetrieveTeamMemberBookingProfileResponse]] = UNSET
    """The returned team members' booking profiles, as a map with ``team_member_id`` as the key and
    `TeamMemberBookingProfile <entity:TeamMemberBookingProfile>`__ the value."""

    errors: Optional[list[Error]] = UNSET
    """Errors that occurred during the request."""


class BulkRetrieveTeamMemberBookingProfilesResponseDict(TypedDict):
    team_member_booking_profiles: NotRequired[dict[str, RetrieveTeamMemberBookingProfileResponseDict]]
    errors: NotRequired[list[ErrorDict]]

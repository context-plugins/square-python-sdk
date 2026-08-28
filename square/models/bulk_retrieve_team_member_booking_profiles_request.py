from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BulkRetrieveTeamMemberBookingProfilesRequest(SdkBaseModel):
    """Request payload for the `BulkRetrieveTeamMemberBookingProfiles
    <api-endpoint:Bookings-BulkRetrieveTeamMemberBookingProfiles>`__ endpoint."""

    team_member_ids: list[str]
    """A non-empty list of IDs of team members whose booking profiles you want to retrieve."""


class BulkRetrieveTeamMemberBookingProfilesRequestDict(TypedDict):
    team_member_ids: list[str]

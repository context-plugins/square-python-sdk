from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.team_member_assigned_locations_assignment_type import TeamMemberAssignedLocationsAssignmentTypeOrStr


class TeamMemberAssignedLocations(SdkBaseModel):
    """An object that represents a team member's assignment to locations."""

    assignment_type: Optional[TeamMemberAssignedLocationsAssignmentTypeOrStr] = UNSET
    """Enumerates the possible assignment types that the team member can have."""

    location_ids: Optional[list[str | None]] = UNSET
    """The explicit locations that the team member is assigned to."""


class TeamMemberAssignedLocationsDict(TypedDict):
    assignment_type: NotRequired[TeamMemberAssignedLocationsAssignmentTypeOrStr]
    location_ids: NotRequired[list[str | None]]

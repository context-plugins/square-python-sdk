from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .team_member import TeamMember, TeamMemberDict


class CreateTeamMemberResponse(SdkBaseModel):
    """Represents a response from a create request containing the created ``TeamMember`` object or error messages."""

    team_member: Optional[TeamMember] = UNSET
    """A record representing an individual team member for a business."""

    errors: Optional[list[Error]] = UNSET
    """The errors that occurred during the request."""


class CreateTeamMemberResponseDict(TypedDict):
    team_member: NotRequired[TeamMemberDict]
    errors: NotRequired[list[ErrorDict]]

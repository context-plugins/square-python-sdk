from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .team_member import TeamMember, TeamMemberDict


class RetrieveTeamMemberResponse(SdkBaseModel):
    """Represents a response from a retrieve request containing a ``TeamMember`` object or error messages."""

    team_member: Optional[TeamMember] = UNSET
    """A record representing an individual team member for a business."""

    errors: Optional[list[Error]] = UNSET
    """The errors that occurred during the request."""


class RetrieveTeamMemberResponseDict(TypedDict):
    team_member: NotRequired[TeamMember | TeamMemberDict]
    errors: NotRequired[list[Error | ErrorDict]]

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .team_member import TeamMember, TeamMemberDict


class UpdateTeamMemberRequest(SdkBaseModel):
    """Represents an update request for a ``TeamMember`` object."""

    team_member: Optional[TeamMember] = UNSET
    """A record representing an individual team member for a business."""


class UpdateTeamMemberRequestDict(TypedDict):
    team_member: NotRequired[TeamMemberDict]

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .team_member import TeamMember, TeamMemberDict


class TeamMemberCreatedEventObject(SdkBaseModel):
    team_member: Optional[TeamMember] = UNSET
    """A record representing an individual team member for a business."""


class TeamMemberCreatedEventObjectDict(TypedDict):
    team_member: NotRequired[TeamMember | TeamMemberDict]

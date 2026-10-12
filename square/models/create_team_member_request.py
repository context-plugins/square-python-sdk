from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .team_member import TeamMember, TeamMemberDict


class CreateTeamMemberRequest(SdkBaseModel):
    """Represents a create request for a ``TeamMember`` object."""

    idempotency_key: Optional[str] = UNSET
    """A unique string that identifies this ``CreateTeamMember`` request. Keys can be any valid string, but must be
    unique for every request. For more information, see `Idempotency
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__.

    The minimum length is 1 and the maximum length is 45."""

    team_member: Optional[TeamMember] = UNSET
    """A record representing an individual team member for a business."""


class CreateTeamMemberRequestDict(TypedDict):
    idempotency_key: NotRequired[str]
    team_member: NotRequired[TeamMemberDict]

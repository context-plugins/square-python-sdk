from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .create_team_member_response import CreateTeamMemberResponse, CreateTeamMemberResponseDict
from .error import Error, ErrorDict


class BulkCreateTeamMembersResponse(SdkBaseModel):
    """Represents a response from a bulk create request containing the created ``TeamMember`` objects or error
    messages."""

    team_members: Optional[dict[str, CreateTeamMemberResponse]] = UNSET
    """The successfully created ``TeamMember`` objects. Each key is the ``idempotency_key`` that maps to the
    ``CreateTeamMemberRequest``."""

    errors: Optional[list[Error]] = UNSET
    """The errors that occurred during the request."""


class BulkCreateTeamMembersResponseDict(TypedDict):
    team_members: NotRequired[dict[str, CreateTeamMemberResponseDict]]
    errors: NotRequired[list[ErrorDict]]

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .update_team_member_response import UpdateTeamMemberResponse, UpdateTeamMemberResponseDict


class BulkUpdateTeamMembersResponse(SdkBaseModel):
    """Represents a response from a bulk update request containing the updated ``TeamMember`` objects or error
    messages."""

    team_members: Optional[dict[str, UpdateTeamMemberResponse]] = UNSET
    """The successfully updated ``TeamMember`` objects. Each key is the ``team_member_id`` that maps to the
    ``UpdateTeamMemberRequest``."""

    errors: Optional[list[Error]] = UNSET
    """The errors that occurred during the request."""


class BulkUpdateTeamMembersResponseDict(TypedDict):
    team_members: NotRequired[dict[str, UpdateTeamMemberResponse | UpdateTeamMemberResponseDict]]
    errors: NotRequired[list[Error | ErrorDict]]

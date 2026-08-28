from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .team_member import TeamMember, TeamMemberDict


class SearchTeamMembersResponse(SdkBaseModel):
    """Represents a response from a search request containing a filtered list of ``TeamMember`` objects."""

    team_members: Optional[list[TeamMember]] = UNSET
    """The filtered list of ``TeamMember`` objects."""

    cursor: Optional[str] = UNSET
    """The opaque cursor for fetching the next page. For more information, see `pagination
    <https://developer.squareup.com/docs/working-with-apis/pagination>`__."""

    errors: Optional[list[Error]] = UNSET
    """The errors that occurred during the request."""


class SearchTeamMembersResponseDict(TypedDict):
    team_members: NotRequired[list[TeamMember | TeamMemberDict]]
    cursor: NotRequired[str]
    errors: NotRequired[list[Error | ErrorDict]]

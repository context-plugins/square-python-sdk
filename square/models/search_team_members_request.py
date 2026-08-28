from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .search_team_members_query import SearchTeamMembersQuery, SearchTeamMembersQueryDict


class SearchTeamMembersRequest(SdkBaseModel):
    """Represents a search request for a filtered list of ``TeamMember`` objects."""

    query: Optional[SearchTeamMembersQuery] = UNSET
    """Represents the parameters in a search for ``TeamMember`` objects."""

    limit: Optional[int] = UNSET
    """The maximum number of ``TeamMember`` objects in a page (100 by default)."""

    cursor: Optional[str] = UNSET
    """The opaque cursor for fetching the next page. For more information, see `pagination
    <https://developer.squareup.com/docs/working-with-apis/pagination>`__."""


class SearchTeamMembersRequestDict(TypedDict):
    query: NotRequired[SearchTeamMembersQuery | SearchTeamMembersQueryDict]
    limit: NotRequired[int]
    cursor: NotRequired[str]

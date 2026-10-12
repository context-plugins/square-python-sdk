from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .search_team_members_filter import SearchTeamMembersFilter, SearchTeamMembersFilterDict


class SearchTeamMembersQuery(SdkBaseModel):
    """Represents the parameters in a search for ``TeamMember`` objects."""

    filter: Optional[SearchTeamMembersFilter] = UNSET
    """Represents a filter used in a search for ``TeamMember`` objects. ``AND`` logic is applied between the individual
    fields, and ``OR`` logic is applied within list-based fields. For example, setting this filter value:
    ```
    filter = (locations_ids = ["A", "B"], status = ACTIVE)
    ```
    returns only active team members assigned to either location "A" or "B"."""


class SearchTeamMembersQueryDict(TypedDict):
    filter: NotRequired[SearchTeamMembersFilterDict]

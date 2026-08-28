from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.team_member_status import TeamMemberStatusOrStr


class SearchTeamMembersFilter(SdkBaseModel):
    """Represents a filter used in a search for ``TeamMember`` objects. ``AND`` logic is applied between the individual
    fields, and ``OR`` logic is applied within list-based fields. For example, setting this filter value:
    ```
    filter = (locations_ids = ["A", "B"], status = ACTIVE)
    ```
    returns only active team members assigned to either location "A" or "B"."""

    location_ids: Optional[list[str | None]] = UNSET
    """When present, filters by team members assigned to the specified locations. When empty, includes team members
    assigned to any location."""

    status: Optional[TeamMemberStatusOrStr] = UNSET
    """Enumerates the possible statuses the team member can have within a business."""

    is_owner: OptionalNullable[bool] = UNSET
    """When present and set to true, returns the team member who is the owner of the Square account."""


class SearchTeamMembersFilterDict(TypedDict):
    location_ids: NotRequired[list[str | None]]
    status: NotRequired[TeamMemberStatusOrStr]
    is_owner: NotRequired[bool | None]

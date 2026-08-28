from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .team_member_wage import TeamMemberWage, TeamMemberWageDict


class GetTeamMemberWageResponse(SdkBaseModel):
    """A response to a request to get a ``TeamMemberWage``. The response contains the requested ``TeamMemberWage``
    objects and might contain a set of ``Error`` objects if the request resulted in errors."""

    team_member_wage: Optional[TeamMemberWage] = UNSET
    """Job and wage information for a `team member <entity:TeamMember>`__. This convenience object provides details
    needed to specify the ``wage`` field for a `timecard <entity:Timecard>`__."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class GetTeamMemberWageResponseDict(TypedDict):
    team_member_wage: NotRequired[TeamMemberWage | TeamMemberWageDict]
    errors: NotRequired[list[Error | ErrorDict]]

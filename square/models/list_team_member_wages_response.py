from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .team_member_wage import TeamMemberWage, TeamMemberWageDict


class ListTeamMemberWagesResponse(SdkBaseModel):
    """The response to a request for a set of ``TeamMemberWage`` objects. The response contains a set of
    ``TeamMemberWage`` objects."""

    team_member_wages: Optional[list[TeamMemberWage]] = UNSET
    """A page of ``TeamMemberWage`` results."""

    cursor: Optional[str] = UNSET
    """The value supplied in the subsequent request to fetch the next page of ``TeamMemberWage`` results."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class ListTeamMemberWagesResponseDict(TypedDict):
    team_member_wages: NotRequired[list[TeamMemberWageDict]]
    cursor: NotRequired[str]
    errors: NotRequired[list[ErrorDict]]

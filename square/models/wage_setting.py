from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .job_assignment import JobAssignment, JobAssignmentDict


class WageSetting(SdkBaseModel):
    """Represents information about the overtime exemption status, job assignments, and compensation for a `team member
    <entity:TeamMember>`__."""

    team_member_id: OptionalNullable[str] = UNSET
    """The ID of the team member associated with the wage setting."""

    job_assignments: OptionalNullable[list[JobAssignment]] = UNSET
    """**Required** The ordered list of jobs that the team member is assigned to. The first job assignment is considered
    the team member's primary job."""

    is_overtime_exempt: OptionalNullable[bool] = UNSET
    """Whether the team member is exempt from the overtime rules of the seller's country."""

    version: Optional[int] = UNSET
    """**Read only** Used for resolving concurrency issues. The request fails if the version provided does not match the
    server version at the time of the request. If not provided, Square executes a blind write, potentially overwriting
    data from another write. For more information, see `optimistic concurrency
    <https://developer.squareup.com/docs/working-with-apis/optimistic-concurrency>`__."""

    created_at: Optional[str] = UNSET
    """The timestamp when the wage setting was created, in RFC 3339 format."""

    updated_at: Optional[str] = UNSET
    """The timestamp when the wage setting was last updated, in RFC 3339 format."""


class WageSettingDict(TypedDict):
    team_member_id: NotRequired[str | None]
    job_assignments: NotRequired[list[JobAssignmentDict] | None]
    is_overtime_exempt: NotRequired[bool | None]
    version: NotRequired[int]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]

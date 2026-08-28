from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Job(SdkBaseModel):
    """Represents a job that can be assigned to `team members <entity:TeamMember>`__. This object defines the job's
    title and tip eligibility. Compensation is defined in a `job assignment <entity:JobAssignment>`__ in a team member's
    wage setting."""

    id: Optional[str] = UNSET
    """**Read only** The unique Square-assigned ID of the job. If you need a job ID for an API request, call `ListJobs
    <api-endpoint:Team-ListJobs>`__ or use the ID returned when you created the job. You can also get job IDs from a
    team member's wage setting."""

    title: OptionalNullable[str] = UNSET
    """The title of the job."""

    is_tip_eligible: OptionalNullable[bool] = UNSET
    """Indicates whether team members can earn tips for the job."""

    created_at: Optional[str] = UNSET
    """The timestamp when the job was created, in RFC 3339 format."""

    updated_at: Optional[str] = UNSET
    """The timestamp when the job was last updated, in RFC 3339 format."""

    version: Optional[int] = UNSET
    """**Read only** The current version of the job. Include this field in ``UpdateJob`` requests to enable `optimistic
    concurrency <https://developer.squareup.com/docs/working-with-apis/optimistic-concurrency>`__ control and avoid
    overwrites from concurrent requests. Requests fail if the provided version doesn't match the server version at the
    time of the request."""


class JobDict(TypedDict):
    id: NotRequired[str]
    title: NotRequired[str | None]
    is_tip_eligible: NotRequired[bool | None]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    version: NotRequired[int]

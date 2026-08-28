from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .job import Job, JobDict


class RetrieveJobResponse(SdkBaseModel):
    """Represents a `RetrieveJob <api-endpoint:Team-RetrieveJob>`__ response. Either ``job`` or ``errors`` is present in
    the response."""

    job: Optional[Job] = UNSET
    """Represents a job that can be assigned to `team members <entity:TeamMember>`__. This object defines the job's
    title and tip eligibility. Compensation is defined in a `job assignment <entity:JobAssignment>`__ in a team member's
    wage setting."""

    errors: Optional[list[Error]] = UNSET
    """The errors that occurred during the request."""


class RetrieveJobResponseDict(TypedDict):
    job: NotRequired[Job | JobDict]
    errors: NotRequired[list[Error | ErrorDict]]

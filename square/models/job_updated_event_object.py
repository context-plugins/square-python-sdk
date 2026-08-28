from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .job import Job, JobDict


class JobUpdatedEventObject(SdkBaseModel):
    job: Optional[Job] = UNSET
    """Represents a job that can be assigned to `team members <entity:TeamMember>`__. This object defines the job's
    title and tip eligibility. Compensation is defined in a `job assignment <entity:JobAssignment>`__ in a team member's
    wage setting."""


class JobUpdatedEventObjectDict(TypedDict):
    job: NotRequired[Job | JobDict]

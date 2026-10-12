from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .job import Job, JobDict


class UpdateJobRequest(SdkBaseModel):
    """Represents an `UpdateJob <api-endpoint:Team-UpdateJob>`__ request."""

    job: Job
    """Represents a job that can be assigned to `team members <entity:TeamMember>`__. This object defines the job's
    title and tip eligibility. Compensation is defined in a `job assignment <entity:JobAssignment>`__ in a team member's
    wage setting."""


class UpdateJobRequestDict(TypedDict):
    job: JobDict

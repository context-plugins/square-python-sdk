from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .job import Job, JobDict


class CreateJobRequest(SdkBaseModel):
    """Represents a `CreateJob <api-endpoint:Team-CreateJob>`__ request."""

    job: Job
    """Represents a job that can be assigned to `team members <entity:TeamMember>`__. This object defines the job's
    title and tip eligibility. Compensation is defined in a `job assignment <entity:JobAssignment>`__ in a team member's
    wage setting."""

    idempotency_key: str
    """A unique identifier for the ``CreateJob`` request. Keys can be any valid string, but must be unique for each
    request. For more information, see `Idempotency
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__."""


class CreateJobRequestDict(TypedDict):
    job: Job | JobDict
    idempotency_key: str

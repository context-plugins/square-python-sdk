from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .job import Job, JobDict


class ListJobsResponse(SdkBaseModel):
    """Represents a `ListJobs <api-endpoint:Team-ListJobs>`__ response. Either ``jobs`` or ``errors`` is present in the
    response. If additional results are available, the ``cursor`` field is also present."""

    jobs: Optional[list[Job]] = UNSET
    """The retrieved jobs. A single paged response contains up to 100 jobs."""

    cursor: Optional[str] = UNSET
    """An opaque cursor used to retrieve the next page of results. This field is present only if the request succeeded
    and additional results are available. For more information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""

    errors: Optional[list[Error]] = UNSET
    """The errors that occurred during the request."""


class ListJobsResponseDict(TypedDict):
    jobs: NotRequired[list[Job | JobDict]]
    cursor: NotRequired[str]
    errors: NotRequired[list[Error | ErrorDict]]

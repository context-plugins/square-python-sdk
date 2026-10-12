from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .timecard import Timecard, TimecardDict


class UpdateTimecardResponse(SdkBaseModel):
    """The response to a request to update a ``Timecard``. The response contains the updated ``Timecard`` object and
    might contain a set of ``Error`` objects if the request resulted in errors."""

    timecard: Optional[Timecard] = UNSET
    """A record of the hourly rate, start time, and end time of a single timecard (shift) for a team member. This might
    include a record of the start and end times of breaks taken during the shift."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class UpdateTimecardResponseDict(TypedDict):
    timecard: NotRequired[TimecardDict]
    errors: NotRequired[list[ErrorDict]]

from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .timecard import Timecard, TimecardDict


class UpdateTimecardRequest(SdkBaseModel):
    """A request to update a ``Timecard`` object."""

    timecard: Timecard
    """A record of the hourly rate, start time, and end time of a single timecard (shift) for a team member. This might
    include a record of the start and end times of breaks taken during the shift."""


class UpdateTimecardRequestDict(TypedDict):
    timecard: Timecard | TimecardDict

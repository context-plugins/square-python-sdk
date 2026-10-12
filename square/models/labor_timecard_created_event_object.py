from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .timecard import Timecard, TimecardDict


class LaborTimecardCreatedEventObject(SdkBaseModel):
    timecard: Optional[Timecard] = UNSET
    """A record of the hourly rate, start time, and end time of a single timecard (shift) for a team member. This might
    include a record of the start and end times of breaks taken during the shift."""


class LaborTimecardCreatedEventObjectDict(TypedDict):
    timecard: NotRequired[TimecardDict]

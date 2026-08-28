from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .scheduled_shift import ScheduledShift, ScheduledShiftDict


class UpdateScheduledShiftRequest(SdkBaseModel):
    scheduled_shift: ScheduledShift
    """Represents a specific time slot in a work schedule. This object is used to manage the lifecycle of a scheduled
    shift from the draft to published state. A scheduled shift contains the latest draft shift details and current
    published shift details."""


class UpdateScheduledShiftRequestDict(TypedDict):
    scheduled_shift: ScheduledShift | ScheduledShiftDict

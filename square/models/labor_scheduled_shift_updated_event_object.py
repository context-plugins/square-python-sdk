from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .scheduled_shift import ScheduledShift, ScheduledShiftDict


class LaborScheduledShiftUpdatedEventObject(SdkBaseModel):
    scheduled_shift: Optional[ScheduledShift] = Field(default=UNSET, alias="ScheduledShift")
    """Represents a specific time slot in a work schedule. This object is used to manage the lifecycle of a scheduled
    shift from the draft to published state. A scheduled shift contains the latest draft shift details and current
    published shift details."""


class LaborScheduledShiftUpdatedEventObjectDict(TypedDict):
    scheduled_shift: NotRequired[ScheduledShift | ScheduledShiftDict]

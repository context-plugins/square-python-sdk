from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .scheduled_shift import ScheduledShift, ScheduledShiftDict


class UpdateScheduledShiftResponse(SdkBaseModel):
    """Represents an `UpdateScheduledShift <api-endpoint:Labor-UpdateScheduledShift>`__ response. Either
    ``scheduled_shift`` or ``errors`` is present in the response."""

    scheduled_shift: Optional[ScheduledShift] = UNSET
    """Represents a specific time slot in a work schedule. This object is used to manage the lifecycle of a scheduled
    shift from the draft to published state. A scheduled shift contains the latest draft shift details and current
    published shift details."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class UpdateScheduledShiftResponseDict(TypedDict):
    scheduled_shift: NotRequired[ScheduledShift | ScheduledShiftDict]
    errors: NotRequired[list[Error | ErrorDict]]

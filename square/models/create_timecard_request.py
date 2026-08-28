from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .timecard import Timecard, TimecardDict


class CreateTimecardRequest(SdkBaseModel):
    """Represents a request to create a ``Timecard``."""

    idempotency_key: Optional[str] = UNSET
    """A unique string value to ensure the idempotency of the operation."""

    timecard: Timecard
    """A record of the hourly rate, start time, and end time of a single timecard (shift) for a team member. This might
    include a record of the start and end times of breaks taken during the shift."""


class CreateTimecardRequestDict(TypedDict):
    idempotency_key: NotRequired[str]
    timecard: Timecard | TimecardDict

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.weekday import WeekdayOrStr


class WorkweekConfig(SdkBaseModel):
    """Sets the day of the week and hour of the day that a business starts a workweek. This is used to calculate
    overtime pay."""

    id: Optional[str] = UNSET
    """The UUID for this object."""

    start_of_week: WeekdayOrStr
    """The days of the week."""

    start_of_day_local_time: str
    """The local time at which a business week starts. Represented as a string in ``HH:MM`` format (``HH:MM:SS`` is also
    accepted, but seconds are truncated)."""

    version: Optional[int] = UNSET
    """Used for resolving concurrency issues. The request fails if the version provided does not match the server
    version at the time of the request. If not provided, Square executes a blind write; potentially overwriting data
    from another write."""

    created_at: Optional[str] = UNSET
    """A read-only timestamp in RFC 3339 format; presented in UTC."""

    updated_at: Optional[str] = UNSET
    """A read-only timestamp in RFC 3339 format; presented in UTC."""


class WorkweekConfigDict(TypedDict):
    id: NotRequired[str]
    start_of_week: WeekdayOrStr
    start_of_day_local_time: str
    version: NotRequired[int]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]

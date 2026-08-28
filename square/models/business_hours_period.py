from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.day_of_week import DayOfWeekOrStr


class BusinessHoursPeriod(SdkBaseModel):
    """Represents a period of time during which a business location is open."""

    day_of_week: Optional[DayOfWeekOrStr] = UNSET
    """Indicates the specific day of the week."""

    start_local_time: OptionalNullable[str] = UNSET
    """The start time of a business hours period, specified in local time using partial-time RFC 3339 format. For
    example, ``8:30:00`` for a period starting at 8:30 in the morning. Note that the seconds value is always :00, but it
    is appended for conformance to the RFC."""

    end_local_time: OptionalNullable[str] = UNSET
    """The end time of a business hours period, specified in local time using partial-time RFC 3339 format. For example,
    ``21:00:00`` for a period ending at 9:00 in the evening. Note that the seconds value is always :00, but it is
    appended for conformance to the RFC."""


class BusinessHoursPeriodDict(TypedDict):
    day_of_week: NotRequired[DayOfWeekOrStr]
    start_local_time: NotRequired[str | None]
    end_local_time: NotRequired[str | None]

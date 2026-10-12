from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .date_range import DateRange, DateRangeDict
from .enums.timecard_workday_matcher import TimecardWorkdayMatcherOrStr


class TimecardWorkday(SdkBaseModel):
    """A ``Timecard`` search query filter parameter that sets a range of days that a ``Timecard`` must start or end in
    before passing the filter condition."""

    date_range: Optional[DateRange] = UNSET
    """A range defined by two dates. Used for filtering a query for Connect v2 objects that have date properties."""

    match_timecards_by: Optional[TimecardWorkdayMatcherOrStr] = UNSET
    """Defines the logic used to apply a workday filter."""

    default_timezone: OptionalNullable[str] = UNSET
    """Location-specific timezones convert workdays to datetime filters. Every location included in the query must have
    a timezone or this field must be provided as a fallback. Format: the IANA timezone database identifier for the
    relevant timezone."""


class TimecardWorkdayDict(TypedDict):
    date_range: NotRequired[DateRangeDict]
    match_timecards_by: NotRequired[TimecardWorkdayMatcherOrStr]
    default_timezone: NotRequired[str | None]

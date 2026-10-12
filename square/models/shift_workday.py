from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .date_range import DateRange, DateRangeDict
from .enums.shift_workday_matcher import ShiftWorkdayMatcherOrStr


class ShiftWorkday(SdkBaseModel):
    """A ``Shift`` search query filter parameter that sets a range of days that a ``Shift`` must start or end in before
    passing the filter condition.

    Deprecated at Square API version 2025-05-21. See the `migration notes
    <https://developer.squareup.com/docs/labor-api/what-it-does#migration-notes>`__."""

    date_range: Optional[DateRange] = UNSET
    """A range defined by two dates. Used for filtering a query for Connect v2 objects that have date properties."""

    match_shifts_by: Optional[ShiftWorkdayMatcherOrStr] = UNSET
    """Defines the logic used to apply a workday filter."""

    default_timezone: OptionalNullable[str] = UNSET
    """Location-specific timezones convert workdays to datetime filters. Every location included in the query must have
    a timezone or this field must be provided as a fallback. Format: the IANA timezone database identifier for the
    relevant timezone."""


class ShiftWorkdayDict(TypedDict):
    date_range: NotRequired[DateRangeDict]
    match_shifts_by: NotRequired[ShiftWorkdayMatcherOrStr]
    default_timezone: NotRequired[str | None]

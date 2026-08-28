from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.timecard_filter_status import TimecardFilterStatusOrStr
from .time_range import TimeRange, TimeRangeDict
from .timecard_workday import TimecardWorkday, TimecardWorkdayDict


class TimecardFilter(SdkBaseModel):
    """Defines a filter used in a search for ``Timecard`` records. ``AND`` logic is used by Square's servers to apply
    each filter property specified."""

    location_ids: Optional[list[str | None]] = UNSET
    """Fetch timecards for the specified location."""

    status: Optional[TimecardFilterStatusOrStr] = UNSET
    """Specifies the ``status`` of ``Timecard`` records to be returned."""

    start: Optional[TimeRange] = UNSET
    """Represents a generic time range. The start and end values are represented in RFC 3339 format. Time ranges are
    customized to be inclusive or exclusive based on the needs of a particular endpoint. Refer to the relevant
    endpoint-specific documentation to determine how time ranges are handled."""

    end: Optional[TimeRange] = UNSET
    """Represents a generic time range. The start and end values are represented in RFC 3339 format. Time ranges are
    customized to be inclusive or exclusive based on the needs of a particular endpoint. Refer to the relevant
    endpoint-specific documentation to determine how time ranges are handled."""

    workday: Optional[TimecardWorkday] = UNSET
    """A ``Timecard`` search query filter parameter that sets a range of days that a ``Timecard`` must start or end in
    before passing the filter condition."""

    team_member_ids: Optional[list[str | None]] = UNSET
    """Fetch timecards for the specified team members."""


class TimecardFilterDict(TypedDict):
    location_ids: NotRequired[list[str | None]]
    status: NotRequired[TimecardFilterStatusOrStr]
    start: NotRequired[TimeRange | TimeRangeDict]
    end: NotRequired[TimeRange | TimeRangeDict]
    workday: NotRequired[TimecardWorkday | TimecardWorkdayDict]
    team_member_ids: NotRequired[list[str | None]]

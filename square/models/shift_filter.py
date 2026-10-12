from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.shift_filter_status import ShiftFilterStatusOrStr
from .shift_workday import ShiftWorkday, ShiftWorkdayDict
from .time_range import TimeRange, TimeRangeDict


class ShiftFilter(SdkBaseModel):
    """Defines a filter used in a search for ``Shift`` records. ``AND`` logic is used by Square's servers to apply each
    filter property specified.

    Deprecated at Square API version 2025-05-21. See the `migration notes
    <https://developer.squareup.com/docs/labor-api/what-it-does#migration-notes>`__."""

    location_ids: OptionalNullable[list[str]] = UNSET
    """Fetch shifts for the specified location."""

    employee_ids: OptionalNullable[list[str]] = UNSET
    """Fetch shifts for the specified employees. DEPRECATED at version 2020-08-26. Use ``team_member_ids`` instead."""

    status: Optional[ShiftFilterStatusOrStr] = UNSET
    """Specifies the ``status`` of ``Shift`` records to be returned.

    Deprecated at Square API version 2025-05-21. See the `migration notes
    <https://developer.squareup.com/docs/labor-api/what-it-does#migration-notes>`__."""

    start: Optional[TimeRange] = UNSET
    """Represents a generic time range. The start and end values are represented in RFC 3339 format. Time ranges are
    customized to be inclusive or exclusive based on the needs of a particular endpoint. Refer to the relevant
    endpoint-specific documentation to determine how time ranges are handled."""

    end: Optional[TimeRange] = UNSET
    """Represents a generic time range. The start and end values are represented in RFC 3339 format. Time ranges are
    customized to be inclusive or exclusive based on the needs of a particular endpoint. Refer to the relevant
    endpoint-specific documentation to determine how time ranges are handled."""

    workday: Optional[ShiftWorkday] = UNSET
    """A ``Shift`` search query filter parameter that sets a range of days that a ``Shift`` must start or end in before
    passing the filter condition.

    Deprecated at Square API version 2025-05-21. See the `migration notes
    <https://developer.squareup.com/docs/labor-api/what-it-does#migration-notes>`__."""

    team_member_ids: OptionalNullable[list[str]] = UNSET
    """Fetch shifts for the specified team members. Replaced ``employee_ids`` at version "2020-08-26"."""


class ShiftFilterDict(TypedDict):
    location_ids: NotRequired[list[str] | None]
    employee_ids: NotRequired[list[str] | None]
    status: NotRequired[ShiftFilterStatusOrStr]
    start: NotRequired[TimeRangeDict]
    end: NotRequired[TimeRangeDict]
    workday: NotRequired[ShiftWorkdayDict]
    team_member_ids: NotRequired[list[str] | None]

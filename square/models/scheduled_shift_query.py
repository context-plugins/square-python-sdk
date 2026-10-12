from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .scheduled_shift_filter import ScheduledShiftFilter, ScheduledShiftFilterDict
from .scheduled_shift_sort import ScheduledShiftSort, ScheduledShiftSortDict


class ScheduledShiftQuery(SdkBaseModel):
    """Represents filter and sort criteria for the ``query`` field in a `SearchScheduledShifts
    <api-endpoint:Labor-SearchScheduledShifts>`__ request."""

    filter: Optional[ScheduledShiftFilter] = UNSET
    """Defines filter criteria for a `SearchScheduledShifts <api-endpoint:Labor-SearchScheduledShifts>`__ request.
    Multiple filters in a query are combined as an ``AND`` operation."""

    sort: Optional[ScheduledShiftSort] = UNSET
    """Defines sort criteria for a `SearchScheduledShifts <api-endpoint:Labor-SearchScheduledShifts>`__ request."""


class ScheduledShiftQueryDict(TypedDict):
    filter: NotRequired[ScheduledShiftFilterDict]
    sort: NotRequired[ScheduledShiftSortDict]

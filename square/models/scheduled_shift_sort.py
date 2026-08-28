from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.scheduled_shift_sort_field import ScheduledShiftSortFieldOrStr
from .enums.sort_order import SortOrderOrStr


class ScheduledShiftSort(SdkBaseModel):
    """Defines sort criteria for a `SearchScheduledShifts <api-endpoint:Labor-SearchScheduledShifts>`__ request."""

    field: Optional[ScheduledShiftSortFieldOrStr] = UNSET
    """Defines valid values for the ``field`` sort setting in a `SearchScheduledShifts
    <api-endpoint:Labor-SearchScheduledShifts>`__ request."""

    order: Optional[SortOrderOrStr] = UNSET
    """The order (e.g., chronological or alphabetical) in which results from a request are returned."""


class ScheduledShiftSortDict(TypedDict):
    field: NotRequired[ScheduledShiftSortFieldOrStr]
    order: NotRequired[SortOrderOrStr]

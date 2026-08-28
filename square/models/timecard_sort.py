from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.sort_order import SortOrderOrStr
from .enums.timecard_sort_field import TimecardSortFieldOrStr


class TimecardSort(SdkBaseModel):
    """Sets the sort order of search results."""

    field: Optional[TimecardSortFieldOrStr] = UNSET
    """Enumerates the ``Timecard`` fields to sort on."""

    order: Optional[SortOrderOrStr] = UNSET
    """The order (e.g., chronological or alphabetical) in which results from a request are returned."""


class TimecardSortDict(TypedDict):
    field: NotRequired[TimecardSortFieldOrStr]
    order: NotRequired[SortOrderOrStr]

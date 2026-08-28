from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .timecard_filter import TimecardFilter, TimecardFilterDict
from .timecard_sort import TimecardSort, TimecardSortDict


class TimecardQuery(SdkBaseModel):
    """The parameters of a ``Timecard`` search query, which includes filter and sort options."""

    filter: Optional[TimecardFilter] = UNSET
    """Defines a filter used in a search for ``Timecard`` records. ``AND`` logic is used by Square's servers to apply
    each filter property specified."""

    sort: Optional[TimecardSort] = UNSET
    """Sets the sort order of search results."""


class TimecardQueryDict(TypedDict):
    filter: NotRequired[TimecardFilter | TimecardFilterDict]
    sort: NotRequired[TimecardSort | TimecardSortDict]

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.search_events_sort_field import SearchEventsSortFieldOrStr
from .enums.sort_order import SortOrderOrStr


class SearchEventsSort(SdkBaseModel):
    """Criteria to sort events by."""

    field: Optional[SearchEventsSortFieldOrStr] = UNSET
    """Specifies the sort key for events returned from a search."""

    order: Optional[SortOrderOrStr] = UNSET
    """The order (e.g., chronological or alphabetical) in which results from a request are returned."""


class SearchEventsSortDict(TypedDict):
    field: NotRequired[SearchEventsSortFieldOrStr]
    order: NotRequired[SortOrderOrStr]

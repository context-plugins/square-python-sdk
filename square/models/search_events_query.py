from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .search_events_filter import SearchEventsFilter, SearchEventsFilterDict
from .search_events_sort import SearchEventsSort, SearchEventsSortDict


class SearchEventsQuery(SdkBaseModel):
    """Contains query criteria for the search."""

    filter: Optional[SearchEventsFilter] = UNSET
    """Criteria to filter events by."""

    sort: Optional[SearchEventsSort] = UNSET
    """Criteria to sort events by."""


class SearchEventsQueryDict(TypedDict):
    filter: NotRequired[SearchEventsFilter | SearchEventsFilterDict]
    sort: NotRequired[SearchEventsSort | SearchEventsSortDict]

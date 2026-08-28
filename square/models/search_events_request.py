from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .search_events_query import SearchEventsQuery, SearchEventsQueryDict


class SearchEventsRequest(SdkBaseModel):
    """Searches `Event <entity:Event>`__s for your application."""

    cursor: Optional[str] = UNSET
    """A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of
    events for your original query.

    For more information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""

    limit: Optional[int] = UNSET
    """The maximum number of events to return in a single page. The response might contain fewer events. The default
    value is 100, which is also the maximum allowed value.

    For more information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.

    Default: 100"""

    query: Optional[SearchEventsQuery] = UNSET
    """Contains query criteria for the search."""


class SearchEventsRequestDict(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]
    query: NotRequired[SearchEventsQuery | SearchEventsQueryDict]

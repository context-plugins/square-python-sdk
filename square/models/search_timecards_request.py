from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .timecard_query import TimecardQuery, TimecardQueryDict


class SearchTimecardsRequest(SdkBaseModel):
    """A request for a filtered and sorted set of ``Timecard`` objects."""

    query: Optional[TimecardQuery] = UNSET
    """The parameters of a ``Timecard`` search query, which includes filter and sort options."""

    limit: Optional[int] = UNSET
    """The number of resources in a page (200 by default)."""

    cursor: Optional[str] = UNSET
    """An opaque cursor for fetching the next page."""


class SearchTimecardsRequestDict(TypedDict):
    query: NotRequired[TimecardQuery | TimecardQueryDict]
    limit: NotRequired[int]
    cursor: NotRequired[str]

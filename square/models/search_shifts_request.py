from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .shift_query import ShiftQuery, ShiftQueryDict


class SearchShiftsRequest(SdkBaseModel):
    """A request for a filtered and sorted set of ``Shift`` objects."""

    query: Optional[ShiftQuery] = UNSET
    """The parameters of a ``Shift`` search query, which includes filter and sort options.

    Deprecated at Square API version 2025-05-21. See the `migration notes
    <https://developer.squareup.com/docs/labor-api/what-it-does#migration-notes>`__."""

    limit: Optional[int] = UNSET
    """The number of resources in a page (200 by default)."""

    cursor: Optional[str] = UNSET
    """An opaque cursor for fetching the next page."""


class SearchShiftsRequestDict(TypedDict):
    query: NotRequired[ShiftQuery | ShiftQueryDict]
    limit: NotRequired[int]
    cursor: NotRequired[str]

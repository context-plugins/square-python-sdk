from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .scheduled_shift_query import ScheduledShiftQuery, ScheduledShiftQueryDict


class SearchScheduledShiftsRequest(SdkBaseModel):
    """Represents a `SearchScheduledShift <api-endpoint:Labor-SearchScheduledShift>`__ request."""

    query: Optional[ScheduledShiftQuery] = UNSET
    """Represents filter and sort criteria for the ``query`` field in a `SearchScheduledShifts
    <api-endpoint:Labor-SearchScheduledShifts>`__ request."""

    limit: Optional[int] = UNSET
    """The maximum number of results to return in a single response page. The default value is 50."""

    cursor: Optional[str] = UNSET
    """The pagination cursor returned by the previous call to this endpoint. Provide this cursor to retrieve the next
    page of results for your original request. For more information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""


class SearchScheduledShiftsRequestDict(TypedDict):
    query: NotRequired[ScheduledShiftQueryDict]
    limit: NotRequired[int]
    cursor: NotRequired[str]

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .timecard import Timecard, TimecardDict


class SearchTimecardsResponse(SdkBaseModel):
    """The response to a request for ``Timecard`` objects. The response contains the requested ``Timecard`` objects and
    might contain a set of ``Error`` objects if the request resulted in errors."""

    timecards: Optional[list[Timecard]] = UNSET
    """Timecards."""

    cursor: Optional[str] = UNSET
    """An opaque cursor for fetching the next page."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class SearchTimecardsResponseDict(TypedDict):
    timecards: NotRequired[list[Timecard | TimecardDict]]
    cursor: NotRequired[str]
    errors: NotRequired[list[Error | ErrorDict]]

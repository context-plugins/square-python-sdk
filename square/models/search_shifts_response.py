from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .shift import Shift, ShiftDict


class SearchShiftsResponse(SdkBaseModel):
    """The response to a request for ``Shift`` objects. The response contains the requested ``Shift`` objects and might
    contain a set of ``Error`` objects if the request resulted in errors."""

    shifts: Optional[list[Shift]] = UNSET
    """Shifts."""

    cursor: Optional[str] = UNSET
    """An opaque cursor for fetching the next page."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class SearchShiftsResponseDict(TypedDict):
    shifts: NotRequired[list[ShiftDict]]
    cursor: NotRequired[str]
    errors: NotRequired[list[ErrorDict]]

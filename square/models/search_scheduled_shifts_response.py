from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .scheduled_shift import ScheduledShift, ScheduledShiftDict


class SearchScheduledShiftsResponse(SdkBaseModel):
    """Represents a `SearchScheduledShifts <api-endpoint:Labor-SearchScheduledShifts>`__ response. Either
    ``scheduled_shifts`` or ``errors`` is present in the response."""

    scheduled_shifts: Optional[list[ScheduledShift]] = UNSET
    """A paginated list of scheduled shifts that match the query conditions."""

    cursor: Optional[str] = UNSET
    """The pagination cursor used to retrieve the next page of results. This field is present only if additional results
    are available."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class SearchScheduledShiftsResponseDict(TypedDict):
    scheduled_shifts: NotRequired[list[ScheduledShift | ScheduledShiftDict]]
    cursor: NotRequired[str]
    errors: NotRequired[list[Error | ErrorDict]]

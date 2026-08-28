from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .availability import Availability, AvailabilityDict
from .error import Error, ErrorDict


class SearchAvailabilityResponse(SdkBaseModel):
    availabilities: Optional[list[Availability]] = UNSET
    """List of appointment slots available for booking."""

    errors: Optional[list[Error]] = UNSET
    """Errors that occurred during the request."""


class SearchAvailabilityResponseDict(TypedDict):
    availabilities: NotRequired[list[Availability | AvailabilityDict]]
    errors: NotRequired[list[Error | ErrorDict]]

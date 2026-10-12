from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class EnableEventsResponse(SdkBaseModel):
    """Defines the fields that are included in the response body of a request to the `EnableEvents
    <api-endpoint:Events-EnableEvents>`__ endpoint.

    Note: if there are errors processing the request, the events field will not be present."""

    errors: Optional[list[Error]] = UNSET
    """Information on errors encountered during the request."""


class EnableEventsResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]

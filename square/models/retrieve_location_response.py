from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .location import Location, LocationDict


class RetrieveLocationResponse(SdkBaseModel):
    """Defines the fields that the `RetrieveLocation <api-endpoint:Locations-RetrieveLocation>`__ endpoint returns in a
    response."""

    errors: Optional[list[Error]] = UNSET
    """Information about errors encountered during the request."""

    location: Optional[Location] = UNSET
    """Represents one of a business' `locations <https://developer.squareup.com/docs/locations-api>`__."""


class RetrieveLocationResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    location: NotRequired[LocationDict]

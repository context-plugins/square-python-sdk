from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .location import Location, LocationDict


class ListLocationsResponse(SdkBaseModel):
    """Defines the fields that are included in the response body of a request to the `ListLocations
    <api-endpoint:Locations-ListLocations>`__ endpoint.

    Either ``errors`` or ``locations`` is present in a given response (never both)."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    locations: Optional[list[Location]] = UNSET
    """The business locations."""


class ListLocationsResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    locations: NotRequired[list[Location | LocationDict]]

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .location import Location, LocationDict


class UpdateLocationRequest(SdkBaseModel):
    """The request object for the `UpdateLocation <api-endpoint:Locations-UpdateLocation>`__ endpoint."""

    location: Optional[Location] = UNSET
    """Represents one of a business' `locations <https://developer.squareup.com/docs/locations-api>`__."""


class UpdateLocationRequestDict(TypedDict):
    location: NotRequired[LocationDict]

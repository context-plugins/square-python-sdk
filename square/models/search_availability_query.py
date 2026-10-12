from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .search_availability_filter import SearchAvailabilityFilter, SearchAvailabilityFilterDict


class SearchAvailabilityQuery(SdkBaseModel):
    """The query used to search for buyer-accessible availabilities of bookings."""

    filter: SearchAvailabilityFilter
    """A query filter to search for buyer-accessible availabilities by."""


class SearchAvailabilityQueryDict(TypedDict):
    filter: SearchAvailabilityFilterDict

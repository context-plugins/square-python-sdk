from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .search_availability_query import SearchAvailabilityQuery, SearchAvailabilityQueryDict


class SearchAvailabilityRequest(SdkBaseModel):
    query: SearchAvailabilityQuery
    """The query used to search for buyer-accessible availabilities of bookings."""


class SearchAvailabilityRequestDict(TypedDict):
    query: SearchAvailabilityQueryDict

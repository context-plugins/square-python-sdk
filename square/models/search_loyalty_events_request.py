from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .loyalty_event_query import LoyaltyEventQuery, LoyaltyEventQueryDict


class SearchLoyaltyEventsRequest(SdkBaseModel):
    """A request to search for loyalty events."""

    query: Optional[LoyaltyEventQuery] = UNSET
    """Represents a query used to search for loyalty events."""

    limit: Optional[int] = UNSET
    """The maximum number of results to include in the response. The last page might contain fewer events. The default
    is 30 events."""

    cursor: Optional[str] = UNSET
    """A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of
    results for your original query. For more information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""


class SearchLoyaltyEventsRequestDict(TypedDict):
    query: NotRequired[LoyaltyEventQueryDict]
    limit: NotRequired[int]
    cursor: NotRequired[str]

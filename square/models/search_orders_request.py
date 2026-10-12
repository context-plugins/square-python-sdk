from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .search_orders_query import SearchOrdersQuery, SearchOrdersQueryDict


class SearchOrdersRequest(SdkBaseModel):
    location_ids: Optional[list[str]] = UNSET
    """The location IDs for the orders to query. All locations must belong to the same merchant.

    Max: 10 location IDs."""

    cursor: Optional[str] = UNSET
    """A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of
    results for your original query. For more information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""

    query: Optional[SearchOrdersQuery] = UNSET
    """Contains query criteria for the search."""

    limit: Optional[int] = UNSET
    """The maximum number of results to be returned in a single page.

    Default: ``500`` Max: ``1000``"""

    return_entries: Optional[bool] = UNSET
    """A Boolean that controls the format of the search results. If ``true``, ``SearchOrders`` returns `OrderEntry
    <entity:OrderEntry>`__ objects. If ``false``, ``SearchOrders`` returns complete order objects.

    Default: ``false``."""


class SearchOrdersRequestDict(TypedDict):
    location_ids: NotRequired[list[str]]
    cursor: NotRequired[str]
    query: NotRequired[SearchOrdersQueryDict]
    limit: NotRequired[int]
    return_entries: NotRequired[bool]

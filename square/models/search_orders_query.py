from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .search_orders_filter import SearchOrdersFilter, SearchOrdersFilterDict
from .search_orders_sort import SearchOrdersSort, SearchOrdersSortDict


class SearchOrdersQuery(SdkBaseModel):
    """Contains query criteria for the search."""

    filter: Optional[SearchOrdersFilter] = UNSET
    """Filtering criteria to use for a ``SearchOrders`` request. Multiple filters are ANDed together."""

    sort: Optional[SearchOrdersSort] = UNSET
    """Sorting criteria for a ``SearchOrders`` request. Results can only be sorted by a timestamp field."""


class SearchOrdersQueryDict(TypedDict):
    filter: NotRequired[SearchOrdersFilterDict]
    sort: NotRequired[SearchOrdersSortDict]

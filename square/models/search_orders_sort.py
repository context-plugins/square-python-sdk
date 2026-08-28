from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.search_orders_sort_field import SearchOrdersSortFieldOrStr
from .enums.sort_order import SortOrderOrStr


class SearchOrdersSort(SdkBaseModel):
    """Sorting criteria for a ``SearchOrders`` request. Results can only be sorted by a timestamp field."""

    sort_field: SearchOrdersSortFieldOrStr
    """Specifies which timestamp to use to sort ``SearchOrder`` results."""

    sort_order: Optional[SortOrderOrStr] = UNSET
    """The order (e.g., chronological or alphabetical) in which results from a request are returned."""


class SearchOrdersSortDict(TypedDict):
    sort_field: SearchOrdersSortFieldOrStr
    sort_order: NotRequired[SortOrderOrStr]

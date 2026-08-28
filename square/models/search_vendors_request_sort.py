from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.search_vendors_request_sort_field import SearchVendorsRequestSortFieldOrStr
from .enums.sort_order import SortOrderOrStr


class SearchVendorsRequestSort(SdkBaseModel):
    """Defines a sorter used to sort results from `SearchVendors <api-endpoint:Vendors-SearchVendors>`__."""

    field: Optional[SearchVendorsRequestSortFieldOrStr] = UNSET
    """The field to sort the returned `Vendor <entity:Vendor>`__ objects by."""

    order: Optional[SortOrderOrStr] = UNSET
    """The order (e.g., chronological or alphabetical) in which results from a request are returned."""


class SearchVendorsRequestSortDict(TypedDict):
    field: NotRequired[SearchVendorsRequestSortFieldOrStr]
    order: NotRequired[SortOrderOrStr]

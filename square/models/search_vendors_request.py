from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .search_vendors_request_filter import SearchVendorsRequestFilter, SearchVendorsRequestFilterDict
from .search_vendors_request_sort import SearchVendorsRequestSort, SearchVendorsRequestSortDict


class SearchVendorsRequest(SdkBaseModel):
    """Represents an input into a call to `SearchVendors <api-endpoint:Vendors-SearchVendors>`__."""

    filter: Optional[SearchVendorsRequestFilter] = UNSET
    """Defines supported query expressions to search for vendors by."""

    sort: Optional[SearchVendorsRequestSort] = UNSET
    """Defines a sorter used to sort results from `SearchVendors <api-endpoint:Vendors-SearchVendors>`__."""

    cursor: Optional[str] = UNSET
    """A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of
    results for the original query.

    See the `Pagination <https://developer.squareup.com/docs/working-with-apis/pagination>`__ guide for more
    information."""


class SearchVendorsRequestDict(TypedDict):
    filter: NotRequired[SearchVendorsRequestFilterDict]
    sort: NotRequired[SearchVendorsRequestSortDict]
    cursor: NotRequired[str]

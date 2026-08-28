from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.customer_sort_field import CustomerSortFieldOrStr
from .enums.sort_order import SortOrderOrStr


class CustomerSort(SdkBaseModel):
    """Represents the sorting criteria in a `search query <entity:CustomerQuery>`__ that defines how to sort customer
    profiles returned in `SearchCustomers <api-endpoint:Customers-SearchCustomers>`__ results."""

    field: Optional[CustomerSortFieldOrStr] = UNSET
    """Specifies customer attributes as the sort key to customer profiles returned from a search."""

    order: Optional[SortOrderOrStr] = UNSET
    """The order (e.g., chronological or alphabetical) in which results from a request are returned."""


class CustomerSortDict(TypedDict):
    field: NotRequired[CustomerSortFieldOrStr]
    order: NotRequired[SortOrderOrStr]

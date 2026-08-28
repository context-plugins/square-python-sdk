from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .customer_filter import CustomerFilter, CustomerFilterDict
from .customer_sort import CustomerSort, CustomerSortDict


class CustomerQuery(SdkBaseModel):
    """Represents filtering and sorting criteria for a `SearchCustomers <api-endpoint:Customers-SearchCustomers>`__
    request."""

    filter: Optional[CustomerFilter] = UNSET
    """Represents the filtering criteria in a `search query <entity:CustomerQuery>`__ that defines how to filter
    customer profiles returned in `SearchCustomers <api-endpoint:Customers-SearchCustomers>`__ results."""

    sort: Optional[CustomerSort] = UNSET
    """Represents the sorting criteria in a `search query <entity:CustomerQuery>`__ that defines how to sort customer
    profiles returned in `SearchCustomers <api-endpoint:Customers-SearchCustomers>`__ results."""


class CustomerQueryDict(TypedDict):
    filter: NotRequired[CustomerFilter | CustomerFilterDict]
    sort: NotRequired[CustomerSort | CustomerSortDict]
